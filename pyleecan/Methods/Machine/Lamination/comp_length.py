# -*- coding: utf-8 -*-


def comp_length(self):
    """Compure the total length of the Lamination (including radial
    ventilations duct)

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Lt: float
        Total Lenght of the Lamination [m]

    """
    if self.Nrvd is None or self.Wrvd is None:
        return self.L1
    else:
        return self.L1 + self.Nrvd * self.Wrvd
