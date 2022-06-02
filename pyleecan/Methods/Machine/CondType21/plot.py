from matplotlib.patches import Patch, Rectangle
from ....Functions.init_fig import init_fig


def plot(self, fig=None, ax=None):
    """Plot a Conductor in a matplotlib fig

    Parameters
    ----------
    self : CondType21
        A CondType21 object
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
    """

    patches_list = []

    # Conductor insulation
    Wcond = self.comp_width()
    Hcond = self.comp_height()
    patches_list.append(Rectangle((0, 0), Wcond, Hcond, color="g"))

    # Conductor
    patches_list.append(
        Rectangle((self.Wins, self.Wins), self.Wbar, self.Hbar, color="r")
    )

    # Display
    (fig, ax, _, _) = init_fig(fig=fig, ax=ax)
    for patch in patches_list:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")

    # The conductor is centered
    ax.set_xlim(0 - Wcond / 10, Wcond * 11.0 / 10.0)
    ax.set_ylim(0 - Hcond / 10, Hcond * 11.0 / 10.0)

    # Legend
    patch_leg = list()  # Symbol
    label_leg = list()  # Text
    if self.Wins > 0:
        patch_leg.append(Patch(color="g"))
        label_leg.append("Conductor insulation")
    patch_leg.append(Patch(color="r"))
    label_leg.append("Active bar section")

    ax.legend(patch_leg, label_leg)
    fig.show()
    return fig, ax
