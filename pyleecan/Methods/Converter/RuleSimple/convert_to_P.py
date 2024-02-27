def convert_to_P(self, other_dict, machine, other_unit_dict):
    """Selects value in other_dict and implements it in machine

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

    # select correct value
    # The value is return in pyleecan unit (SI)
    other_value = self.get_other(other_dict, self.other_key_list, other_unit_dict)

    # possibility to have str in other_value, if other_value is a str we have an equivalent, and we can't multiply a str.
    # The "if" here handles this issue
    if self.scaling_to_P != 1:
        other_value = other_value * self.scaling_to_P

    machine = self.set_P(machine, other_value, self.P_obj_path)

    return machine
