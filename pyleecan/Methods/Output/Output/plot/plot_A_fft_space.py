# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_fft_space import plot_A_fft_space as plot_A_fft_space_fct


def plot_A_fft_space(
    self,
    Data_str,
    t=None,
    t_index=0,
    is_spaceorder=False,
    r_max=100,
    fund_harm=None,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
    mag_max=None,
    is_auto_ticks=True,
    fig=None,
):
    """Plots a field as a function of space (angle)

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data object to plot (e.g. "mag.Br")
    t : float
        time value at which to slice
    t_index : int
        time index at which to slice
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
    fund_harm : float
        frequency of the fundamental harmonic
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
        in fft, adjust ticks to wavenumbers (deactivate if too close)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    plot_A_fft_space_fct(
        data,
        t=t,
        t_index=t_index,
        is_spaceorder=is_spaceorder,
        r_max=r_max,
        fund_harm=fund_harm,
        is_norm=is_norm,
        unit=unit,
        data_list=data_list,
        legend_list=legend_list,
        color_list=color_list,
        save_path=save_path,
        mag_max=mag_max,
        is_auto_ticks=is_auto_ticks,
        fig=fig,
    )
