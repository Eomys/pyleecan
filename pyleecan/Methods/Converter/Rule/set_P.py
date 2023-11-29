def set_P(self, machine, other_value, path):
    """Set value in machine

    Parameters
    ----------
    self : Rule
        A Rule object
    machine : Machine
        A pyleecan machine
    other_value :
        value to set in other_dict
    path : str
        path to set the value


    Return
    ----------
    machine
    """
    # set value in object machine
    value_split = path.split(".")

    # value_split[-1] is the attribut that we want to set ("W1")
    # path is the attribut chain to set the attribut ("machine.stator.slot")
    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = eval('path+"."+value_split[temp]')

    setattr(
        eval(path),
        value_split[-1],
        other_value,
    )
    return machine
