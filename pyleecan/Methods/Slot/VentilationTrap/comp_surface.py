# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the surface of all the axial ventilation ducts

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object

    Returns
    -------
    surface: float
        Axial ventilation ducts total surface [m**2]

    """

    self.check()

    return (self.W1 + self.W2) * 0.5 * self.D0 * self.Zh
