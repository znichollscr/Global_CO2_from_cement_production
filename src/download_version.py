# script to download files for a given version from zenodo
import argparse
import requests
import shutil
from pathlib import Path
from zipfile import ZipFile
from versions import versions
from definitions import downloaded_data_folder

# handle command line parameter
parser = argparse.ArgumentParser()
parser.add_argument("--version", help="Version to read")
args = parser.parse_args()
version = args.version

root_path = Path(".")

version_info = versions[version]
record_id = version_info["ref"].split(".")[-1]
url = f"https://zenodo.org/api/records/{record_id}/files-archive"

local_folder = root_path / downloaded_data_folder / version_info["folder"]
if not local_folder.exists():
    local_folder.mkdir()
local_filename = local_folder / f"{record_id}.zip"

#download all data in zip file
r = requests.get(url, stream=True)
with open(str(local_filename), 'wb') as f:
    shutil.copyfileobj(r.raw, f)

# extract data
with ZipFile(str(local_filename), 'r') as f:
    f.extractall(local_folder)

# delete the zip file
local_filename.unlink()