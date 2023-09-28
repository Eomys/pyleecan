from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Functions.labels import decode_label, MAG_LAB, LAM_LAB

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


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
    win_title=None,
    is_legend=True,
    is_winding_connection=False,
):
    """Plot a Lamination with Magnets in a matplotlib fig

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only : bool
        True to plot only the lamination (remove the magnet)
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
    win_title : str
        Window title
    is_legend : bool
        True to add the legend
    is_winding_connection : bool
        True to display winding connections (not used)

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    if self.is_stator:
        Lam_Name = "Stator"
        lam_color = STATOR_COLOR
    else:
        Lam_Name = "Rotor"
        lam_color = ROTOR_COLOR

    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    # Get the lamination surfaces
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if LAM_LAB in label_dict["surf_type"]:
            patches.extend(
                surf.get_patches(
                    color=lam_color, is_edge_only=is_edge_only, edgecolor=edgecolor
                )
            )
        elif MAG_LAB in label_dict["surf_type"]:
            if not is_lam_only:
                patches.extend(
                    surf.get_patches(
                        color=MAGNET_COLOR,
                        is_edge_only=is_edge_only,
                        edgecolor=edgecolor,
                    )
                )
        else:
            patches.extend(
                surf.get_patches(is_edge_only=is_edge_only, edgecolor=edgecolor)
            )
    # Display the result
    (fig, ax, patch_leg, label_leg) = init_fig(fig)
    ax.set_xlabel("(m)")
    ax.set_ylabel("(m)")
    for patch in patches:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Rext * 1.5
    ax.set_xlim(-Lim, Lim)
    ax.set_ylim(-Lim, Lim)

    # Window title
    if (
        win_title is None
        and self.parent is not None
        and self.parent.name not in [None, ""]
    ):
        win_title = self.parent.name + " " + Lam_Name
    elif win_title is None:
        win_title = Lam_Name
    manager = plt.get_current_fig_manager()
    if manager is not None:
        manager.set_window_title(win_title)

    # Add the legend
    if not is_edge_only:
        if self.is_stator:
            patch_leg.append(Patch(color=STATOR_COLOR))
            label_leg.append("Stator")
            ax.set_title("Stator with Magnet")
        else:
            patch_leg.append(Patch(color=ROTOR_COLOR))
            label_leg.append("Rotor")
            ax.set_title("Rotor with Magnet")
        if not is_lam_only:
            patch_leg.append(Patch(color=MAGNET_COLOR))
            label_leg.append("Magnet")

        if is_legend:
            ax.legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    return fig, ax
