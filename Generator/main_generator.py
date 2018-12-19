# -*- coding: utf-8 -*-
"""Created on Mon Nov 10 15:44:20 2014
@author: pierre_b
"""
from os import mkdir
from os.path import isdir, join

from pyleecan.Generator.class_generator import generate_class
from pyleecan.Generator.read_fct import read_all
from pyleecan.Generator import MAIN_DIR

# List of the main packages (to sort the classes)
PACKAGE_LIST = ["Geometry", "Machine", "Material", "Slot"]


def generate_code(root_path):
    """Generate pyleecan Classes code according to doc in root_path

    Parameters
    ----------
    root_path : str
        Path to the main folder of Pyleecan

    Returns
    -------
    None
    """
    CLASS_DIR = join(root_path, "Classes")
    TEST_DIR = join(root_path, "Tests")
    DOC_DIR = join(root_path, "Generator", "ClassesRef")
    print("Reading classes csv in :" + DOC_DIR)
    print("Saving generated files in :" + CLASS_DIR)

    # A file to import every classes quickly
    import_file = open(join(TEST_DIR, "Classes", "import_all.py"), "w")
    import_file.write("# -*- coding: utf-8 -*-\n\n")

    # Read all the csv files
    gen_dict = read_all(DOC_DIR)

    # Generate all the class files
    for class_name, class_dict in list(gen_dict.items()):
        import_file.write(
            "from pyleecan.Classes." + class_name + " import " + class_name + "\n"
        )
        print("Generation of " + class_name + " class")
        generate_class(gen_dict, class_name, CLASS_DIR)
    import_file.close()


if __name__ == "__main__":
    generate_code(MAIN_DIR)
