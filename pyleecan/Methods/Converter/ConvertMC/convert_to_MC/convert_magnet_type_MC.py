def convert_magnet_type_MC(self):
    """Selection correct magnet and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # conversion to Motor-CAD
    motor_type = type(self.machine.rotor.slot).__name__

    # selection type of Slot
    if motor_type == "SlotM11":
        name_slot = "Surface_Radial"

    elif motor_type == "":
        name_slot = ""

    else:
        raise Exception("Conversion of machine doesn't exist")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {}
        temp_dict = self.other_dict["[Design_Options]"]
        temp_dict["BPM_Rotor"] = name_slot
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_slot
