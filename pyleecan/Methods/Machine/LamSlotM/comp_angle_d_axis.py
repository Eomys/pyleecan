from numpy import pi


def comp_angle_d_axis(self):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis
    By convention the first magnet is +

    Parameters
    ----------
    self : LamSlotM
        A LamSlotM object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    if self.has_magnet() and self.magnet.type_magnetization == 3:
        return 0
    else:
        return pi / self.get_pole_pair_number() / 2
