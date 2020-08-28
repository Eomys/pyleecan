# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_fft2 import plot_A_fft2 as plot_A_fft2_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField

from matplotlib.pyplot import subplots


def plot_A_fft2(
    self,
    Data_str,
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
    component_list=None,
):
    """2D color plot of the 2D Fourier Transform of a field

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
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
    component_list : list
        list of component names to plot in separate figures
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    if "get_" in Data_str.split(".")[1]: # get method
        data = getattr(phys, Data_str.split(".")[1])()
    else:
        data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        ncomp = len(component_list)
        fig, axs = subplots(1, ncomp, tight_layout=True, figsize=(20, 10))
        for i, comp in enumerate(component_list):
            plot_A_fft2_fct(
                data.components[comp],
                is_phase=is_phase,
                is_deg=is_deg,
                is_elecorder=is_elecorder,
                is_spaceorder=is_spaceorder,
                freq_max=freq_max,
                r_max=r_max,
                mag_max=mag_max,
                is_norm=is_norm,
                unit=unit,
                colormap=colormap,
                save_path=save_path,
                fig=fig,
                subplot_index=i,
            )

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
        plot_A_fft2_fct(
            data,
            is_phase=is_phase,
            is_deg=is_deg,
            is_elecorder=is_elecorder,
            is_spaceorder=is_spaceorder,
            freq_max=freq_max,
            r_max=r_max,
            mag_max=mag_max,
            is_norm=is_norm,
            unit=unit,
            colormap=colormap,
            save_path=save_path,
            fig=fig,
        )
