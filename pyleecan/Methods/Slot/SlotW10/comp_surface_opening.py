from numpy import sin


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation)

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    Sop: float
        Slot opening surface [m**2]

    """

    Rbo = self.get_Rbo()

    S1 = self.H0 * self.W0
    H1 = self.get_H1()
    S2 = 0.5 * (self.W0 + self.W1) * H1

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + S2 - Sarc
    else:
        return S1 + S2 + Sarc
