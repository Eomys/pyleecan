def set_other(self, other_dict, P_value, other_unit_dict, path_list):
    """Set P_value value in other_dict

    Parameters
    ----------
    self : Rule
        A Rule object
    other_dict : dict
        dict created from the file to be converted
    P_value :
        value to set in other_dict
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)
    path_list : list
        list with path to set the value


    Return
    ----------
    other_dict
    """
    unit = other_unit_dict[self.unit_type]

    P_value = P_value / unit  # set in correct unit

    # Make sure that all the sub-keys exist
    dict_temp = other_dict
    for key in path_list[:-1]:
        if key not in dict_temp:
            dict_temp[key] = dict()
        dict_temp = dict_temp[key]

    # Set the value
    last_key = path_list[-1]
    dict_temp[last_key] = P_value

    return other_dict
