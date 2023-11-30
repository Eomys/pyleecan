import matplotlib.pyplot as plt
from numpy import pi, exp, angle

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
    self : HoleM58
        A HoleM58 object
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
        0: No active surface, 1: active surface as winding, 2: active surface as magnet
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
        Figure containing the schematics
    ax : Matplotlib.axes.Axes object
        Axis containing the schematics
    -------
    lam : LamHole / LamSlot
        Default lamination used for the schematics
    """

    # Use some default parameter
    if is_default:
        hole = type(self)(
            Zh=8,
            W0=20e-3,
            W1=12e-3,
            W2=6e-3,
            W3=2 * pi / 8 * 0.6,
            H0=17e-3,
            H1=5e-3,
            H2=5e-3,
            R0=1.7e-3,
        )
        lam = LamHole(
            Rint=0.021, Rext=0.075, is_internal=True, is_stator=False, hole=[hole]
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

    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The hole is not inside a Lamination")
        lam = self.parent

        # Remove the magnets
        if type_add_active == 0:
            lam.hole[0].remove_magnet()

        alpha = pi / 2  # To rotate the schematics
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
            # H0
            line = Segment(
                point_dict["Z1"].real * exp(1j * alpha),
                Rbo * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H0",
                offset_label=self.H2 * 0.2 + 1j * self.H0 * 0.35,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H1
            line = Segment(
                Rbo * exp(1j * angle(point_dict["Zc2"])) * exp(1j * alpha),
                (Rbo - self.H1) * exp(1j * angle(point_dict["Zc2"])) * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H1",
                offset_label=self.H2 * 0.3,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H2
            line = Segment(
                point_dict["Z6"].real * exp(1j * alpha),
                point_dict["Z1"].real * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H2",
                offset_label=self.H2 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # R0
            Zlim1 = (Rbo - self.H1) * exp(1j * angle(point_dict["Zc1"]))
            Zlim2 = (Rbo - self.H1 - self.R0) * exp(1j * angle(point_dict["Zc1"]))
            plot_quote(
                (Rbo - self.H1) * exp(1j * angle(point_dict["Zc1"])) * exp(1j * alpha),
                Zlim1 * exp(1.02j * alpha),
                Zlim2 * exp(1.02j * alpha),
                (Rbo - self.H1 - self.R0)
                * exp(1j * angle(point_dict["Zc1"]))
                * exp(1j * alpha),
                offset_label=-self.H2 * 0.8,
                fig=fig,
                ax=ax,
                label="R0",
            )

            # W0
            Zlim1 = point_dict["Z2"] + 0.2 * self.H0
            Zlim2 = point_dict["Z11"] + 0.2 * self.H0
            plot_quote(
                point_dict["Z2"] * exp(1j * alpha),
                Zlim1 * exp(1j * alpha),
                Zlim2 * exp(1j * alpha),
                point_dict["Z11"] * exp(1j * alpha),
                offset_label=(1 + 1j) * self.H2 * 0.2,
                fig=fig,
                ax=ax,
                label="W0",
            )
            if type_add_active != 0:
                # W1
                line = Segment(
                    point_dict["Z6"] * exp(1j * alpha),
                    point_dict["Z7"] * exp(1j * alpha),
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="W1",
                    offset_label=-1j * self.H2 * 0.5,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
                # W2
                line = Segment(
                    point_dict["Z6"] * exp(1j * alpha),
                    point_dict["Z5"] * exp(1j * alpha),
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="W2",
                    offset_label=-1j * self.H2 * 0.5,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
            # W3
            line = Arc1(
                begin=point_dict["Zc2"] * exp(1j * alpha),
                end=point_dict["Zc1"] * exp(1j * alpha),
                radius=abs(point_dict["Zc1"]),
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W3",
                offset_label=(1 + 1j) * self.H2 * 0.2,
                fontsize=SC_FONT_SIZE,
            )

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
            # H1 radius
            line = Arc1(
                begin=(Rbo - self.H1) * exp(-1j * pi / 2) * exp(1j * alpha),
                end=(Rbo - self.H1) * exp(1j * pi / 2) * exp(1j * alpha),
                radius=Rbo - self.H1,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # W1 lines
            line = Segment(
                0,
                abs(point_dict["Zc1"])
                * 1.5
                * exp(1j * angle(point_dict["Zc1"]))
                * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            line = Segment(
                0,
                abs(point_dict["Zc2"])
                * 1.5
                * exp(1j * angle(point_dict["Zc2"]))
                * exp(1j * alpha),
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
                point_dict["Z2"] * exp(1j * alpha),
                point_dict["Z5"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            line = Segment(
                point_dict["Z8"] * exp(1j * alpha),
                point_dict["Z11"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # R0 Arc
            line = Arc1(
                begin=point_dict["Z4"] * exp(1j * alpha),
                end=point_dict["Z3"] * exp(1j * alpha),
                radius=self.R0,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

        # Zooming and cleaning
        W = (point_dict["Zc1"].imag + self.R0) * 1.05
        Rint = (Rbo - self.H0 - self.H2) * 0.9
        Rext = self.parent.Rext * 1.05

        ax.axis("equal")
        ax.set_ylim(Rint, Rext)
        ax.set_xlim(-W, W)
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
