from ...Functions.Load.import_class import import_class
from ...Functions.labels import HOLEM_LAB, HOLEV_LAB


def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one"""
    convert_list = []
    _search_(init_dict, convert_list)

    for obj_dict in convert_list:
        if is_Winding_dict(obj_dict):
            convert_Winding(obj_dict)
        elif is_HoleUD_dict(obj_dict):
            convert_HoleUD(obj_dict)


def _search_(obj, convert_list, parent=None):
    # add to list for later conversion
    if is_HoleUD_dict(obj):
        convert_list.append(obj)
    elif is_Winding_dict(obj):
        if (
            parent is not None
            and "slot" in parent.keys()
            and "Zs" in parent["slot"].keys()
        ):
            # Add Zs for wind_mat generation
            obj["Zs"] = parent["slot"]["Zs"]
        convert_list.append(obj)
    else:
        # walk through the dict
        for value in obj.values():
            if isinstance(value, dict):
                # recursively search the dict
                _search_(value, convert_list, parent=obj)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        # recursively search the dict
                        _search_(item, convert_list, parent=obj)


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
    """Update the content of the dict"""
    print("Old machine version detected, Updating the HoleUD object")
    for ii in range(len(hole_dict["surf_list"])):
        if "HoleMagnet" in hole_dict["surf_list"][ii]["label"]:
            hole_dict["surf_list"][ii]["label"] = HOLEM_LAB
        else:
            hole_dict["surf_list"][ii]["label"] = HOLEV_LAB


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
    print("Old machine version detected, Updating the Winding object")
    # Update Npcpp
    if "Npcpp" in wind_dict.keys():
        wind_dict["Npcp"] = wind_dict.pop("Npcpp")

    # Update user_wind_mat
    if wind_dict["__class__"] == "WindingUD":
        if "user_wind_mat" in wind_dict.keys():
            wind_dict["wind_mat"] = wind_dict["user_wind_mat"]

    # Update class
    if wind_dict["__class__"] in [
        "WindingCW1L",
        "WindingCW2LR",
        "WindingCW2LT",
        "WindingDW1L",
        "WindingDW2L",
    ]:
        # Load Winding main parameters
        if "qs" in wind_dict.keys():
            qs = wind_dict["qs"]
        else:
            qs = 3
        if "p" in wind_dict.keys():
            p = wind_dict["p"]
        else:
            p = 3
        if "coil_pitch" in wind_dict.keys():
            coil_pitch = wind_dict["coil_pitch"]
        else:
            coil_pitch = 0
        if "Ntcoil" in wind_dict.keys():
            Ntcoil = wind_dict["Ntcoil"]
        else:
            Ntcoil = 1

        if (
            qs is None
            or p is None
            or coil_pitch is None
            or "Zs" not in wind_dict
            or wind_dict["Zs"] is None
        ):
            # Winding not fully defined => Use Star of slot
            wind_dict["__class__"] = "Winding"
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
                # Updating dict
                wind_dict["wind_mat"] = new_wind.wind_mat.tolist()
                wind_dict["__class__"] = "WindingUD"
                wind_dict["Nlayer"] = new_wind.Nlayer
            except Exception:
                # Not able to generate winding matrix => Star of Slot
                wind_dict["__class__"] = "Winding"
