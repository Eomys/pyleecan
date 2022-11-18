import matplotlib.pyplot as plt
from numpy import pi, exp, angle

from ....Classes.Arc1 import Arc1
from ....Classes.Lamination import Lamination
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
    is_add_schematics=True,
    is_add_main_line=True,
    save_path=None,
    is_show_fig=True,
    fig=None,
    ax=None,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : BoreSinePole
        A BoreSinePole object
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
        bore = type(self)(N=8, delta_d=10e-3, delta_q=50e-3, W0=165e-3, alpha=0)
        lam = Lamination(
            Rint=0.135, Rext=0.3, is_internal=True, is_stator=False, bore=bore
        )
        return bore.plot_schematics(
            is_default=False,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            save_path=save_path,
            is_show_fig=is_show_fig,
            fig=fig,
            ax=ax,
        )
    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The bore is not inside a Lamination")
        lam = self.parent
        fig, ax = lam.plot(is_show_fig=False, fig=fig, ax=ax)

        # Comp point coordinates
        lines = self.get_bore_line()
        Zq1 = lines[0].get_end()
        Zq2 = lines[-1].get_begin()
        Rbo = self.parent.get_Rbo()
        alpha = pi / self.N
        # H = self.Rarc / 8  # Small distance for label placement

        # Adding schematics
        if is_add_schematics:
            # delta_q
            p1 = Rbo + self.delta_d - self.delta_q
            p2 = Rbo + self.delta_d
            line = Segment(p1 * exp(2j * alpha), p2 * exp(2j * alpha))
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="delta_q",
                offset_label=self.delta_q / 2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W0
            line = Segment(Zq1 * exp(2 * 1j * alpha), Zq2 * exp(4 * 1j * alpha))
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=0,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Rbo + delta_d
            line = Segment(0, Rbo + self.delta_d)
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="Rbo + delta_d",
                offset_label=-Rbo / 4,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

        if is_add_main_line:
            plot_args = dict(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Ox axis
            # line = Segment(0, lam.Rext * 1.5)
            # line.plot(**plot_args)
            # Rarc
            # line = Segment(Zc, Z1)
            # line.plot(
            #     fig=fig,
            #     ax=ax,
            #     color=MAIN_LINE_COLOR,
            #     linestyle=MAIN_LINE_STYLE,
            #     linewidth=MAIN_LINE_WIDTH,
            # )
            # line = Segment(Zc, Z2)
            # line.plot(
            #     fig=fig,
            #     ax=ax,
            #     color=MAIN_LINE_COLOR,
            #     linestyle=MAIN_LINE_STYLE,
            #     linewidth=MAIN_LINE_WIDTH,
            # )
            # Machine center
            line = Segment(0, Rbo * exp(1j * alpha))
            line.plot(**plot_args)
            # Rbo circle arc
            Z1 = Rbo * exp(-1j * pi / 2)
            Z2 = Rbo * exp(1j * pi / 2)
            line = Arc1(begin=Z1, end=Z2, radius=Rbo, is_trigo_direction=True)
            line.plot(**plot_args)
            line = Arc1(begin=Z2, end=Z1, radius=Rbo, is_trigo_direction=True)
            line.plot(**plot_args)
            # Rbo + delta_d circle arc
            R = Rbo + self.delta_d
            Z1 = R * exp(-1j * pi / 2)
            Z2 = R * exp(1j * pi / 2)
            line = Arc1(begin=Z1, end=Z2, radius=R, is_trigo_direction=True)
            line.plot(**plot_args)
            line = Arc1(begin=Z2, end=Z1, radius=R, is_trigo_direction=True)
            line.plot(**plot_args)

        # Zooming and cleaning

        ax.axis("equal")
        ax.set_xlim(0, Rbo)
        ax.set_ylim(-Rbo / 10, Rbo * 1.1)
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
