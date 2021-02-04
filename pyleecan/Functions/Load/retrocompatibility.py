def _search_(obj, convert_list):
    # V 1.0.4 => 1.1.0: New definition for LamSlotMag + SlotMag
    if (
        "__class__" in obj.keys()
        and obj["__class__"] == "MachineSIPMSM"
        and "magnet" not in obj["rotor"]
    ):
        # add to list for later conversion
        convert_list.append(obj)
    else:
        # walk through the dict
        for value in obj.values():
            if isinstance(value, dict):
                # recursively search the dict
                _search_(value, convert_list)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        # recursively search the dict
                        _search_(item, convert_list)


def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one"""
    convert_list = []
    _search_(init_dict, convert_list)

    # V 1.0.4 => 1.1.0: New definition for LamSlotMag + SlotMag
    for machine_dict in convert_list:
        print("Old machine version detected, Updating the LamSlotMag object")
        # readability
        rotor = machine_dict["rotor"]
        slot = machine_dict["rotor"]["slot"]

        # Moving the magnet (use only one magnet)
        if len(slot["magnet"]) > 1:
            print(
                "LamSlotMag with more than one magnet per pole "
                + "is not available for now. Only keeping first magnet."
            )
        rotor["magnet"] = slot["magnet"][0]
        slot.pop("magnet")

        # Update the slot with the magnet parameters
        if rotor["magnet"] is not None:
            slot["__class__"] = "SlotM" + rotor["magnet"]["__class__"][-2:]
            slot["Wmag"] = rotor["magnet"]["Wmag"]
            slot["Hmag"] = rotor["magnet"]["Hmag"]
            if "Rtop" in rotor["magnet"]:
                slot["Rtopm"] = rotor["magnet"]["Rtop"]
            rotor["magnet"]["__class__"] = "Magnet"
