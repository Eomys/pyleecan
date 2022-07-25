from ....Functions.Geometry.comp_flower_arc import comp_flower_arc
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Methods import ParentMissingError
from numpy import pi, sqrt, exp


def get_bore_line(self, prop_dict=None):
    """Return the bore line description

    Parameters
    ----------
    self : BoreLSRPM
        A BoreLSRPM object
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_list : list
        List of bore lines
    """

    if self.parent is not None:
        if self.is_yoke():
            R = self.parent.get_Ryoke()
        else:
            R = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The Bore object is not inside a Lamination")

    # Compute the shape

    alpha1 = pi / self.N

    # Z1
    Z1 = R * exp(-1j * alpha1)

    # ZC1
    ZC1 = (R - self.Rarc) * exp(-1j * alpha1)
    XC1 = ZC1.real
    YC1 = ZC1.imag

    # Z2
    X2 = sqrt(self.Rarc ** 2 - (self.W1 + YC1) ** 2) + XC1
    Y2 = -self.W1
    Z2 = X2 + 1j * Y2

    Z3 = Z2.conjugate()
    Z4 = Z1.conjugate()

    # Create the lines
    bore_list = list()
    for ii in range(self.N):

        bore_list.append(
            Arc1(
                begin=Z1 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                end=Z2 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                radius=self.Rarc,
                is_trigo_direction=True,
                prop_dict=prop_dict,
            )
        )

        bore_list.append(
            Segment(
                Z2 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                Z3 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                prop_dict=prop_dict,
            )
        )

        bore_list.append(
            Arc1(
                begin=Z3 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                end=Z4 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                radius=self.Rarc,
                is_trigo_direction=True,
                prop_dict=prop_dict,
            )
        )

    return bore_list
