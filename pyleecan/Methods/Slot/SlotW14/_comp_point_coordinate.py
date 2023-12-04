from numpy import arcsin, cos, exp, pi, sin


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()
    hssp = pi / self.Zs

    # alpha is the angle to rotate P0 so ||P1,P9|| = W0
    alpha = arcsin(self.W0 / (2 * Rbo))
    Harc = float(Rbo * (1 - cos(alpha)))
    H1 = self.get_H1()

    Z1 = Rbo * exp(-1j * alpha)
    if self.is_outwards():
        R1 = Rbo - Harc + self.H0 + H1
        Z2 = Z1 + self.H0
    else:
        R1 = Rbo - Harc - self.H0 - H1
        Z2 = Z1 - self.H0
    # In the slot ref: Z3=x7+j*y7 with x7 = R1
    # In the tooth ref: Zt7 = xt7 + j*yt7 with yt7 = W3/2
    # Zt7 = Z3 * exp(1j*hsp) = (x7+jy7)*(cos(hsp)+1j*sin(hsp))
    # yt7 = W3/2 = x7*sin(hsp)+y7*cos(hsp)
    Z3 = R1 + 1j * (self.W3 / 2 - R1 * sin(hssp)) / cos(hssp)

    # Z3t is Z3 in tooth ref
    Z3t = Z3 * exp(1j * hssp)
    if self.is_outwards():
        Z4t = Z3t + self.H3
    else:
        Z4t = Z3t - self.H3
    # In the slot ref: Z5=x5+j*y5 with y5 = 0
    # In the tooth ref: Zt5 = xt5 + j*yt5 with xt5 = xt6
    # Zt5 = Z5 * exp(1j*hsp) = x5*cos(hsp)+1j*x5*sin(hsp)
    # x5 = real(Z4t)/cos(hsp)

    Z5 = Z4t.real / cos(hssp)
    Z4 = Z4t * exp(-1j * hssp)

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z4.conjugate()
    point_dict["Z7"] = Z3.conjugate()
    point_dict["Z8"] = Z2.conjugate()
    point_dict["Z9"] = Z1.conjugate()

    return point_dict
