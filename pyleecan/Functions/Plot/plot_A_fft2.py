# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_4D import plot_A_4D
from numpy import meshgrid, pi, max as np_max
from ...definitions import config_dict


def plot_A_fft2(
    data,
    is_phase=False,
    is_deg=True,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    mag_max=None,
    is_norm=False,
    unit="SI",
    colormap=None,
    save_path=None,
    fig=None,
):
    """2D color plot of the 2D Fourier Transform of a field

    Parameters
    ----------
    data : Data
        a Data object
    is_phase : bool
        boolean indicating if the phase must be plot (subplot)
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
    colormap : colormap object
        colormap prescribed by user
    save_path : str
        path and name of the png file to save
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")
    title = "FFT2 of " + data.name
    if colormap is None:
        colormap = config_dict["color_dict"]["COLOR_MAP"]
    if is_elecorder:
        xlabel = "Electrical order []"
        elec_max = freq_max / data.normalizations.get("elec_order")
        x_str = "freqs=[0," + str(elec_max) + "]{elec_order}"
    else:
        xlabel = "Frequency [Hz]"
        x_str = "freqs=[0," + str(freq_max) + "]"
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

    # Extract the field
    results = data.get_magnitude_along(x_str, y_str, unit=unit)

    wavenumber = results["wavenumber"]
    freqs = results["freqs"]
    A_mag = results[data.symbol]

    wavenumber_map, freqs_map = meshgrid(wavenumber, freqs)
    freqs_flat = freqs_map.flatten()
    wavenumber_flat = wavenumber_map.flatten()
    A_mag_flat = A_mag.flatten()
    size_flat = 1000 * A_mag_flat / np_max(A_mag_flat)

    zlabel = r"$|\widehat{" + data.symbol + "}|\, [" + unit + "]$"

    if mag_max is None:
        mag_max = np_max(A_mag)

    # Plot the original graph
    plot_A_4D(
        freqs_flat,
        wavenumber_flat,
        A_mag_flat,
        size_flat,
        colormap=colormap,
        z_max=mag_max,
        z_min=0,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        fig=fig,
        type="scatter",
        save_path=save_path,
    )

    if is_phase:
        if is_deg:
            (freqs, wavenumber, A_phase) = data.get_phase_along(x_str, y_str, unit="°")
            zlabel = r"$Angle(" + data.symbol + ")\, [°]$"
            mag_max = 180
        else:
            (freqs, wavenumber, A_phase) = data.get_phase_along(
                x_str, y_str, unit="rad"
            )
            zlabel = r"$Angle(" + data.symbol + ")\, [rad]$"
            mag_max = pi

        freqs_map, wavenumber_map = meshgrid(freqs, wavenumber)
        freqs_flat = freqs_map.flatten()
        wavenumber_flat = wavenumber_map.flatten()
        A_phase_flat = A_phase.flatten()
        size_flat = 1000 * A_mag_flat / np_max(A_mag_flat)

        # Plot the original graph
        plot_A_4D(
            freqs_flat,
            wavenumber_flat,
            A_phase_flat,
            size_flat,
            z_max=mag_max,
            z_min=-mag_max,
            colormap=colormap,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            zlabel=zlabel,
            fig=fig,
            type="scatter",
            save_path=save_path,
        )
