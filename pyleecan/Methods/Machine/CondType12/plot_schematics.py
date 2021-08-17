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


def plot_schematics(
    self,
    is_default=False,
    is_add_schematics=True,
    is_add_main_line=True,
    save_path=None,
    is_show_fig=True,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : CondType12
        A CondType12 object
    is_default : bool
        True: plot default schematics, else use current slot values
    is_add_schematics : bool
        True to display the schematics information (W0, H0...)
    is_add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        To call show at the end of the method
    """

    # Use some default parameter
    if is_default:
        cond = type(self)(Wins_cond=40e-3, Wwire=10e-3, Wins_wire=2e-3, Nwppc=4)
        cond.plot_schematics(
            is_default=False,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            save_path=save_path,
            is_show_fig=is_show_fig,
        )
    else:
        # Getting the main plot
        self.plot(is_show_fig=False)  # center slot on Ox axis
        fig = plt.gcf()
        ax = plt.gca()
        a = self.Wwire / 2 + self.Wins_wire

        # Adding schematics
        if is_add_schematics:
            # Wwire
            line = Segment(a - self.Wwire / 2 + 1j * a, a + self.Wwire / 2 + 1j * a)
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Wwire",
                offset_label=1j * self.Wins_wire,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Wins_wire
            line = Segment(
                -self.Wwire / 2 - self.Wins_wire + 1j * self.Wins_wire,
                -self.Wwire / 2 - self.Wins_wire - 1j * self.Wins_wire,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="2*Wins_wire",
                offset_label=-8 * self.Wins_wire,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Wins_cond
            line = Segment(-1j * self.Wins_cond / 2, 1j * self.Wins_cond / 2)
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Wins_cond",
                offset_label=-1j * self.Wins_cond * 0.25 + self.Wins_wire,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Nwppc_rad
            ax.text(
                -a - self.Wwire,
                a,
                "Nwppc=4",
                fontsize=SC_FONT_SIZE,
                bbox=TEXT_BOX,
            )

        # Zooming and cleaning
        W = self.comp_width() * 1.05

        plt.axis("equal")
        ax.set_xlim(-W / 2, W / 2)
        ax.set_ylim(-W / 2, W / 2)
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
