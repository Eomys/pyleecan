# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.plot
Frame plot methods
@date Created on Mon Jan 26 17:45:37 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch
from matplotlib.pyplot import axis

from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import FRAME_COLOR


def plot(self, fig=None, sym=1, alpha=0, delta=0, is_edge_only=False):
    """Plot the Frame in a matplotlib fig

    Parameters
    ----------
    self : Frame
        A Frame object
    fig :
        if None, open a new fig and plot, else add to the gcf (Default value = None)
    sym : int
        Symmetry factor (1= plot full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches

    Returns
    -------
    None

    """

    # plot only if the frame has a height >0
    if self.comp_height_eq() != 0:
        (fig, axes, patch_leg, label_leg) = init_fig(fig)
        surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
        patches = list()
        for surf in surf_list:
            if surf.label is not None and surf.label == "Frame":
                patches.append(
                    surf.get_patch(color=FRAME_COLOR, is_edge_only=is_edge_only)
                )
            else:
                patches.append(surf.get_patch(is_edge_only=is_edge_only))

        axes.set_xlabel("(m)")
        axes.set_ylabel("(m)")
        axes.set_title("Frame")
        for patch in patches:
            axes.add_patch(patch)
        axis("equal")

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.1
        axes.set_xlim(-Lim, Lim, auto=True)
        axes.set_ylim(-Lim, Lim, auto=True)

        if not is_edge_only:
            patch_leg.append(Patch(color=FRAME_COLOR))
            label_leg.append("Frame")
            axes.legend(patch_leg, label_leg)

        fig.show()
