# -*- coding: utf-8 -*-
import sys

from pyleecan.GUI import gui_option

gui_option.unit.unit_m = 0  # Select m as unit
gui_option.unit.unit_m2 = 0  # Select m² as unit

# Disable GUI log
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
