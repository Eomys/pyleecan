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
    try:
        import black

        system('"{}" -m black .'.format(sys.executable))
        if black.__version__.split(".")[0] != "24":
            print("\n############################################")
            print(
                "WARNING: The official version of black for pyleecan is 24, please update your black version"
            )
            print("############################################\n")
    except ImportError:
        print("/!\\ Please install and run black (version 24) /!\\")
