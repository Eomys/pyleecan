from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Functions.Plot.get_color_legend_from_surface import (
    get_color_legend_from_surface,
)

ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


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
    is_winding_connection=False,
):
    """Plot a Lamination with Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object
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
        color, legend = get_color_legend_from_surface(surf, is_lam_only)

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
    if is_show_fig:
        fig.show()
    return fig, ax
