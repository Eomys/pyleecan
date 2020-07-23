# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_time import plot_A_time as plot_A_time_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_A_time(
    self,
    Data_str,
    index_list=[0],
    alpha=None,
    alpha_index=0,
    is_fft=False,
    is_elecorder=False,
    freq_max=20000,
    is_norm=False,
    unit="SI",
    data_list=[],
    component_list=None,
    legend_list=[],
    color_list=[],
    save_path=None,
    y_min=None,
    y_max=None,
    mag_max=None,
    is_auto_ticks=True,
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    index_list : list
        list of indices to take from a components axis
    alpha : float
        angle value at which to slice
    alpha_index : int
        angle index at which to slice
    is_fft : bool
        boolean indicating if we want to plot the time-fft below the plot
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    freq_max : int
        maximum value of the frequency for the fft axis
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    data_list : list
        list of Data objects to compare
    component_list : list
        list of component names to plot in separate figures
    legend_list : list
        list of legends to use for each Data object (including reference one) instead of data.name
    color_list : list
        list of colors to use for each Data object
    save_path : str
        path and name of the png file to save
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        for comp in component_list:
            plot_A_time_fct(
                data.components[comp],
                index_list=index_list,
                alpha=alpha,
                alpha_index=alpha_index,
                is_fft=is_fft,
                is_elecorder=is_elecorder,
                freq_max=freq_max,
                is_norm=is_norm,
                unit=unit,
                data_list=[dat.components[comp] for dat in data_list],
                legend_list=legend_list,
                color_list=color_list,
                save_path=save_path,
                y_min=y_min,
                y_max=y_max,
                mag_max=mag_max,
                is_auto_ticks=is_auto_ticks,
                fig=fig,
            )

    else:
        plot_A_time_fct(
            data,
            index_list=index_list,
            alpha=alpha,
            alpha_index=alpha_index,
            is_fft=is_fft,
            is_elecorder=is_elecorder,
            freq_max=freq_max,
            is_norm=is_norm,
            unit=unit,
            data_list=data_list,
            legend_list=legend_list,
            color_list=color_list,
            save_path=save_path,
            y_min=y_min,
            y_max=y_max,
            mag_max=mag_max,
            is_auto_ticks=is_auto_ticks,
            fig=fig,
        )
