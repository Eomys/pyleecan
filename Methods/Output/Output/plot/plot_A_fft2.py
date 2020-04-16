# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from .....Functions.Plot.plot_A_3D import plot_A_3D
from numpy import meshgrid, append, pi


def plot_A_fft2(
    self,
    Data_str,
    is_phase=False,
    is_deg=True,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    mag_max=100,
    is_norm=False,
    unit="SI",
    colormap="RdBu",
    out_list=[],
):
    """2D color plot of the 2D Fourier Transform of a field

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    is_deg : bool
        boolean indicating if the phase must be converted to degrees
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    freq_max : int
        maximum value of the frequency for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
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
    fig = plt.figure(tight_layout=True, figsize=(20, 10))
    title = "FFT2 of " + A.name
    if is_elecorder:
        xlabel = "Electrical order []"
        elec_max = freq_max / A.normalizations.get("elec_order")
        x_str = "freqs=[0," + str(elec_max) + "]{elec_order}"
    else:
        xlabel = "Frequency [Hz]"
        x_str = "freqs=[0," + str(freq_max) + "]"
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

    # Extract the field
    (freqs, wavenumber, A_mag) = A.get_magnitude_along(x_str, y_str, unit=unit)

    wavenumber = append(wavenumber, wavenumber[-1] + 1) - 0.5
    freqs = append(freqs, freqs[-1] + 1)
    wavenumber_map, freqs_map = meshgrid(wavenumber, freqs)

    zlabel = r"$|\widehat{" + A.symbol + "}|\, [" + unit + "]$"

    # Plot the original graph
    plot_A_3D(
        freqs_map,
        wavenumber_map,
        A_mag,
        colormap=colormap,
        z_max=mag_max,
        z_min=0,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        is_newfig=False,
        fig=fig,
        type="pcolor",
    )

    if is_phase:
        if is_deg:
            (freqs, wavenumber, A_phase) = A.get_phase_along(x_str, y_str, unit="°")
            zlabel = r"$Angle(" + A.symbol + ")\, [°]$"
            mag_max = 180
        else:
            (freqs, wavenumber, A_phase) = A.get_phase_along(x_str, y_str, unit="rad")
            zlabel = r"$Angle(" + A.symbol + ")\, [rad]$"
            mag_max = pi

        # Plot the original graph
        plot_A_3D(
            freqs_map,
            wavenumber_map,
            A_phase,
            z_max=mag_max,
            z_min=-mag_max,
            colormap=colormap,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            zlabel=zlabel,
            is_newfig=False,
            fig=fig,
            type="pcolor",
        )
