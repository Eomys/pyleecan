def convert_to_P(self, other_dict, machine, other_unit_dict):
    """Select value in other_dict and implements in machine

    Parameters
    ----------
    self : RuleSimple
        A RuleSimple object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    """
    # selection correct value

    other_value = self.get_other(
        other_dict, self.other_key_list, other_unit_dict
    )  # Return in SI

    # possibility to have str in other_value
    if self.scaling_to_P != 1:
        other_value = other_value * self.scaling_to_P

    machine = self.set_P(machine, other_value, self.P_obj_path)

    return machine
