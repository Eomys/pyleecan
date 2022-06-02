# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from itertools import groupby
import textwrap


def comp_coeff(self, material):
    """Enables to compute the coefficients of the loss model with a curve fitting
    on loss data stored in the material

    Parameters
    ----------
    material : Material
        A material object, corresponding to the material used in the electrical machine.
        This material object must contain loss data as an ImportMatrixVal object.
        This matrix must contain 3 rows, correspoding to the excitation frequency (Hz),
        the peak magnetic flux density (T), and the loss density (W/kg) in this order.
    """

    def comp_loss(xdata, k_hy, k_ed, k_ex):
        f = xdata[0]
        B = xdata[1]
        return k_hy * f * B ** 2 + k_ed * (f * B) ** 2 + k_ex * (f * B) ** 1.5

    def group_by_frequency(loss_data):
        groups = []
        uniquekeys = []
        loss_data_T = loss_data.T
        for k, g in groupby(loss_data_T, lambda x: x[0]):
            groups.append(list(g))  # Store group iterator as a list
            uniquekeys.append(k)
        return groups, uniquekeys

    loss_data = material.mag.LossData.get_data()
    f = loss_data[0]
    B = loss_data[1]
    loss = loss_data[2]
    xdata = np.array([f, B])
    ydata = np.array(loss)
    popt, _ = curve_fit(
        comp_loss, xdata, ydata, bounds=([0, 0, 0], [np.inf, np.inf, np.inf])
    )

    if self.is_show_fig:
        groups, uniquekeys = group_by_frequency(loss_data)
        fig = plt.figure("Curve fitting for Iron losses", figsize=(14, 7))
        B_check = np.linspace(0, 2, 1000)
        ax = plt.gca()
        for index, key in enumerate(uniquekeys):
            f_check = np.ones((1000,)) * key
            xverif = np.array([f_check, B_check])
            values = np.array(groups[index])
            B_experimental = values[:, 1]
            loss_experimental = values[:, 2]
            color = next(ax._get_lines.prop_cycler)["color"]
            plt.plot(
                B_experimental,
                loss_experimental,
                color=color,
                label=f"measurements with f={key}Hz",
                marker="o",
            )
            plt.plot(
                B_check,
                comp_loss(xverif, *popt),
                color=color,
                linestyle="dashed",
                label=f"fitting with f={key}Hz",
            )
        plt.xlabel("Peak magnetic flux density (T)")
        plt.ylabel("Iron loss (W/kg")
        plt.title(f"Curve fitting for the iron loss of the {material.name} material")
        text = textwrap.dedent(
            fr"""                    
                                $P_{{loss}}=k_{{hy}} f B^2 + k_{{ed}} (fB)^2 + k_{{ex}} (fB)^{{1.5}}$
                                where:
                                $k_{{hy}}$ = {popt[0]:.5E}
                                $k_{{ed}}$ = {popt[1]:.5E}
                                $k_{{ex}}$ = {popt[2]:.5E}
                                """
        )
        fig.text(0.02, 0.5, text, fontsize=12)
        plt.subplots_adjust(left=0.23)
        plt.legend()
        plt.show()

    self.k_hy = popt[0]
    self.k_ed = popt[1]
    self.k_ex = popt[2]
