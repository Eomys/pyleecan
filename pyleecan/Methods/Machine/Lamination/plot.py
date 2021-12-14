import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.pyplot import legend

from ....Functions.init_fig import init_fig
from ....definitions import config_dict

VENT_COLOR = config_dict["PLOT"]["COLOR_DICT"]["VENT_COLOR"]
VENT_EDGE = config_dict["PLOT"]["COLOR_DICT"]["VENT_EDGE"]
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
    is_show_fig=True,
    save_path=None,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : Lamination
        A Lamination object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only: bool
        True to plot only the lamination (no effect for Lamination object)
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
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None

    Returns
    -------

    """
    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR
    (fig, axes, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()

    # Color Selection for Lamination
    for surf in surf_list:
        if surf.label is not None and "Lamination" in surf.label:
            patches.extend(surf.get_patches(color=lam_color, is_edge_only=is_edge_only))
        elif surf.label is not None and "Ventilation_" in surf.label:
            patches.extend(
                surf.get_patches(
                    color=VENT_COLOR, edgecolor=VENT_EDGE, is_edge_only=is_edge_only
                )
            )
        else:
            patches.extend(surf.get_patches(is_edge_only=is_edge_only))

    # Display the result
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axes.axis("equal")

    # The Lamination is centered in the figure
    Lim = self.Rext * 1.5
    axes.set_xlim(-Lim, Lim)
    axes.set_ylim(-Lim, Lim)

    # Adding legend
    if not is_edge_only:
        if self.is_stator:
            patch_leg.append(Patch(color=STATOR_COLOR))
            label_leg.append("Stator")
            axes.set_title("Stator without slot")
        else:
            patch_leg.append(Patch(color=ROTOR_COLOR))
            label_leg.append("Rotor")
            axes.set_title("Rotor without slot")

        legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    if save_path is not None:
        fig.savefig(save_path)
        plt.close()
