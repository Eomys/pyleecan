# -*- coding: utf-8 -*-

from ....Functions.Plot.plot_A_2D import plot_A_2D
from ....Functions.init_fig import init_subplot

import matplotlib.pyplot as plt


def plot(self, skew_axis=None, fig=None, ax=None, lam_name=""):
    """Plots skew angle 
    
    Parameters
    ----------
    self : Skew
        a Skew object

    """

    if self.angle_list is None:
        self.comp_angle()

    angle_list = self.angle_list
    z_list = self.z_list

    if self.is_step:
        if skew_axis is None:
            plot_A_2D(
                [3 / 2 * z_list[0] - z_list[1] / 2]
                + z_list
                + [3 / 2 * z_list[-1] - z_list[-2] / 2],
                [[angle_list[0]] + angle_list + [angle_list[-1]]],
                xlabel="z [m]",
                ylabel=lam_name + " skew angle [rad]",
                type="step",
                fig=fig,
                ax=ax,
            )
        else:
            # fig, ax = init_subplot(fig=fig)
            L = self.parent.comp_length()
            ax = plot_A_2D(
                [z * L for z in skew_axis],
                [angle_list + [angle_list[-1]]],
                type="step",
                fig=fig,
                ax=ax,
            )
            plot_A_2D(
                z_list,
                [angle_list],
                xlabel="z [m]",
                ylabel=lam_name + " skew angle [rad]",
                type="scatter",
                fig=fig,
                ax=ax,
            )
            plt.gcf()
            plt.grid()
    else:
        plot_A_2D(
            z_list,
            [angle_list],
            xlabel="z [m]",
            ylabel=lam_name + " skew angle [rad]",
            type="curve_point",
            fig=fig,
            ax=ax,
        )

    return ax
