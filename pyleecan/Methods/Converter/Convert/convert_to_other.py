def convert_to_other(self, machine):
    """conversion obj machine in dict

    Parameters
    ----------
    machine : Machine
        A pyleecan machine

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """
    self.machine = machine
    self.is_P_to_other = True
    self.other_dict = {}
    self.rules_list = []

    other_unit_dict = self.init_other_unit()
    # conversion machine in dict
    self.other_dict = self.convert(other_unit_dict)
    return self.other_dict
