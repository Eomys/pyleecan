# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_time_space import (
    plot_A_time_space as plot_A_time_space_fct,
)
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_A_time_space(
    self,
    Data_str,
    is_deg=True,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    z_max=None,
    is_norm=False,
    unit="SI",
    colormap="RdBu_r",
    save_path=None,
    is_auto_ticks=True,
    component_list=None,
):
    """Plots a field as a function of time and space (angle)

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
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
    colormap : colormap object
        colormap prescribed by user
    save_path : str
        path and name of the png file to save
    is_auto_ticks : bool
        in fft, adjust ticks to freqs and wavenumbers (deactivate if too close)
    component_list : list
        list of component names to plot in separate figures
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        for comp in component_list:
            plot_A_time_space_fct(
                data.components[comp],
                is_deg=is_deg,
                is_elecorder=is_elecorder,
                is_spaceorder=is_spaceorder,
                freq_max=freq_max,
                r_max=r_max,
                z_max=z_max,
                is_norm=is_norm,
                unit=unit,
                colormap=colormap,
                save_path=save_path,
                is_auto_ticks=is_auto_ticks,
            )

    else:
        plot_A_time_space_fct(
            data,
            is_deg=is_deg,
            is_elecorder=is_elecorder,
            is_spaceorder=is_spaceorder,
            freq_max=freq_max,
            r_max=r_max,
            z_max=z_max,
            is_norm=is_norm,
            unit=unit,
            colormap=colormap,
            save_path=save_path,
            is_auto_ticks=is_auto_ticks,
        )
