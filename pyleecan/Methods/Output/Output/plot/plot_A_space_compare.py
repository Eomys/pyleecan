# -*- coding: utf-8 -*-

from .....Functions.init_fig import init_fig
from .....Functions.Plot.plot_A_2D import plot_A_2D
from numpy import array, squeeze


def plot_A_space_compare(
    self,
    Data_str,
    t=None,
    t_index=0,
    is_deg=True,
    is_fft=False,
    is_spaceorder=False,
    r_max=100,
    fund_harm=None,
    is_norm=False,
    unit="SI",
    index_list=[],
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
    index_list : list
        list of indices to compare
    """

    # Get Data object names
    Phys = getattr(self, Data_str.split(".")[0])
    A = getattr(Phys, Data_str.split(".")[1])

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
    list_str = A.axes[0].name
    legend_list = ["Overall"]
    color_list = ["k-", "b--", "r--", "g--", "o--", "p--"]
    if is_deg:
        xlabel = "Angle [°]"
    else:
        xlabel = "Angle [rad]"
    if unit == "SI":
        unit = A.unit
    if is_norm:
        ylabel = r"$\frac{" + A.symbol + "}{" + A.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + A.symbol + "\, [" + unit + "]$"

    # Extract the fields
    if t != None:
        t_str = "time=" + str(t)
    else:
        t_str = "time[" + str(t_index) + "]"

    Ydatas = []
    if is_deg:
        for i in index_list:
            (angle, Ydata) = A.compare_along(
                "angle{°}",
                t_str,
                list_str + "[" + str(i) + "]",
                unit=unit,
                is_norm=is_norm,
            )
            Ydatas.append(array(Ydata))
            legend_list.append(A.axes[0].values[i])
    else:
        for i in index_list:
            (angle, axis_i, Ydata) = A.compare_along(
                "angle",
                t_str,
                list_str + "[" + str(i) + "]",
                unit=unit,
                is_norm=is_norm,
            )
            Ydatas.append(array(Ydata))
            legend_list.append(A.axes[0].values[i])

    Ydata = squeeze(Ydatas)

    title = A.name + " over space at " + t_str

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

    if is_fft:  # FFT of first axis only
        title = "FFT of " + A.name
        ylabel = r"$|\widehat{" + A.symbol + "}|\, [" + unit + "]$"

        if is_spaceorder:
            order_max = r_max / A.normalizations.get("space_order")
            xlabel = "Space order []"
            (wavenumber, Ydata) = A.compare_magnitude_along(
                "wavenumber=[0," + str(order_max) + "]{space_order}",
                t_str,
                unit=unit,
                is_norm=False,
            )

        else:
            xlabel = "Wavenumber []"
            (wavenumber, Ydata) = A.compare_magnitude_along(
                "wavenumber=[0," + str(r_max) + "]", t_str, unit=unit, is_norm=False
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
