# -*- coding: utf-8 -*-


def comp_radius(self):
    """Compute the radius of the two circle that contains all the ventilation
    ducts

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    (Rmin, Rmax): tuple
        Tuple of circle radius [m]

    """

    self.check()

    Rmin = self.H0
    Rmax = self.D0 + self.H0

    return (Rmin, Rmax)
