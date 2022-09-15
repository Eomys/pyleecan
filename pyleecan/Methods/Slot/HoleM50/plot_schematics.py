import matplotlib.pyplot as plt
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.LamHole import LamHole
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
    type_add_active=True,
    save_path=None,
    is_show_fig=True,
    fig=None,
    ax=None,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object
    is_default : bool
        True: plot default schematics, else use current slot values
    is_add_point_label : bool
        True to display the name of the points (Z1, Z2....)
    is_add_schematics : bool
        True to display the schematics information (W0, H0...)
    is_add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    type_add_active : int
        0: No active surface, 1: active surface as winding, 2: active surface as magnet
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
        hole = type(self)(
            H0=0.01496,
            H1=0.0065,
            H2=0.003,
            H3=0.0085,
            H4=0.004,
            W0=0.042,
            W1=0.005,
            W2=0.004,
            W3=0.007,
            W4=0.0129,
            Zh=8,
        )
        lam = LamHole(
            Rint=0.05532, Rext=0.0812, is_internal=True, is_stator=False, hole=[hole]
        )
        return hole.plot_schematics(
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
    elif type_add_active == 0:
        # Remove magnets
        lam = self.parent.copy()
        lam.hole[0].remove_magnet()
        return lam.hole[0].plot_schematics(
            is_default=False,
            is_add_point_label=is_add_point_label,
            is_add_schematics=is_add_schematics,
            is_add_main_line=is_add_main_line,
            type_add_active=2,
            save_path=save_path,
            is_show_fig=is_show_fig,
            fig=fig,
            ax=ax,
        )
    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The hole is not inside a Lamination")
        lam = self.parent
        alpha = pi / 2  # To rotate the schematics
        rot = exp(1j * alpha)
        fig, ax = lam.plot(
            alpha=pi / self.Zh + alpha,
            is_show_fig=False,
            is_lam_only=type_add_active == 0,
            fig=fig,
            ax=ax,
        )  # center hole on Ox axis
        sp = 2 * pi / self.Zh
        Rbo = self.get_Rbo()
        point_dict = self._comp_point_coordinate()

        # Adding point label
        if is_add_point_label:
            for name, Z in point_dict.items():
                Z = Z * rot
                ax.text(Z.real, Z.imag, name, fontsize=P_FONT_SIZE, bbox=TEXT_BOX)

        # Adding schematics
        if is_add_schematics:
            kwargs = dict(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W0
            line = Segment(point_dict["Z9"] * rot, point_dict["Z9s"] * rot)
            line.plot(
                label="W0", offset_label=self.W0 * 0.3 + 1j * self.H3 * 0.2, **kwargs
            )
            # W1
            line = Segment(
                (point_dict["Z8"] + point_dict["Z7"]) / 2 * rot,
                (point_dict["Z8s"] + point_dict["Z7s"]) / 2 * rot,
            )
            line.plot(label="W1", offset_label=-1j * self.H3 * 0.4, **kwargs)
            # W2
            line = Segment(point_dict["Z8"] * rot, point_dict["Z8b"] * rot)
            line.plot(label="W2", offset_label=1j * self.H3 * 0.2, **kwargs)
            # W3
            line = Segment(
                (point_dict["Z1s"] + point_dict["Z11s"]) * 0.5 * rot,
                (point_dict["Z1"] + point_dict["Z11"]) * 0.5 * rot * exp(1j * sp),
            )
            line.plot(label="W3", offset_label=-1j * self.H3 * 0.3, **kwargs)
            # W4
            line = Segment(point_dict["Z5"] * rot, point_dict["Z4"] * rot)
            line.plot(label="W4", offset_label=-1j * self.H3 * 0.3, **kwargs)
            # H0
            line = Segment(Rbo * rot, point_dict["Z8"].real * rot)
            line.plot(
                label="H0", offset_label=self.W0 * 0.05 + 1j * self.H3 * 0.2, **kwargs
            )
            # H1
            line = Segment(
                Rbo * exp(-1j * sp / 2) * rot,
                (Rbo - self.H1) * exp(-1j * sp / 2) * rot,
            )
            line.plot(label="H1", offset_label=self.H3 * 0.2, **kwargs)
            # H2
            line = Segment(
                (point_dict["Z3s"] + point_dict["Z6s"]) * 0.5 * rot,
                (point_dict["Z4s"] + point_dict["Z5s"]) * 0.5 * rot,
            )
            line.plot(label="H2", offset_label=self.H3 * 0.2, **kwargs)
            # H3
            line = Segment(point_dict["Z4s"] * rot, point_dict["Z8cs"] * rot)
            line.plot(label="H3", offset_label=self.H3 * 0.2, **kwargs)
            # H4
            line = Segment(point_dict["Z9s"] * rot, point_dict["Z10s"] * rot)
            line.plot(label="H4", offset_label=self.H3 * 0.2, **kwargs)

        if is_add_main_line:
            lines = []
            # Ox axis
            lines.append(Segment(0, lam.Rext * 1.5 * rot))

            # Tooth axis
            lines.append(Segment(0, lam.Rext * 1.5 * exp(1j * sp / 2) * rot))

            lines.append(Segment(0, lam.Rext * 1.5 * exp(-1j * sp / 2) * rot))
            # H1 radius
            R = Rbo - self.H1
            rot_N = exp(-1j * pi / 2 * 0.9) * rot
            rot_P = exp(1j * pi / 2 * 0.9) * rot
            lines.append(
                Arc1(begin=R * rot_N, end=R * rot_P, radius=R, is_trigo_direction=True)
            )
            # H4 radius
            R = Rbo - self.H1 + self.H4
            lines.append(
                Arc1(begin=R * rot_N, end=R * rot_P, radius=R, is_trigo_direction=True)
            )
            # W1 lines
            lines.append(Segment(point_dict["Z7"] * rot, point_dict["Z7s"] * rot))
            lines.append(Segment(point_dict["Z8"] * rot, point_dict["Z8s"] * rot))
            # W2 lines
            lines.append(Segment(point_dict["Z8"] * rot, point_dict["Z8a"] * rot))
            lines.append(Segment(point_dict["Z8s"] * rot, point_dict["Z8as"] * rot))
            # H2 lines
            lines.append(Segment(point_dict["Z3s"] * rot, point_dict["Z6s"] * rot))

            for line in lines:
                line.plot(
                    fig=fig,
                    ax=ax,
                    color=MAIN_LINE_COLOR,
                    linestyle=MAIN_LINE_STYLE,
                    linewidth=MAIN_LINE_WIDTH,
                )

        # Zooming and cleaning
        W = abs(point_dict["Z11s"].imag) * 1.3
        Rint = self.parent.Rint
        Rext = self.parent.Rext

        ax.axis("equal")
        ax.set_ylim(Rint, Rext)
        ax.set_xlim(-W, W)
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
