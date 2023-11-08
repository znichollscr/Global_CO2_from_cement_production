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

root_path = Path(".")

version_info = versions[version]

# there are no input files
# if files are in the target folder consider them to be output files
output_folder = root_path / downloaded_data_folder / version_info["folder"]
if output_folder.exists():
    output_files = list(output_folder.iterdir())

datalad.api.run(
    cmd=f"./venv/bin/python3 src/download_version.py --version {version}",
    dataset=root_path,
    message=f"Download data for {version}.",
    inputs=[],
    outputs=output_files,
    dry_run=None,
    explicit=False,
)