def convert_to_P(self, file_path):
    """conversion file in obj machine

    Parameters
    ----------
    path_to_other : str
        A path to file

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """

    self.is_P_to_other = False
    self.file_path = file_path
    # conversion file in dict
    self.other_dict = self.convert_other_to_dict()
    self.rules_list = []

    # conversion dict in machine
    machine = self.convert()

    return machine
