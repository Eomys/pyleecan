# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

SHAFT_COLOR = config_dict["color_dict"]["SHAFT_COLOR"]


def plot(self, fig=None, sym=1, alpha=0, delta=0, is_edge_only=False):
    """Plot the Shaft in a matplotlib fig

    Parameters
    ----------
    self : Shaft
        A Shaft object
    fig :
        if none, open a new fig and plot, else add to the current
        one (Default value = None)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches

    Returns
    -------
    None
    """

    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    # Get the shaft surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        patches.extend(surf.get_patches(color=SHAFT_COLOR, is_edge_only=is_edge_only))
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Shaft")
    for patch in patches:
        axes.add_patch(patch)
    axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Drsh * 0.6
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    # Add legend
    if not is_edge_only:
        patch_leg.append(Patch(color=SHAFT_COLOR))
        label_leg.append("Shaft")

        legend(patch_leg, label_leg)
    fig.show()
