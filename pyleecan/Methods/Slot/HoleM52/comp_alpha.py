# -*- coding: utf-8 -*-

from numpy import arcsin, pi


def comp_alpha(self):
    """The opening angle with a W3 teeth width and Rbo - H0 radius

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    alpha: float
        Angle between P1 and P9 (cf schematics) [rad]

    """
    Rbo = self.get_Rbo()

    alpha_tooth = 2 * arcsin(self.W3 / (2 * (Rbo - self.H0)))
    slot_pitch = 2 * pi / self.Zh

    return slot_pitch - alpha_tooth
