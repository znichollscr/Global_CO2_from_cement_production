# script that calls datalad to run the data reading function

import argparse
import datalad.api
from pathlib import Path
from versions import versions
from definitions import get_output_filename, downloaded_data_folder, extracted_data_folder

# handle command line parameter
parser = argparse.ArgumentParser()
parser.add_argument("--version", help="Version to read")
args = parser.parse_args()
version = args.version

root_path = Path("..")

version_info = versions[version]
input_files = [root_path / downloaded_data_folder / version_info["folder"] / version_info[
    "filename"]]
suffixes = ['nc', 'yaml', 'csv']
output_file_template = (root_path / downloaded_data_folder / version_info["folder"] /
                        get_output_filename(version))
output_files = [f"{str(output_file_template)}.{suffix}" for suffix in suffixes]


datalad.api.run(
    cmd=f"./venv/bin/python3 src/read_version.py --version {version}",
    dataset=root_path,
    message=f"Read data for {version}.",
    inputs=input_files,
    outputs=output_files,
    dry_run=True,
    explicit=True,
)