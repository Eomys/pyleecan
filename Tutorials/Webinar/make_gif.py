import imageio
from os import listdir

def make_gif(xoutput):
    folder = xoutput.get_path_result()
    img_list = list()
    for filename in listdir(folder):
        if filename[-4:] == ".png":
            img_list.append(imageio.imread(join(folder,filename)))

    imageio.mimsave(join(folder,"machine.gif"), img_list, duration = 0.7)