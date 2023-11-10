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

    try:
        path = value_split[0]
        for temp in range(1, len(value_split) - 1):
            path = eval('path+"."+value_split[temp]')

        P_value = getattr(
            eval(path),
            value_split[-1],
        )
    except Exception:
        raise Exception(
            f"Value equivalent at {path_machine} isn't found in obj machine"
        )

    return P_value
