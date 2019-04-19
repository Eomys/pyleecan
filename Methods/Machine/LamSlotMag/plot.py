# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMag.plot
Lamination with Magnets plot method
@date Created on Mon Dec 22 14:22:39 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import MAGNET_COLOR, ROTOR_COLOR, STATOR_COLOR


def plot(self, fig=None, is_magnet=True, sym=1, alpha=0, delta=0, is_edge_only=False):
    """Plot a Lamination with Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
    is_magnet :
        If True plot the magnets (Default value = True)
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

    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR

    (fig, axes, patch_leg, label_leg) = init_fig(fig)

    # Get the lamination surfaces
    surf_list = self.build_geometry(
        is_magnet=is_magnet, sym=sym, alpha=alpha, delta=delta
    )
    patches = list()
    for surf in surf_list:
        if "Ext" in surf.label:
            patches.append(surf.get_patch(color=lam_color, is_edge_only=is_edge_only))
        elif "Magnet" in surf.label:
            patches.append(
                surf.get_patch(color=MAGNET_COLOR, is_edge_only=is_edge_only)
            )
        else:
            patches.append(surf.get_patch(is_edge_only=is_edge_only))
    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Rext * 1.5
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    # Add the legend
    if not is_edge_only:
        if self.is_stator:
            patch_leg.append(Patch(color=STATOR_COLOR))
            label_leg.append("Stator")
            axes.set_title("Stator with Magnet")
        else:
            patch_leg.append(Patch(color=ROTOR_COLOR))
            label_leg.append("Rotor")
            axes.set_title("Rotor with Magnet")

        legend(patch_leg, label_leg)
    fig.show()
