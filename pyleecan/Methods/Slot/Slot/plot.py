from ....Functions.init_fig import init_fig
from ....definitions import config_dict

ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot(self, fig=None, ax=None, is_show_fig=True):
    """Plot the Slot in a matplotlib fig

    Parameters
    ----------
    self : Slot
        A Slot object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """
    surf = self.get_surface()

    # Display the result
    (fig, ax, patch_leg, label_leg) = init_fig(fig, ax)
    ax.set_xlabel("[m]")
    ax.set_ylabel("[m]")
    ax.set_title("Slot")

    # Add the slot to the fig
    if self.get_is_stator:
        patches = surf.get_patches(color=STATOR_COLOR)
    else:
        patches = surf.get_patch(color=ROTOR_COLOR)
    for patch in patches:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")
    if is_show_fig:
        fig.show()
    return fig, ax
