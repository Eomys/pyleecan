from matplotlib.patches import Patch

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

FRAME_COLOR = config_dict["PLOT"]["COLOR_DICT"]["FRAME_COLOR"]


def plot(
    self,
    fig=None,
    ax=None,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_show_fig=True,
):
    """Plot the Frame in a matplotlib fig

    Parameters
    ----------
    self : Frame
        A Frame object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    sym : int
        Symmetry factor (1= plot full machine, 2= half of the machine...)
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

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    # plot only if the frame has a height >0
    if self.comp_height_eq() != 0:
        (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")
        surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
        patches = list()
        for surf in surf_list:
            patches.extend(
                surf.get_patches(
                    color=FRAME_COLOR, is_edge_only=is_edge_only, edgecolor=edgecolor
                )
            )

        ax.set_xlabel("(m)")
        ax.set_ylabel("(m)")
        ax.set_title("Frame")
        for patch in patches:
            ax.add_patch(patch)
        ax.axis("equal")

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.1
        ax.set_xlim(-Lim, Lim, auto=True)
        ax.set_ylim(-Lim, Lim, auto=True)

        if not is_edge_only:
            patch_leg.append(Patch(color=FRAME_COLOR))
            label_leg.append("Frame")
            ax.legend(patch_leg, label_leg)
        if is_show_fig:
            fig.show()
        return fig, ax
