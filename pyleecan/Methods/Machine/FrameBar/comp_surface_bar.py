from numpy import pi, arcsin


def comp_surface_bar(self):
    """Compute the surface of the structural Bars

    Parameters
    ----------
    self : FrameBar
        A FrameBar object

    Returns
    -------
    Sbar: float
        Surface of the structural Bars [m**2]

    """
    # #Calculation for rectangular shape
    # n_bar = self._get_Nbar()
    # w_bar = self._get_wbar()
    # h_gap = self.comp_height_gap()
    # Sbar = n_bar * w_bar * h_gap

    # Calculation for circular shape
    r_out = self._get_Rint()
    h_gap = self.comp_height_gap()
    r_in = r_out - h_gap
    rot_angle = 2 * arcsin(self.wbar / 2.0 / r_in)
    Sbar = self.Nbar * pi * (r_out**2 - r_in**2) * rot_angle / (2 * pi)

    return Sbar
