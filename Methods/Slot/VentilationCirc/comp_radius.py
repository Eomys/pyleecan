# -*- coding: utf-8 -*-


def comp_radius(self):
    """Compute the radius of the two circle that contains all the ventilation
    ducts

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    (Rmin, Rmax): tuple
        Tuple of circle radius [m]

    """

    self.check()

    Rmin = self.H0 - self.D0 / 2.0
    Rmax = self.H0 + self.D0 / 2.0

    return (Rmin, Rmax)
