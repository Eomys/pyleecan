# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_space import plot_A_space as plot_A_space_fct


def plot_A_space(
    self,
    Data_str,
    index_list=[0],
    t=None,
    t_index=0,
    is_deg=True,
    is_fft=False,
    is_spaceorder=False,
    r_max=100,
    fund_harm=None,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
):
    """Plots a field as a function of space (angle)

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data object to plot (e.g. "mag.Br")
    index_list : list
        list of indices to take from a components axis
    t : float
        time value at which to slice
    t_index : int
        time index at which to slice
    is_deg : bool
        boolean indicating if the angle must be converted to degrees
    is_fft : bool
        boolean indicating if we want to plot the space-fft below the plot
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
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    plot_A_space_fct(
        data,
        index_list=index_list,
        t=t,
        t_index=t_index,
        is_deg=is_deg,
        is_fft=is_fft,
        is_spaceorder=is_spaceorder,
        r_max=r_max,
        fund_harm=fund_harm,
        is_norm=is_norm,
        unit=unit,
        data_list=data_list,
        legend_list=legend_list,
        color_list=color_list,
        save_path=save_path,
    )
