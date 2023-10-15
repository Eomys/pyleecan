import matplotlib.pyplot as plt
from numpy import pi, exp, angle as np_angle

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
    self : VentilationPolar
        A VentilationPolar object
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
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    -------
    lam : LamSlot
        Default lamination used for the schematics

    """

    # Use some default parameter
    if is_default:
        hole = type(self)(
            H0=0.125,
            Zh=8,
            Alpha0=0.3,
            D0=0.05,
            W1=2 * pi / 16,
        )
        lam = LamHole(
            Rint=0.1, Rext=0.2, is_internal=True, is_stator=False, hole=[hole]
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
        fig, ax = lam.plot(
            alpha=0,
            is_show_fig=False,
            is_lam_only=True,  # No magnet
            fig=fig,
            ax=ax,
        )  # center hole on Ox axis
        point_dict = self._comp_point_coordinate()

        # Adding point label
        if is_add_point_label:
            for name, Z in point_dict.items():
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
            line = Segment(0, point_dict["Z1"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H0",
                offset_label=self.D0 / 4 * 1j,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # D0
            line = Segment(
                point_dict["Z1"] * exp(1j * 2 * pi / self.Zh),
                point_dict["Z2"] * exp(1j * 2 * pi / self.Zh),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="D0",
                offset_label=self.D0 / 4,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Alpha0
            line = Arc1(
                begin=self.H0 + self.D0 / 2,
                end=point_dict["Zc"],
                radius=self.H0 + self.D0 / 2,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Alpha0",
                offset_label=self.D0 / 4 * (1 - 1.5j),
                fontsize=SC_FONT_SIZE,
            )
            # W1
            Rtop = self.H0 + self.D0
            Rarc = (Rtop + lam.Rext) / 2
            line = Arc1(
                begin=Rarc * exp(1j * (self.Alpha0 - self.W1 / 2)),
                end=Rarc * exp(1j * (self.Alpha0 + self.W1 / 2)),
                radius=Rarc,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W1",
                offset_label=self.D0 / 4,
                fontsize=SC_FONT_SIZE,
            )

        if is_add_main_line:
            # Ox axis
            line = Segment(0, lam.Rext * 1.5)
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Center axis
            line = Segment(0, lam.Rext * 1.5 * exp(1j * self.Alpha0))
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # H0 radius
            line = Arc1(
                begin=self.H0 * exp(-1j * pi / 2 * 0.9),
                end=self.H0 * exp(1j * pi / 2 * 0.9),
                radius=self.H0,
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # H0+D0 radius
            line = Arc1(
                begin=(self.H0 + self.D0) * exp(-1j * pi / 2 * 0.9),
                end=(self.H0 + self.D0) * exp(1j * pi / 2 * 0.9),
                radius=(self.H0 + self.D0),
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Vent side 1 axis
            line = Segment(0, lam.Rext * 1.5 * exp(1j * np_angle(point_dict["Z1"])))
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Vent side 2 axis
            line = Segment(0, lam.Rext * 1.5 * exp(1j * np_angle(point_dict["Z3"])))
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

        # Zooming and cleaning
        W = abs(point_dict["Z2"].imag) * 1.3
        Rint = self.parent.Rint
        Rext = self.parent.Rext

        ax.axis("equal")
        ax.set_ylim(-Rext / 10, Rext * 0.9)
        ax.set_xlim(Rext / 10, Rext)
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
