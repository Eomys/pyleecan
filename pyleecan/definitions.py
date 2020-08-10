# -*- coding: utf-8 -*-
import os
import platform
import shutil
import sys
from json import load
from logging import getLogger
from os.path import abspath, dirname, isdir, isfile, join, normpath, realpath
from matplotlib.colors import ListedColormap
from matplotlib.cm import get_cmap, register_cmap
from numpy import load as np_load
from matplotlib import font_manager

ROOT_DIR = normpath(abspath(join(dirname(__file__), ".."))).replace("\\", "/")
# Further import
try:
    from .Functions.init_environment import get_config_dict, init_user_dir
except ImportError:
    # Add root dir to python path
    sys.path.insert(0, ROOT_DIR)
    exec(
        "from pyleecan.Functions.init_environment import get_config_dict, init_user_dir"
    )

MAIN_DIR = dirname(realpath(__file__)).replace("\\", "/")

PACKAGE_NAME = MAIN_DIR[len(ROOT_DIR) + 1 :]  # To allow to change pyleecan directory
GEN_DIR = join(MAIN_DIR, "Generator").replace("\\", "/")
DOC_DIR = join(GEN_DIR, "ClassesRef").replace("\\", "/")
DATA_DIR = join(MAIN_DIR, "Data").replace("\\", "/")
# Absolute path to  internal classes ref. dir
INT_DIR = join(GEN_DIR, "Internal").replace("\\", "/")

GUI_DIR = join(MAIN_DIR, "GUI").replace("\\", "/")
RES_PATH = join(GUI_DIR, "Resources").replace("\\", "/")  # Default Resouces folder name
RES_NAME = "pyleecan.qrc"  # Default Resouces file name

TEST_DIR = join(ROOT_DIR, "Tests").replace("\\", "/")

# User folder (to store machine/materials/config)
if platform.system() == "Windows":
    USER_DIR = join(os.environ["APPDATA"], PACKAGE_NAME)
    USER_DIR = USER_DIR.replace("\\", "/")
else:
    USER_DIR = os.environ["HOME"] + "/.local/share/" + PACKAGE_NAME
CONF_PATH = join(USER_DIR, "main_config_dict.json")
if not isdir(USER_DIR):
    init_user_dir()

# Load the config file (create one if it doesn't exist)
config_dict = get_config_dict()
# Update config_dict content
config_dict["MAIN"]["MACHINE_DIR"] = join(USER_DIR, "Machine")
config_dict["MAIN"]["MATLIB_DIR"] = join(USER_DIR, "Material")

config_dict["GUI"]["CSS_PATH"] = join(USER_DIR, "GUI", config_dict["GUI"]["CSS_NAME"])
