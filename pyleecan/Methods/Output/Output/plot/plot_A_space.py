# -*- coding: utf-8 -*-

from .....Functions.init_fig import init_fig
from .....Functions.Plot.plot_A_2D import plot_A_2D
from numpy import squeeze

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
    color_list=["tab:blue","tab:red","tab:olive","k","tab:orange","tab:pink"]
):
    """Plots a field as a function of space (angle)

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
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
    out_list : list
        list of Output objects to compare
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
    is_multiple = False
    for axis in data.axes:
        if axis.is_multiple:
            is_multiple = True
            legend_list = [axis.values.tolist()[i] for i in index_list] + legend_list
            list_str = axis.name
    if not is_multiple:
        legend_list = [self.post.legend_name] + legend_list
    if unit == "SI":
        unit = data.unit
    if is_norm:
        ylabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + data.symbol + "\, [" + unit + "]$"

    # Prepare the extractions
    if is_deg:
        a_str = "angle{°}"
        xlabel = "Angle [°]"
    else:
        a_str = "angle"
        xlabel = "Angle [rad]"
    if t != None:
        t_str = "time=" + str(t)
    else:
        t_str = "time[" + str(t_index) + "]"

    # Extract the fields
    if is_multiple:
        Ydata = []
        for i in index_list:
            (angle, Ydatas) = data.compare_along(
                a_str, t_str, list_str+"["+str(i)+"]", data_list=data_list, unit=unit, is_norm=is_norm
            )
            Ydata.append(Ydatas[0])
        Ydata.append(Ydatas[-1])
    else:
        (angle, Ydata) = data.compare_along(
            a_str, t_str, data_list=data_list, unit=unit, is_norm=is_norm
        )

    title = data.name + " over space at " + t_str

    # Plot the original graph
    plot_A_2D(
        angle,
        Ydata,
        legend_list=legend_list,
        color_list=color_list,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    if is_fft:
        title = "FFT of " + data.name
        if data.symbol == "Magnitude":
            ylabel = "Magnitude [" + unit + "]"
        else:
            ylabel = r"$|\widehat{" + data.symbol + "}|\, [" + unit + "]$"
        legend_list = [legend_list[0]] + [legend_list[-1]]

        if is_spaceorder:
            order_max = r_max / data.normalizations.get("space_order")
            xlabel = "Space order []"
            (wavenumber, Ydata) = data.compare_magnitude_along(
                "wavenumber=[0," + str(order_max) + "]{space_order}",
                t_str,
                data_list=data_list,
                unit=unit,
                is_norm=False,
            )

        else:
            xlabel = "Wavenumber []"
            (wavenumber, Ydata) = data.compare_magnitude_along(
                "wavenumber=[0," + str(r_max) + "]",
                t_str,
                data_list=data_list,
                unit=unit,
                is_norm=False,
            )

        plot_A_2D(
            wavenumber,
            Ydata,
            legend_list=legend_list,
            color_list=color_list,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type="bargraph",
            is_fund=True,
            fund_harm=fund_harm,
        )
