from ....Methods import ParentMissingError


def get_Ryoke(self):
    """Return the parent lamination yoke radius
    (to make lam.notch[ii].notch_shape match lam.slot parent)

    Parameters
    ----------
    self : Notch
        A Notch object

    Returns
    -------
    Ryoke: float
        The parent lamination yoke radius [m]

    """

    if self.parent is not None:
        return self.parent.get_Ryoke()
    else:
        raise ParentMissingError("Error: The notch is not inside a Lamination")
