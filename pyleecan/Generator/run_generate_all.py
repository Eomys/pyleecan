# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath
from os import listdir, remove, system

begin = len(normpath(abspath(join(dirname(__file__), "../.."))))
end = len(normpath(abspath(join(dirname(__file__), ".."))))
MAIN_DIR = dirname(realpath(__file__))

package_name = MAIN_DIR[begin + 1 : end]

# Add the directory to the python path
sys.path.append(MAIN_DIR[:begin])

exec("from " + package_name + ".Generator.run_generate_classes import generate_code")
exec("from " + package_name + ".Generator.gui_generator import generate_gui")
exec("from " + package_name + ".Generator.read_fct import read_all")
exec("from " + package_name + ".definitions import MAIN_DIR, DOC_DIR, INT_DIR")

if __name__ == "__main__":
    gen_dict = read_all(DOC_DIR, is_internal=False, in_path=INT_DIR)
    generate_code(MAIN_DIR, gen_dict)
    generate_gui(gen_dict, is_gen_resource=True)
    # Run black
    try:
        import black

        system('"{}" -m black .'.format(sys.executable))
    except ImportError:
        print("/!\\ Please install and run black /!\\")
