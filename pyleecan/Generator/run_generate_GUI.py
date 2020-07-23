# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir
from os import listdir, remove, mkdir, system

begin = len(normpath(abspath(join(dirname(__file__), "../.."))))
end = len(normpath(abspath(join(dirname(__file__), ".."))))
MAIN_DIR = dirname(realpath(__file__))

package_name = MAIN_DIR[begin + 1 : end]

# Add the directory to the python path
sys.path.append(MAIN_DIR[:begin])

exec("from " + package_name + ".Generator.gui_generator import generate_gui")
exec("from " + package_name + ".Generator.read_fct import read_all")
exec("from " + package_name + ".definitions import MAIN_DIR")


if __name__ == "__main__":
    DOC_DIR = join(MAIN_DIR, "Generator", "ClassesRef")
    gen_dict = read_all(DOC_DIR)
    print("#############################\nGenerating gui....")
    generate_gui(gen_dict, is_gen_resource=False)

    # Run black
    system("{} -m black .".format(sys.executable))
