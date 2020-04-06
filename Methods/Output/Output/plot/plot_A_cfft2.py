# -*- coding: utf-8 -*-

from pyleecan.Functions.Plot.plot_A_3D import plot_A_3D


def plot_A_cfft2(
    self,
    Data_str,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    mag_max=1.0,
    N_stem=100,
    is_norm=False,
    unit="SI",
    out_list=[],
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
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    out_list : list
        list of Output objects to compare
    """

    # Get Data object names
    Phys = getattr(self, Data_str.split(".")[0])
    A = getattr(Phys, Data_str.split(".")[1])
    B_list = []
    for out in out_list:
        Phys = getattr(out, Data_str.split(".")[0])
        B_list.append(getattr(Phys, Data_str.split(".")[1]))

    # Set plot
    title = "Complex FFT2 of " + A.name
    if is_elecorder:
        xlabel = "Electrical order []"
        elec_max = freq_max / A.normalizations.get("elec_order")
        x_str = "freqs=[-" + str(elec_max) + "," + str(elec_max) + "]{elec_order}"
    else:
        xlabel = "Frequency [Hz]"
        x_str = "freqs=[-" + str(freq_max) + "," + str(freq_max) + "]"
    if is_spaceorder:
        ylabel = "Spatial order []"
        order_max = r_max / A.normalizations.get("space_order")
        y_str = (
            "wavenumber=[-" + str(order_max) + "," + str(order_max) + "]{space_order}"
        )
    else:
        ylabel = "Wavenumber []"
        y_str = "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]"
    if unit == "SI":
        unit = A.unit
    zlabel = r"$\widehat{" + A.symbol + "}\, [" + unit + "]$"

    # Extract the field
    (F_flat, R_flat, B_FT_flat) = A.get_harmonics(
        N_stem, x_str, y_str, unit=unit, is_norm=False, is_flat=True,
    )

    # Plot the original graph
    plot_A_3D(
        F_flat,
        R_flat,
        B_FT_flat,
        x_max=freq_max,
        y_max=r_max,
        z_max=mag_max,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        type="stem",
    )
