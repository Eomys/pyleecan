# -*- coding: utf-8 -*-

from numpy import abs as arcsin, exp, pi, cos, tan


def _comp_W(self):
    """Compute W1 and W2 method (cste tooth compatibility)

    Parameters
    ----------
    self : SlotW11_2
        A SlotW11_2 object

    Returns
    -------
    None

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    Harc = Rbo - abs(Z1.real)

    # To compute the slot width we use the fact that
    # alpha_tooth + alpha_slot = slot_pitch
    slot_pitch = 2 * pi / self.Zs

    # H0 and H1 are radial
    if self.is_outwards():
        radius = Rbo + self.get_H1() + self.H0
    else:
        radius = Rbo - self.get_H1() - self.H0

    alpha_T1 = float(arcsin(self.W3 / (2 * radius)))
    alpha_S1 = slot_pitch - 2 * alpha_T1
    self.W1 = 2 * tan(alpha_S1 / 2) * radius

    # define W2
    if self.is_outwards():
        self.W2 = (
            2
            * tan(slot_pitch / 2)
            * (
                Rbo
                - Harc
                + self.H0
                + self.get_H1()
                + self.H2
                - self.R1
                - self.W3 / (2 * tan(slot_pitch / 2) * cos(slot_pitch / 2))
            )
        )

    else:
        self.W2 = (
            2
            * tan(slot_pitch / 2)
            * (
                Rbo
                - Harc
                - self.H0
                - self.get_H1()
                - self.H2
                + self.R1
                - self.W3 / (2 * tan(slot_pitch / 2) * cos(slot_pitch / 2))
            )
        )
