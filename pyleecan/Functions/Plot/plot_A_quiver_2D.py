# -*- coding: utf-8 -*-

from .....Functions.init_fig import init_fig
from .....Functions.Plot.plot_A_2D import plot_A_2D
from numpy import squeeze, split


def plot_A_quiver_2D(
    self, Data_str, t=None, t_index=0, is_norm=False, unit="SI",
):
    """Plots a 2D vector field

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data object to plot (e.g. "mag.Br")
    t : float
        time value at which to slice
    t_index : int
        time index at which to slice
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

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
    (xy, Ydata) = data.get_along("xy", t_str, unit=unit, is_norm=is_norm)

    # Plot the original graph
    plot_A_2D(
        xy, [Ydata], fig=fig, title=title, xlabel=xlabel, ylabel=ylabel, type="quiver",
    )
