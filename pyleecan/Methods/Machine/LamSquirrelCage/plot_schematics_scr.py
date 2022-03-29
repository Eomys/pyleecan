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


def plot_schematics_scr(
    self,
    is_default=False,
    is_add_schematics=True,
    is_add_main_line=True,
    save_path=None,
    is_show_fig=True,
):
    """Plot the schematics of the short circuit ring

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    is_default : bool
        True: plot default schematics, else use current lamination values
    is_add_schematics : bool
        True to display the schematics information (Hscr, Lscr...)
    is_add_main_line : bool
        True to display "main lines" (dotted lines and Z axis)
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        To call show at the end of the method
    """

    # Use some default parameter
    if is_default:
        lam = type(self)(
            is_stator=False, is_internal=True, Rint=0, Rext=1, Hscr=0.1, Lscr=0.2
        )
        lam.plot_schematics_scr(
            is_default=False,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            save_path=save_path,
            is_show_fig=is_show_fig,
        )
    else:
        # Getting the main plot
        self.plot_side(is_show_fig=False)
        fig = plt.gcf()
        ax = plt.gca()
        Lt = self.comp_length()

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
                offset_label=self.H0 * 0.1 + 1j * self.W0 * 0.1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W1
            Zlim1 = point_dict["Z2"].real + 1j * point_dict["Z3"].imag
            Zlim2 = point_dict["Z9"].real + 1j * point_dict["Z8"].imag
            plot_quote(
                point_dict["Z3"],
                Zlim1,
                Zlim2,
                point_dict["Z8"],
                offset_label=self.get_H1() * 0.1 + 1j * self.W0 * 0.1,
                fig=fig,
                ax=ax,
                label="W1",
            )
            # W2
            Zlim1 = point_dict["Z5"] + sign * 0.1 * self.H2
            Zlim2 = point_dict["Z6"] + sign * 0.1 * self.H2
            plot_quote(
                point_dict["Z5"],
                Zlim1,
                Zlim2,
                point_dict["Z6"],
                offset_label=sign * 0.05 * self.H2,
                fig=fig,
                ax=ax,
                label="W2",
            )
            # H0
            line = Segment(point_dict["Z10"], point_dict["Z9"])
            line.plot(
                fig=fig,
                ax=ax,
                label="H0",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.W0 * 0.1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H1
            line = Segment(point_dict["Z9"], point_dict["Z7"])
            line.plot(
                fig=fig,
                ax=ax,
                label="H1",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.W0 * 0.1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H2
            line = Segment(point_dict["Z6"].real, point_dict["Z7"].real)
            line.plot(
                fig=fig,
                ax=ax,
                label="H2",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.W0 * 0.1,
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
            self.plot_active(fig=fig, is_show_fig=False, is_add_wedge=is_add_wedge)
        elif type_add_active == 2:  # Magnet
            self.plot_active(
                fig=fig,
                is_show_fig=False,
                enforced_default_color=MAGNET_COLOR,
            )

        # Zooming and cleaning
        W = (
            max(point_dict["Z8"].imag, point_dict["Z6"].imag, point_dict["Z10"].imag)
            * 1.1
        )
        Rint = min(point_dict["Z6"].real, point_dict["Z1"].real)
        Rext = max(point_dict["Z6"].real, point_dict["Z1"].real)

        plt.axis("equal")
        ax.set_xlim(Rint, Rext)
        ax.set_ylim(-W, W)
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(type(self).__name__ + " Schematics")
        ax.set_title("")
        ax.get_legend().remove()
        ax.set_axis_off()

        # Save / Show
        if save_path is not None:
            fig.savefig(save_path)
            plt.close()

        if is_show_fig:
            fig.show()
