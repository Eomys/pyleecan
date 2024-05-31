from numpy import pi


def comp_surface_gap(self):
    """Compute the surface of the Gap between the Frame and outer Lamination

    Parameters
    ----------
    self : FrameBar
        A FrameBar object

    Returns
    -------
    Sgap: float
        Surface of the Gap [m**2]

    """

    # Surface of the external disk
    S_ext = (self.Rext**2) * pi
    # Surface of the internal disk
    S_int = (self.Rint**2) * pi
    # Surface of the bars
    S_bar = self.comp_surface_bar()

    Sgap = S_ext - S_int - S_bar

    return Sgap
