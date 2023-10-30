from ...Functions.labels import (
    decode_label,
    STATOR_LAB,
    ROTOR_LAB,
    KEY_LAB,
    HOLEM_LAB,
    HOLEV_LAB,
    MAG_LAB,
    LAM_LAB,
    VENT_LAB,
    WEDGE_LAB,
)
from ...definitions import config_dict

if "WEDGE_COLOR" not in config_dict["PLOT"]["COLOR_DICT"]:
    config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"] = "y"
WEDGE_COLOR = config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"]

if "KEY_COLOR" not in config_dict["PLOT"]["COLOR_DICT"]:
    config_dict["PLOT"]["COLOR_DICT"]["KEY_COLOR"] = "y"
KEY_COLOR = config_dict["PLOT"]["COLOR_DICT"]["KEY_COLOR"]

VENT_COLOR = config_dict["PLOT"]["COLOR_DICT"]["VENT_COLOR"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


def get_path_color_from_label(label, label_dict=None):
    """Return the color to use for a patch in plot machine

    Parameters
    ----------
    label : str
        Label of the surface to color
    label_dict : dict
        To avoid decoding label twice

    Returns
    -------
    color : str
        Color to use on the patch
    """

    if label_dict is None:
        label_dict = decode_label(label)

    if LAM_LAB in label_dict["surf_type"] and STATOR_LAB in label_dict["lam_type"]:
        return STATOR_COLOR
    elif LAM_LAB in label_dict["surf_type"] and ROTOR_LAB in label_dict["lam_type"]:
        return ROTOR_COLOR
    elif HOLEM_LAB in label_dict["surf_type"] or MAG_LAB in label_dict["surf_type"]:
        return MAGNET_COLOR
    elif VENT_LAB in label_dict["surf_type"] or HOLEV_LAB in label_dict["surf_type"]:
        return VENT_COLOR
    elif WEDGE_LAB in label_dict["surf_type"]:
        return WEDGE_COLOR
    elif KEY_LAB in label_dict["surf_type"]:
        return KEY_COLOR
    else:
        raise Exception("Unknown label for plot " + label)
