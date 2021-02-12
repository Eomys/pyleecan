from numpy import angle, exp


def comp_normal(self, return_type=2):
    """Compute the normal direction of the Line
    Normal point is "on top" (begin=O and end on Ox)

    Parameters
    ----------
    self : Line
        a Line object
    return_type: int
        0: (Zbegin+Zend)/2 (even for arc) and the normal point as tuple
        1: Z2 - Z1 (with Z1 and Z2 the points from return_type 0)
        2: the angle of the vector of return_type 1 according to Ox [rad]

    Returns
    -------
    normal: tuple, complex, float
        cf return_type
    """

    Zb = self.get_begin()
    Ze = self.get_end()
    Zm = (Zb + Ze) / 2  # "Middle" of the line
    L = self.comp_length() / 3

    # In ref begin=O and end on Ox
    Zm2 = (Zm - Zb) * exp(-1j * angle(Ze - Zb))
    Zn2 = Zm2 + 1j * L

    Zn = Zn2 * exp(1j * angle(Ze - Zb)) + Zb

    if return_type == 0:
        return (Zm, Zn)
    elif return_type == 1:
        return Zn - Zm
    else:
        return angle(Zn - Zm)
