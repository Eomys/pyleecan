# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot.plot
Slot for Magnet plot methods
@date Created on Tue Dec 09 09:43:33 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

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
        axes.add_patch(surf.get_patch(color=STATOR_COLOR))
    else:
        axes.add_patch(surf.get_patch(color=ROTOR_COLOR))

    # Axis Setup
    axis("equal")
    fig.show()
