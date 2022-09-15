import matplotlib.pyplot as plt
from numpy import pi, exp
import numpy as np

from ....Classes.Arc1 import Arc1
from ....Classes.LamSlot import LamSlot
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.Winding import Winding
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
    self : SlotW60
        A SlotW60 object
    is_default : bool
        True: plot default schematics, else use current slot values
    is_add_point_label : bool
        True to display the name of the points (Z1, Z2....)
    is_add_schematics : bool
        True to display the schematics information (W0, H0...)
    is_add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    type_add_active : int
        0: No active surface, 1: active surface as winding, 2: active surface as magnet, 3: active surface as winding + wedges
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
    """

    # Use some default parameter
    if is_default:
        slot = type(self)(
            Zs=12,
            H1=20e-3,
            H2=65e-3,
            W1=100e-3,
            W2=40e-3,
            R1=100e-3,
            W3=17e-3,
            H3=17e-3,
            H4=17e-3,
        )
        lam = LamSlot(Rint=0.135, Rext=0.3, is_internal=True, is_stator=True, slot=slot)

        return slot.plot_schematics(
            is_default=False,
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
        fig, ax = lam.plot(is_show_fig=False, fig=fig, ax=ax)  # center slot on Ox axis
        point_dict = dict()
        point_dict_temp = self._comp_point_coordinate()
        for key in point_dict_temp:
            point_dict[key] = point_dict_temp[key] * exp(
                1j * (pi / self.Zs + 4 * pi / self.Zs)
            )
            point_dict[key + "d"] = point_dict[key] * exp(1j * (2 * pi / self.Zs))
            point_dict[key + "dd"] = point_dict[key + "d"] * exp(
                1j * (2 * pi / self.Zs)
            )

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
            # W1
            line = Segment(
                (point_dict["Z2d"] + point_dict["Z3d"]) / 2,
                (point_dict["Z9"] + point_dict["Z10"]) / 2,
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="W1",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=0.9j * self.W1 * 0.1 - (0.007 + 0j),
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H1
            Zlim1 = point_dict["Z2d"]
            Zlim2 = point_dict["Z3d"]
            plot_quote(
                point_dict["Z2d"],
                Zlim1 - (0.006 + 0j),
                Zlim2 - (0.006 + 0j),
                point_dict["Z3d"],
                offset_label=self.H1 * -1.0 - 0.6j * self.W1 * 0.05,
                fig=fig,
                ax=ax,
                label="H1",
            )
            # H2
            Zlim1 = point_dict["Z8"]
            Zlim2 = point_dict["Z7"]
            plot_quote(
                point_dict["Z8"],
                Zlim1 + (0.035 + 0j),
                Zlim2 + (0.035 + 0j),
                point_dict["Z7"],
                offset_label=self.H1 * 0.3 + 2j * self.W1 * 0.05,
                fig=fig,
                ax=ax,
                label="H2",
            )
            # W2
            line = Segment(
                (point_dict["Z4d"] + point_dict["Z5d"]) / 2,
                (point_dict["Z8"] + point_dict["Z7"]) / 2,
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="W2",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=-1.6j * self.W1 * 0.1 - (0.007 + 0j),
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # R1
            Zlim1 = point_dict["Z2dd"]
            Zlim2 = point_dict["Zcd"]
            plot_quote(
                point_dict["Zcd"],
                Zlim1,
                Zlim2,
                point_dict["Z10d"],
                offset_label=0.009 * self.W1 + 0.010j,
                fig=fig,
                ax=ax,
                label="R1",
            )

            # W5d
            Zlim1 = point_dict["Zw5d"]
            Zlim2 = point_dict["Zw5d"]
            plot_quote(
                point_dict["Z3d"],
                Zlim1,
                Zlim2,
                point_dict["Z5d"],
                offset_label=0,
                fig=fig,
                ax=ax,
                label=None,
            )
            # W5
            Zlim1 = point_dict["Zw5"]
            Zlim2 = point_dict["Zw5"]
            plot_quote(
                point_dict["Z3"],
                Zlim1,
                Zlim2,
                point_dict["Z5"],
                offset_label=0,
                fig=fig,
                ax=ax,
                label=None,
            )
            # H3
            line = Segment(
                ((point_dict["Z3d"] + point_dict["Z4d"]) / 2) + (0.008 + 0j),
                ((point_dict["Zw4d"] + point_dict["Zw1d"]) / 2),
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="H3",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=(-0.2j * self.W1 * 0.1) - (0.020 + 0j),
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H4
            line = Segment(
                ((point_dict["Z5d"] + point_dict["Zw5d"]) / 2) + (0.008 + 0j),
                ((point_dict["Zw2d"] + point_dict["Zw3d"]) / 2),
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="H4",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=(-0.2j * self.W1 * 0.1) - (0.020 + 0j),
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W3
            line = Segment(
                ((point_dict["Zw5"] + point_dict["Z3"]) / 2),
                ((point_dict["Zw4"] + point_dict["Zw3"]) / 2),
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="W3",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=(-1.8j * self.W1 * 0.1) - (0.007 + 0j),
                is_arrow=True,
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
            # Top arc
            line = Arc1(
                begin=self.get_Rbo(),
                end=-self.get_Rbo(),
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
            is_add_wedge = False  # No wedge for this false
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                is_add_wedge=is_add_wedge,
                wind_mat=np.ones((1, 2, self.Zs, 1)),
                alpha=pi / self.Zs + 2 * pi / self.Zs,
            )
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                is_add_wedge=is_add_wedge,
                wind_mat=np.ones((1, 2, self.Zs, 1)),
                alpha=pi / self.Zs + 4 * pi / self.Zs,
            )
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                is_add_wedge=is_add_wedge,
                wind_mat=np.ones((1, 2, self.Zs, 1)),
                alpha=pi / self.Zs + 6 * pi / self.Zs,
            )
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                is_add_wedge=is_add_wedge,
                wind_mat=np.ones((1, 2, self.Zs, 1)),
                alpha=pi / self.Zs + 8 * pi / self.Zs,
            )

        elif type_add_active == 2:  # Magnet
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                enforced_default_color=MAGNET_COLOR,
            )

        # Zooming and cleaning
        ax.axis("equal")
        ax.set_ylim(abs(point_dict["Z1"]) * 0.5, abs(point_dict["Z1"]) * 1.2)
        ax.set_xlim(self.W1 * -0.5, self.W1 * 0.5)
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(type(self).__name__ + " Schematics")
        ax.set_title("")
        ax.get_legend().remove()
        ax.set_axis_off()

        # Save / Show
        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)

        if is_show_fig:
            fig.show()
        return fig, ax
