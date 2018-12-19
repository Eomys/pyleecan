"""Created on June 18th 2018

@author: franco_i
"""
from numpy import arcsin, exp, pi, sqrt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    point_list: list
        A list of Points and rot_sign

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
            + sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1 ** 2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 + self.H3
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        Z7 = Z8 - self.H0
        # Rotation to get the tooth on X axis
        Z7 = Z7 * exp(1j * slot_pitch / 2)
        Z8 = Z8 * exp(1j * slot_pitch / 2)
        Z6 = (
            Z7.real
            - sqrt(-4 * ((Z7.imag - (self.W3 / 2.0 + self.R1)) ** 2 - self.R1 ** 2)) / 2
            + 1j * self.W3 / 2.0
        )
        Z5 = Z6 - self.H3
        rot_sign = -1  # Rotation direction for Arc1
    Z8, Z7, Z6, Z5 = (
        Z8 * exp(-1j * slot_pitch / 2),
        Z7 * exp(-1j * slot_pitch / 2),
        Z6 * exp(-1j * slot_pitch / 2),
        Z5 * exp(-1j * slot_pitch / 2),
    )
    # symetry
    Z4 = Z5.conjugate()
    Z3 = Z6.conjugate()
    Z2 = Z7.conjugate()
    Z1 = Z8.conjugate()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, rot_sign]
