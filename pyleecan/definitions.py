# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir, isfile
import os
import platform
import shutil
from logging import getLogger
from json import dump, load


def create_folder(conf_dict):
    """
    Create Pyleecan folder to copy Data into it.
    
    Windows: %APPDATA%/Pyleecan
    Linux and MacOS: $HOME/.local/share/Pyleecan
    """
    logger = getLogger("Pyleecan")

    if not isdir(PYLEECAN_USER_DIR):
        # Create Pyleecan folder and copy Data folder
        logger.debug("Copying Data folder in " + PYLEECAN_USER_DIR + "/Data")
        shutil.copytree(
            __file__[: max(__file__.rfind("/"), __file__.rfind("\\"))] + "/Data",
            PYLEECAN_USER_DIR + "/Data",
        )
        with open(PYLEECAN_USER_DIR + "/config.json", "w") as conf_file:
            dump(conf_dict, conf_file, sort_keys=True, indent=4, separators=(",", ": "))


def edit_config_dict(key, value, conf_dict):
    """Edit and save the config dict
    """
    conf_dict[key] = value

    with open(PYLEECAN_USER_DIR + "/config.json", "w") as conf_file:
        dump(conf_dict, conf_file, sort_keys=True, indent=4, separators=(",", ": "))


ROOT_DIR = normpath(abspath(join(dirname(__file__), ".."))).replace("\\", "/")
MAIN_DIR = dirname(realpath(__file__)).replace("\\", "/")

PACKAGE_NAME = MAIN_DIR[len(ROOT_DIR) + 1 :]  # To allow to change pyleecan directory

GEN_DIR = join(MAIN_DIR, "Generator").replace("\\", "/")
DOC_DIR = join(GEN_DIR, "ClassesRef").replace(
    "\\", "/"
)  # Absolute path to classes reference dir
INT_DIR = join(GEN_DIR, "Internal").replace(
    "\\", "/"
)  # Absolute path to  internal classes ref. dir

GUI_DIR = join(MAIN_DIR, "GUI").replace("\\", "/")
RES_PATH = join(GUI_DIR, "Resources").replace("\\", "/")  # Default Resouces folder name
RES_NAME = "pyleecan.qrc"  # Default Resouces file name

TEST_DIR = join(MAIN_DIR, "../Tests")

# Pyleecan user folder
if platform.system() == "Windows":
    PYLEECAN_USER_DIR = join(os.environ["APPDATA"], PACKAGE_NAME)
    PYLEECAN_USER_DIR = PYLEECAN_USER_DIR.replace("\\", "/")
else:
    PYLEECAN_USER_DIR = os.environ["HOME"] + "/.local/share/" + PACKAGE_NAME

if isfile(join(PYLEECAN_USER_DIR, "config.json")):  # Load the config file if it exist
    with open(join(PYLEECAN_USER_DIR, "config.json"), "r") as config_file:
        config_dict = load(config_file)
else:  # Default values
    config_dict = dict(
        DATA_DIR=join(PYLEECAN_USER_DIR, "Data"),
        MATLIB_DIR=join(
            PYLEECAN_USER_DIR, "Data", "Material"
        ),  # Material library directory
        UNIT_M=1,  # length unit: 0 for m, 1 for mm
        UNIT_M2=1,  # Surface unit: 0 for m^2, 1 for mm^2
        COLOR_DICT_NAME="pyleecan_color.json",  # Name of the color set to use
    )
create_folder(config_dict)

DATA_DIR = config_dict["DATA_DIR"]
MATLIB_DIR = config_dict["MATLIB_DIR"]

# Load the color_dict
color_path = join(config_dict["DATA_DIR"], config_dict["COLOR_DICT_NAME"])
if not isfile(color_path):  # Default colors
    color_path = join(config_dict["DATA_DIR"], "pyleecan_color.json")
with open(color_path, "r") as color_file:
    config_dict["color_dict"] = load(color_file)
