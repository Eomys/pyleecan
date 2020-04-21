from ....Methods import ParentMissingError


def get_Rbo(self):
    """Return the parent lamination bore radius

    Parameters
    ----------
    self : Notch
        A Notch object

    Returns
    -------
    Rbo: float
        The parent lamination bore radius [m]

    """

    if self.parent is not None:
        return self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The notch is not inside a Lamination")
