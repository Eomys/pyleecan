def convert_to_P(self, other_dict, machine, other_unit_dict):
    """Selects value in other_dict and implements it in machine

    Parameters
    ----------
    self : RulesComplex
        A RuleComplex object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)
    """
    machine = self.other_to_P(self, machine, other_dict, other_unit_dict)

    return machine
