from ....Functions.Geometry.comp_flower_arc import comp_flower_arc
from ....Classes.Arc1 import Arc1
from ....Methods import ParentMissingError
from numpy import pi, exp


def get_bore_line(self, label=None):
    """Return the bore line description

    Parameters
    ----------
    self : BoreUD
        A BoreUD object

    Returns
    -------
    bore_list : list
        List of bore lines
    """

    if label is not None:
        for line in self.line_list:
            line.label = label

    return self.line_list
