from os.path import dirname, abspath, normpath, join
from os import listdir, getcwd
from Diagram import Diagram

print(getcwd())

DOC_DIR = normpath(abspath(join(dirname(__file__),"..","ClassesRef")))

def draw_all_diagrams(direction="TB",specify_direction = False):
    list_dir=[join(DOC_DIR, folder_name) for folder_name in listdir(DOC_DIR)]
    for path in list_dir:
        Diagram([path], direction=direction,specify_direction=specify_direction).draw_diagram()
    Diagram(list_dir, name = "Pyleecan", direction=direction,specify_direction=specify_direction).draw_diagram()
    Diagram([DOC_DIR+r"\Simulation"], name = "only_simu",parent_class_name= "Simulation").draw_diagram()

def main():
    draw_all_diagrams()
    
    
if __name__ == "__main__":
    main()