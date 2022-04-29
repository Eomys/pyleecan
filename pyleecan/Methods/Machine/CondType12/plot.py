from matplotlib.patches import Circle, Patch
from ....Functions.init_fig import init_fig
from numpy import exp, pi, sqrt

from ....definitions import config_dict

COND_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0].copy()
INS_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][1].copy()
COND_INS_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][2].copy()
# Remove alpha from phases
COND_COLOR[3] = 1
INS_COLOR[3] = 1
COND_INS_COLOR[3] = 1


def plot(self, is_show_fig=True,fig=None,ax=None):
    """Plot a Conductor in a matplotlib fig

    Parameters
    ----------
    self : CondType12
        A CondType12 object
    is_show_fig : bool
        To call show at the end of the method
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot

    Raises
    _______
    NotPlotableError
        You can't plot a coil with Nwppc>4
    """

    patches_list = []

    # Conductor insultation
    patches_list.append(Circle((0, 0), self.Wins_cond / 2, color=COND_INS_COLOR))

    # Computation of the center of the wire
    center_list = []
    if self.Nwppc == 1:
        center_list.append((0, 0))
    elif self.Nwppc == 2:
        center_list.append((0, self.Wwire / 2 + self.Wins_wire))
        center_list.append((0, -self.Wwire / 2 - self.Wins_wire))
    elif self.Nwppc == 3:
        # The 3 centers are on the edges of an Equilateral Triangle
        # (side length : a = Dwire + 2Wins_wire)
        # The Radius of the circumscribed cercle is : a *sqrt(3)/3
        R = (self.Wwire + 2 * self.Wins_wire) * sqrt(3) / 3.0
        center_list.append((0, R))
        # We found the coordinate of the other center by complex rotation
        Z2 = R * 1j * exp(1j * 2 * pi / 3)
        Z3 = R * 1j * exp(-1j * 2 * pi / 3)
        center_list.append((Z2.real, Z2.imag))
        center_list.append((Z3.real, Z3.imag))
    elif self.Nwppc == 4:
        # The 4 centers are on the edges of a square
        # (side length : a =Dwire + 2Wins_wire)
        a = self.Wwire / 2 + self.Wins_wire
        center_list.append((a, a))
        center_list.append((a, -a))
        center_list.append((-a, a))
        center_list.append((-a, -a))
    else:
        raise NotPlotableError("You can't plot a coil with Nwppc>4")

    # Creation of the wires
    for center in center_list:
        # Wire insulation
        patches_list.append(
            Circle(center, self.Wwire / 2 + self.Wins_wire, color=INS_COLOR)
        )
        # Wire conductor
        patches_list.append(Circle(center, self.Wwire / 2, color=COND_COLOR))

    # Display
    (fig, ax, _, _) = init_fig(fig=fig, ax=ax)
    for patch in patches_list:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")

    # The conductor is centered
    ax_lim = self.Wins_cond / 2 + self.Wins_cond / 10
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # Legend
    patch_leg = list()  # Symbol
    label_leg = list()  # Text
    patch_leg.append(Patch(color=COND_INS_COLOR))
    label_leg.append("Coil insulation")
    patch_leg.append(Patch(color=INS_COLOR))
    label_leg.append("Wire insulation")
    patch_leg.append(Patch(color=COND_COLOR))
    label_leg.append("Active wire section")

    ax.legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    return fig, ax


class NotPlotableError(Exception):
    """ """

    pass
