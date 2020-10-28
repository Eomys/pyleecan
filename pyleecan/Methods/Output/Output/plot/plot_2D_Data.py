# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_2D_Data import plot_2D_Data as plot_2D_Data_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_2D_Data(
    self,
    Data_str,
    *arg_list,
    is_norm=False,
    unit="SI",
    data_list=[],
    component_list=None,
    legend_list=[],
    color_list=[],
    save_path=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    is_auto_ticks=True,
    barwidth=100,
    type_plot=None,
    fund_harm_dict=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    *arg_list : list of str
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
    x_min : float
        minimum value for the x-axis
    x_max : float
        maximum value for the x-axis
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    is_grid : bool
        boolean indicating if the grid must be displayed
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm_dict : dict
        Dict containing axis name as key and frequency/order/wavenumber of fundamental harmonic as value to display fundamental harmonic in red in the fft

    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Get fundamental harmonic properties from Output
    if fund_harm_dict is None:
        fund_harm_dict = self.get_fund_harm(data)

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

            plot_2D_Data_fct(
                data.components[comp],
                arg_list,
                is_norm=is_norm,
                unit=unit,
                data_list=[dat.components[comp] for dat in data_list],
                legend_list=legend_list,
                color_list=color_list,
                save_path=save_path_comp,
                x_min=x_min,
                x_max=x_max,
                y_min=y_min,
                y_max=y_max,
                is_logscale_x=is_logscale_x,
                is_logscale_y=is_logscale_y,
                is_disp_title=is_disp_title,
                is_grid=is_grid,
                is_auto_ticks=is_auto_ticks,
                fig=fig,
                barwidth=barwidth,
                type_plot=type_plot,
                fund_harm_dict=fund_harm_dict,
            )
            fig.show()

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
        plot_2D_Data_fct(
            data,
            arg_list,
            is_norm=is_norm,
            unit=unit,
            data_list=data_list,
            legend_list=legend_list,
            color_list=color_list,
            save_path=save_path,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            is_logscale_x=is_logscale_x,
            is_logscale_y=is_logscale_y,
            is_disp_title=is_disp_title,
            is_grid=is_grid,
            is_auto_ticks=is_auto_ticks,
            fig=fig,
            barwidth=barwidth,
            type_plot=type_plot,
            fund_harm_dict=fund_harm_dict,
        )
        fig.show()
