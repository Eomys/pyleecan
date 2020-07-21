# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_fft_time import plot_A_fft_time as plot_A_fft_time_fct


def plot_A_fft_time(
    self,
    Data_str,
    alpha=None,
    alpha_index=0,
    is_elecorder=False,
    freq_max=20000,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
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
    alpha : float
        angle value at which to slice
    alpha_index : int
        angle index at which to slice
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
    legend_list : list
        list of legends to use for each Data object (including reference one) instead of data.name
    color_list : list
        list of colors to use for each Data object
    save_path : str
        path and name of the png file to save
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    plot_A_fft_time_fct(
        data,
        alpha=alpha,
        alpha_index=alpha_index,
        is_elecorder=is_elecorder,
        freq_max=freq_max,
        is_norm=is_norm,
        unit=unit,
        data_list=data_list,
        legend_list=legend_list,
        color_list=color_list,
        save_path=save_path,
        mag_max=mag_max,
        is_auto_ticks=is_auto_ticks,
    )
