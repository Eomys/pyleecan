from ....Functions.Load.import_class import import_class
from numpy import pi
from ....definitions import config_dict
from matplotlib.patches import Patch

PATCH_COLOR_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR_ALPHA"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot_preview_notch(self, index, fig=None, ax=None):
    """Preview the position/shape of a notch on the lamination

    Parameters
    ----------
    self : Lamination
        Lamination object
    index : int
        Index of the notch to preview
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

    if self.notch is None:
        raise Exception("No notch set")
    if index > len(self.notch) - 1:
        raise Exception(
            "Requested notch index "
            + str(index)
            + ", "
            + str(len(self.notch))
            + " notches were set"
        )
    # Plot the original lamination without notches
    lam = self.copy()
    lam.notch = list()

    fig, ax = lam.plot(
        fig=fig,
        ax=ax,
        is_lam_only=True,
    )

    # Create equivalent LamSlot with notch as slot
    LamSlot = import_class("pyleecan.Classes", "LamSlot")
    lam_notch = LamSlot(
        is_stator=lam.is_stator,
        is_internal=lam.is_internal,
        Rint=lam.Rint,
        Rext=lam.Rext,
        slot=self.notch[index].notch_shape,
    )
    fig, ax = lam_notch.plot(
        fig=fig,
        ax=ax,
        is_edge_only=True,
        edgecolor="r--",
        alpha=-pi / self.notch[index].notch_shape.Zs + self.notch[index].alpha,
    )
    # Setup legend
    if self.is_stator:
        name = "Stator"
        color = STATOR_COLOR
    else:
        name = "Rotor"
        color = ROTOR_COLOR
    patch_leg = [
        Patch(facecolor=color, edgecolor="k"),
        Patch(facecolor=PATCH_COLOR_ALPHA, edgecolor="r", linestyle="--"),
    ]
    label_leg = ["Current " + name, "Notches"]
    ax.set_axis_off()
    ax.legend(patch_leg, label_leg)

    return fig, ax
