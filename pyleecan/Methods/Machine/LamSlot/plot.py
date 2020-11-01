# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot(
    self,
    fig=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    is_display=True,
    is_show_fig=True,
):
    """Plot the Lamination with empty Slots in a matplotlib fig

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
    is_lam_only: bool
        True to plot only the lamination (No effect for LamSlot)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    is_display : bool
        False to return the patches
    is_show_fig : bool
        To call show at the end of the method
    Returns
    -------
    patches : list
        List of Patches
    """

    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR

    (fig, axes, patch_leg, label_leg) = init_fig(fig)

    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        if "Lamination" in surf.label:
            patches.extend(surf.get_patches(color=lam_color, is_edge_only=is_edge_only))
        else:
            patches.extend(surf.get_patches(is_edge_only=is_edge_only))
    # Display the result
    if is_display:
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
            if self.is_stator and "Stator" not in label_leg:
                patch_leg.append(Patch(color=STATOR_COLOR))
                label_leg.append("Stator")
                axes.set_title("Stator with empty slot")
            elif not self.is_stator and "Rotor" not in label_leg:
                patch_leg.append(Patch(color=ROTOR_COLOR))
                label_leg.append("Rotor")
                axes.set_title("Rotor with empty slot")

            legend(patch_leg, label_leg)
        if is_show_fig:
            fig.show()
    else:
        return patches
