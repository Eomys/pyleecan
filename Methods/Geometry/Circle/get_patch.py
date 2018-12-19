# -*- coding: utf-8 -*-
from matplotlib.patches import Circle

from pyleecan.Methods.Machine import PATCH_COLOR, PATCH_EDGE


def get_patch(self, color=PATCH_COLOR, edgecolor=PATCH_EDGE):
    """Returns the Circle Patch to be display in matplotlib

    Parameters
    ----------
    self : Circle
          a Circle object
    color :
        the color of the Patch (Default value = PATCH_COLOR)
    edgecolor :
        edgecolor of the Patch (Default value = PATCH_EDGE)

    Returns
    -------
    patch : matplotlib.patches.Circle
        The patch corresponding to the surface
    """

    # check if the Circle is correct
    self.check()
    # the coordinates of the center of the circle
    Zr = self.center.real
    Zi = self.center.imag

    return Circle(xy=(Zr, Zi), radius=self.radius, facecolor=color, edgecolor=edgecolor)
