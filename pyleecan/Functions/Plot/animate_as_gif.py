# -*- coding: utf-8 -*-

import imageio
from os.path import join
from os import remove
from glob import glob


def animate_as_gif(
    func, data, save_path, file_name, t_index_max, **kwargs
):
    """Animate an existing plot command as a gif

    Parameters
    ----------
    func : function
        plot command
    data : Data
        Data object to plot
    save_path : str
        path where to save the gif
    file_name : str
        name of the gif file
    t_index_max : int
        maximum time index for the animation
    kwargs : dict
        parameters of func
    """
    
    with imageio.get_writer(join(save_path, file_name), mode='I') as writer:
        for i in range(t_index_max):
            save_path_temp = save_path + "\\temp_" + str(i) + ".png"
            kwargs["t_index"] = i
            kwargs["save_path"] = save_path_temp
            func(data, **kwargs)
            image = imageio.imread(save_path_temp)
            writer.append_data(image)
    
    for file in glob(save_path + "\\temp_*"):
        remove(file)