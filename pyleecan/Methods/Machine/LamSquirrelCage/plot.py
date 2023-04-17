from matplotlib.patches import Patch, Wedge
from ....Classes.LamSlotWind import LamSlotWind
from ....Functions.init_fig import init_fig
from ....definitions import config_dict

BAR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["BAR_COLOR"]
SCR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["SCR_COLOR"]


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
    is_winding_connection=False,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only : bool
        True to plot only the lamination (remove the bare)
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
    is_winding_connection : bool
        True to display winding connections (not used)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    # Lamination and ventilation ducts patches
    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Plot the lamination
    LamSlotWind.plot(
        self,
        fig=fig,
        ax=ax,
        is_lam_only=is_lam_only,
        sym=sym,
        alpha=alpha,
        delta=delta,
        is_edge_only=is_edge_only,
        is_show_fig=is_show_fig,
    )

    # init figure again to get updated label_leg and patch_leg
    (fig, ax, patch_leg, label_leg) = init_fig(fig, ax=ax)

    # setup the patch of the short circuit ring if needed
    patches = list()
    if not is_lam_only:
        try:
            Rmw = self.slot.comp_radius_mid_active()
            patches.append(
                Wedge(
                    (0, 0),
                    Rmw + self.Hscr / 2.0,
                    0,
                    360 / sym,
                    width=self.Hscr,
                    color=SCR_COLOR,
                )
            )  # Full ring
        except:
            pass

    # Display the result
    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")
    ax.set_title("Squirrel Cage Rotor")

    # Axis Setup
    ax.axis("equal")
    Lim = self.Rext * 1.5
    ax.set_xlim(-Lim, Lim)
    if sym == 1:
        ax.set_ylim(-Lim, Lim)
    else:
        ax.set_ylim(-Lim * 0.3, Lim)

    if not is_lam_only:
        # Add the short ciruit ring to the fig
        for patch in patches:
            ax.add_patch(patch)
        if "Short Circuit Ring" not in label_leg:
            patch_leg.append(Patch(color=SCR_COLOR))
            label_leg.append("Short Circuit Ring")

        ax.legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    return fig, ax
