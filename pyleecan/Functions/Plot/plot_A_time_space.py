# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from ...definitions import config_dict
from ...Functions.Plot.plot_3D_Data import plot_3D_Data
from ...Functions.Plot.plot_2D_Data import plot_2D_Data

FONT_NAME = config_dict["PLOT"]["FONT_NAME"]


def plot_A_time_space(
    data,
    is_deg=True,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    z_max=None,
    is_norm=False,
    unit="SI",
    save_path=None,
    is_auto_ticks=True,
    is_show_fig=None,
    fig=None,
    color_list=[],
):
    """Plots a field as a function of time and space (angle)

    Parameters
    ----------
    data : Data
        a Data object
    is_deg : bool
        boolean indicating if the angle must be converted to degrees
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    freq_max : float
        maximum value of the frequency for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
    z_max : float
        maximum value for the field
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_auto_ticks : bool
        in fft, adjust ticks to freqs and wavenumbers (deactivate if too close)
    is_show_fig : bool
        True to show figure after plot
    color_list : list
        list of colors to use for each curve
    """

    if is_show_fig is None:
        is_show_fig = True if fig is None else False

    # Set plot
    fig, axs = plt.subplots(3, 2, tight_layout=True, figsize=(20, 10))
    title = data.name + " over time and space"

    # pcolorplot
    if is_deg:
        angle_str = "angle{°}"
    else:
        angle_str = "angle{rad}"

    plot_3D_Data(
        data,
        "time",
        angle_str,
        is_norm=is_norm,
        unit=unit,
        z_max=z_max,
        fig=fig,
        ax=axs[0, 0],
        is_auto_ticks=is_auto_ticks,
        is_show_fig=False,
        is_2D_view=True,
    )

    # 2D plots
    # time
    plot_2D_Data(
        data,
        "time",
        fig=fig,
        ax=axs[1, 0],
        color_list=color_list,
        is_auto_ticks=is_auto_ticks,
        is_show_fig=False,
    )

    # angle
    plot_2D_Data(
        data,
        angle_str,
        fig=fig,
        ax=axs[2, 0],
        color_list=color_list,
        is_auto_ticks=is_auto_ticks,
        is_show_fig=False,
    )

    # fft time
    if is_elecorder:
        elec_max = None
        for ax in data.axes:
            if ax.name == "time":
                try:
                    elec_max = freq_max / ax.normalizations["elec_order"]
                except:
                    pass

        if elec_max is None:
            freq_str = "freqs=[0," + str(freq_max) + "]"
        else:
            freq_str = "freqs->elec_order[0," + str(elec_max) + "]"
    else:
        freq_str = "freqs=[0," + str(freq_max) + "]"

    plot_2D_Data(
        data,
        freq_str,
        fig=fig,
        ax=axs[1, 1],
        unit=unit,
        color_list=color_list,
        is_auto_ticks=is_auto_ticks,
        is_show_fig=False,
    )

    # fft space
    if is_spaceorder:
        order_max = None
        for ax in data.axes:
            if ax.name == "angle":
                try:
                    order_max = r_max / ax.normalizations["space_order"]
                except:
                    pass

        if order_max is None:
            wavenb_str = "wavenumber=[0," + str(r_max) + "]"
        else:
            wavenb_str = "wavenumber->space_order[0," + str(order_max) + "]"
    else:
        wavenb_str = "wavenumber=[0," + str(r_max) + "]"

    plot_2D_Data(
        data,
        wavenb_str,
        fig=fig,
        ax=axs[2, 1],
        unit=unit,
        color_list=color_list,
        is_auto_ticks=is_auto_ticks,
        is_show_fig=False,
    )

    axs[0, 1].axis("off")
    axs[0, 1].title("off")

    fig.canvas.set_window_title(title)
    fig.suptitle(title, x=0.65, fontsize=24, fontname=FONT_NAME)
    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()
