def convert_slot_type_MC(self):
    """Selection correct slot and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    motor_type = type(self.machine.stator.slot).__name__

    # selection type of Slot
    if motor_type == "SlotW11":
        name_slot = "Parallel_Tooth"

    elif motor_type == "SlotW14":
        name_slot = "Parallel_tooth_SqB"

    elif motor_type == "SlotW21":
        name_slot = "Parallel_Slot"

    elif motor_type == "SlotW23":
        name_slot = "Tapered_slot"

    elif motor_type == "SlotW29":
        name_slot = "Form_Wound"

    else:
        raise Exception("Conversion of machine doesn't exist")

    # writting in dict
    if "[Calc_Options]" not in self.other_dict:
        self.other_dict["[Calc_Options]"] = {}
        temp_dict = self.other_dict["[Calc_Options]"]
        temp_dict["Slot_Type"] = name_slot
    else:
        self.other_dict["[Calc_Options]"]["Slot_Type"] = name_slot
