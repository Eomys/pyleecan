def convert_to_other(self):
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

    self.is_P_to_other = True
    self.other_dict = {}
    self.rules_list = []

    # conversion machine in dict
    self.other_dict = self.convert()
    return self.other_dict
