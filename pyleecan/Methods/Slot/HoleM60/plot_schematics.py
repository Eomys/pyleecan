import matplotlib.pyplot as plt
from numpy import pi, exp, angle

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Segment import Segment
from pyleecan.definitions import config_dict
from pyleecan.Functions.Plot import (
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
from pyleecan.Methods import ParentMissingError

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
    self : HoleM60
        A HoleM60 object
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
            Zh=4,
            W0=pi * 0.5,
            W1=2e-2,
            W2=7e-2,
            W3=8e-3,
            H0=12e-3,
            H1=10e-3,
        )
        lam = LamHole(
            Rint=0.03, Rext=0.12, is_internal=True, is_stator=False, hole=[hole]
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
        # W0
        line = Arc1(
            begin=point_dict["ZM1s"] * exp(1j * alpha),
            end=point_dict["ZM1"] * exp(1j * alpha),
            radius=abs(
                (point_dict["ZM1"] + point_dict["Z1"]) / 2
                - (point_dict["ZM1s"] + point_dict["Z1s"]) / 2
            ),
            is_trigo_direction=True,
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="W0",
            offset_label=(1 + 1j) * self.H1 * 0.4,
            fontsize=SC_FONT_SIZE,
        )
        # W1, magnet width only if magnet is visible
        if type_add_active == 2:
            line = Segment(
                point_dict["ZM1"] * exp(1j * alpha),
                point_dict["ZM2"] * exp(1j * alpha),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W1",
                offset_label=(1 + 1j) * self.H1 * 0.25,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
        # W2
        line = Segment(
            point_dict["Z3s"] * exp(1j * alpha),
            point_dict["Z6s"] * exp(1j * alpha),
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="W2",
            offset_label=-1j * self.H1,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # W3
        line = Segment(
            point_dict["Z1"] * exp(1j * alpha),
            point_dict["Z1s"] * exp(1j * alpha),
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="W3",
            offset_label=1j * self.H1 * 0.5,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # H0
        line = Segment(
            point_dict["Z2s"] * exp(1j * alpha),
            point_dict["Z4s"] * exp(1j * alpha),
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="H0",
            offset_label=-1j * self.H1,
            is_arrow=True,
            fontsize=SC_FONT_SIZE,
        )
        # H1
        A = angle(point_dict["Z3"])
        line = Segment(
            Rbo * exp(1j * A) * exp(1j * alpha),
            (Rbo - self.H1) * exp(1j * A) * exp(1j * alpha),
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=ARROW_COLOR,
            linewidth=ARROW_WIDTH,
            label="H1",
            offset_label=self.H1 * 0.5,
            is_arrow=True,
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
        # Tooth axis
        line = Segment(0, lam.Rext * 1.5 * exp(1j * sp / 2) * exp(1j * alpha))
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )
        line = Segment(0, lam.Rext * 1.5 * exp(-1j * sp / 2) * exp(1j * alpha))
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )
        # H1 radius
        A = angle(point_dict["Z3"])
        line = Segment(0, Rbo * exp(1j * A) * exp(1j * alpha))
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )
        line = Arc1(
            begin=(Rbo - self.H1) * exp(-1j * pi / 2 * 0.9) * exp(1j * alpha),
            end=(Rbo - self.H1) * exp(1j * pi / 2 * 0.9) * exp(1j * alpha),
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
        # H0 lines
        line = Segment(
            point_dict["Z2"] * exp(1j * alpha), point_dict["Z4"] * exp(1j * alpha)
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )
        line = Segment(
            point_dict["Z1"] * exp(1j * alpha), point_dict["Z5"] * exp(1j * alpha)
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )
        line = Segment(
            point_dict["Z1s"] * exp(1j * alpha), point_dict["Z5s"] * exp(1j * alpha)
        )
        line.plot(
            fig=fig,
            ax=ax,
            color=MAIN_LINE_COLOR,
            linestyle=MAIN_LINE_STYLE,
            linewidth=MAIN_LINE_WIDTH,
        )

    # Zooming and cleaning
    W = (point_dict["Z"] * exp(1j * sp)).imag
    Rint = self.parent.Rint
    Rext = self.parent.Rext

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
