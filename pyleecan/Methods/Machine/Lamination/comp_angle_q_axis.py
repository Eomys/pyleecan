from numpy import pi


def comp_angle_q_axis(self):
    """Compute the angle between the X axis and the first q+ axis
    By convention a "Tooth" is centered on the X axis
    By convention the first magnet is +

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    q_angle = self.comp_angle_q_axis()
    p = self.get_pole_pair_number()
    return q_angle + pi / p / 2
