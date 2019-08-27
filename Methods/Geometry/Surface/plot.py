# -*- coding: utf-8 -*-

from matplotlib.pyplot import axis, legend

from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import PATCH_COLOR, PATCH_EDGE


def plot(self, fig=None, color=PATCH_COLOR, edgecolor=PATCH_EDGE, is_edge_only=False):
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

    Returns
    -------
    None
    """

    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")

    axes.add_patch(
        self.get_patch(color=color, edgecolor=edgecolor, is_edge_only=is_edge_only)
    )

    # Axis Setup
    axis("equal")

    fig.show()
