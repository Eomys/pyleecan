# -*- coding: utf-8 -*-

from numpy import sin, pi


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    S: float
        Slot opening surface [m**2]

    """
    if self.is_cstt_tooth and (self.W1 is None or self.W2 is None):
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    Rbo = self.get_Rbo()

    # Wint is the with at the top of the opening
    alpha = self.comp_angle_opening()
    if self.is_outwards():
        Wint = 2 * sin(alpha / 2) * (Rbo + self.H0)
        # Arc between opening H0 and wedge H1
        Sarc = ((Rbo + self.H0) ** 2.0) / 2.0 * (alpha - sin(alpha))
        # The opening part is radial
        S1 = (pi * ((Rbo + self.H0) ** 2) - pi * (Rbo**2)) * alpha / (2 * pi) - Sarc
    else:
        Wint = 2 * sin(alpha / 2) * (Rbo - self.H0)
        # Arc between opening H0 and wedge H1
        Sarc = ((Rbo - self.H0) ** 2.0) / 2.0 * (alpha - sin(alpha))
        # The opening part is radial
        S1 = (pi * (Rbo**2) - pi * ((Rbo - self.H0) ** 2)) * alpha / (2 * pi) + Sarc

    S2 = 0.5 * self.get_H1() * (Wint + self.W1)

    return S1 + S2
