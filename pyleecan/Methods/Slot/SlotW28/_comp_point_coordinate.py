from numpy import arcsin, exp, pi, sqrt
from ....Classes.Arc1 import Arc1


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates
    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))
    slot_pitch = 2 * pi / self.Zs

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z8 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z7 = Z8 + self.H0
        # Rotation to get the tooth on X axis
        Z7 = Z7 * exp(1j * slot_pitch / 2)
        Z8 = Z8 * exp(1j * slot_pitch / 2)
        # Z7 = x7 + 1j*y7
        # Z6 = x + 1j * W3/2
        # C2,Z6 _|_ Z6,Z5 => Re(C2) = Re(Z6)
        # ||Z6,zc2|| = R1 => Zc2 = x + 1j*(W3/2+R1)
        # ||Z7,zc2||² = R1² => (x7-x)²+ (y7-(W3/2+R1))² = R1²

        # x² - 2*x7 x + (x7²+(y7-(W3/2+R1))²-R1²) = 0
        # D = 4*x7² - 4*(x7²+(y7-(W3/2+R1))²-R1²) = -4((y7-(W3/2+R1))²-R1²)
        # x = x7 + sqrt(-4((y7-(W3/2+R1))²-R1²))/2
        Z6 = (
            Z7.real
            + sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1**2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 + self.H3
        rot_sign = 1
    else:  # inward slot
        Z7 = Z8 - self.H0
        # Rotation to get the tooth on X axis
        Z7 = Z7 * exp(1j * slot_pitch / 2)
        Z8 = Z8 * exp(1j * slot_pitch / 2)
        Z6 = (
            Z7.real
            - sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1**2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 - self.H3
        rot_sign = -1

    # Tooth ref to slot
    Z1, Z2, Z3, Z4 = (
        Z8 * exp(-1j * slot_pitch / 2),
        Z7 * exp(-1j * slot_pitch / 2),
        Z6 * exp(-1j * slot_pitch / 2),
        Z5 * exp(-1j * slot_pitch / 2),
    )

    point_dict = dict()
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    # symetry
    point_dict["Z5"] = Z4.conjugate()
    point_dict["Z6"] = Z3.conjugate()
    point_dict["Z7"] = Z2.conjugate()
    point_dict["Z8"] = Z1.conjugate()
    # Center
    A = Arc1(Z2, Z3, rot_sign * self.R1, self.is_outwards())
    point_dict["Zc1"] = A.get_center()
    point_dict["Zc2"] = (point_dict["Z4"] + point_dict["Z5"]) / 2
    point_dict["Zc3"] = point_dict["Zc1"].conjugate()
    return point_dict
