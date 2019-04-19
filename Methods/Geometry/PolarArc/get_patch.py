# -*- coding: utf-8 -*-
from matplotlib.patches import Polygon

from pyleecan.Methods.Machine import (
    PATCH_COLOR,
    PATCH_EDGE,
    PATCH_COLOR_ALPHA,
    PATCH_EDGE_ALPHA,
)


def get_patch(self, color=PATCH_COLOR, edgecolor=PATCH_EDGE, is_edge_only=False):
    """Returns the PolarArc Patch to be display in matplotlib
    Parameters
    ----------
    self : PolarArc
        a PolarArc object
    color :
        The color of the patch (Default value = PATCH_COLOR)
    edgecolor :
        The color of the edgecolor (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color

    Returns
    -------
    patch : matplotlib.patches.Polygon
        The patch corresponding to the surface
    """

    # check if the PolarArc is correct
    self.check()

    if is_edge_only:
        color = PATCH_COLOR_ALPHA
        edgecolor = PATCH_EDGE_ALPHA

    line_list = self.get_lines()
    Z_list = list()
    # For each  Line discretize
    for line in line_list:
        Z_list.extend(line.discretize())

    # abscissa coordinate
    Zr_list = list()
    # ordinate coordinate
    Zi_list = list()

    for ii in range(len(Z_list)):
        Zr_list.append(Z_list[ii].real)
        Zi_list.append(Z_list[ii].imag)
    point_list = list(zip(Zr_list, Zi_list))
    return Polygon(point_list, facecolor=color, edgecolor=edgecolor)
