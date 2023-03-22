# -*- coding: utf-8 -*-
from matplotlib.patches import Polygon

from ....definitions import config_dict

PATCH_EDGE = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE"]
PATCH_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR"]
PATCH_COLOR_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR_ALPHA"]
PATCH_EDGE_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE_ALPHA"]


def get_patches(
    self, color=PATCH_COLOR, edgecolor=None, is_edge_only=False, linestyle=None
):
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
    linestyle : str
        Line style of the edge {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

    Returns
    -------
    patch_list : list of matplotlib.patches.Polygon
        List of patches corresponding to the surface
    """

    # Set default color
    if edgecolor is None and not is_edge_only:
        edgecolor = PATCH_EDGE
    elif edgecolor is None and is_edge_only:
        edgecolor = PATCH_EDGE_ALPHA
    if is_edge_only:
        color = PATCH_COLOR_ALPHA
    if "--" in edgecolor:
        edgecolor = edgecolor.replace("-", "")
        linestyle = "--"

    # check if the PolarArc is correct
    self.check()

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
    return [
        Polygon(point_list, facecolor=color, edgecolor=edgecolor, linestyle=linestyle)
    ]
