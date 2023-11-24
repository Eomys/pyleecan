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
    BAR_LAB,
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
PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
BAR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["BAR_COLOR"]

PLUS_HATCH = "++"
MINUS_HATCH = ".."


def get_color_legend_from_surface(surf, is_lam_only=False):
    """Return the color and legend to use for plot the surface

    Parameters
    ----------
    surf : Surface
        Surfaces on which we want the color and legend
    is_lam_only : bool
        True to plot only the lamination (remove the Winding)

    Returns
    -------
    color : str
        Color to use on the patch
    legend : str
        Legend to display for the surface
    """
    label_dict = decode_label(surf.label)

    if LAM_LAB in label_dict["surf_type"] and STATOR_LAB in label_dict["lam_type"]:
        return STATOR_COLOR, "Stator"

    elif LAM_LAB in label_dict["surf_type"] and ROTOR_LAB in label_dict["lam_type"]:
        return ROTOR_COLOR, "Rotor"

    elif VENT_LAB in label_dict["surf_type"]:
        return VENT_COLOR, None

    # Before will always be ploted
    elif is_lam_only:
        return None, None

    # After will be ploted only if we do not want the lamination only.
    elif HOLEV_LAB in label_dict["surf_type"]:
        return VENT_COLOR, None

    elif HOLEM_LAB in label_dict["surf_type"] or MAG_LAB in label_dict["surf_type"]:
        return MAGNET_COLOR, "Magnet"

    elif WEDGE_LAB in label_dict["surf_type"]:
        return WEDGE_COLOR, "Wedge"

    elif KEY_LAB in label_dict["surf_type"]:
        return KEY_COLOR, "Key"

    elif BAR_LAB in label_dict["surf_type"]:
        return BAR_COLOR, f"{label_dict['lam_type']} Bar"

    else:
        raise Exception(f"Unknown label for plot {surf.label}")
