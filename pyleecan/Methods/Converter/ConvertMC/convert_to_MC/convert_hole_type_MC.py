def convert_hole_type_MC(self):
    """Selection correct hole and implementation in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    motor_type = type(self.machine.stator.slot).__name__

    # selection type of Slot
    if motor_type == "HoleM62" and self.machine.rotor.hole.W0_is_rad == False:
        name_slot = "Embedded_Parallel"

    elif motor_type == "HoleM62":
        name_slot = "Embedded_Radial"

    elif motor_type == "HoleM63":
        name_slot = "Embedded_Breadleaof"

    elif motor_type == "HoleM63":
        name_slot = "Interior_Flat(simple)"

    elif motor_type == "HoleM52":
        name_slot = "Interior_Flat(web)"

    elif motor_type == "HoleM60":
        name_slot = "Interior_V(simple)"

    elif motor_type == "HoleM57":
        name_slot = "Interior_V(web)"

    elif motor_type == "HoleM61":
        name_slot = "Interior_U-Shape"

    else:
        raise Exception("Conversion of machine doesn't exist")

    # writting in dict
    if "[Calc_Options]" not in self.other_dict:
        self.other_dict["[Calc_Options]"] = {}
        temp_dict = self.other_dict["[Calc_Options]"]
        temp_dict["Slot_Type"] = name_slot
    else:
        self.other_dict["[Calc_Options]"]["Slot_Type"] = name_slot

    return len(self.machine.rotor.hole)
