# -*- coding: utf-8 -*-

import imageio
from os.path import join
from os import remove
from glob import glob
from SciDataTool import VectorField
from matplotlib.pyplot import subplots


def animate_as_gif(
    func,
    data_list,
    save_path="./",
    file_name="animated_plot.gif",
    index_var="t_index",
    index_max=50,
    index_step=1,
    component_list=None,
    **kwargs
):
    """Animate an existing plot command as a gif: animate

    Parameters
    ----------
    func : function
        plot command
    data_list : Data or [Data]
        Data object or list to plot
    save_path : str
        path where to save the gif
    file_name : str
        name of the gif file
    index_var : str
        name of the plot parameter along which to animate
    index_max : int
        maximum value of the index
    index_step : int
        step for the index (number of frames = index_max / index_step)
    component_list : list
        list of component names to plot in separate figures
    kwargs : dict
        parameters of func
    """

    with imageio.get_writer(join(save_path, file_name), mode="I") as writer:
        if isinstance(data_list, list):
            for i, data in enumerate(data_list):
                if isinstance(data, VectorField):
                    if component_list is None:  # default: extract all components
                        component_list = data.components.keys()
                    ncomp = len(component_list)
                    fig, axs = subplots(2, ncomp, tight_layout=True, figsize=(20, 10))
                    for j in range(0, index_max, index_step):
                        save_path_temp = save_path + "\\temp_" + str(j) + ".png"
                        kwargs["save_path"] = save_path_temp
                        for k, comp in enumerate(component_list):
                            func(data.components[comp], fig=fig, subplot_index=k, **kwargs)
                        image = imageio.imread(save_path_temp)
                        writer.append_data(image)
                

                else:
                    for j in range(0, index_max, index_step):
                        save_path_temp = save_path + "\\temp_" + str(j) + ".png"
                        kwargs["save_path"] = save_path_temp
                        func(data, **kwargs)
                        image = imageio.imread(save_path_temp)
                        writer.append_data(image)
       
        else:
            if isinstance(data_list, VectorField):
                if component_list is None:  # default: extract all components
                    component_list = data.components.keys()
                ncomp = len(component_list)
                for j in range(0, index_max, index_step):
                    fig, axs = subplots(1, ncomp, tight_layout=True, figsize=(20, 10))
                    save_path_temp = save_path + "\\temp_" + str(j) + ".png"
                    kwargs[index_var] = j
                    kwargs["save_path"] = save_path_temp
                    for k, comp in enumerate(component_list):
                        func(data_list.components[comp], fig=fig, subplot_index=k, **kwargs)
                    image = imageio.imread(save_path_temp)
                    writer.append_data(image)
            else:
                for j in range(0, index_max, index_step):
                    save_path_temp = save_path + "\\temp_" + str(j) + ".png"
                    kwargs[index_var] = j
                    kwargs["save_path"] = save_path_temp
                    func(data_list, **kwargs)
                    image = imageio.imread(save_path_temp)
                    writer.append_data(image)

    for file in glob(save_path + "\\temp_*"):
        remove(file)
