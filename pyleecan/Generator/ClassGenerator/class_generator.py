# -*- coding: utf-8 -*-
from os.path import join

from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import (
    find_import_type,
    get_value_str,
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
)
from ...Generator.ClassGenerator.import_method_generator import import_method
from ...Generator.ClassGenerator.init_method_generator import generate_init
from ...Generator.ClassGenerator.str_method_generator import generate_str
from ...Generator.ClassGenerator.as_dict_method_generator import generate_as_dict
from ...Generator.ClassGenerator.copy_method_generator import generate_copy
from ...Generator.ClassGenerator.properties_generator import generate_properties
from ...Generator.ClassGenerator.init_void_method_generator import generate_init_void
from ...Generator.ClassGenerator.eq_method_generator import generate_eq
from ...Generator.ClassGenerator.compare_method_generator import generate_compare
from ...Generator.ClassGenerator.size_of_method_generator import generate_size_of
from ...Generator.ClassGenerator.set_None_method_generator import generate_set_None


def generate_class(
    gen_dict, class_name, path_to_gen, soft_name="pyleecan", is_log=True
):
    """generate the corresponding class file (erase the previous code)

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    class_name : str
        name of the class to generate
    path_to_gen : str
        path to the file to save the class code

    Returns
    -------
    None

    """

    class_dict = gen_dict[class_name]
    class_pack = class_dict["package"]

    # Start of file generation
    # Create or Erase the file by opening it
    class_file = open(join(path_to_gen, class_name + ".py"), "w")

    # List of non python type to import
    import_type_list = list(find_import_type(gen_dict, class_dict, []))
    if class_name in import_type_list:  # For recursive class
        import_type_list.remove(class_name)
    # Encoding
    class_file.write("# -*- coding: utf-8 -*-\n")

    # Warning
    class_file.write(
        "# File generated according to "
        + class_dict["path"][class_dict["path"].find("Generator") :]
        + "\n"
    )
    if class_dict["is_internal"]:
        class_file.write(
            "# WARNING! Internal version of the class: DO NOT SHARE ON GITHUB !\n"
        )
    class_file.write("# WARNING! All changes made in this file will be lost!\n")
    class_file.write(
        '"""Method code available at https://github.com/Eomys/'
        + soft_name
        + "/tree/master/"
        + soft_name
        + "/Methods/"
        + class_dict["package"]
        + "/"
        + class_dict["name"]
        + '\n"""\n\n'
    )

    # Import
    class_file.write("from os import linesep\n")
    class_file.write("from sys import getsizeof\n")
    if is_log:
        class_file.write("from logging import getLogger\n")

    if "ndarray" in import_type_list:
        class_file.write("from ._check import set_array, " + "check_var, raise_\n")
    else:
        class_file.write("from ._check import check_var, raise_\n")

    # Get logger function
    if is_log:
        class_file.write("from ..Functions.get_logger import get_logger\n")

    #
    # if len(class_dict["properties"]) == 0 and class_dict["mother"] == "":
    #     class_file.write("from ..Functions.get_logger import check_init_dict\n")

    # Save function
    class_file.write("from ..Functions.save import save\n")
    class_file.write("from ..Functions.load import load_init_dict\n")
    class_file.write("from ..Functions.Load.import_class import import_class\n")
    # Copy method
    class_file.write("from copy import deepcopy\n")

    # Import of the mother_class (FrozenClass by default)
    # All the classes file are in the Classes folder (regardless of their main package)
    if class_dict["mother"] != "" and "." not in class_dict["mother"]:
        class_file.write(
            "from ." + class_dict["mother"] + " import " + class_dict["mother"] + "\n\n"
        )
    elif class_dict["mother"] != "" and "." in class_dict["mother"]:
        class_split = class_dict["mother"].split(".")
        # Daughter of external package class
        class_file.write(
            "from " + ".".join(class_split[:-1]) + " import " + class_split[-1] + "\n\n"
        )
    else:
        class_file.write("from ._frozen import FrozenClass\n\n")

    # Import all the methods of the class
    # The methods are in Methods.<Main package>.<class name>, one file per method
    if len(class_dict["methods"]) > 0:
        class_file.write("# Import all class method\n")
        class_file.write(
            "# Try/catch to remove unnecessary dependencies in unused method\n"
        )
    for meth in class_dict["methods"]:
        class_file.write(import_method(class_pack, class_name, meth))
    if len(class_dict["methods"]) > 0:
        class_file.write("\n")

    # ImportMatrixVal for ImportMatrix setter
    if "ImportMatrix" in import_type_list:
        class_file.write("from ..Classes.ImportMatrixVal import ImportMatrixVal\n")
        class_file.write("from numpy import ndarray\n")
        if "ndarray" not in import_type_list and "{ndarray}" not in import_type_list:
            import_type_list.append("ndarray")
    # Import Array from numpy
    if (
        "{ndarray}" in import_type_list
        or "[ndarray]" in import_type_list
        or "ndarray" in import_type_list
    ):
        class_file.write("from numpy import array, array_equal\n")
    if "{ndarray}" in import_type_list:
        import_type_list.remove("{ndarray}")
    if "[ndarray]" in import_type_list:
        import_type_list.remove("[ndarray]")
    if "ndarray" in import_type_list:
        import_type_list.remove("ndarray")
    if "[]" in import_type_list:
        class_file.write("from numpy import array, ndarray\n")
    if "function" in import_type_list:
        class_file.write("from ntpath import basename\n")
        class_file.write("from os.path import isfile\n")
        class_file.write("from ._check import CheckTypeError\n")
        class_file.write("import numpy as np\n")
        class_file.write("import random\n")
        import_type_list.remove("function")
    class_file.write("from numpy import isnan\n")  # For compare

    # Import types from other package
    types_imported = []
    for import_type in import_type_list:
        if "." in import_type and "SciDataTool" not in import_type:
            class_file.write("from cloudpickle import dumps, loads\n")
            class_file.write("from ._check import CheckTypeError\n")

            # Remove the list if needed
            if import_type.startswith("["):
                import_type = import_type[1:-1]

            # Extract import name
            from_name = import_type[: import_type.rfind(".")]
            type_name = import_type[import_type.rfind(".") + 1 :]

            # Import the type if not already imported
            if type_name not in types_imported:
                class_file.write("try :\n")
                class_file.write(
                    TAB + "from " + from_name + " import " + type_name + "\n"
                )
                class_file.write("except ImportError :\n")
                class_file.write(TAB + type_name + " = ImportError\n")

                types_imported.append(type_name)

    # Import of all needed software type for empty init
    class_file.write("from ._check import InitUnKnowClassError\n")

    # Class declaration
    if class_dict["mother"] != "" and "." not in class_dict["mother"]:
        class_file.write(
            "\n\nclass " + class_name + "(" + class_dict["mother"] + "):\n"
        )
    elif class_dict["mother"] != "" and "." in class_dict["mother"]:
        class_file.write(
            "\n\nclass "
            + class_name
            + "("
            + class_dict["mother"].split(".")[-1]
            + "):\n"
        )
    else:
        class_file.write("\n\nclass " + class_name + "(FrozenClass):\n")

    # Class Docstring
    if class_dict["desc"] != "":
        class_file.write(TAB + '"""' + class_dict["desc"] + '"""\n')
    class_file.write("\n")

    # Declare all class Constante (VERSION should be a constante for every classes)
    for cst in class_dict["constants"]:
        class_file.write(TAB + cst["name"] + " = " + str(cst["value"]) + "\n")
    class_file.write("\n")

    # Asign all the Methods of the class
    if len(class_dict["methods"]) > 1:
        class_file.write(
            TAB
            + "# Check ImportError to remove unnecessary dependencies in unused method\n"
        )
    for meth in class_dict["methods"]:
        meth_name = meth.split(".")[-1]
        if class_pack not in ["", None]:
            class_file.write(
                TAB
                + "# cf Methods."
                + class_pack
                + "."
                + class_name
                + "."
                + meth
                + "\n"
            )
        else:
            class_file.write(TAB + "# cf Methods." + class_name + "." + meth + "\n")
        class_file.write(TAB + "if isinstance(" + meth_name + ", ImportError):\n")
        class_file.write(TAB2 + meth_name + " = property(\n")
        class_file.write(TAB3 + "fget=lambda x: raise_(\n")
        # PEP8 formating
        if len(class_name) + 2 * len(meth_name) > 39:
            # 2 lines Import text
            class_file.write(TAB4 + "ImportError(\n")
            class_file.write(
                TAB5 + """"Can't use """ + class_name + " method " + meth_name + ': "\n'
            )
            class_file.write(TAB5 + "+ str(" + meth_name + ")\n")
            class_file.write(TAB4 + ")\n")
        elif len(class_name) + 2 * len(meth_name) > 29:
            # Import text on line different line
            class_file.write(TAB4 + "ImportError(\n")
            class_file.write(
                TAB5 + """"Can't use """ + class_name + " method " + meth_name + ': "'
            )
            class_file.write(" + str(" + meth_name + ")\n")
            class_file.write(TAB4 + ")\n")
        else:  # On one line
            class_file.write(
                TAB4
                + """ImportError("Can't use """
                + class_name
                + " method "
                + meth_name
                + ': " + str('
                + meth_name
                + "))\n"
            )
        class_file.write(TAB3 + ")\n")
        class_file.write(TAB2 + ")\n")
        class_file.write(TAB + "else:\n")
        class_file.write(TAB2 + meth_name + " = " + meth_name + "\n")
    # Save methods
    class_file.write(TAB + "# generic save method is available in all object\n")
    if "save" not in class_dict["methods"]:
        class_file.write(TAB + "save = save\n")

    if is_log:
        class_file.write(TAB + "# get_logger method is available in all object\n")
        class_file.write(TAB + "get_logger = get_logger\n\n")

    # Add the __init__ method
    if "__init__" not in class_dict["methods"]:
        if len(class_dict["properties"]) == 0 and class_dict["mother"] == "":
            class_file.write(generate_init_void(class_name, soft_name=soft_name) + "\n")
        else:
            class_file.write(
                generate_init(gen_dict, class_dict, soft_name=soft_name) + "\n"
            )

    # Add the __str__ method
    if "__str__" not in class_dict["methods"]:
        class_file.write(generate_str(gen_dict, class_dict) + "\n")

    # Add the __eq__ method
    if "__eq__" not in class_dict["methods"]:
        class_file.write(generate_eq(gen_dict, class_dict) + "\n")

    # Add the compare method
    if "compare" not in class_dict["methods"]:
        class_file.write(generate_compare(gen_dict, class_dict) + "\n")

    # Add the __sizeof__ method
    class_file.write(generate_size_of(gen_dict, class_dict))

    # Add the as_dict method
    if "as_dict" not in class_dict["methods"]:
        class_file.write(generate_as_dict(gen_dict, class_dict) + "\n")

    # Add the copy method
    if "copy" not in class_dict["methods"]:
        class_file.write(generate_copy(gen_dict, class_dict) + "\n")

    # Add the _set_None method
    if "_set_None" not in class_dict["methods"]:
        class_file.write(generate_set_None(gen_dict, class_dict, soft_name=soft_name))

    # Add all the properties getter and setter
    if len(class_dict["properties"]) > 0:
        class_file.write(
            "\n" + generate_properties(gen_dict, class_dict, soft_name=soft_name) + "\n"
        )

    # End of class generation
    class_file.close()
