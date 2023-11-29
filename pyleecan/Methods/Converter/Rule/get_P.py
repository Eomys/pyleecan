def get_P(self, path_machine, machine):
    """Select value in machine

    Parameters
    ----------
    self : Rule
        A Rule object
    machine : Machine
        A obj machine
    path_machine : str
        str with the path in obj machine

    Return
    ----------
    P_value
    """
    # select value in object machine
    value_split = path_machine.split(".")

    # value_split[-1] is the attribut that we want to retrieve ("W1")
    # path is the attribut chain to get the attribut ("machine.stator.slot")
    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = path + "." + value_split[temp]

    try:
        P_value = getattr(
            eval(path),
            value_split[-1],
        )
    except Exception:
        raise ValueError(
            f"Value equivalent at {path_machine} isn't found in obj machine"
        )

    return P_value
