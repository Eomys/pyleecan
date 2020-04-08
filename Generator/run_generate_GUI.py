# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join

sys.path.insert(0, normpath(abspath(join(dirname(__file__), "..", ".."))))

from os import mkdir
from os.path import isdir

from pyleecan.Generator.class_generator import generate_class
from pyleecan.Generator.gui_generator import generate_gui
from pyleecan.Generator.read_fct import read_all
from pyleecan.definitions import MAIN_DIR


if __name__ == "__main__":
    DOC_DIR = join(MAIN_DIR, "Generator", "ClassesRef")
    gen_dict = read_all(DOC_DIR)
    print("#############################\nGenerating gui....")
    generate_gui(gen_dict, is_gen_resource=False)
