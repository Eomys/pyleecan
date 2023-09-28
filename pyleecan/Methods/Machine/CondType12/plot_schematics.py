import matplotlib.pyplot as plt
from ....Classes.Segment import Segment
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
    fig=None,
    ax=None,
    is_single=False,
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
    """

    # Use some default parameter
    if is_default and is_single:
        cond = type(self)(Wins_cond=40e-3, Wwire=35e-3, Wins_wire=5e-3, Nwppc=1)
        return cond.plot_schematics(
            is_default=False,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            save_path=save_path,
            is_show_fig=is_show_fig,
            fig=fig,
            ax=ax,
            is_single=is_single,
        )
    elif is_default:
        cond = type(self)(Wins_cond=40e-3, Wwire=10e-3, Wins_wire=2e-3, Nwppc=4)
        return cond.plot_schematics(
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
        fig, ax = self.plot(is_show_fig=False, fig=fig, ax=ax)  # center slot on Ox axis
        a = self.Wwire / 2 + self.Wins_wire

        # Adding schematics
        if is_add_schematics:
            if is_single:
                # Wwire
                line = Segment(-self.Wwire / 2, self.Wwire / 2)
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="Conductor diameter",
                    offset_label=1j * self.Wins_wire / 2,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
                # Wins_wire
                line = Segment(
                    1j * (self.Wwire / 2 + self.Wins_wire), 1j * self.Wwire / 2
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="Insulator thickness",
                    offset_label=self.Wins_wire / 2,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
            else:
                # Wwire
                line = Segment(a - self.Wwire / 2 + 1j * a, a + self.Wwire / 2 + 1j * a)
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="Strand diameter",
                    offset_label=1j * self.Wins_wire,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
                # Wins_wire
                line = Segment(
                    -self.Wwire / 2 - self.Wins_wire + 1j * self.Wins_wire,
                    -self.Wwire / 2 - self.Wins_wire,
                )
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=ARROW_COLOR,
                    linewidth=ARROW_WIDTH,
                    label="Insulator thickness",
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
                    label="Overall diameter",
                    offset_label=-1j * self.Wins_cond * 0.25 + self.Wins_wire / 2,
                    is_arrow=True,
                    fontsize=SC_FONT_SIZE,
                )
                # Nwppc_rad
                ax.text(
                    -a - 2 * self.Wwire,
                    2.5 * a,
                    "Strands in hand: 4",
                    fontsize=SC_FONT_SIZE,
                    bbox=TEXT_BOX,
                )

        # Zooming and cleaning
        if is_single:
            W = self.comp_width() * 1.2
        else:
            W = self.comp_width() * 1.05

        ax.axis("equal")
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
            plt.close(fig=fig)

        if is_show_fig:
            fig.show()
        return fig, ax
