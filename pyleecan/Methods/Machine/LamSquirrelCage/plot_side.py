from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig
from ....definitions import config_dict

ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]


def plot_side(self, fig=None, ax=None, is_show_fig=True, save_path=None):
    """Plot the side view of the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None

    Returns
    -------
    None
    """

    # Lamination and ventilation ducts patches
    (fig, axes, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")
    Lt = self.comp_length()
    patches = list()  # List of patches to draw the lamination
    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR

    # Comp important point coordinates
    ZBLext = -self.Rext - Lt / 2 * 1j  # Bottom Lamination Ext
    ZBLint = self.Rint - Lt / 2 * 1j  # Bottom Lamination Int

    # Draw Lamination rectangle(s)
    if self.Rint == 0:
        patches.append(
            Rectangle(
                xy=(ZBLext.real, ZBLext.imag),
                width=2 * self.Rext,
                height=Lt,
                color=lam_color,
            )
        )
    else:
        patches.append(  # Left
            Rectangle(
                xy=(ZBLext.real, ZBLext.imag),
                width=self.Rext - self.Rint,
                height=Lt,
                color=lam_color,
            )
        )
        patches.append(  # Right
            Rectangle(
                xy=(ZBLint.real, ZBLint.imag),
                width=self.Rext - self.Rint,
                height=Lt,
                color=lam_color,
            )
        )

    # Add Lewout rectangles

    # Add short circuit ring rectangles

    # Display the result
    axes.set_xlabel("[m]")
    axes.set_ylabel("[m]")
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axes.axis("equal")

    if is_show_fig:
        fig.show()
    if save_path is not None:
        fig.savefig(save_path)
        plt.close()
