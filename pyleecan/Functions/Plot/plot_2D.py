from SciDataTool.Functions.Plot.plot_2D import plot_2D as plot_2D_fct
from ...definitions import config_dict

# Import values from config dict
COLOR_LIST = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


def plot_2D(
    Xdatas,
    Ydatas,
    legend_list=[""],
    color_list=None,
    linestyle_list=["-"],
    linewidth_list=[2],
    title="",
    xlabel="",
    ylabel="",
    fig=None,
    ax=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    type_plot="curve",
    fund_harm=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    xticks=None,
    save_path=None,
    barwidth=100,
    is_show_fig=None,
    win_title=None,
):
    """Plots a 2D graph (curve, bargraph or barchart) comparing fields in Ydatas

    Parameters
    ----------
    Xdatas : ndarray
        array of x-axis values
    Ydatas : list
        list of y-axes values
    legend_list : list
        list of legends
    color_list : list
        list of colors to use for each curve
    linewidth_list : list
        list of line width to use for each curve
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    is_grid : bool
        boolean indicating if the grid must be displayed
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm : float
        frequency/order/wavenumber of the fundamental harmonic that must be displayed in red in the fft
    x_min : float
        minimum value for the x-axis
    x_max : float
        maximum value for the x-axis
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    xticks : list
        list of ticks to use for the x-axis
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    is_show_fig : bool
        True to show figure after plot
    win_title : str
        Title of the plot window
    """

    print(
        "WARNING: plot_2D function is deprecated and will be removed from the next release. Please use SciDataTool.Functions.Plot.plot_2D instead."
    )

    if color_list is None:
        color_list = COLOR_LIST

    # Call SciDataTool plot function
    plot_2D_fct(
        Xdatas,
        Ydatas,
        legend_list=legend_list,
        color_list=color_list,
        linestyle_list=linestyle_list,
        linewidth_list=linewidth_list,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        fig=fig,
        ax=ax,
        is_logscale_x=is_logscale_x,
        is_logscale_y=is_logscale_y,
        is_disp_title=is_disp_title,
        is_grid=is_grid,
        type_plot=type_plot,
        fund_harm=fund_harm,
        x_min=x_min,
        x_max=x_max,
        y_min=y_min,
        y_max=y_max,
        xticks=xticks,
        save_path=save_path,
        barwidth=barwidth,
        is_show_fig=is_show_fig,
        win_title=win_title,
        font_name=FONT_NAME,
        font_size_title=FONT_SIZE_TITLE,
        font_size_label=FONT_SIZE_LABEL,
        font_size_legend=FONT_SIZE_LEGEND,
    )
