# -*- coding: utf-8 -*-

import sys
from logging import ERROR, INFO, basicConfig, getLogger
from os.path import abspath, dirname, join, normpath

from matplotlib import use

from ..Classes.GUIOption import GUIOption
from ..definitions import config_dict

# Set Matplotlib backend
use("qtagg")  # Use PySide6 backend

gui_option = GUIOption()
gui_option.unit.unit_m = config_dict["GUI"]["UNIT_M"]  # Use mm
gui_option.unit.unit_m2 = config_dict["GUI"]["UNIT_M2"]  # Use mm²
