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
        if self.is_yoke():
            R = self.parent.get_Ryoke()
        else:
            R = self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The Bore object is not inside a Lamination")

    # Compute the shape
    (alpha_lim, zL, zR) = comp_flower_arc(2 * pi / self.N, self.Rarc, R)

    # Create the lines
    bore_list = list()
    for ii in range(self.N):
        rot = exp(1j * (2 * pi / self.N * (ii - 1) + self.alpha))
        arc = Arc1(begin=zR * rot, end=zL * rot, radius=self.Rarc, prop_dict=prop_dict)
        bore_list.append(arc)
    return bore_list
