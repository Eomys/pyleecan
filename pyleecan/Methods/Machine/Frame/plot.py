# -*- coding: utf-8 -*-

from matplotlib.patches import Patch
from matplotlib.pyplot import axis

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

FRAME_COLOR = config_dict["color_dict"]["FRAME_COLOR"]


def plot(self, fig=None, sym=1, alpha=0, delta=0, is_edge_only=False, is_show=True):
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
    is_show : bool
        To call show at the end of the method

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
            patches.extend(
                surf.get_patches(color=FRAME_COLOR, is_edge_only=is_edge_only)
            )

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
        if is_show:
            fig.show()
