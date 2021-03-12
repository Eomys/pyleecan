from numpy import angle, exp


def comp_normal(self):
    """Compute the normal direction of the Line
    Normal point is "on top" (begin=O and end on Ox)

    Parameters
    ----------
    self : Line
        a Line object

    Returns
    -------
    normal: float
        Angle of the vector between (Zbegin+Zend)/2 (even for arc) and the normal point [rad]
    """

    Zb = self.get_begin()
    Ze = self.get_end()
    Zm = (Zb + Ze) / 2  # "Middle" of the line
    L = self.comp_length() / 3

    # In ref begin=O and end on Ox
    Zm2 = (Zm - Zb) * exp(-1j * angle(Ze - Zb))
    Zn2 = Zm2 + 1j * L

    Zn = Zn2 * exp(1j * angle(Ze - Zb)) + Zb

    return angle(Zn - Zm)
