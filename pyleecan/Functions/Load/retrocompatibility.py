from ...Functions.Load.import_class import import_class


def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one"""
    convert_list = []
    _search_(init_dict, convert_list)

    # V 1.0.4 => 1.1.0: New definition for LamSlotMag + SlotMag
    for obj_dict in convert_list:
        if is_LamSlotMag_dict(obj_dict):
            convert_LamSlotMag(obj_dict)
        elif is_Winding_dict(obj_dict):
            convert_Winding(obj_dict)


def _search_(obj, convert_list, parent=None):
    # add to list for later conversion
    if is_LamSlotMag_dict(obj):
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
# V 1.0.4 => 1.1.0
# LamSlotMag list of magnet to single magnet
# SlotMag and SlotWind unification
############################################
def is_LamSlotMag_dict(obj_dict):
    """Check if the object need to be updated for LamSlotMag"""
    return (
        "__class__" in obj_dict.keys()
        and obj_dict["__class__"] == "LamSlotMag"
        and "magnet" not in obj_dict.keys()
    )


def convert_LamSlotMag(lam_dict):
    """Update the content of the dict"""
    print("Old machine version detected, Updating the LamSlotMag object")
    # readability
    slot = lam_dict["slot"]

    # Moving the magnet (use only one magnet)
    if len(slot["magnet"]) > 1:
        print(
            "LamSlotMag with more than one magnet per pole "
            + "is not available for now. Only keeping first magnet."
        )
    lam_dict["magnet"] = slot["magnet"][0]
    slot.pop("magnet")

    # Update the slot with the magnet parameters
    if lam_dict["magnet"] is not None:
        slot["__class__"] = "SlotM" + lam_dict["magnet"]["__class__"][-2:]
        slot["Wmag"] = lam_dict["magnet"]["Wmag"]
        slot["Hmag"] = lam_dict["magnet"]["Hmag"]
        if "Rtop" in lam_dict["magnet"]:
            slot["Rtopm"] = lam_dict["magnet"]["Rtop"]
        lam_dict["magnet"]["__class__"] = "Magnet"


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

    # Update class
    if wind_dict["__class__"] in [
        "WindingCW1L",
        "WindingCW2LR",
        "WindingCW2LT",
        "WindingDW1L",
        "WindingDW2L",
    ]:
        old_class = wind_dict["__class__"]
        wind_dict["__class__"] = "WindingUD"
        WindingUD = import_class("pyleecan.Classes", "WindingUD")
        new_wind = WindingUD()
        if "qs" in wind_dict.keys():
            new_wind.qs = wind_dict["qs"]
        else:
            new_wind.qs = 3
        if "p" in wind_dict.keys():
            new_wind.p = wind_dict["p"]
        else:
            new_wind.p = 3
        if "coil_pitch" in wind_dict.keys():
            new_wind.coil_pitch = wind_dict["coil_pitch"]
        else:
            new_wind.coil_pitch = 0
        if "Ntcoil" in wind_dict.keys():
            new_wind.Ntcoil = wind_dict["Ntcoil"]
        else:
            new_wind.Ntcoil = 1
        # Generate Winding matrix
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
        wind_dict["wind_mat"] = new_wind.wind_mat.tolist()
        wind_dict["Nlayer"] = new_wind.Nlayer
