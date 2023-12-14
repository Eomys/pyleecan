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

    path = ".".join(value_split[:-1])
    # value_split[-1] is the attribut that we want to retrieve ("W1")
    # path is the attribut chain to get the attribut ("machine.stator.slot")

    try:
        P_value = getattr(
            eval(path),
            value_split[-1],
        )
    except AttributeError:
        raise ValueError(
            f"Value equivalent at {path_machine} isn't found in obj machine"
        )

    return P_value
