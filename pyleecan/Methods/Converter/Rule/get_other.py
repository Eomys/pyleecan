def get_other(self, other_dict, other_path_list, other_unit_dict):
    """Select value in other_dict and change the value to be in SI

    Parameters
    ----------
    self : Rule
        A Rule object
    other_dict : dict
        dict with all other param
    other_path_list : list
        list with path to set value ( ["[Dimensions]", "Pole_Arc"])
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Return
    ----------
    other_value
    """

    unit = other_unit_dict[self.unit_type]

    try:
        # selection correct value in other_dict
        for temp in other_path_list:
            other_dict = other_dict[temp]
    except AttributeError:
        raise ValueError(
            f"Value equivalent at {other_path_list} isn't found in other_dict"
        )

    other_value = other_dict * unit

    return other_value  # return in SI
