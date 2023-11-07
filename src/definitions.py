# this file holds  definitions for folder names file names etc
from versions import versions

downloaded_data_folder = "downloaded_data"
extracted_data_folder = "extracted_data"

def get_output_filename(version: str) -> str:
    version_info = versions[version]
    return f"Robbie_Andrew_Cement_Production_CO2_{version_info['ver_str_short']}"