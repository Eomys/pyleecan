# -*- coding: utf-8 -*-
from .loggers import init_default_log
import os
import platform

PACKAGE_NAME = "pyleecan"
# User folder (to store machine/materials/config)
if platform.system() == "Windows":
    USER_DIR = os.path.join(os.environ["APPDATA"], PACKAGE_NAME)
    USER_DIR = USER_DIR.replace("\\", "/")
else:
    USER_DIR = os.environ["HOME"] + "/.local/share/" + PACKAGE_NAME

__version__ = "1.4.0"

init_default_log()
