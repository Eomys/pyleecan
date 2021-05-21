def comp_surface(self):
    """Compute the surface of ALL THE NOTCHES

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object

    Returns
    -------
    Snotch : float
        surface of ALL THE NOTCHES
    """

    return self.notch_shape.Zs * self.notch_shape.comp_surface()
