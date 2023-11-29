def convert_magnet_to_MC(self):
    """Selects correct magnet and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # conversion to Motor-CAD
    magnet_type = type(self.machine.rotor.slot).__name__

    # selection type of Slot
    if (
        magnet_type == "SlotM11" and self.machine.rotor.slot.H0 == 0
    ):  # magnet is on surface of rotor
        name_slot = "Surface_Radial"

    elif (
        magnet_type == "SlotM15" and self.machine.rotor.slot.H0 == 0
    ):  # magnet is on surface of rotor
        name_slot = "Surface_Parallel"

    elif magnet_type == "SlotM13":
        name_slot = "Surface_Breadleaof"

    elif magnet_type == "SlotM11":
        name_slot = "Inset_Radial"

    elif magnet_type == "SlotM15":
        name_slot = "Inset_Parallel"

    elif magnet_type == "SlotM12":
        name_slot = "Inset_Breadleaof"

    elif magnet_type == "SlotM16":
        name_slot = "Spoke"

    else:
        raise ValueError(f"Conversion of a {magnet_type} magnet doesn't exist")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"BPM_Rotor": name_slot}
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_slot

    self.get_logger().info(f"Conversion {magnet_type} into {name_slot}")
