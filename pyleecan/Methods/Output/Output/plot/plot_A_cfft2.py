# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_3D import plot_A_3D


def plot_A_cfft2(
    self,
    Data_str,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    mag_max=1.0,
    N_stem=100,
    disp_negative=False,
    is_norm=False,
    unit="SI",
):
    """3D stem plot of the 2D Fourier Transform of a field

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
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
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Set plot
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
        order_max = r_max / data.normalizations.get("space_order")
        y_str = (
            "wavenumber=[-" + str(order_max) + "," + str(order_max) + "]{space_order}"
        )
    else:
        ylabel = "Wavenumber []"
        y_str = "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]"
    if unit == "SI":
        unit = data.unit
    zlabel = r"$|\widehat{" + data.symbol + "}|\, [" + unit + "]$"

    # Extract the field
    (F_flat, R_flat, B_FT_flat) = data.get_harmonics(
        N_stem, x_str, y_str, unit=unit, is_norm=False, is_flat=True
    )

    # Plot the original graph
    plot_A_3D(
        F_flat,
        R_flat,
        B_FT_flat,
        x_min=x_min,
        x_max=freq_max,
        y_max=r_max,
        z_max=mag_max,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        type="stem",
    )
