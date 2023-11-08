def set_other(self, other_dict, P_value):
    """Set P_value value in other_dict

    Parameters
    ----------
    self : RuleSimple
        A RuleSimple object
    other_dict : dict
        dict created from the file to be converted
    P_value :
        value to set in other_dict


    Return
    ----------
    other_dict
    """
    # Make sure that all the sub-keys exist
    dict_temp = other_dict
    for key in self.other_key_list[:-1]:
        if key not in dict_temp:
            dict_temp[key] = dict()
        dict_temp = dict_temp[key]
    # Set the value
    last_key = self.other_key_list[-1]
    dict_temp[last_key] = P_value

    return other_dict
