# -*- coding: utf-8 -*-

from matplotlib.patches import Patch, Polygon
from matplotlib.pyplot import axis, legend
from numpy import array, exp, pi

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

MAGNET_COLOR = config_dict["PLOT"]["color_dict"]["MAGNET_COLOR"]


def plot(self, fig=None, display_field=False):
    """Plot the Magnet in a matplotlib fig

    Parameters
    ----------
    self : Magnet
        A Magnet object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    display_field : bool
        if true, will display magnetization field arrow (Default value = False)

    Returns
    -------
    None
    """

    surf_list = self.build_geometry()
    patches = list()
    for surf in surf_list:
        patches.extend(surf.get_patches(color=MAGNET_COLOR))

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Magnet")

    # Add the magnet to the fig
    for patch in patches:
        axes.add_patch(patch)

    # Add the field if needed
    if display_field:
        arrow_list = self.build_magnetization_field(Rbo)
        for arrow in arrow_list:
            axes.annotate(
                "",
                xy=(arrow[0].real, arrow[0].imag),
                xycoords="data",
                xytext=(arrow[1].real, arrow[1].imag),
                textcoords="data",
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
            )

    # Axis Setup
    axis("equal")

    # Legend setup
    if "Magnet" not in label_leg:
        patch_leg.append(Patch(color=MAGNET_COLOR))
        label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    fig.show()
