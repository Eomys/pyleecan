# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_3D import plot_A_3D
from numpy import meshgrid


def plot_A_surf(
    self,
    Data_str,
    is_deg=True,
    t_max=1.0,
    a_max=400,
    z_max=1.0,
    is_norm=False,
    unit="SI",
    colormap="RdBu_r",
):
    """Plots the isosurface of a field in 3D

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    is_deg : bool
        boolean indicating if the angle must be converted to degrees
    t_max : float
        maximum value of the time for the x axis
    a_max : float
        maximum value of the angle for the y axis
    z_max : float
        maximum value of the magnitude for the z axis
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    colormap : colormap object
        colormap prescribed by user
    """

    # Get Data object name
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Set plot
    title = data.name + " as a function of time and space"
    xlabel = "Time [s]"
    if is_deg:
        ylabel = "Angle [°]"
    else:
        ylabel = "Angle [rad]"
    if unit == "SI":
        unit = data.unit
    if is_norm:
        zlabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        zlabel = r"$" + data.symbol + "\, [" + unit + "]$"

    # Extract the field
    if is_deg:
        (time, angle, Br) = data.get_along(
            "time", "angle{°}", unit=unit, is_norm=is_norm
        )
    else:
        (time, angle, Br) = data.get_along(
            "time", "angle{°}", unit=unit, is_norm=is_norm
        )

    time_map, angle_map = meshgrid(time, angle)

    # Plot the original graph
    plot_A_3D(
        time_map,
        angle_map,
        Br,
        colormap=colormap,
        x_max=t_max,
        y_max=a_max,
        z_max=z_max,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        type="surf",
    )
