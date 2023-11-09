def convert_to_other(self, other_dict, machine, other_unit_dict):
    """Select value in machine and implements in other_dict

    Parameters
    ----------
    self : RulesComplex
        A RuleComplex object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    """
    other_dict = self.P_to_other(self, machine, other_dict)

    return other_dict
