def convert_to_P(self, other_dict, machine):
    """Select value in other_dict and implements in machine

    Parameters
    ----------
    self : RulesComplex
        A RuleComplex object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    """
    machine = self.other_to_P(self, machine)

    return machine
