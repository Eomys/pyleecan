# -*- coding: utf-8 -*-

import sys
from logging import ERROR, INFO, basicConfig, getLogger
from matplotlib import use
from ..Classes.GUIOption import GUIOption
from ..definitions import config_dict
from os.path import abspath, dirname, join, normpath

# Set Matplotlib backend
use("Qt5Agg")  # Use qtpy backend

gui_option = GUIOption()
gui_option.unit.unit_m = config_dict["GUI"]["UNIT_M"]  # Use mm
gui_option.unit.unit_m2 = config_dict["GUI"]["UNIT_M2"]  # Use mm²
