# -*- coding: utf-8 -*-

from numpy import abs as np_abs, arcsin, exp, pi, sin


def _comp_W(self):
    """Compute W1 and W2 method (cste tooth compatibility)

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object
    Zs : int
        Number of Slot

    Returns
    -------
    None

    """
    Rbo = self.get_Rbo()

    # To compute the slot width we use the fact that
    # alpha_tooth + alpha_slot = slot_pitch
    slot_pitch = 2 * pi / self.Zs

    # H0 and H1 are radial
    if self.is_outwards():
        R1 = Rbo + self.get_H1() + self.H0
    else:
        R1 = Rbo - self.get_H1() - self.H0

    alpha_T1 = float(arcsin(self.W3 / (2 * R1)))
    alpha_S1 = slot_pitch - 2 * alpha_T1
    self.W1 = 2 * sin(alpha_S1 / 2) * R1

    # H2 is parallel to the tooth axis
    if self.is_outwards():
        R2 = np_abs(R1 * exp(1j * alpha_T1) + self.H2)
    else:
        R2 = np_abs(R1 * exp(1j * alpha_T1) - self.H2)

    alpha_T2 = float(arcsin(self.W3 / (2 * R2)))
    alpha_S2 = slot_pitch - 2 * alpha_T2
    self.W2 = 2 * sin(alpha_S2 / 2) * R2
