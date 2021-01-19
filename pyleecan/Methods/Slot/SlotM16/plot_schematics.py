from numpy import pi
from ....Classes.LamSlot import LamSlot
from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
import matplotlib.pyplot as plt
from ....Methods import ParentMissingError
from ....Functions.Plot import (
    P_FONT_SIZE,
    SC_FONT_SIZE,
    TEXT_BOX,
    ARROW_WIDTH,
    ARROW_COLOR,
    SC_LINE_COLOR,
    SC_LINE_STYLE,
    SC_LINE_WIDTH,
    MAIN_LINE_COLOR,
    MAIN_LINE_STYLE,
    MAIN_LINE_WIDTH,
    plot_quote,
)


def plot_schematics(
    self,
    is_default=False,
    add_point_label=False,
    add_schematics=True,
    add_main_line=True,
    add_active=True,
    save_path=None,
    is_show_fig=True,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object
    is_default : bool
        True: plot default schematics, else use current slot values
    add_point_label : bool
        True to display the name of the points (Z1, Z2....)
    add_schematics : bool
        True to display the schematics information (W0, H0...)
    add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    add_active : bool
        True to display the active surface
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        To call show at the end of the method
    """

    # Use some default parameter
    if is_default:
        slot = type(self)(Zs=4, W0=0.02, H0=0.01, H1=0.06, W1=0.04)
        lam = LamSlot(
            Rint=80e-3, Rext=240e-3, is_internal=True, is_stator=False, slot=slot
        )
        slot.plot_schematics(
            is_default=False,
            add_point_label=add_point_label,
            add_schematics=add_schematics,
            add_main_line=add_main_line,
            add_active=add_active,
            save_path=save_path,
            is_show_fig=is_show_fig,
        )
    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The slot is not inside a Lamination")
        lam = self.parent
        lam.plot(alpha=pi / self.Zs, is_show_fig=False)  # center slot on Ox axis
        fig = plt.gcf()
        ax = plt.gca()
        point_dict = self._comp_point_coordinate()
        if self.is_outwards():
            sign = +1
        else:
            sign = -1

        # Adding point label
        if add_point_label:
            for name, Z in point_dict.items():
                ax.text(
                    Z.real,
                    Z.imag,
                    name,
                    fontsize=P_FONT_SIZE,
                    bbox=TEXT_BOX,
                )

        # Adding schematics
        if add_schematics:
            # W0
            line = Segment(point_dict["Z7"], point_dict["Z2"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=self.H0 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W1
            line = Segment(point_dict["Z5"], point_dict["Z4"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W1",
                offset_label=self.H0 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H0
            plot_quote(
                Z1=point_dict["Z1"],
                Zlim1=point_dict["Z1"].real + 1j * point_dict["Z3"].imag,
                Zlim2=point_dict["Z3"],
                Z2=point_dict["Z2"],
                offset_label=1j * 0.1 * self.W0,
                fig=fig,
                ax=ax,
                label="H0",
            )
            # H1
            line = Segment(point_dict["Z5"], point_dict["Z6"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H1",
                offset_label=1j * self.W0 * 0.1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

        if add_main_line:
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
                end=point_dict["Z8"],
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

        if add_active:
            self.plot_active(fig=fig, is_show_fig=False)

        # Zooming and cleaning
        W = self.W1 / 2 * 1.2
        Rint, Rext = self.comp_radius()

        plt.axis("equal")
        ax.set_xlim(Rint, Rext)
        ax.set_ylim(-W, W)
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
