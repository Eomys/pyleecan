from numpy import arcsin, exp, pi, sqrt, sin, cos


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rbo = self.get_Rbo()

    hsp = pi / self.Zs  # Half slot pitch

    # ZXt => Complex coordinate in the tooth ref
    # ZX => Complex coordinate in the slot ref
    y1t = self.W1 + self.W3 / 2
    # Point Zch slot midium high point
    Zch = Rbo + self.H2
    # Point Zcl slot midium low point
    Zcl = Rbo

    # relation bewteen the axis tooth and the axis slot
    Zcht = Zch * exp(1j * hsp)
    xcht = Zch * cos(hsp)
    ycht = Zch * sin(hsp)

    Zclt = Zcl * exp(1j * hsp)
    xclt = Zcl * cos(hsp)
    yclt = Zcl * sin(hsp)

    # Line Zch Zcl
    # y=-(xcht-xclt)/(ycht-yclt)*x+ycht+xcht*(xcht-xclt)/(ycht-yclt)

    # Z4
    x4t = (
        (self.W1 + self.W3 / 2 - ycht - xcht * (xcht - xclt) / (ycht - yclt))
        * -(ycht - yclt)
        / (xcht - xclt)
    )
    y4t = (
        -(xcht - xclt) / (ycht - yclt) * x4t
        + ycht
        + xcht * (xcht - xclt) / (ycht - yclt)
    )
    Z4t = x4t + 1j * y4t
    Z4 = Z4t * exp(-1j * hsp)
    # Z3
    x3t = x4t
    y3t = y4t - self.W1 + self.R1
    Z3t = x3t + 1j * y3t
    Z3 = Z3t * exp(-1j * hsp)
    # Z2
    x2t = x3t - self.R1
    y2t = self.W3 / 2
    Z2t = x2t + 1j * y2t
    Z2 = Z2t * exp(-1j * hsp)
    # Z1
    y1t = self.W3 / 2
    x1t = sqrt((Rbo) ** 2 - (y1t) ** 2)
    Z1t = x1t + 1j * y1t
    Z1 = Z1t * exp(-1j * hsp)

    # Z9 damper winding point

    x9t = x1t + self.H3
    y9t = self.W3 / 2
    Z9t = x9t + 1j * y9t
    Z9 = Z9t * exp(-1j * hsp)

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z4.conjugate()
    point_dict["Z6"] = Z3.conjugate()
    point_dict["Z7"] = Z2.conjugate()
    point_dict["Z8"] = Z1.conjugate()
    point_dict["Z9"] = Z9
    point_dict["Z10"] = Z9.conjugate()
    point_dict["Zcl"] = Rbo
    point_dict["Zcm"] = Rbo + self.H3
    point_dict["Zch"] = Rbo + self.H2
    point_dict["Zmid"] = (point_dict["Zcl"] + point_dict["Zch"]) / 2.0
    # Zc1
    xc1 = Z2.real
    yc1 = Z3.imag
    Zc1 = (xc1 + 1j * yc1).conjugate()

    point_dict["Zc1"] = Zc1

    return point_dict
