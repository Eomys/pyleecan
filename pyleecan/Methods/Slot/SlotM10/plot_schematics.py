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
        slot = type(self)(Zs=8, H0=20e-3, W0=45e-3, Hmag=17.5e-3, Wmag=30e-3)
        lam = LamSlot(
            Rint=0.1, Rext=0.135, is_internal=True, is_stator=False, slot=slot
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
            line = Segment(point_dict["Z3"], point_dict["Z2"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=self.Hmag * 0.1,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Wmag
            plot_quote(
                Z1=point_dict["ZM2"],
                Zlim1=point_dict["ZM2"] - sign * 0.5 * self.Hmag,
                Zlim2=point_dict["ZM3"] - sign * 0.5 * self.Hmag,
                Z2=point_dict["ZM3"],
                offset_label=0.25 * self.Hmag,
                fig=fig,
                ax=ax,
                label="Wmag",
            )
            # H0
            line = Segment(point_dict["Z1"], point_dict["Z2"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H0",
                offset_label=1j * -0.1 * self.W0,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # Hmag
            Zlim1 = point_dict["Z3"] - sign * self.Hmag
            Zlim2 = point_dict["Z3"]
            plot_quote(
                point_dict["ZM3"],
                Zlim1,
                Zlim2,
                point_dict["ZM4"],
                offset_label=1j * 0.2 * self.Hmag,
                fig=fig,
                ax=ax,
                label="Hmag",
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
                end=point_dict["Z4"],
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
        W = self.W0 / 2 * 1.4
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
