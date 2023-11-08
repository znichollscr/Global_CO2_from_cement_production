# define tasks for Andrew Cement data repository
from doit import get_var

# create virtual environment
def task_setup_venv():
    """Create virtual environment"""
    return {
        'file_dep': ['requirements_dev.txt', 'setup.cfg', 'pyproject.toml'],
        'actions': ['python3 -m venv venv',
                    './venv/bin/pip install --upgrade pip wheel',
                    './venv/bin/pip install --upgrade --upgrade-strategy '
                    'eager -e .[dev]',
                    # I needed .['dev'] for this to work but maybe it's just my shell..
                    'touch venv',],
        'targets': ['venv'],
        'verbosity': 2,
    }

read_config = {
    "version": get_var('version', None),
}

def task_read_version():
    """ Read specific version of the data"""
    return {
        'actions': [f"./venv/bin/python src/read_version_datalad.py "
                    f"--version={read_config['version']}"],
        'verbosity': 2,
        'setup': ['setup_venv'],
    }

def task_download_version():
    """ Download specific version of the data"""
    return {
        'actions': [f"./venv/bin/python src/download_version_datalad.py "
                    f"--version={read_config['version']}"],
        'verbosity': 2,
        'setup': ['setup_venv'],
    }
