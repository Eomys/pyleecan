# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ....Functions.init_fig import init_fig
from ....Methods.Machine import MAGNET_COLOR


def plot(self, fig=None, display_magnet=True):
    """Plot the Hole in a matplotlib fig

    Parameters
    ----------
    self : Hole
        A Hole object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    display_magnet : bool
        if True, plot the magnet inside the hole, if there is any (Default value = True)

    Returns
    -------
    None
    """
    display = fig is None
    if display:
        color = "k"
    else:
        color = "w"

    surf_hole = self.build_geometry()
    patches = list()
    for surf in surf_hole:
        if "Magnet" in surf.label and display_magnet:
            patches.extend(surf.get_patches(color=MAGNET_COLOR))
        else:
            patches.extend(surf.get_patches(color=color))

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Hole")

    # Add all the hole (and magnet) to fig
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axis("equal")
    Lim = self.get_Rbo() * 1.2
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    if display_magnet and "Magnet" in [surf.label for surf in surf_hole]:
        patch_leg.append(Patch(color=MAGNET_COLOR))
        label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    fig.show()
