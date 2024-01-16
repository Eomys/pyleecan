from collections.abc import KeysView


def keys(self) -> KeysView:
    """Return the keys of the solution_dict

    Returns
    -------
    _type_
        _description_
    """
    return self.solution_dict.keys()
