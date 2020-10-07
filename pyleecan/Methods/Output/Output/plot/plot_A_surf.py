# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_A_surf import plot_A_surf as plot_A_surf_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField

from matplotlib.pyplot import subplots


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
    colormap=None,
    save_path=None,
    component_list=None,
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
    component_list : list
        list of component names to plot in separate figures
    """

    # Get Data object name
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        ncomp = len(component_list)
        fig, axs = subplots(
            1,
            ncomp,
            tight_layout=True,
            figsize=(20, 10),
            subplot_kw=dict(projection="3d"),
        )
        for i, comp in enumerate(component_list):
            plot_A_surf_fct(
                data.components[comp],
                is_deg=is_deg,
                t_max=t_max,
                a_max=a_max,
                z_min=z_min,
                z_max=z_max,
                is_norm=is_norm,
                unit=unit,
                colormap=colormap,
                save_path=save_path,
                fig=fig,
                subplot_index=i,
            )

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(
            None, shape="rectangle", is_3d=True
        )
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
            fig=fig,
        )

    fig.show()
