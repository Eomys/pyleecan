from numpy import sqrt


def comp_nb_radial_wire(self):
    """Return number of adjacent wires in radial direction

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    Nwppc_rad: int
        Number of adjacent wires in radial direction

    """

    return int(sqrt(self.Nwppc))
