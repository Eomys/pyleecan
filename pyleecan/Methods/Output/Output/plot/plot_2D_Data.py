# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_2D_Data import plot_2D_Data as plot_2D_Data_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_2D_Data(
    self,
    Data_str,
    *args,
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
    barwidth=100,
    type_plot=None,
    fund_harm=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    *args : list of str
        arguments to specify which axes to plot
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
        full path of the png file where the figure is saved if save_path is not None
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm : float
        frequency/order/wavenumber of the fundamental harmonic that must be displayed in red in the fft
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        for i, comp in enumerate(component_list):
            (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

            if save_path is not None:
                save_path_comp = (
                    save_path.split(".")[0] + "_" + comp + "." + save_path.split(".")[1]
                )
            else:
                save_path_comp = None

            if fund_harm is None:
                # if fund_harm is None:
                #     mag_max = max(Ydatas[i])
                #     imax = int(where(Ydatas[i] == mag_max)[0])
                # else:
                #     imax = argmin(abs(Xdatas[i] - fund_harm))
                pass  # Call method to calculate fundharm function of simu and machine

            plot_2D_Data_fct(
                data.components[comp],
                args,
                is_norm=is_norm,
                unit=unit,
                data_list=[dat.components[comp] for dat in data_list],
                legend_list=legend_list,
                color_list=color_list,
                save_path=save_path_comp,
                y_min=y_min,
                y_max=y_max,
                is_auto_ticks=is_auto_ticks,
                fig=fig,
                barwidth=barwidth,
                type_plot=type_plot,
                fund_harm=fund_harm,
            )
            fig.show()

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
        plot_2D_Data_fct(
            data,
            args,
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
            barwidth=barwidth,
            type_plot=type_plot,
            fund_harm=fund_harm,
        )
        fig.show()
