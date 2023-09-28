from numpy import sin


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    S: float
        Slot opening surface [m**2]

    """

    Rbo = self.get_Rbo()

    S0 = self.H0 * self.W0
    S1 = self.H1 * self.W1

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    # Selection type Wedge
    if self.wedge_type == 0:
        if self.is_outwards():
            return S1 + S0 - Sarc
        else:
            return S1 + S0 + Sarc

    if self.wedge_type == 1:
        if self.is_outwards():
            return S0 - Sarc
        else:
            return S0 + Sarc
