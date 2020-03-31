# -*- coding: utf-8 -*-
from matplotlib.patches import Polygon
from pyleecan.Methods.Machine import (
    PATCH_COLOR,
    PATCH_EDGE,
    PATCH_COLOR_ALPHA,
    PATCH_EDGE_ALPHA,
)


def get_patches(self, color=PATCH_COLOR, edgecolor=PATCH_EDGE, is_edge_only=False):
    """Returns the PolarArc Patch to be display in matplotlib

    Parameters
    ----------
    self : SurfLine
        a SurfLine object
    color :
        the color of the patch (Default value = PATCH_COLOR)
    edgecolor :
        the edge color of the patch (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color

    Returns
    -------
    patch_list : list of matplotlib.patches.Polygon
        List of patches corresponding to the surface

    """
    patch_list = self.out_surf.get_patches(
        color=color, edgecolor=edgecolor, is_edge_only=is_edge_only
    )
    # No color for inner surface
    patch_list.extend(self.in_surf.get_patches(is_edge_only=is_edge_only))
    return patch_list
