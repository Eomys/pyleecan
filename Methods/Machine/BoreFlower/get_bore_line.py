from pyleecan.Functions.Geometry.comp_flower_arc import comp_flower_arc
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Methods import ParentMissingError
from numpy import pi, exp


def get_bore_line(self, label=""):
    """Return the bore line description

    Parameters
    ----------
    self : BoreFlower
        A BoreFlower object

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
    (alpha_lim, z_top_left, z_top_right) = comp_flower_arc(
        2 * pi / self.N, self.Rarc, Rbo
    )

    # Create the lines
    bore_list = list()
    for ii in range(self.N):
        bore_list.append(
            Arc1(
                begin=z_top_right * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                end=z_top_left * exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha)),
                radius=self.Rarc,
                is_trigo_direction=True,
                label=label,
            )
        )
    return bore_list
