from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW30
        A SlotW30 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    point_dict = self._comp_point_coordinate()
    if self.R2 != 0:
        Z7 = point_dict["Z7"]
        Z6 = point_dict["Z6"]
    else:
        Z7 = point_dict["Z60"]
        Z6 = point_dict["Z80"]

    Rbo = self.get_Rbo()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Harc = float(Rbo * (1 - cos(alpha / 2)))

    if self.is_outwards():
        return abs(Z7) - Rbo

    else:
        return abs((Z7 + Z6) / 2 - Rbo)
