from SciDataTool.Functions.Plot.plot_2D import plot_2D
from ....Functions.Plot import dict_2D
from ....Functions.load import import_class

from numpy import pi


def plot(
    self,
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

    legend_list = ["Skew pattern"]
    y_list = [[a * 180 / pi for a in angle_list]]
    linestyle_list = ["solid"]

    LamSlotM = import_class("pyleecan.Classes", "LamSlotM")
    LamH = import_class("pyleecan.Classes", "LamH")

    if isinstance(self.parent, (LamSlotM, LamH)):
        legend_list.append("Rotor d-axis")
        y_list.append([0 for z in z_list])
        linestyle_list.append("dashed")

    plot_2D(
        [z_list],
        y_list,
        xlabel="Axial direction from Non Drive End to Drive End [m]",
        ylabel=lam_name + " skew angle [°]",
        type_plot="curve_point",
        fig=fig,
        ax=ax,
        is_show_fig=is_show_fig,
        save_path=save_path,
        win_title=win_title,
        legend_list=legend_list,
        linestyle_list=linestyle_list,
        **dict_2D,
    )
