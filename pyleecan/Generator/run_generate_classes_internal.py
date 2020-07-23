# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, system

sys.path.insert(0, normpath(abspath(join(dirname(__file__), "..", ".."))))

from ..Generator.run_generate_classes import generate_code
from ..Generator.read_fct import read_all
from ..definitions import MAIN_DIR, DOC_DIR, INT_DIR

if __name__ == "__main__":
    gen_dict = read_all(DOC_DIR, is_internal=True, in_path=INT_DIR)
    generate_code(MAIN_DIR, gen_dict)
    # Run black
    system("{} -m black .".format(sys.executable))
