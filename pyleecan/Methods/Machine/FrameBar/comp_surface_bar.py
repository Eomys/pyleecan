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
    n_bar = self._get_Nbar()
    w_bar = self._get_wbar()
    h_gap = self.comp_height_gap()
    Sbar = n_bar * w_bar * h_gap

    return Sbar
