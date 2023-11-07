# this script reads the data for a given version and saves to primap2 native and
# interchange format
import pandas as pd
import primap2 as pm2
import os
import argparse
from pathlib import Path
from helper_functions import get_country_code
from versions import versions
from definitions import get_output_filename, downloaded_data_folder, extracted_data_folder

# handle command line parameter
parser = argparse.ArgumentParser()
parser.add_argument("--version", help="Version to read")
args = parser.parse_args()
version = args.version


compression = dict(zlib=True, complevel=9)
root_path = Path("..")  # Path(os.path.realpath("__file__")).parents[0].absolute()

## set the configuration for conversion to primap2 format
version_info = versions[version]

coords_cols = {
    "area": "index",
}

coords_terminologies = {"area": "ISO3", "category": "IPCC2006", "scenario": "PRIMAP"}

coords_defaults = {
    "source": "Andrew_Cement",
    "provenance": "measured",
    "category": "2.A.1",
    "unit": version_info["unit"],
    "entity": "CO2",
    "scenario": version_info["ver_str_short"],
}

coords_value_mapping = {}

filter_keep = {}
filter_keep.update(version_info["filter_keep"])

filter_remove = {}
filter_remove.update(version_info["filter_remove"])

meta_data = {
    "references": f"{version_info['ref']}, {version_info['ref2']}",
    "rights": "Creative Commons Attribution 4.0 International",
    "contact": f"{version_info['contact']}",
    "title": f"{version_info['title']} - {version_info['ver_str_long']}",
    "comment": f"{version_info['comment']}",
    "institution": f"{version_info['institution']}",
}

filename_and_path = (root_path / downloaded_data_folder / version_info["folder"] /
                     version_info["filename"])
output_folder = root_path / extracted_data_folder / version_info["folder"]
output_file = get_output_filename(version)

# read the data
data_pd = pd.read_csv(filename_and_path)

# transpose for older versions
if version_info["transpose"]:
    data_pd = data_pd.transpose()
    data_pd.columns = data_pd.iloc[0]
    # idx_to_drop =  data_pd.iloc[0].index
    data_pd = data_pd.drop("Year", axis=0)

# map country names to codes
if not version_info["country_code"]:
    country_names = data_pd.index.to_list()
    country_codes = {}
    exceptions = False
    for country in country_names:
        try:
            country_codes[country] = get_country_code(country)
        except Exception as ex:
            print(ex)
            exceptions = True
    data_pd = data_pd.rename(index=country_codes)
    if exceptions:
        raise ValueError(
            "Exceptions occurred during mapping of country names to codes."
        )
else:
    data_pd = data_pd.drop(columns=["UN code", "Name"])

# column names to str for conversion to dates
data_pd.columns = [f"{col:.0f}" for col in data_pd.columns]

# country codes to col instead of index
data_pd = data_pd.reset_index()


# convert to PRIMAP2 interchange format
data_if = pm2.pm2io.convert_wide_dataframe_if(
    data_pd,
    coords_cols=coords_cols,
    coords_defaults=coords_defaults,
    coords_terminologies=coords_terminologies,
    coords_value_mapping=coords_value_mapping,
    filter_keep=filter_keep,
    filter_remove=filter_remove,
    meta_data=meta_data,
)

# convert to PRIMAP2 native format
data_pm2 = pm2.pm2io.from_interchange_format(data_if, data_if.attrs)

# convert back to IF for standardized units
data_if = data_pm2.pr.to_interchange_format()

# save data
if not output_folder.exists():
    output_folder.mkdir()
pm2.pm2io.write_interchange_format(output_folder / (output_file + ".csv"), data_if)
encoding = {var: compression for var in data_pm2.data_vars}
data_pm2.pr.to_netcdf(output_folder / (output_file + ".nc"), encoding=encoding)
