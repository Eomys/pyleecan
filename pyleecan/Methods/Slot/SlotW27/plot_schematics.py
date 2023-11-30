import matplotlib.pyplot as plt
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.LamSlot import LamSlot
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
    type_add_active=1,
    save_path=None,
    is_show_fig=True,
    fig=None,
    ax=None,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object
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
        0: No active surface, 1: active surface as winding, 2: active surface as , 3: active surface as winding + wedges
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
    lam : LamSlot
        Default lamination used for the schematics
    """

    # Use some default parameter
    if is_default:
        slot = type(self)(
            Zs=8, H0=10e-3, H1=40e-3, H2=20e-3, W0=20e-3, W1=40e-3, W2=60e-3, W3=30e-3
        )
        lam = LamSlot(
            Rint=0.135, Rext=0.3, is_internal=False, is_stator=True, slot=slot
        )
        if is_return_default:
            return lam
        else:
            return slot.plot_schematics(
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
            raise ParentMissingError("Error: The slot is not inside a Lamination")
        lam = self.parent
        fig, ax = lam.plot(
            alpha=pi / self.Zs, is_show_fig=False, fig=fig, ax=ax
        )  # center slot on Ox axis
        point_dict = self._comp_point_coordinate()
        if self.is_outwards():
            sign = 1
        else:
            sign = -1
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
            # W0
            line = Segment(point_dict["Z1"], point_dict["Z10"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=-self.H0 * 0.9,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W1
            Zlim1 = point_dict["Z3"] + sign * self.H1 * 0.3
            Zlim2 = point_dict["Z8"] + sign * self.H1 * 0.3
            plot_quote(
                point_dict["Z3"],
                Zlim1,
                Zlim2,
                point_dict["Z8"],
                offset_label=sign * self.H0 * 0.2,
                fig=fig,
                ax=ax,
                label="W1",
            )
            # W2
            line = Segment(point_dict["Z4"], point_dict["Z7"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W2",
                offset_label=self.H0 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W3
            Zlim1 = point_dict["Z6"] + sign * self.H0 * 0.4
            Zlim2 = point_dict["Z5"] + sign * self.H0 * 0.4
            plot_quote(
                point_dict["Z6"],
                Zlim1,
                Zlim2,
                point_dict["Z5"],
                offset_label=self.H0 * 0.2,
                fig=fig,
                ax=ax,
                label="W3",
            )
            # H0
            line = Segment(point_dict["Z10"], point_dict["Z9"])
            line.plot(
                fig=fig,
                ax=ax,
                label="H0",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.W0 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H1
            Zlim1 = point_dict["Z3"].real + 1j * point_dict["Z4"].imag
            Zlim2 = point_dict["Z4"]
            plot_quote(
                point_dict["Z3"],
                Zlim1,
                Zlim2,
                point_dict["Z4"],
                offset_label=-1j * self.H0 * 0.6,
                fig=fig,
                ax=ax,
                label="H1",
            )
            # H2
            Zlim1 = point_dict["Z6"].real + 1j * point_dict["Z7"].imag
            Zlim2 = point_dict["Z7"]
            plot_quote(
                point_dict["Z6"],
                Zlim1,
                Zlim2,
                point_dict["Z7"],
                offset_label=1j * self.H0 * 0.4,
                fig=fig,
                ax=ax,
                label="H2",
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
            # Top arc
            line = Arc1(
                begin=point_dict["Z1"],
                end=point_dict["Z10"],
                radius=self.get_Rbo(),
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

        if type_add_active in [1, 3]:  # Wind and Wedge
            is_add_wedge = type_add_active == 3
            self.plot_active(
                fig=fig, ax=ax, is_show_fig=False, is_add_wedge=is_add_wedge
            )
        elif type_add_active == 2:  # Magnet
            self.plot_active(
                fig=fig,
                ax=ax,
                is_show_fig=False,
                enforced_default_color=MAGNET_COLOR,
            )

        # Zooming and cleaning
        W = max(self.W1, self.W2, self.W3) * 0.7
        Rint = min(point_dict["Z5"].real, point_dict["Z1"].real)
        Rext = max(point_dict["Z5"].real, point_dict["Z1"].real)

        ax.axis("equal")
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
