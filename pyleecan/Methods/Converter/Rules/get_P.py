def get_P(self, machine):
    """Select value in machine

    Parameters
    ----------
    self : RuleSimple
        A RuleSimple object
    other_dict : dict

    Return
    ----------
    P_value
    """
    # select value in object machine
    value_split = self.P_obj_path.split(".")

    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = eval('path+"."+value_split[temp]')

    P_value = getattr(
        eval(path),
        value_split[-1],
    )

    return P_value
