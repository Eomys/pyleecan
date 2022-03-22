from numpy import sqrt


def comp_nb_circumferential_wire(self):
    """Return number of adjacent wires in circumferential direction

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    Nwppc_tan: int
        Number of adjacent wires in circumferential direction

    """

    return int(sqrt(self.Nwppc))
