from numpy import pi


def comp_width_opening(self, is_curved=False):
    """Compute the average opening width of the Slot

    Parameters
    ----------
    self : Slot
        A Slot object
    is_curved : bool
        width opening curved or straight

    Returns
    -------
    W0: float
        Average opening width of the slot [m] or [rad]
    """

    if is_curved:
        R = self.get_Rbo()
        alpha = self.comp_angle_opening()
        Zs = self.parent.get_Zs()
        return 2 * pi * R / Zs - alpha * R
    else:
        line_list = self.build_geometry()
        Z1 = line_list[0].get_begin()
        Z2 = line_list[-1].get_end()
        return abs(Z2 - Z1)
