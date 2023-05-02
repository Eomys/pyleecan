# -*- coding: utf-8 -*-
import os
import shutil
import sys
from json import load
from logging import getLogger
from os.path import abspath, dirname, basename, join, normpath, realpath
from matplotlib.colors import ListedColormap
from matplotlib.cm import get_cmap, register_cmap
from numpy import load as np_load
from matplotlib import font_manager

PYTHON_DEFAULT_ENCODING = "utf-8-sig"

ROOT_DIR = normpath(abspath(join(dirname(__file__), ".."))).replace("\\", "/")
# Further import
try:
    from .Functions.init_environment import get_config_dict
    from pyleecan import PACKAGE_NAME, USER_DIR
except ImportError:
    # Add root dir to python path
    sys.path.insert(0, ROOT_DIR)
    exec("from pyleecan.Functions.init_environment import get_config_dict")
    exec("from pyleecan import PACKAGE_NAME, USER_DIR")

MAIN_DIR = dirname(realpath(__file__)).replace("\\", "/")

GEN_DIR = join(MAIN_DIR, "Generator").replace("\\", "/")
DOC_DIR = join(GEN_DIR, "ClassesRef").replace("\\", "/")
DATA_DIR = join(MAIN_DIR, "Data").replace("\\", "/")
RESULT_DIR = join(MAIN_DIR, "Results").replace("\\", "/")
# Absolute path to  internal classes ref. dir
INT_DIR = join(GEN_DIR, "Internal").replace("\\", "/")

GUI_DIR = join(MAIN_DIR, "GUI").replace("\\", "/")
RES_PATH = join(GUI_DIR, "Resources").replace("\\", "/")  # Default Resouces folder name
RES_NAME = "pyleecan.qrc"  # Default Resouces file name

TEST_DIR = join(ROOT_DIR, "Tests").replace("\\", "/")

CONF_PATH = join(USER_DIR, "main_config_dict.json")

# Matplotlib definitions
# Get a "sans-serif" font as default (works for Linux and Windows)
DEFAULT_FONT = font_manager.FontProperties(family=["sans-serif"]).get_name()
DEFAULT_COLOR_MAP = "RdBu_r"

# Load the config file (create one if it doesn't exist)
config_dict = get_config_dict()
