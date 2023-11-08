def set_P(self, machine, other_value):
    """Set value in machine

    Parameters
    ----------
    self : RuleSimple
        A RuleSimple object
    machine : Machine
        A pyleecan machine
    other_value :
        value to set in other_dict


    Return
    ----------
    machine
    """
    # set value in object machine
    value_split = self.P_obj_path.split(".")

    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = eval('path+"."+value_split[temp]')

    setattr(
        eval(path),
        value_split[-1],
        other_value,
    )
    return machine
