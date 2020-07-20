# Default config_dict
default_config_dict = {"MAIN": {}, "GUI": {}, "PLOT": {}}

default_config_dict["MAIN"]["MACHINE_DIR"] = ""
default_config_dict["MAIN"]["MATLIB_DIR"] = ""

default_config_dict["GUI"]["UNIT_M"] = 1  # length unit: 0 for m, 1 for mm
default_config_dict["GUI"]["UNIT_M2"] = 1  # Surface unit: 0 for m^2, 1 for mm^2
default_config_dict["GUI"]["CSS_NAME"] = "pyleecan.css"
default_config_dict["GUI"]["CSS_PATH"] = ""
# Name of the color set to use
default_config_dict["PLOT"]["COLOR_DICT_NAME"] = "pyleecan_color.json"
default_config_dict["PLOT"]["COLOR_DICT"] = {}
