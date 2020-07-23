# -*- coding: utf-8 -*-

from matplotlib.patches import Circle, Patch
from matplotlib.pyplot import axis, legend

from ....Functions.init_fig import init_fig
from ....definitions import config_dict


PATCH_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR"]
MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]
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
    is_show=True,
):
    """Plot a Lamination with Buried Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamHole
        A LamHole object
    fig :
        if None, open a new fig and plot, else add to the
        current one (Default value = None)
    is_lam_only: bool
        True to plot only the lamination (remove the magnets)
    sym : int
        Symmetry factor (1= plot full machine, 2= half of the machine...)
    alpha : float
        angle for rotation (Default value = 0) [rad]
    delta : complex
        complex for translation (Default value = 0)
    is_edge_only: bool
        To plot transparent Patches
    is_show : bool
        To call show at the end of the method

    Returns
    -------
    None
    """

    # Lamination bore
    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR

    # List of surface to plot the lamination
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        if surf.label is not None and "Lamination" in surf.label:
            patches.extend(surf.get_patches(color=lam_color, is_edge_only=is_edge_only))
        elif surf.label is not None and "Magnet" in surf.label and not is_lam_only:
            patches.extend(
                surf.get_patches(color=MAGNET_COLOR, is_edge_only=is_edge_only)
            )
        else:
            patches.extend(surf.get_patches(is_edge_only=is_edge_only))

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

    # Set legend
    if not is_edge_only:
        if self.is_stator:
            patch_leg.append(Patch(color=STATOR_COLOR))
            label_leg.append("Stator")
            axes.set_title("Stator with Interior Magnet")
        else:
            patch_leg.append(Patch(color=ROTOR_COLOR))
            label_leg.append("Rotor")
            axes.set_title("Rotor with Interior Magnet")
        if not is_lam_only:
            patch_leg.append(Patch(color=MAGNET_COLOR))
            label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    if is_show:
        fig.show()
