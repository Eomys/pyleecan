def convert_to_other(self, other_dict, machine, other_unit_dict):
    """Select value in machine and implements in other_dict

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

    P_value = self.get_P(self.P_obj_path, machine)

    # possibility to have str in other_value and conversion
    if self.scaling_to_P != 1:
        P_value = P_value / self.scaling_to_P

    # set value in other_dict
    other_dict = self.set_other(
        other_dict, P_value, other_unit_dict, self.other_key_list
    )

    return other_dict
