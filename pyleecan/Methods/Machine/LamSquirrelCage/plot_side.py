from matplotlib.patches import Rectangle, Patch
import matplotlib.pyplot as plt
from ....Functions.init_fig import init_fig
from ....definitions import config_dict

ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
BAR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["BAR_COLOR"]
SCR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["SCR_COLOR"]


def plot_side(self, fig=None, ax=None, is_show_fig=True, save_path=None):
    """Plot the side view of the Lamination in a matplotlib fig
    (Z axis left to right)

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
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    # Lamination and ventilation ducts patches
    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax)

    patches = list()  # List of patches to draw the lamination
    if self.is_stator:
        lam_color = STATOR_COLOR
    else:
        lam_color = ROTOR_COLOR

    # Comp all dimensions
    Lt = self.comp_length()
    Hs = self.slot.comp_height()
    Ha = self.slot.comp_height_active()
    Ho = Hs - Ha
    Le = self.winding.Lewout
    Lscr = self.Lscr
    Hscr = self.Hscr

    # Comp point coordinates
    ZLamExt = -Lt / 2 - 1j * self.Rext  # Bottom Lamination Ext
    ZLamInt = -Lt / 2 + 1j * self.Rint  # Bottom Lamination Int
    ZBarTopR = Lt / 2 + 1j * (self.Rext - Hs)  # Top bar right
    ZBarBotR = Lt / 2 + 1j * (-self.Rext + Ho)  # Bottom bar right
    ZBarTopL = -Lt / 2 - Le + 1j * (self.Rext - Hs)  # Top bar left
    ZBarBotL = -Lt / 2 - Le + 1j * (-self.Rext + Ho)  # Bottom bar left
    ZscrRight = (
        Lt / 2 + Le + 1j * (-self.Rext + Ho + Ha / 2 - Hscr / 2)
    )  # Short Circuit Ring Right
    ZscrLeft = (
        -Lt / 2 - Le - Lscr + 1j * (-self.Rext + Ho + Ha / 2 - Hscr / 2)
    )  # Short Circuit Ring Right

    # Draw Lamination rectangle(s)
    if self.Rint == 0:
        patches.append(
            Rectangle(
                xy=(ZLamExt.real, ZLamExt.imag),
                width=Lt,
                height=2 * self.Rext,
                color=lam_color,
            )
        )
    else:
        patches.append(  # Left
            Rectangle(
                xy=(ZLamExt.real, ZLamExt.imag),
                width=Lt,
                height=self.Rext - self.Rint,
                color=lam_color,
            )
        )
        patches.append(  # Right
            Rectangle(
                xy=(ZLamInt.real, ZLamInt.imag),
                width=Lt,
                height=self.Rext - self.Rint,
                color=lam_color,
            )
        )

    # Add Lewout rectangles
    patches.append(  # Top Right
        Rectangle(
            xy=(ZBarTopR.real, ZBarTopR.imag),
            width=Le,
            height=Ha,
            color=BAR_COLOR,
        )
    )
    patches.append(  # Bot Right
        Rectangle(
            xy=(ZBarBotR.real, ZBarBotR.imag),
            width=Le,
            height=Ha,
            color=BAR_COLOR,
        )
    )
    patches.append(  # Top Left
        Rectangle(
            xy=(ZBarTopL.real, ZBarTopL.imag),
            width=Le,
            height=Ha,
            color=BAR_COLOR,
        )
    )
    patches.append(  # Bot Left
        Rectangle(
            xy=(ZBarBotL.real, ZBarBotL.imag),
            width=Le,
            height=Ha,
            color=BAR_COLOR,
        )
    )
    # Add short circuit ring rectangles
    patches.append(
        Rectangle(
            xy=(ZscrRight.real, ZscrRight.imag),
            width=Lscr,
            height=abs(2 * ZscrRight.imag),
            color=SCR_COLOR,
        )
    )
    patches.append(
        Rectangle(
            xy=(ZscrLeft.real, ZscrLeft.imag),
            width=Lscr,
            height=abs(2 * ZscrLeft.imag),
            color=SCR_COLOR,
        )
    )

    # Display the result
    ax.set_xlabel("[m]")
    ax.set_ylabel("[m]")
    for patch in patches:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")
    ax.set_title("Squirrel Cage Rotor side view")
    # Set legend
    if self.is_stator:
        patch_leg.append(Patch(color=STATOR_COLOR))
        label_leg.append("Stator")
    elif not self.is_stator and "Rotor" not in label_leg:
        patch_leg.append(Patch(color=ROTOR_COLOR))
        label_leg.append("Rotor")
    patch_leg.append(Patch(color=BAR_COLOR))
    label_leg.append("Bar")
    patch_leg.append(Patch(color=SCR_COLOR))
    label_leg.append("Short Circuit Ring")
    ax.legend(patch_leg, label_leg)
    if is_show_fig:
        fig.show()
    if save_path is not None:
        fig.savefig(save_path)
        plt.close(fig=fig)
    return fig, ax