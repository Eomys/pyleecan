# -*- coding: utf-8 -*-
from matplotlib.patches import Circle

from ....definitions import config_dict

PATCH_EDGE = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE"]
PATCH_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR"]
PATCH_COLOR_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR_ALPHA"]
PATCH_EDGE_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE_ALPHA"]


def get_patches(
    self, color=PATCH_COLOR, edgecolor=None, is_edge_only=False, linestyle=None
):
    """Returns the Circle Patch to be display in matplotlib

    Parameters
    ----------
    self : Circle
        a Circle object
    color :
        the color of the Patch (Default value = PATCH_COLOR)
    edgecolor :
        edgecolor of the Patch (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color
    linestyle : str
        Line style of the edge {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

    Returns
    -------
    patch_list : list of matplotlib.patches.Circle
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

    # check if the Circle is correct
    self.check()
    # the coordinates of the center of the circle
    Zr = self.center.real
    Zi = self.center.imag

    return [
        Circle(
            xy=(Zr, Zi),
            radius=self.radius,
            facecolor=color,
            edgecolor=edgecolor,
            linestyle=linestyle,
        )
    ]
