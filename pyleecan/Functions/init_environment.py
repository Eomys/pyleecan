import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir, isfile
import os
import platform
import shutil
from json import dump, load
from logging import getLogger

# dynamic import to avoid loop
module = __import__(
    "pyleecan.definitions",
    globals=globals(),
    locals=locals(),
    fromlist=["USER_DIR"],
    level=0,
)
USER_DIR = module.USER_DIR


def create_folder(folder):
    """
    Create Pyleecan folder to copy Data into it.
    
    Windows: %APPDATA%/Pyleecan
    Linux and MacOS: $HOME/.local/share/Pyleecan

    Parameters
    ----------
    folder : str
        folder to create
    """
    if not isdir(USER_DIR + "/" + folder):
        os.makedirs(USER_DIR + "/" + folder)


def edit_config_dict(path, config_dict):
    """update the config file with config_dict values

    Parameters
    ----------
    path : str
        path to the config file to update
    config_dict : dict
        new values to put in the config file
    """
    with open(join(path, "config.json"), "w") as config_file:
        dump(config_dict, config_file, sort_keys=True, indent=4, separators=(",", ": "))


def copy_folder(src, dst):
    """Copy recursively src content in dst folder

    Parameters
    ----------
    src : str
        source folder
    dst : str
        destination folder
    """
    logger = getLogger("Pyleecan")
    if not isdir(USER_DIR):
        # Create Pyleecan folder and copy Data folder
        logger.debug("Copying Data folder in " + USER_DIR + "/" + dst)
        shutil.copytree(
            join(
                dirname(__file__[: max(__file__.rfind("/"), __file__.rfind("\\"))]), src
            ),
            USER_DIR + "/" + dst,
        )


def read_config_dict(path=None, default=None):
    """Reads the GUI config file if path is not specified and workspace config dict if path is defined

    Returns
    -------
    dict
        config dict file
    """
    if path is None:
        if isfile(
            USER_DIR + "/GUI/config.json"
        ):  # Load the GUI config file if it exist
            with open(USER_DIR + "/GUI/config.json", "r") as config_file:
                config_dict = load(config_file)
        else:
            # Setting up the default value of the gui config file
            config_dict = dict(IS_DEFAULT_WORKSPACE=False, WORKSPACE="", WORKSPACES=[])
            if not isdir(join(USER_DIR, "GUI")):
                create_folder("GUI")
                edit_config_dict(join(USER_DIR, "GUI"), config_dict)
            else:
                edit_config_dict(join(USER_DIR, "GUI"), config_dict)
    else:
        if isfile(
            join(path, "config.json")
        ):  # Load the workspace config file if it exists
            with open(join(path, "config.json"), "r") as config_file:
                config_dict = load(config_file)
        else:
            # Setting up the default value of the workspace config file
            config_dict = default
            edit_config_dict(path=path, config_dict=config_dict)
    return config_dict
