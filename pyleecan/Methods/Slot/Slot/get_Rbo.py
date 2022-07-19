from ....Methods import ParentMissingError


def get_Rbo(self):
    """Return the parent lamination bore radius

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    Rbo: float
        The parent lamination bore radius [m]

    """

    if self.parent is not None:
        if self.is_bore in [True, None]:
            return self.parent.get_Rbo()
        else:
            return self.parent.get_Ryoke()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")
