# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend
from numpy import exp

from ....Functions.init_fig import init_fig
from ....Functions.labels import HOLEM_LAB, decode_label
from ....Functions.Geometry.transform_hole_surf import transform_hole_surf
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
    is_all_hole=False,
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
    is_all_hole : bool
        True to plot the Zh holes

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
    if is_all_hole:
        # Duplicate the hole surfaces
        surf_hole = transform_hole_surf(
            hole_surf_list=surf_hole, Zh=self.Zh, sym=1, alpha=0, delta=0
        )

    patches = list()
    for surf in surf_hole:
        label_dict = decode_label(surf.label)
        if HOLEM_LAB in label_dict["surf_type"] and display_magnet:
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
                label_dict = decode_label(surf.label)
                if (
                    HOLEM_LAB in label_dict["surf_type"]
                    and label_dict["T_id"] == mag_id
                ):
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

    if display_magnet and HOLEM_LAB in [surf.label for surf in surf_hole]:
        patch_leg.append(Patch(color=MAGNET_COLOR))
        label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
