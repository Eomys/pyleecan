from ...definitions import config_dict

# Import values from config dict
COLOR_LIST = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


def plot_2D_Data(
    data,
    *arg_list,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=None,
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
    fig=None,
    ax=None,
    barwidth=100,
    type_plot=None,
    fund_harm_dict=None,
    is_show_fig=None,
    win_title=None,
    is_auto_range=True,
    thresh=0.02,
    linestyles=None,
    linewidth_list=[2],
):
    """Plots a field as a function of an axis

    Parameters
    ----------
    data : Data
        a Data object
    *arg_list : list of str
        arguments to specify which axes to plot
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
        full path including folder, name and extension of the file to save if save_path is not None
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
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm_dict : dict
        Dict containing axis name as key and frequency/order/wavenumber of fundamental harmonic as value to display fundamental harmonic in red in the fft
    is_show_fig : bool
        True to show figure after plot
    win_title : str
        Title of the plot window
    """

    print(
        "WARNING: plot_2D_Data function is deprecated and will be removed from the next release. Please use SciDataTool plot_2D_Data method instead."
    )

    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]

    if color_list is None:
        color_list = COLOR_LIST

    # Call SciDataTool method
    data.plot_2D_Data(
        *arg_list,
        is_norm=is_norm,
        unit=unit,
        data_list=data_list,
        legend_list=legend_list,
        color_list=color_list,
        linestyles=linestyles,
        linewidth_list=linewidth_list,
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
        is_auto_range=is_auto_range,
        fig=fig,
        ax=ax,
        barwidth=barwidth,
        type_plot=type_plot,
        fund_harm_dict=fund_harm_dict,
        is_show_fig=is_show_fig,
        win_title=win_title,
        thresh=thresh,
        font_name=FONT_NAME,
        font_size_title=FONT_SIZE_TITLE,
        font_size_label=FONT_SIZE_LABEL,
        font_size_legend=FONT_SIZE_LEGEND,
    )
