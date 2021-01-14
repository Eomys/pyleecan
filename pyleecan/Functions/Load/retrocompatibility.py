def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one"""

    # V 1.0.4 => 1.1.0: New definition for LamSlotMag + SlotMag
    if init_dict["__class__"] == "MachineSIPMSM" and "magnet" not in init_dict["rotor"]:
        print("Old machine version detected, Updating the LamSlotMag object")
        # Moving the magnet (assume only one magnet)
        assert (
            len(init_dict["rotor"]["slot"]["magnet"]) == 1
        ), "LamSlotMag with more than one magnet per pole is no longer available (for now)"
        init_dict["rotor"]["magnet"] = init_dict["rotor"]["slot"]["magnet"][0]
        init_dict["rotor"]["slot"].pop("magnet")
        # Update the slot with the magnet parameters
        init_dict["rotor"]["slot"]["__class__"] = (
            "SlotM" + init_dict["rotor"]["magnet"]["__class__"][-2:]
        )
        init_dict["rotor"]["slot"]["Wmag"] = init_dict["rotor"]["magnet"]["Wmag"]
        init_dict["rotor"]["slot"]["Hmag"] = init_dict["rotor"]["magnet"]["Hmag"]
        if "Rtop" in init_dict["rotor"]["magnet"]:
            init_dict["rotor"]["slot"]["Rtopm"] = init_dict["rotor"]["magnet"]["Rtop"]
        init_dict["rotor"]["magnet"]["__class__"] = "Magnet"
    return init_dict