from collections.abc import ItemsView


def items(self) -> ItemsView:
    """Return the keys and values of the solution_dict

    Returns
    -------
    _type_
        _description_
    """
    return self.solution_dict.items()
