# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.plot
Lamination plot method
@date Created on Mon Apr 20 15:23:02 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import ROTOR_COLOR, STATOR_COLOR, VENT_COLOR, VENT_EDGE


def plot(
    self, fig=None, is_lam_only=False, sym=1, alpha=0, delta=0, is_edge_only=False
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : Lamination
        A Lamination object
    fig :
        if None, open a new fig and plot, else add to the current one (Default value = None)
    is_lam_only: bool
        True to plot only the lamination (no effect for Lamination object)
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

    """
    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR
    (fig, axes, patch_leg, label_leg) = init_fig(fig)

    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()

    # Color Selection for Lamination
    for surf in surf_list:
        if surf.label is not None and "_Ext" in surf.label:
            patches.append(surf.get_patch(color=lam_color, is_edge_only=is_edge_only))
        elif surf.label is not None and "Ventilation_" in surf.label:
            patches.append(
                surf.get_patch(
                    color=VENT_COLOR, edgecolor=VENT_EDGE, is_edge_only=is_edge_only
                )
            )
        else:
            patches.append(surf.get_patch(is_edge_only=is_edge_only))

    # Display the result
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

    # Adding legend
    if not is_edge_only:
        if self.is_stator:
            patch_leg.append(Patch(color=STATOR_COLOR))
            label_leg.append("Stator")
            axes.set_title("Stator without slot")
        else:
            patch_leg.append(Patch(color=ROTOR_COLOR))
            label_leg.append("Rotor")
            axes.set_title("Rotor without slot")

        legend(patch_leg, label_leg)
    fig.show()
