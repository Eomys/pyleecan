def convert_to_P(self, file_path):
    """Convert a "other" file to a Pyleecan machine

    Parameters
    ----------
    self : Convert
        A Convert object
    file_path : str
        A path to "other" file to convert

    Returns
    ---------
    machine : Machine
        The converted pyleecan machine
    """
    self.is_P_to_other = False  # Select rules direction
    # conversion file in dict
    self.convert_other_to_dict(file_path)
    self.rules_list = []

    # conversion dict into machine
    self.convert()
    return self.machine
