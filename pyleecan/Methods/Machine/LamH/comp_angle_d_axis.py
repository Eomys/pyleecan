from numpy import pi


def comp_angle_d_axis(self):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis
    By convention the first magnet is +

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    p = self.get_pole_pair_number()
    if self.has_magnet():
        return pi / p / 2
    else:
        return 0
