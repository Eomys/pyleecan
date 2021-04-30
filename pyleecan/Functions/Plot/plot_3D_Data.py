from ...definitions import config_dict

# Import values from config dict
COLOR_LIST = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"]
COLORMAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


def plot_3D_Data(
    data,
    *arg_list,
    is_norm=False,
    unit="SI",
    save_path=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    z_min=None,
    z_max=None,
    z_range=None,
    color_list=None,
    colormap=None,
    is_auto_ticks=True,
    is_2D_view=False,
    N_stem=100,
    fig=None,
    ax=None,
    is_show_fig=None,
    is_auto_range=True,
    is_same_size=False,
    is_logscale_x=False,
    is_logscale_y=False,
    is_logscale_z=False,
    thresh=0.02,
    is_switch_axes=False,
    win_title=None,
):
    """Plots a field as a function of two axes

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
    z_min : float
        minimum value for the z-axis
    z_max : float
        maximum value for the z-axis
    z_range : float
        range to use for the z-axis
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    is_2D_view : bool
        True to plot Data in xy plane and put z as colormap
    N_stem : int
        number of harmonics to plot (only for stem plots)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    is_show_fig : bool
        True to show figure after plot
    """

    print(
        "WARNING: plot_2D_Data function is deprecated and will be removed from the next release. Please use SciDataTool plot_2D_Data method instead."
    )

    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]

    if color_list is None:
        color_list = COLOR_LIST
    if colormap is None:
        colormap = COLORMAP

    # Call SciDataTool method
    data.plot_3D_Data(
        *arg_list,
        is_norm=is_norm,
        unit=unit,
        save_path=save_path,
        x_min=x_min,
        x_max=x_max,
        y_min=y_min,
        y_max=y_max,
        z_min=z_min,
        z_max=z_max,
        z_range=z_range,
        is_auto_ticks=is_auto_ticks,
        is_auto_range=is_auto_range,
        is_2D_view=is_2D_view,
        is_same_size=is_same_size,
        N_stem=N_stem,
        fig=fig,
        ax=ax,
        is_show_fig=is_show_fig,
        is_logscale_x=is_logscale_x,
        is_logscale_y=is_logscale_y,
        is_logscale_z=is_logscale_z,
        thresh=thresh,
        is_switch_axes=is_switch_axes,
        colormap=colormap,
        win_title=win_title,
        font_name=FONT_NAME,
        font_size_title=FONT_SIZE_TITLE,
        font_size_label=FONT_SIZE_LABEL,
        font_size_legend=FONT_SIZE_LEGEND,
    )
