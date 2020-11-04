# -*- coding: utf-8 -*-

from matplotlib.pyplot import axis, legend

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

PATCH_EDGE = config_dict["PLOT"]["COLOR_DICT"]["PATCH_EDGE"]
PATCH_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR"]


def plot(
    self,
    fig=None,
    color=PATCH_COLOR,
    edgecolor=PATCH_EDGE,
    is_edge_only=False,
    linestyle=None,
    is_disp_point_ref=False,
    is_show_fig=True,
):
    """Plot the Surface patch in a matplotlib fig

    Parameters
    ----------
    self : Surface
        A Surface object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
    color :
        the color of the patch (Default value = PATCH_COLOR)
    edgecolor :
        the edge color of the patch (Default value = PATCH_EDGE)
    is_edge_only: bool
        To set the transparancy of the face color to 0 and 1 for the edge color
    linestyle : str
        Line style of the edge {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    is_disp_point_ref : bool
        True to add the point_ref
    is_show_fig : bool
        To call show at the end of the methods

    Returns
    -------
    None
    """

    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")

    patches = self.get_patches(
        color=color, edgecolor=edgecolor, is_edge_only=is_edge_only, linestyle=linestyle
    )
    for patch in patches:
        axes.add_patch(patch)

    if is_disp_point_ref:
        axes.plot(self.point_ref.real, self.point_ref.imag, "kx")
    # Axis Setup
    axis("equal")

    if is_show_fig:
        fig.show()
