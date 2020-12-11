from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the top of the Slot is an Arc

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    H = self.R3 + self.H3 + self.H2 + self.H1

    # Computation of the arc height
    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    if self.is_outwards():
        return H - Harc
    else:
        return H + Harc
