from ....Methods import ParentMissingError


def get_Rbo(self):
    """Return the parent lamination bore radius
    (to make lam.notch[ii].notch_shape match lam.slot parent)

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
