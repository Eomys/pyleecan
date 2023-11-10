def get_other(self, other_dict, other_path_list, other_unit_dict):
    """Select value in other_dict

    Parameters
    ----------
    self : Rule
        A Rule object
    other_dict : dict
        dict with all other param
    other_path_list : list
        list with path to set value
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Return
    ----------
    other_value
    """

    unit = other_unit_dict[self.unit_type]

    try:
        # selection correct value in other_dict
        dict_temp = other_dict
        for temp in other_path_list:
            dict_temp = dict_temp[temp]
    except Exception:
        raise Exception(
            f"Value equivalent at {other_path_list} isn't found in other_dict"
        )

    other_value = dict_temp * unit

    return other_value
