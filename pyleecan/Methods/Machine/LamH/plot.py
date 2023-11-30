import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from ....Functions.init_fig import init_fig
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
    save_path=None,
    win_title=None,
    is_clean_plot=False,
    is_winding_connection=False,
):
    """Plot a Lamination with Buried Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamH
        A LamH object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
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
    edgecolor:
        Color of the edges if is_edge_only=True
    is_add_arrow : bool
        To add an arrow for the magnetization
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Window title
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

    # Lamination bore
    if self.is_stator:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    # List of surface to plot the lamination
    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()

    for surf in surf_list:
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

    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")

    for patch in patches:
        ax.add_patch(patch)

    # Add Magnetization arrow
    if is_add_arrow:
        self._plot_arrow_mag(ax=ax, sym=sym, alpha=alpha, delta=delta)

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

    # Set legend
    if not is_edge_only:
        ax.set_title(f"{lam_name} with Interior Magnet")
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
    if save_path is not None:
        fig.savefig(save_path)
        plt.close(fig=fig)
    return fig, ax
