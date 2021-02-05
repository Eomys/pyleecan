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
    self : CondType11
        A CondType11 object
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
        cond = type(self)(
            Hwire=10e-3, Wwire=22e-3, Wins_wire=2e-3, Nwppc_rad=3, Nwppc_tan=2
        )
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

        # Adding schematics
        if is_add_schematics:
            # Wwire
            line = Segment(
                3 * self.Wins_wire
                + self.Wwire
                + 1j * (self.Wins_wire + self.Hwire / 2),
                3 * self.Wins_wire
                + 2 * self.Wwire
                + 1j * (self.Wins_wire + self.Hwire / 2),
            )
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
            # Hwire
            line = Segment(
                1j * (3 * self.Wins_wire + self.Hwire)
                + (self.Wins_wire + self.Wwire / 2),
                1j * (3 * self.Wins_wire + 2 * self.Hwire)
                + (self.Wins_wire + self.Wwire / 2),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Hwire",
                offset_label=self.Wins_wire,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Wins_wire
            line = Segment(
                1 * self.Wins_wire
                + self.Wwire
                + 1j * (2 * self.Wins_wire + self.Hwire * 3 / 2),
                3 * self.Wins_wire
                + 1 * self.Wwire
                + 1j * (2 * self.Wins_wire + self.Hwire * 3 / 2),
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Wins_wire",
                offset_label=1j * self.Wins_wire,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Nwppc_rad
            ax.text(
                self.Wins_wire + self.Wwire * 0.2,
                self.Wins_wire + self.Hwire * 0.5,
                "Nwppc_rad=3",
                fontsize=SC_FONT_SIZE,
                bbox=TEXT_BOX,
            )
            # Nwppc_tan
            ax.text(
                self.Wins_wire + self.Wwire * 0.2,
                5 * self.Wins_wire + 2.5 * self.Hwire,
                "Nwppc_tan=2",
                fontsize=SC_FONT_SIZE,
                bbox=TEXT_BOX,
            )

        if is_add_main_line:
            for ii in range(1, self.Nwppc_tan):
                line = Segment(
                    ii * (self.Wwire + 2 * self.Wins_wire),
                    ii * (self.Wwire + 2 * self.Wins_wire) + 1j * self.comp_height(),
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=MAIN_LINE_COLOR,
                    linestyle=MAIN_LINE_STYLE,
                    linewidth=MAIN_LINE_WIDTH,
                )
            for ii in range(1, self.Nwppc_rad):
                line = Segment(
                    1j * ii * (self.Hwire + 2 * self.Wins_wire),
                    1j * ii * (self.Hwire + 2 * self.Wins_wire) + self.comp_width(),
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=MAIN_LINE_COLOR,
                    linestyle=MAIN_LINE_STYLE,
                    linewidth=MAIN_LINE_WIDTH,
                )

        # Zooming and cleaning
        W = self.comp_width() * 1.1
        H = self.comp_height() * 1.1

        plt.axis("equal")
        ax.set_xlim(-W * 0.1, W)
        ax.set_ylim(-H * 0.1, H)
        fig.canvas.set_window_title(type(self).__name__ + " Schematics")
        ax.set_title("")
        ax.get_legend().remove()
        ax.set_axis_off()

        # Save / Show
        if save_path is not None:
            fig.savefig(save_path)
            plt.close()

        if is_show_fig:
            fig.show()
