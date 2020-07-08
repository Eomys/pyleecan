import platform
import os
from os.path import join

# dynamic import to avoid loop
module = __import__(
    "pyleecan.definitions",
    globals=globals(),
    locals=locals(),
    fromlist=["USER_DIR"],
    level=0,
)
USER_DIR = module.USER_DIR

# Default config_dict
default_config_dict = dict(
    DATA_DIR=join(USER_DIR, "Data"),
    MATLIB_DIR=join(USER_DIR, "Data", "Material"),  # Material library directory
    UNIT_M=1,  # length unit: 0 for m, 1 for mm
    UNIT_M2=1,  # Surface unit: 0 for m^2, 1 for mm^2
    COLOR_DICT_NAME="pyleecan_color.json",  # Name of the color set to use
)
