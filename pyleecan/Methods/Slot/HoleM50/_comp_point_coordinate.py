from numpy import arcsin, arctan, cos, exp, array, angle, pi
from numpy import imag as np_imag
from scipy.optimize import fsolve


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """

    Rext = self.get_Rext()

    # magnet pole pitch angle, must be <2*pi/2*p
    alpham = 2 * arcsin(self.W0 / (2 * (Rext - self.H1)))  # angle (Z9,0,Z9')

    Harc = (Rext - self.H1) * (1 - cos(alpham / 2))
    # alpha on schematics
    gammam = arctan((self.H0 - self.H1 - Harc) / (self.W0 / 2.0 - self.W1 / 2.0))
    #  betam = pi/2-alpham/2-gammam;#40.5
    hssp = pi / self.Zh

    x78 = (self.H3 - self.H2) / cos(gammam)  # distance from 7 to 8
    Z9 = Rext - Harc - self.H1 - 1j * self.W0 / 2
    Z8 = Rext - self.H0 - 1j * self.W1 / 2
    Z7 = Rext - self.H0 - x78 - 1j * self.W1 / 2
    Z1 = (Rext - self.H1) * exp(1j * (-hssp + arcsin(self.W3 / (2 * (Rext - self.H1)))))
    Z11 = (Z1 * exp(1j * hssp) + self.H4) * exp(-1j * hssp)
    Z10 = (Z9 * exp(1j * hssp) + self.H4) * exp(-1j * hssp)

    # Magnet coordinate with Z8 as center and x as the top edge of the magnet
    Z8b = self.W2
    Z8c = Z8b + self.W4
    Z5 = Z8b - 1j * self.H3
    Z4 = Z8c - 1j * self.H3
    Z6 = Z5 + 1j * self.H2
    Z3 = Z4 + 1j * self.H2

    Zmag = array([Z8b, Z6, Z5, Z4, Z3, Z8c])
    Zmag = Zmag * exp(1j * angle(Z9 - Z8))
    Zmag = Zmag + Z8

    # final complex numbers Zmag=[Z8b Z6 Z5 Z4 Z3 Z8c]
    (Z8b, Z6, Z5, Z4, Z3, Z8c) = Zmag

    # Rotation so [Z1,Z2] is parallel to the x axis
    Z3r, Z1r, Z6r = Z3 * exp(1j * hssp), Z1 * exp(1j * hssp), Z6 * exp(1j * hssp)
    # numerical resolution to find the last point Z2
    x = fsolve(lambda x: np_imag((Z3r - (Z1r - x)) / (Z6r - Z3r)), self.H3 - self.H2)
    Z2 = (Z1r - x[0]) * exp(-1j * hssp)

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z6
    point_dict["Z7"] = Z7
    point_dict["Z8"] = Z8
    point_dict["Z9"] = Z9
    point_dict["Z10"] = Z10
    point_dict["Z11"] = Z11
    point_dict["Z8c"] = Z8c
    point_dict["Z8b"] = Z8b
    # Symmetry
    point_dict["Z1s"] = Z1.conjugate()
    point_dict["Z2s"] = Z2.conjugate()
    point_dict["Z3s"] = Z3.conjugate()
    point_dict["Z4s"] = Z4.conjugate()
    point_dict["Z5s"] = Z5.conjugate()
    point_dict["Z6s"] = Z6.conjugate()
    point_dict["Z7s"] = Z7.conjugate()
    point_dict["Z8s"] = Z8.conjugate()
    point_dict["Z9s"] = Z9.conjugate()
    point_dict["Z10s"] = Z10.conjugate()
    point_dict["Z11s"] = Z11.conjugate()
    point_dict["Z8cs"] = Z8c.conjugate()
    point_dict["Z8bs"] = Z8b.conjugate()
    return point_dict
