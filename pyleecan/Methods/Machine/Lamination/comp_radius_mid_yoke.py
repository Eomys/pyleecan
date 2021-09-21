def comp_radius_mid_yoke(self):
    """Compute the Lamination middle of the yoke radius

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Ry: float
        middle of the yoke radius [m]

    """

    Hyoke = self.comp_height_yoke()
    if self.is_internal:
        return self.Rint + Hyoke / 2
    else:
        return self.Rext - Hyoke / 2
