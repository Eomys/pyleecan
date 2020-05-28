# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_surf import plot_A_surf as plot_A_surf_fct


def plot_A_surf(
    self,
    Data_str,
    is_deg=True,
    t_max=None,
    a_max=400,
    z_min=None,
    z_max=None,
    is_norm=False,
    unit="SI",
    colormap="RdBu_r",
    save_path=None,
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
    z_min : float
        minimum value of the amplitude for the z axis
    z_max : float
        maximum value of the amplitude for the z axis
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    colormap : colormap object
        colormap prescribed by user
    save_path : str
        path and name of the png file to save
    """

    # Get Data object name
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    plot_A_surf_fct(
        data,
        is_deg=is_deg,
        t_max=t_max,
        a_max=a_max,
        z_min=z_min,
        z_max=z_max,
        is_norm=is_norm,
        unit=unit,
        colormap=colormap,
        save_path=save_path,
    )
