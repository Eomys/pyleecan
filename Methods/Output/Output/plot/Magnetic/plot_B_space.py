# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi


def plot_B_space(self, j_t0=0, is_deg=True, out_list=[]):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self : Output
        an Output object
    j_t0 : int
        Index of the time vector to plot
    is_deg : bool
        True to plot in degree, False in rad
    out_list : list
        List of Output object to compare
    """

    # Extract the field
    if is_deg:
        unit = "°"
    else:
        unit = "rad"
    [angle, Br] = self.mag.Br.get_along(
        "angle{" + unit + "}", "time[" + str(j_t0) + "]"
    )
    [angle, Bt] = self.mag.Bt.get_along(
        "angle{" + unit + "}", "time[" + str(j_t0) + "]"
    )

    # Plot the original graph
    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    axs[0].plot(angle, Br, self.post.line_color, label=self.post.legend_name)
    axs[0].set_title(self.mag.Br.name)
    axs[0].set_xlabel("Position [" + unit + "]")
    axs[0].set_ylabel("Flux [" + self.mag.Br.unit + "]")

    axs[1].plot(angle, Bt, self.post.line_color, label=self.post.legend_name)
    axs[1].set_title(self.mag.Bt.name)
    axs[0].set_xlabel("Position [" + unit + "]")
    axs[0].set_ylabel("Flux [" + self.mag.Bt.unit + "]")

    title = (
        "Airgap total flux density over space time["
        + str(j_t0)
        + "]="
        + str(self.mag.time[j_t0])
        + " s"
    )
    fig.canvas.set_window_title(title)
    fig.suptitle(title, fontsize=16)

    # Add all the other output to compare (if needed)
    for out in out_list:
        if out.mag.Br is not None:
            [angle_out, Br_out] = out.mag.Br.get_along(
                "angle{" + unit + "}", "time[" + str(j_t0) + "]"
            )
            axs[0].plot(
                angle_out, Br_out, out.post.line_color, label=out.post.legend_name,
            )
        if out.mag.Bt is not None:
            [angle_out, Bt_out] = out.mag.Bt.get_along(
                "angle{" + unit + "}", "time[" + str(j_t0) + "]"
            )
            axs[1].plot(
                angle_out, Bt_out, out.post.line_color, label=out.post.legend_name,
            )

    # Add the legend (if the list is not empty)
    if out_list:
        axs[0].legend()
        axs[1].legend()

    fig.show()
