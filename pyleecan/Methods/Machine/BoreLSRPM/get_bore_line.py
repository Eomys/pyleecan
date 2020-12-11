from ....Functions.Geometry.comp_flower_arc import comp_flower_arc
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Methods import ParentMissingError
from numpy import pi, sqrt, exp


def get_bore_line(self, label=""):
    """Return the bore line description

    Parameters
    ----------
    self : BoreLSRPM
        A BoreLSRPM object

    Returns
    -------
    bore_list : list
        List of bore lines
    """

    if self.parent is not None:
        Rbo = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")

    # Compute the shape

    alpha1 = pi / self.N

    # Z1
    Z1 = Rbo * exp(-1j * alpha1)

    # ZC1
    ZC1 = (Rbo - self.Rarc) * exp(-1j * alpha1)
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
                label=label,
            )
        )

        bore_list.append(
            Segment(
                Z2 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                Z3 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
            )
        )

        bore_list.append(
            Arc1(
                begin=Z3 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                end=Z4 * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                radius=self.Rarc,
                is_trigo_direction=True,
                label=label,
            )
        )

    return bore_list
