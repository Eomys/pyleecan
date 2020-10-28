# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_2D import plot_2D


def plot_A_quiver_2D(
    data,
    t=None,
    t_index=0,
    is_norm=False,
    unit="SI",
    is_show_fig=None,
    save_path=None,
    fig=None,
):
    """Plots a 2D vector field

    Parameters
    ----------
    data : Data
        a Data object
    t : float
        time value at which to slice
    t_index : int
        time index at which to slice
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    is_show_fig : bool
        True to show figure after plot
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")

    xlabel = "x [m]"
    ylabel = "y [m]"
    # Prepare the extractions
    if t != None:
        t_str = "time=" + str(t)
    else:
        t_str = "time[" + str(t_index) + "]"
    title = data.name + " over space at " + t_str

    # Extract the fields
    results = data.get_along("xy", t_str, unit=unit, is_norm=is_norm)
    xy = results["xy"]
    Ydata = results[data.symbol]

    # Plot the original graph
    plot_2D(
        xy,
        [Ydata],
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        type="quiver",
        is_show_fig=is_show_fig,
        save_path=save_path,
    )
