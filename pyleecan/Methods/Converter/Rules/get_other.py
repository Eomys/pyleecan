def get_other(self, other_dict, other_path_list, unit):
    """Select value in other_dict

    Parameters
    ----------
    self : RuleSimple
        A RuleSimple object
    other_path_list : list
        list with path to set value

    Return
    ----------
    other_value
    """

    # selection correct value in other_dict
    dict_temp = other_dict
    for temp in other_path_list:
        dict_temp = dict_temp[temp]

    other_value = dict_temp * unit

    return other_value
