# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_quiver_2D import (
    plot_A_quiver_2D as plot_A_quiver_2D_fct,
)


def plot_A_quiver_2D(self, Data_str, t=None, t_index=0, is_norm=False, unit="SI"):
    """Plots a field as a function of space (angle)

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
    if "get_" in Data_str.split(".")[1]:  # get method
        data = getattr(phys, Data_str.split(".")[1])()
    else:
        data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    plot_A_quiver_2D_fct(data, t=t, t_index=t_index, is_norm=is_norm, unit=unit)
