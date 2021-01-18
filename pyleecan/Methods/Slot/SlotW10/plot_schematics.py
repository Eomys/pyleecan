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
    self : SlotW10
        A SlotW10 object
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
        slot = type(self)(
            Zs=8, H0=10e-3, W0=20e-3, H1=10e-3, H2=40e-3, W1=40e-3, W2=30e-3
        )
        lam = LamSlot(
            Rint=0.135, Rext=0.3, is_internal=False, is_stator=True, slot=slot
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
            sign = 1
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

        if add_active:
            self.plot_active(fig=fig, is_show_fig=False)

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
