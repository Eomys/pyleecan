import matplotlib.pyplot as plt
from numpy import pi, exp, angle, cos, sin

from ....Classes.Arc1 import Arc1
from ....Classes.LamHole import LamHole
from ....Classes.Segment import Segment
from ....definitions import config_dict
from ....Functions.Plot import (
    ARROW_COLOR,
    ARROW_WIDTH,
    MAIN_LINE_COLOR,
    MAIN_LINE_STYLE,
    MAIN_LINE_WIDTH,
    P_FONT_SIZE,
    SC_FONT_SIZE,
    SC_LINE_COLOR,
    SC_LINE_STYLE,
    SC_LINE_WIDTH,
    TEXT_BOX,
    plot_quote,
)
from ....Methods import ParentMissingError

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


def plot_schematics(
    self,
    is_default=False,
    is_return_default=False,
    is_add_point_label=False,
    is_add_schematics=True,
    is_add_main_line=True,
    type_add_active=True,
    save_path=None,
    is_show_fig=True,
    fig=None,
    ax=None,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object
    is_default : bool
        True: plot default schematics, else use current slot values
    is_return_default : bool
        True: return the default lamination used for the schematics (skip plot)
    is_add_point_label : bool
        True to display the name of the points (Z1, Z2....)
    is_add_schematics : bool
        True to display the schematics information (W0, H0...)
    is_add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    type_add_active : int
        0: No active surface, 2: active surface as magnet
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        To call show at the end of the method
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
    -------
    lam : LamHole / LamSlot
        Default lamination used for the schematics
    """

    # Use some default parameter
    if is_default:
        hole = type(self)(
            Zh=8,
            H1=0.002373479,
            W0=3.88e-03,
            W1=12.6 / 180 * pi,
            W2=0.0007,
            R1=0.0003,
            R2=0.019327,
            R3=0.0165,
        )
        lam = LamHole(
            Rint=14e-3,
            Rext=50e-3,
            is_internal=True,
            is_stator=False,
            L1=0.105,
            Nrvd=2,
            Wrvd=0.05,
            hole=[hole],
        )
        if is_return_default:
            return lam
        else:
            return hole.plot_schematics(
                is_default=False,
                is_return_default=False,
                is_add_point_label=is_add_point_label,
                is_add_schematics=is_add_schematics,
                is_add_main_line=is_add_main_line,
                type_add_active=type_add_active,
                save_path=save_path,
                is_show_fig=is_show_fig,
                fig=fig,
                ax=ax,
            )
    elif type_add_active == 0:
        # Remove magnets
        lam = self.parent.copy()
        lam.hole[0].remove_magnet()
        return lam.hole[0].plot_schematics(
            is_default=False,
            is_add_point_label=is_add_point_label,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            type_add_active=2,
            save_path=save_path,
            is_show_fig=is_show_fig,
            fig=fig,
            ax=ax,
        )
    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The hole is not inside a Lamination")
        lam = self.parent
        alpha = 0  # To rotate the schematics
        fig, ax = lam.plot(
            alpha=pi / self.Zh + alpha,
            is_show_fig=False,
            is_lam_only=type_add_active == 0,
            fig=fig,
            ax=ax,
        )  # center hole on Ox axis
        sp = 2 * pi / self.Zh
        Rbo = self.get_Rbo()
        point_dict = self._comp_point_coordinate()

        # Adding point label
        if is_add_point_label:
            for name, Z in point_dict.items():
                Z = Z * exp(1j * alpha)
                ax.text(
                    Z.real,
                    Z.imag,
                    name,
                    fontsize=P_FONT_SIZE,
                    bbox=TEXT_BOX,
                )

        # Adding schematics
        if is_add_schematics:
            # H1
            line = Segment(
                (point_dict["Z5"] + point_dict["Z6"]) / 2 * exp(1j * alpha),
                Rbo * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H1",
                offset_label=self.H1 + 1j * self.H1 * 0.25,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # W0
            line = Segment(
                point_dict["Z5"] * exp(1j * alpha),
                point_dict["Z6"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=-0.005,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # R1
            line = Segment(
                point_dict["Zc1"] * exp(1j * alpha),
                point_dict["Z2"] * exp(1j * alpha),
            )

            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="R1",
                offset_label=self.H1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # R2
            line = Segment(
                0 * exp(1j * alpha),
                point_dict["Z8"].real * exp(1j * (alpha)),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="R2",
                offset_label=self.H1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # R3
            line = Segment(
                0 * exp(1j * alpha),
                point_dict["Z10"] * exp(1j * (alpha)),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="R3",
                offset_label=-self.H1 * 2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # W1
            line = Segment(
                self.R2 * exp(1j * alpha),
                point_dict["Zw1"] * exp(1j * (alpha)),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W1",
                offset_label=0.00065,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # W2
            line = Segment(
                (point_dict["Zw2"] + 0.005 * exp(1j * self.W1)) * exp(1j * (alpha)),
                (point_dict["Zw1"] + 0.005 * exp(1j * self.W1)) * exp(1j * (alpha)),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W2",
                offset_label=1j * 0.0015 - 0.003,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            ### TODO:W1 W2

        if is_add_main_line:
            # Ox axis
            line = Segment(0, lam.Rext * 1.5 * exp(1j * alpha))
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Guide line 1
            line = Segment(0, lam.Rext * 1.5 * exp(1j * (alpha + 12.6 / 180 * pi)))
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Guide line 2
            line = Segment(
                0 - 1j * 0.0007 / cos(12.6 / 180 * pi),
                lam.Rext * 1.5 * exp(1j * (alpha + 12.6 / 180 * pi))
                - 1j * 0.0007 / cos(12.6 / 180 * pi),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # R1 radius
            line = Arc1(
                begin=point_dict["Z1"],
                end=point_dict["Z2"],
                radius=self.R1,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

            # W1 radius

            line = Arc1(
                begin=point_dict["Zw1"] * exp(1j * alpha),
                end=self.R2 * exp(1j * alpha),
                radius=self.R2,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

            # Magnet lines
            line = Segment(
                point_dict["Z8"] * exp(1j * alpha),
                point_dict["Z3"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            line = Segment(
                point_dict["Z7"] * exp(1j * alpha),
                point_dict["Z4"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

        # Zooming and cleaning
        W = 4e-3
        Rint = self.R3 * 0.9
        Rext = self.parent.Rext * 1.2

        # ax.axis("equal")
        ax.set_xlim(Rint, Rext)
        ax.set_ylim(-W, W)
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(type(self).__name__ + " Schematics")
        ax.set_title("")
        ax.get_legend().remove()
        ax.set_axis_off()
        fig.tight_layout()

        # Save / Show
        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)

        if is_show_fig:
            fig.show()
        return fig, ax
