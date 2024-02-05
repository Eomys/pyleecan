from collections.abc import ValuesView


def values(self) -> ValuesView:
    """Return the solutions of the solution_dict

    Returns
    -------
    _type_
        _description_
    """
    return self.solution_dict.values()
