from SciDataTool.Functions.Plot.plot_2D import plot_2D
from ....Functions.Plot import dict_2D

from numpy import pi


def plot(
    self,
    skew_axis=None,
    fig=None,
    ax=None,
    lam_name="",
    is_show_fig=False,
    save_path=None,
    win_title=None,
):
    """Plots skew angle

    Parameters
    ----------
    self : Skew
        a Skew object

    """

    angle_list, z_list = self.comp_pattern()

    plot_2D(
        [z_list],
        [[a * 180 / pi for a in angle_list]],
        xlabel="Axial direction [m]",
        ylabel=lam_name + " skew angle [°]",
        type_plot="curve_point",
        fig=fig,
        ax=ax,
        is_show_fig=is_show_fig,
        save_path=save_path,
        win_title=win_title,
        **dict_2D,
    )
