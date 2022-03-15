from ...Functions.Load.import_class import import_class
from ...Functions.labels import HOLEM_LAB, HOLEV_LAB
from logging import getLogger
from ...loggers import GUI_LOG_NAME


def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one"""
    _search_(init_dict)

    # for obj_dict in convert_list:
    #     if is_Winding_dict(obj_dict):
    #         convert_Winding(obj_dict)
    #     elif is_HoleUD_dict(obj_dict):
    #         convert_HoleUD(obj_dict)


def _search_(obj, parent=None, parent_index=None):
    # add to list for later conversion
    if is_HoleUD_dict(obj):
        parent[parent_index] = convert_HoleUD(obj)
        # convert_list.append(obj)
    elif is_Winding_dict(obj):
        if (
            parent is not None
            and "slot" in parent.keys()
            and "Zs" in parent["slot"].keys()
        ):
            # Add Zs for wind_mat generation
            obj["Zs"] = parent["slot"]["Zs"]
        parent[parent_index] = convert_Winding(obj)
        # convert_list.append(obj)
    else:
        # walk through the dict
        for key, value in obj.items():
            if isinstance(value, dict):
                # recursively search the dict
                _search_(value, parent=obj, parent_index=key)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        # recursively search the dict
                        _search_(item, parent=value, parent_index=i)


############################################
# V  1.3.2 = > 1.4.0
# Updating HoleUD surface label
# Label reorganization
############################################
def is_HoleUD_dict(obj_dict):
    """Check if the object need to be updated for HoleUD"""
    if "__class__" in obj_dict.keys() and obj_dict["__class__"] == "HoleUD":
        # Old label : Hole_Rotor_R0_T0_S0
        # Old label : HoleMagnet_Rotor_Parallel_N_R0_T0_S0
        return len(obj_dict["surf_list"][0]["label"].split("_")) > 3
    else:
        return False


def convert_HoleUD(hole_dict):
    """Update the content of the dict and instantiate object"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the HoleUD object"
    )
    # Copy dict to keep original version
    hole_dict_new = hole_dict.copy()
    for ii in range(len(hole_dict["surf_list"])):
        if "HoleMagnet" in hole_dict["surf_list"][ii]["label"]:
            hole_dict_new["surf_list"][ii]["label"] = HOLEM_LAB
        else:
            hole_dict_new["surf_list"][ii]["label"] = HOLEV_LAB
    # Instantiate object
    HoleUD = import_class("pyleecan.Classes", "HoleUD")
    return HoleUD(init_dict=hole_dict_new)


######################
# v 1.2.1 => 1.3.0
# Winding star of slot
######################
def is_Winding_dict(obj_dict):
    """Check if the object need to be updated for Winding"""
    return (
        "__class__" in obj_dict.keys()
        and obj_dict["__class__"]
        in [
            "WindingCW1L",
            "WindingCW2LR",
            "WindingCW2LT",
            "WindingDW1L",
            "WindingDW2L",
        ]
        or "__class__" in obj_dict.keys()
        and obj_dict["__class__"]
        in [
            "Winding",
            "WindingUD",
            "WindingSC",
        ]
        and "Npcpp" in obj_dict.keys()
    )


def convert_Winding(wind_dict):
    """Update the old Winding classes to WindingUD"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the Winding object"
    )
    # Copy dict to keep original version
    wind_dict_new = wind_dict.copy()
    # Update Npcpp
    if "Npcpp" in wind_dict_new.keys():
        wind_dict_new["Npcp"] = wind_dict_new.pop("Npcpp")

    # Update user_wind_mat
    if wind_dict_new["__class__"] == "WindingUD":
        if "user_wind_mat" in wind_dict_new.keys():
            wind_dict_new["wind_mat"] = wind_dict_new["user_wind_mat"]

    # Update class
    if wind_dict_new["__class__"] in [
        "WindingCW1L",
        "WindingCW2LR",
        "WindingCW2LT",
        "WindingDW1L",
        "WindingDW2L",
    ]:
        # Load Winding main parameters
        if "qs" in wind_dict_new.keys():
            qs = wind_dict_new["qs"]
        else:
            qs = 3
        if "p" in wind_dict_new.keys():
            p = wind_dict_new["p"]
        else:
            p = 3
        if "coil_pitch" in wind_dict_new.keys():
            coil_pitch = wind_dict_new["coil_pitch"]
        else:
            coil_pitch = 0
        if "Ntcoil" in wind_dict_new.keys():
            Ntcoil = wind_dict_new["Ntcoil"]
        else:
            Ntcoil = 1

        if (
            qs is None
            or p is None
            or coil_pitch is None
            or "Zs" not in wind_dict_new
            or wind_dict_new["Zs"] is None
        ):
            # Winding not fully defined => Use Star of slot
            Winding = import_class("pyleecan.Classes", "Winding")
            return Winding(init_dict=wind_dict_new)
        else:
            # Generate old Winding matrix as UD
            old_class = wind_dict["__class__"]
            WindingUD = import_class("pyleecan.Classes", "WindingUD")
            new_wind = WindingUD(qs=qs, p=p, Ntcoil=Ntcoil, coil_pitch=coil_pitch)
            try:
                if old_class == "WindingCW1L":
                    new_wind.init_as_CW1L(Zs=wind_dict["Zs"])
                elif old_class == "WindingCW2LR":
                    new_wind.init_as_CW2LR(Zs=wind_dict["Zs"])
                elif old_class == "WindingCW2LT":
                    new_wind.init_as_CW2LT(Zs=wind_dict["Zs"])
                elif old_class == "WindingDW1L":
                    new_wind.init_as_DWL(Zs=wind_dict["Zs"], nlay=1)
                elif old_class == "WindingDW2L":
                    new_wind.init_as_DWL(Zs=wind_dict["Zs"], nlay=2)
                return new_wind
            except Exception:
                # Not able to generate winding matrix => Star of Slot
                Winding = import_class("pyleecan.Classes", "Winding")
                return Winding(init_dict=wind_dict_new)

    else:
        Winding_class = import_class("pyleecan.Classes", wind_dict_new["__class__"])
        return Winding_class(init_dict=wind_dict_new)

def is_before_version(ref_version, check_version):
    """Check if a version str is before another version str

    Parameters
    ----------
    ref_version : str
        Reference version to compare with ("1.2.3" for instance)
    check_version : str
        Version to check if before reference ("1.3.4" for instance)

    Returns
    -------
    is_before : bool
        True if check_version is before ref_version
    """
    ref_list = [int(val) for val in ref_version.split(".")]
    check_list = [int(val) for val in check_version.split(".")]

    for ii in range(len(check_list)):
        if len(ref_list) < ii + 1:
            return False
        if ref_list[ii] > check_list[ii]:
            return True
        elif ref_list[ii] < check_list[ii]:
            return False
