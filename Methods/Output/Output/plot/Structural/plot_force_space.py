# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi


def plot_force_space(self, j_t0=0, is_deg=True, out_list=[]):
    """Plot the airgap surface forces as a function of space

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

    # Adapt the unit
    if is_deg:
        unit = "[°]"
        angle = self.struct.angle * 180 / pi
    else:
        unit = "[rad]"
        angle = self.struct.angle

    # Plot the original graph
    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    axs[0].plot(
        angle,
        self.struct.Prad[j_t0, :],
        self.post.line_color,
        label=self.post.legend_name,
    )
    axs[0].set_title("Radial Air-gap Surface Force")
    axs[0].set_xlabel("Position " + unit)
    axs[0].set_ylabel("Surface force [N/m²]")

    axs[1].plot(
        angle,
        self.struct.Ptan[j_t0, :],
        self.post.line_color,
        label=self.post.legend_name,
    )
    axs[1].set_title("Tangential Air-gap Surface Force")
    axs[1].set_xlabel("Position " + unit)
    axs[1].set_ylabel("Surface force [N/m²]")

    title = (
        "Air-gap magnetic forces over space, time["
        + str(j_t0)
        + "]="
        + str(self.struct.time[j_t0])
        + " s"
    )
    fig.canvas.set_window_title(title)
    fig.suptitle(title, fontsize=16)

    # Add all the other output to compare (if needed)
    for out in out_list:
        if is_deg:
            angle_out = out.struct.angle * 180 / pi
        else:
            angle_out = out.struct.angle
        if out.struct.Prad is not None:
            axs[0].plot(
                angle_out,
                out.struct.Prad[j_t0, :],
                out.post.line_color,
                label=out.post.legend_name,
            )
        if out.struct.Ptan is not None:
            axs[1].plot(
                angle_out,
                out.struct.Ptan[j_t0, :],
                out.post.line_color,
                label=out.post.legend_name,
            )

    # Add the legend (if the list is not empty)
    if out_list:
        axs[0].legend()
        axs[1].legend()

    fig.show()
