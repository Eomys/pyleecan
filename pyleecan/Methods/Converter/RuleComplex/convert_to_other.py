def convert_to_other(self, other_dict, machine):
    """Select value in machine and implements in other_dict

    Parameters
    ----------
    self : RulesComplex
        A RuleComplex object
    other_dict : dict

    machine : Machine

    """
    other_dict = self.P_to_other(self, other_dict)

    return other_dict
