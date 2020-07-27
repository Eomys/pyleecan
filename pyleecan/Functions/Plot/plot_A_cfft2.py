# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_3D import plot_A_3D
from numpy import max as np_max


def plot_A_cfft2(
    data,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    mag_max=None,
    N_stem=100,
    disp_negative=False,
    is_norm=False,
    unit="SI",
    save_path=None,
    fig=None,
    subplot_index=None,
):
    """3D stem plot of the 2D Fourier Transform of a field

    Parameters
    ----------
    data : Data
        a Data object
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    freq_max : int
        maximum value of the frequency for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
    mag_max : int
        maximum value of the magnitude
    N_stem : int
        number of stems to plot
    disp_negative : bool
        plot negative frequencies
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    save_path : str
        path and name of the png file to save
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")
    title = "Complex FFT2 of " + data.name
    if is_elecorder:
        xlabel = "Electrical order []"
        freq_max = freq_max / data.normalizations.get("elec_order")
        if disp_negative:
            x_str = "freqs=[-" + str(freq_max) + "," + str(freq_max) + "]{elec_order}"
            x_min = -freq_max
        else:
            x_str = "freqs=[0," + str(freq_max) + "]{elec_order}"
            x_min = 0
    else:
        xlabel = "Frequency [Hz]"
        if disp_negative:
            x_str = "freqs=[-" + str(freq_max) + "," + str(freq_max) + "]"
            x_min = -freq_max
        else:
            x_str = "freqs=[0," + str(freq_max) + "]"
            x_min = 0
    if is_spaceorder:
        ylabel = "Spatial order []"
        r_max = r_max / data.normalizations.get("space_order")
        y_str = "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]{space_order}"
    else:
        ylabel = "Wavenumber []"
        y_str = "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]"
    if unit == "SI":
        unit = data.unit
    elif "dB" in unit:
        unit_str = "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
    else:
        unit_str = "[" + unit + "]"
        
    if data.symbol == "Magnitude":
        zlabel = "Magnitude " + unit_str
    else:
        zlabel = r"$|\widehat{" + data.symbol + "}|$ " + unit_str

    # Extract the field
    results = data.get_harmonics(
        N_stem, x_str, y_str, unit=unit, is_norm=False, is_flat=True
    )
    F_flat = results["freqs"]
    R_flat = results["wavenumber"]
    B_FT_flat = results[data.symbol]
    if mag_max is None:
        mag_max = np_max(B_FT_flat)

    # Plot the original graph
    plot_A_3D(
        F_flat,
        R_flat,
        B_FT_flat,
        fig=fig,
        x_min=x_min,
        x_max=freq_max,
        y_min=r_max,
        y_max=-r_max,
        z_min=0,
        z_max=mag_max,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        type="stem",
        save_path=save_path,
        subplot_index=subplot_index,
    )
