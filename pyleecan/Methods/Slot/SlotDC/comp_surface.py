from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the top of the Slot is an Arc

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    [
        Z1,
        Z2,
        Z3,
        Z4,
        Z5,
        Z6,
        Z7,
        Z8,
        Z9,
        Z10,
        Z11,
        Z12,
        _,
        _,
        _,
    ] = self._comp_point_coordinate()

    Rbo = self.get_Rbo()

    Swind = self.comp_surface_active()
    # Rectangle Z12,Z11,Z2,Z1
    S6 = self.W1 * abs(Z12.real - Z11.real)
    # Top arc of the slot (on bore radius)
    alpha = self.comp_angle_opening()
    Sarc = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    if self.is_outwards():
        return Swind + S6 - Sarc
    else:
        return Swind + S6 + Sarc
