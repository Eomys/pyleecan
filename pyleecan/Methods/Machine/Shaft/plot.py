from matplotlib.patches import Patch

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

SHAFT_COLOR = config_dict["PLOT"]["COLOR_DICT"]["SHAFT_COLOR"]


def plot(
    self,
    fig=None,
    ax=None,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    is_show_fig=True,
):
    """Plot the Shaft in a matplotlib fig

    Parameters
    ----------
    self : Shaft
        A Shaft object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    is_show_fig : bool
        To call show at the end of the method

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")
    # Get the shaft surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        patches.extend(surf.get_patches(color=SHAFT_COLOR, is_edge_only=is_edge_only))
    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")
    ax.set_title("Shaft")
    for patch in patches:
        ax.add_patch(patch)
    ax.axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Drsh * 0.6
    ax.set_xlim(-Lim, Lim)
    ax.set_ylim(-Lim, Lim)

    # Add legend
    if not is_edge_only:
        patch_leg.append(Patch(color=SHAFT_COLOR))
        label_leg.append("Shaft")

        ax.legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    return fig, ax
