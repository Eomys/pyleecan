import matplotlib.pyplot as plt
import numpy as np

from .comp_coeff import comp_loss_val


def plot_fitting(self, material, is_show_fig=True):
    """Plot the fitted loss curves (from fitted coefficients k_hy, k_ed, k_ex, beta) and the loss data stored in the material

    Parameters
    ----------
    self : LossModelBertotti
        A loss model to compute Bertotti losses
    material : Material
        A material object, corresponding to the material used in the electrical machine.
        This material object must contain loss data as an ImportMatrixVal object.
        This matrix must contain 3 rows, correspoding to the excitation frequency (Hz),
        the peak magnetic flux density (T), and the loss density (W/kg) in this order.
    is_show_fig : bool
        True to show figure
    """

    loss_data = material.mag.LossData.get_data()
    f = loss_data[0]
    B = loss_data[1]
    loss = loss_data[2]

    f_un, i0 = np.unique(f, return_inverse=True)
    fig = plt.figure("Curve fitting for Bertotti iron loss model", figsize=(14, 7))
    B_check = np.linspace(0, 2, 1000)

    ax = plt.gca()

    for ii, f_val in enumerate(f_un):
        f_check = np.ones((1000,)) * f_val
        x_check = np.array([f_check, B_check])
        j0 = np.where(i0 == ii)[0]
        B_experimental = B[j0]
        loss_experimental = loss[j0]
        # x_experimental = values[:, :2].T
        # fitted_loss = comp_loss(x_experimental, *popt)
        # R_list.append(
        #     (key, (np.corrcoef(fitted_loss, loss_experimental)[0, 1]) ** 2)
        # )
        color = ax._get_lines._prop_cycle._cycler_items[np.mod(ii, 10)]["color"]
        # color =  plt.rcParams['axes.prop_cycle']
        plt.plot(
            B_experimental,
            loss_experimental,
            color=color,
            label=f"measurements with f={f_val}Hz",
            marker="o",
        )

        loss_val = comp_loss_val(x_check, self.k_hy, self.k_ed, self.k_ex, self.alpha_B)
        plt.plot(
            B_check,
            loss_val,
            color=color,
            linestyle="dashed",
            label=f"fitting with f={f_val}Hz",
        )
    plt.xlabel("Peak magnetic flux density (T)")
    plt.ylabel("Iron loss (W/kg)")
    plt.title(
        f"Curve fitting for the Bertotti iron loss model of the {material.name} material"
    )

    txt = " $P_{{loss}}=k_{{hy}} f B^{\\beta} + k_{{ed}} (f B)^2 + k_{{ex}} (f B)^{{1.5}}$\n"

    txt += "where:\n"
    txt += "$k_{{hy}}$ = " + format(self.k_hy, ".5E") + "\n"
    txt += "$k_{{ed}}$ = " + format(self.k_ed, ".5E") + "\n"
    txt += "$k_{{ex}}$ = " + format(self.k_ex, ".5E") + "\n"
    txt += "$\\beta$ = " + format(self.alpha_B, ".5E") + "\n"

    # txt += "$\\alpha_f$ = " + format(popt[2], '.5E') +"\n"
    # txt += "$\\alpha_B$ = " + format(popt[3], '.5E') +"\n"
    # plt.title(f"Curve fitting for the iron loss of the {material.name} material")
    # text = textwrap.dedent(
    #     fr"""
    #                         $P_{{loss}}=k_{{hy}} f B^2 + k_{{ed}} (f B)^2 + k_{{ex}} (f B)^{{1.5}}$
    #                         where:
    #                         $k_{{hy}}$ = {popt[0]:.5E}
    #                         $k_{{ed}}$ = {popt[1]:.5E}
    #                         $k_{{ex}}$ = {popt[2]:.5E}
    #                         """
    # )

    fig.text(0.02, 0.5, txt, fontsize=12)
    plt.subplots_adjust(left=0.26)
    plt.legend()
    if is_show_fig:
        plt.show()
