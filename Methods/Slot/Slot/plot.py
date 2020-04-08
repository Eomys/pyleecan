# -*- coding: utf-8 -*-

from matplotlib.pyplot import axis
from pyleecan.Methods.Machine import ROTOR_COLOR, STATOR_COLOR

from pyleecan.Functions.init_fig import init_fig


def plot(self, fig=None):
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
    None
    """
    surf = self.get_surface()

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Slot")

    # Add the slot to the fig
    if self.get_is_stator:
        patches = surf.get_patches(color=STATOR_COLOR)
    else:
        patches = surf.get_patch(color=ROTOR_COLOR)
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axis("equal")
    fig.show()
