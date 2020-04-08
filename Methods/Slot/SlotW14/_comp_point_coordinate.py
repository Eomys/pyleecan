from numpy import arcsin, cos, exp, pi, sin, tan, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    point_list: list
        A list of 9 Points and W2

    """
    Rbo = self.get_Rbo()
    hssp = pi / self.Zs

    # alpha is the angle to rotate P0 so ||P1,P9|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))
    Harc = float(Rbo * (1 - cos(alpha)))

    Z9 = Rbo * exp(-1j * alpha)
    if self.is_outwards():
        R1 = Rbo - Harc + self.H0 + self.H1
        Z8 = Z9 + self.H0
    else:
        R1 = Rbo - Harc - self.H0 - self.H1
        Z8 = Z9 - self.H0
    # In the slot ref: Z7=x7+j*y7 with x7 = R1
    # In the tooth ref: Zt7 = xt7 + j*yt7 with yt7 = W3/2
    # Zt7 = Z7 * exp(1j*hsp) = (x7+jy7)*(cos(hsp)+1j*sin(hsp))
    # yt7 = W3/2 = x7*sin(hsp)+y7*cos(hsp)
    Z7 = R1 + 1j * (self.W3 / 2 - R1 * sin(hssp)) / cos(hssp)

    # Z7t is Z7 in tooth ref
    Z7t = Z7 * exp(1j * hssp)
    if self.is_outwards():
        Z6t = Z7t + self.H3
    else:
        Z6t = Z7t - self.H3
    # In the slot ref: Z5=x5+j*y5 with y5 = 0
    # In the tooth ref: Zt5 = xt5 + j*yt5 with xt5 = xt6
    # Zt5 = Z5 * exp(1j*hsp) = x5*cos(hsp)+1j*x5*sin(hsp)
    # x5 = real(Z6t)/cos(hsp)

    Z5 = Z6t.real / cos(hssp)
    Z6 = Z6t * exp(-1j * hssp)

    # Symmetry
    Z4 = Z6.conjugate()
    Z3 = Z7.conjugate()
    Z2 = Z8.conjugate()
    Z1 = Z9.conjugate()

    return [Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
