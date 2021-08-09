# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend
from numpy import exp

from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Methods import ParentMissingError

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


def plot(
    self,
    fig=None,
    ax=None,
    display_magnet=True,
    is_add_arrow=False,
    is_add_ref=False,
    is_show_fig=True,
):
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
    is_add_arrow : bool
        To add an arrow for the magnetization
    is_add_ref : bool
        True to add the reference points of the surfaces

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
    (fig, axes, patch_leg, label_leg) = init_fig(fig, ax)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Hole")

    # Add all the hole (and magnet) to fig
    for patch in patches:
        axes.add_patch(patch)

    # Magnetization
    if is_add_arrow:
        H = self.comp_height()
        mag_dict = self.comp_magnetization_dict()
        for magnet_name, mag_dir in mag_dict.items():
            # Get the correct surface
            mag_surf = None
            mag_id = magnet_name.split("_")[-1]
            for surf in surf_hole:
                if "Magnet" in surf.label and "_T" + mag_id in surf.label:
                    mag_surf = surf
                    break
            # Create arrow coordinates
            Z1 = mag_surf.point_ref
            Z2 = mag_surf.point_ref + H / 5 * exp(1j * mag_dir)
            axes.annotate(
                text="",
                xy=(Z2.real, Z2.imag),
                xytext=(Z1.real, Z1.imag),
                arrowprops=dict(arrowstyle="->", linewidth=1, color="b"),
            )

    # Add reference point
    if is_add_ref:
        for surf in self.surf_list:
            axes.plot(surf.point_ref.real, surf.point_ref.imag, "rx")

    # Axis Setup
    axes.axis("equal")
    try:
        Lim = self.get_Rbo() * 1.2
        axes.set_xlim(-Lim, Lim)
        axes.set_ylim(-Lim, Lim)
    except ParentMissingError:
        pass

    if display_magnet and "Magnet" in [surf.label for surf in surf_hole]:
        patch_leg.append(Patch(color=MAGNET_COLOR))
        label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
