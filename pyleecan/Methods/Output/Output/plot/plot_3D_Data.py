# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_3D_Data import plot_3D_Data as plot_3D_Data_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_3D_Data(
    self,
    Data_str,
    *args,
    component_list=None,
    is_norm=False,
    unit="SI",
    save_path=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    z_min=None,
    z_max=None,
    is_auto_ticks=True,
    is_2D_view=False,
    N_stem=100,
    fig=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    *args : list of str
        arguments to specify which axes to plot
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    data_list : list
        list of Data objects to compare
    component_list : list
        list of component names to plot in separate figures
    legend_list : list
        list of legends to use for each Data object (including reference one) instead of data.name
    color_list : list
        list of colors to use for each Data object
    save_path : str
        path and name of the png file to save
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        for i, comp in enumerate(component_list):
            (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

            if save_path is not None:
                save_path_comp = (
                    save_path.split(".")[0] + "_" + comp + "." + save_path.split(".")[1]
                )
            else:
                save_path_comp = None

            plot_3D_Data_fct(
                data.components[comp],
                args,
                is_norm=is_norm,
                unit=unit,
                save_path=save_path_comp,
                x_min=x_min,
                x_max=x_max,
                y_min=y_min,
                y_max=y_max,
                z_min=z_min,
                z_max=z_max,
                is_auto_ticks=is_auto_ticks,
                is_2D_view=is_2D_view,
                N_stem=N_stem,
                fig=fig,
            )

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
        plot_3D_Data_fct(
            data,
            args,
            is_norm=is_norm,
            unit=unit,
            save_path=save_path,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            z_min=z_min,
            z_max=z_max,
            is_auto_ticks=is_auto_ticks,
            is_2D_view=is_2D_view,
            N_stem=N_stem,
            fig=fig,
        )

    fig.show()
