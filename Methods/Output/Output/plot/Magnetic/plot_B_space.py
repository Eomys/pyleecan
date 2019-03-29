# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi


def plot_B_space(self, j_t0=0, is_deg=True):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self : Output
        an Output object
    j_t0 : int
        Index of the time vector to plot
    is_deg : bool
        True to plot in degree, False in rad
    """

    if is_deg:
        unit = "[°]"
        angle = self.mag.angle * 180 / pi
    else:
        unit = "[rad]"
        angle = self.mag.angle

    fig, axs = plt.subplots(1, 2, constrained_layout=True)

    title = (
        "Airgap total flux density over space time["
        + str(j_t0)
        + "]="
        + str(self.mag.time[j_t0])
        + " s"
    )
    fig.canvas.set_window_title(title)
    fig.suptitle(title, fontsize=16)

    axs[0].plot(angle, self.mag.Br[j_t0, :])
    axs[0].set_title("Radial Flux")
    axs[0].set_xlabel("Position " + unit)
    axs[0].set_ylabel("Flux [T]")

    axs[1].plot(angle, self.mag.Bt[j_t0, :])
    axs[1].set_title("Tangential Flux")
    axs[1].set_xlabel("Position " + unit)
    axs[1].set_ylabel("Flux [T]")

    plt.show()
