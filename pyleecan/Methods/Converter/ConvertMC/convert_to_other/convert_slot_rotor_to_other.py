def convert_slot_rotor_to_MC(self):
    """Selection correct slot and implementation in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    slot_type = type(self.machine.rotor.slot).__name__

    # selection type of Slot
    if slot_type == "SlotW11":
        name_slot = "Parallel_Tooth"

    elif slot_type == "SlotW30":
        name_slot = "Pear"

    elif slot_type == "SlotW23":
        name_slot = "Rectangular"

    elif slot_type == "SlotW26":
        name_slot = "Round"

    else:
        raise Exception("Conversion of machine doesn't exist")

    self.get_logger().info(f"Conversion {slot_type} into {name_slot}")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"Top_Bar": name_slot}
    else:
        self.other_dict["[Design_Options]"]["Top_Bar"] = name_slot
