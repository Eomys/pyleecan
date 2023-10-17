from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from numpy import pi, exp
from ....Functions.init_fig import init_fig
from ....Functions.labels import decode_label, MAG_LAB, LAM_LAB
from ....Functions.Plot.get_color_legend_from_surface import (
    get_color_legend_from_surface,
)


def plot(
    self,
    fig=None,
    ax=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_add_arrow=False,
    is_show_fig=True,
    win_title=None,
    is_legend=True,
    is_clean_plot=False,
    is_winding_connection=False,
):
    """Plot a Lamination with Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamSlotM
        A LamSlotM object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only : bool
        True to plot only the lamination (remove the magnet)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    edgecolor:
        Color of the edges if is_edge_only=True
    is_show_fig : bool
        To call show at the end of the method
    win_title : str
        Window title
    is_legend : bool
        True to add the legend
    is_clean_plot : bool
        True to remove title, legend, axis (only machine on plot with white background)
    is_winding_connection : bool
        True to display winding connections (not used)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    if self.is_stator:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Get the lamination surfaces
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        label_dict = decode_label(surf.label)
        color, legend = get_color_legend_from_surface(surf, is_lam_only)

        if color is not None:
            patches.extend(
                surf.get_patches(
                    color=color,
                    is_edge_only=is_edge_only,
                    edgecolor=edgecolor,
                )
            )
        if not is_edge_only and legend is not None and legend not in label_leg:
            label_leg.append(legend)
            patch_leg.append(Patch(color=color))

        # Add the magnetization direction as arrow on top of the lamination
        if (
            not is_lam_only
            and MAG_LAB in label_dict["surf_type"]
            and label_dict["S_id"] == 0
        ):
            if hasattr(self, "magnet"):
                mag_type = self.magnet.type_magnetization
            else:
                mag_type = self.magnet_north.type_magnetization
            if is_add_arrow and mag_type in [0, 1]:  # Radial or Parallel only
                # Create arrow coordinates
                Zs = self.slot.Zs
                H = self.slot.comp_height_active()
                for ii in range(Zs // sym):
                    # if mag is not None and mag.type_magnetization == 3:
                    #     off -= pi / 2
                    Z1 = (abs(surf.point_ref) + delta - H / 4) * exp(
                        1j * (ii * 2 * pi / Zs + pi / Zs + alpha)
                    )
                    Z2 = (abs(surf.point_ref) + delta + H / 4) * exp(
                        1j * (ii * 2 * pi / Zs + pi / Zs + alpha)
                    )
                    # Change arrow direction for North/South
                    if ii % 2 == 1:
                        ax.annotate(
                            text="",
                            xy=(Z1.real, Z1.imag),
                            xytext=(Z2.real, Z2.imag),
                            arrowprops=dict(arrowstyle="->", linewidth=1, color="b"),
                        )
                    else:
                        ax.annotate(
                            text="",
                            xy=(Z2.real, Z2.imag),
                            xytext=(Z1.real, Z1.imag),
                            arrowprops=dict(arrowstyle="->", linewidth=1, color="b"),
                        )

    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")
    for patch in patches:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Rext * 1.5
    ax.set_xlim(-Lim, Lim)
    ax.set_ylim(-Lim, Lim)

    # Window title
    if (
        win_title is None
        and self.parent is not None
        and self.parent.name not in [None, ""]
    ):
        win_title = self.parent.name + " " + lam_name
    elif win_title is None:
        win_title = lam_name
    manager = plt.get_current_fig_manager()
    if manager is not None:
        manager.set_window_title(win_title)

    # Add the legend
    if not is_edge_only:
        ax.set_title(f"{lam_name} with Magnet")

        if is_legend:
            ax.legend(patch_leg, label_leg)

    # Clean figure
    if is_clean_plot:
        ax.set_axis_off()
        ax.axis("equal")
        if ax.get_legend() is not None:
            ax.get_legend().remove()
        ax.set_title("")

    if is_show_fig:
        fig.show()
    return fig, ax
