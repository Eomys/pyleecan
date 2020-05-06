# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir
import os
import platform
import shutil
from logging import getLogger

ROOT_DIR = normpath(abspath(join(dirname(__file__), "..")))
MAIN_DIR = dirname(realpath(__file__))

PACKAGE_NAME = MAIN_DIR[len(ROOT_DIR) + 1 :]  # To allow to change pyleecan directory

GEN_DIR = join(MAIN_DIR, "Generator")
DOC_DIR = join(GEN_DIR, "ClassesRef")  # Absolute path to classes reference dir
INT_DIR = join(GEN_DIR, "Internal")  # Absolute path to  internal classes ref. dir

GUI_DIR = join(MAIN_DIR, "GUI")
RES_PATH = join(GUI_DIR, "Resources")  # Default Resouces folder name
RES_NAME = ".qrc"  # Default Resouces file name

TEST_DIR = join(MAIN_DIR, "../Tests")

# Pyleecan user folder
if platform.system() == "Windows":
    PYLEECAN_USER_DIR = os.environ["APPDATA"] + "/Pyleecan"
    PYLEECAN_USER_DIR = PYLEECAN_USER_DIR.replace("\\", "/")
else:
    PYLEECAN_USER_DIR = os.environ["HOME"] + "/.local/share/Pyleecan"


DATA_DIR = join(PYLEECAN_USER_DIR, "Data")  # Absolute path to default data dir
MATLIB_DIR = join(DATA_DIR, "Material")


def create_folder():
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
