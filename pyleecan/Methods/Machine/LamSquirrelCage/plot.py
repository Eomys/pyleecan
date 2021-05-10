# -*- coding: utf-8 -*-

from matplotlib.patches import Patch, Polygon, Wedge
from matplotlib.pyplot import axis, legend
from numpy import array, exp, pi
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
    is_show_fig=True,
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
    is_show_fig : bool
        To call show at the end of the method

    Returns
    -------
    None
    """

    # Lamination and ventilation ducts patches
    (fig, axes, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Plot the lamination
    LamSlotWind.plot(
        self,
        fig=fig,
        is_lam_only=is_lam_only,
        sym=sym,
        alpha=alpha,
        delta=delta,
        is_edge_only=is_edge_only,
        is_show_fig=is_show_fig,
    )

    # init figure again to get updated label_leg and patch_leg
    (fig, axes, patch_leg, label_leg) = init_fig(fig)

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
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Squirrel Cage Rotor")

    # Axis Setup
    axes.axis("equal")
    Lim = self.Rext * 1.5
    axes.set_xlim(-Lim, Lim)
    if sym == 1:
        axes.set_ylim(-Lim, Lim)
    else:
        axes.set_ylim(-Lim*0.3, Lim)

    if not is_lam_only:
        # Add the short ciruit ring to the fig
        for patch in patches:
            axes.add_patch(patch)
        if "Short Circuit Ring" not in label_leg:
            patch_leg.append(Patch(color=SCR_COLOR))
            label_leg.append("Short Circuit Ring")

        legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
