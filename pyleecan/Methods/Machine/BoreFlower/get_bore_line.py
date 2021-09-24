from ....Functions.Geometry.comp_flower_arc import comp_flower_arc
from ....Classes.Arc1 import Arc1
from ....Methods import ParentMissingError
from numpy import pi, exp


def get_bore_line(self, prop_dict=None):
    """Return the bore line description

    Parameters
    ----------
    self : BoreFlower
        A BoreFlower object
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_list : list
        List of bore lines
    """

    if self.parent is not None:
        Rbo = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The Bore object is not inside a Lamination")

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
                prop_dict=prop_dict,
            )
        )
    return bore_list
