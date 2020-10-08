# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_2D import plot_A_2D


def plot_A_quiver_2D(data, t=None, t_index=0, is_norm=False, unit="SI"):
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
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
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
    plot_A_2D(
        xy, [Ydata], fig=fig, title=title, xlabel=xlabel, ylabel=ylabel, type="quiver"
    )

    fig.show()
