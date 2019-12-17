# -*- coding: utf-8 -*-
"""Created on Tue Nov 04 09:01:21 2014
@author: pierre_b
"""
from codecs import open as open_co
from os.path import join

from pyleecan.Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from pyleecan.Generator.read_fct import (
    find_import_type,
    get_value_str,
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
)


def generate_class(gen_dict, class_name, path_to_gen):
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
    class_file = open_co(join(path_to_gen, class_name + ".py"), "w", "utf-8")

    # List of non python type to import
    import_type_list = list(find_import_type(gen_dict, class_dict, []))
    if class_name in import_type_list:  # For recursive class
        import_type_list.remove(class_name)
    # Encoding
    class_file.write("# -*- coding: utf-8 -*-\n")

    # Warning
    class_file.write('"""File generated according to ' + class_dict["path"] + "\n")
    if class_dict["is_internal"]:
        class_file.write(
            "WARNING! Internal version of the class: DO NOT SHARE ON GITHUB !\n"
        )
    class_file.write('WARNING! All changes made in this file will be lost!\n"""\n\n')

    # Import
    class_file.write("from os import linesep\n")
    if "ndarray" in import_type_list:
        class_file.write(
            "from pyleecan.Classes.check import set_array, "
            + "check_init_dict, check_var, raise_\n"
        )
    else:
        class_file.write(
            "from pyleecan.Classes.check import check_init_dict, check_var, raise_\n"
        )
    # Save function
    class_file.write("from pyleecan.Functions.save import save\n")

    # Import of the mother_class (FrozenClass by default)
    # All the classes file are in the Classes folder (regardless of their main package)
    if class_dict["mother"] != "":
        class_file.write(
            "from pyleecan.Classes."
            + class_dict["mother"]
            + " import "
            + class_dict["mother"]
            + "\n\n"
        )
    else:
        class_file.write("from pyleecan.Classes.frozen import FrozenClass\n\n")

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

    # For Matrix and Vector (numpy) property
    if "ndarray" in import_type_list:
        class_file.write("from numpy import array, array_equal\n")
        import_type_list.remove("ndarray")

    # Import of all needed pyleecan type for empty init
    class_file.write("from pyleecan.Classes.check import InitUnKnowClassError\n")
    for pyleecan_type in import_type_list:
        class_file.write(
            "from pyleecan.Classes." + pyleecan_type + " import " + pyleecan_type + "\n"
        )

    # Class declaration
    if class_dict["mother"] != "":
        class_file.write(
            "\n\nclass " + class_name + "(" + class_dict["mother"] + "):\n"
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
        class_file.write(
            TAB + "# cf Methods." + class_pack + "." + class_name + "." + meth + "\n"
        )
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
    class_file.write(TAB + "# save method is available in all object\n")
    class_file.write(TAB + "save = save\n\n")

    # Add the __init__ method
    if len(class_dict["properties"]) == 0 and class_dict["mother"] == "":
        class_file.write(generate_init_void() + "\n")
    else:
        class_file.write(generate_init(gen_dict, class_dict) + "\n")

    # Add the __str__ method
    class_file.write(generate_str(gen_dict, class_dict) + "\n")

    # Add the __eq__ method
    class_file.write(generate_eq(gen_dict, class_dict) + "\n")

    # Add the as_dict method
    class_file.write(generate_as_dict(gen_dict, class_dict) + "\n")

    # Add the _set_None method
    class_file.write(generate_set_None(gen_dict, class_dict))

    # Add all the properties getter and setter
    if len(class_dict["properties"]) > 0:
        class_file.write("\n" + generate_properties(gen_dict, class_dict) + "\n")

    # End of class generation
    class_file.close()


def import_method(class_pack, class_name, meth):
    """Method to generate the code to import a method (with import check)

    Parameters
    ----------
    class_pack : str
        Package of the class (Machine, Simulation, Material...)
    class_name : str
        Name of the class
    meth : str
        Path to the method in the class Method folder
        (subfolder.name if any subfolder)

    Returns
    -------
    code: str
        Corresponding code
    """

    meth_name = meth.split(".")[-1]
    code = "try:\n"
    code += (
        TAB
        + "from pyleecan.Methods."
        + class_pack
        + "."
        + class_name
        + "."
        + meth
        + " import "
        + meth_name
        + "\n"
    )
    code += "except ImportError as error:\n"
    code += TAB + meth_name + " = error\n\n"
    return code


def generate_init(gen_dict, class_dict):
    """Generate the code for the __init__ method for the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)


    Returns
    -------
    init_str : str
        String containing the __init__ method code
    """

    class_name = class_dict["name"]
    init_str = ""  # This string is for the generated code

    init_by_var = ""  # For the initialisation with the argument
    # Add the parent property only in the top mother classes
    if class_dict["mother"] == "":
        init_by_var += TAB2 + "self.parent = None\n"

    for prop in class_dict["properties"]:
        if prop["type"] in PYTHON_TYPE:
            # Add => "self.my_var = my_var\n" to init_by_var
            init_by_var += TAB2 + "self." + prop["name"] + " = " + prop["name"] + "\n"
        elif prop["type"] == "ndarray":
            # Default value is None which should call the corresponding init
            init_by_var += (
                TAB2 + "# " + prop["name"] + " can be None, a ndarray or a list\n"
            )
            init_by_var += (
                TAB2 + 'set_array(self, "' + prop["name"] + '", ' + prop["name"] + ")\n"
            )
        elif is_list_pyleecan_type(prop["type"]):
            # List of pyleecan type
            init_by_var += (
                TAB2
                + "# "
                + prop["name"]
                + " can be None or a list of "
                + prop["type"][1:-1]
                + " object\n"
            )
            init_by_var += TAB2 + "self." + prop["name"] + " = list()\n"
            init_by_var += TAB2 + "if type(" + prop["name"] + ") is list:\n"
            init_by_var += TAB3 + "for obj in " + prop["name"] + ":\n"
            init_by_var += TAB4 + "if obj is None:  # Default value\n"
            init_by_var += (
                TAB5
                + "self."
                + prop["name"]
                + ".append("
                + prop["type"][1:-1]
                + "())\n"
            )
            type_dict = gen_dict[prop["type"][1:-1]]
            daug_list = type_dict["daughters"]
            init_by_var += generate_set_class_by_dict_list(
                prop["name"], prop["type"][1:-1], daug_list
            )
            init_by_var += TAB4 + "else:\n"
            init_by_var += TAB5 + "self." + prop["name"] + ".append(obj)\n"
            init_by_var += TAB2 + "elif " + prop["name"] + " is None:\n"
            init_by_var += TAB3 + "self." + prop["name"] + " = list()\n"
            init_by_var += TAB2 + "else:\n"
            init_by_var += TAB3 + "self." + prop["name"] + " = " + prop["name"] + "\n"

        elif is_dict_pyleecan_type(prop["type"]):
            # List of pyleecan type
            init_by_var += (
                TAB2
                + "# "
                + prop["name"]
                + " can be None or a dict of "
                + prop["type"][1:-1]
                + " object\n"
            )
            init_by_var += TAB2 + "self." + prop["name"] + " = dict()\n"
            init_by_var += TAB2 + "if type(" + prop["name"] + ") is dict:\n"
            init_by_var += TAB3 + "for key, obj in " + prop["name"] + ".items():\n"
            type_dict = gen_dict[prop["type"][1:-1]]
            daug_list = type_dict["daughters"]
            init_by_var += generate_set_class_by_dict_dict(
                prop["name"], prop["type"][1:-1], daug_list
            )
            init_by_var += TAB4 + "else:\n"
            init_by_var += TAB5 + "self." + prop["name"] + "[key] = obj\n"
            init_by_var += TAB2 + "elif " + prop["name"] + " is None:\n"
            init_by_var += TAB3 + "self." + prop["name"] + " = dict()\n"
            init_by_var += TAB2 + "else:\n"
            init_by_var += (
                TAB3
                + "self."
                + prop["name"]
                + " = "
                + prop["name"]
                + "# Should raise an error\n"
            )

        else:  # For pyleecan Type
            init_by_var += (
                TAB2
                + "# "
                + prop["name"]
                + " can be None, a "
                + prop["type"]
                + " object or a dict\n"
            )
            type_dict = gen_dict[prop["type"]]
            daug_list = type_dict["daughters"]
            init_by_var += generate_set_class_by_dict(
                prop["name"], prop["type"], daug_list
            )
            init_by_var += TAB2 + "else:\n"
            init_by_var += TAB3 + "self." + prop["name"] + " = " + prop["name"] + "\n"

    # Load all the properties including mother ones
    (all_properties, mother_prop_list) = get_mother_attr(
        gen_dict, class_dict, "properties"
    )

    mother_arg_list = ""  # For the call of super init
    for prop in mother_prop_list:
        if mother_arg_list != "":  # Avoid the first coma
            # Add => ", my_var = my_var" to mother_arg_list
            mother_arg_list += ", " + prop["name"] + "=" + prop["name"]
        else:
            # Add => "my_var = my_var" to mother_arg_list
            mother_arg_list += prop["name"] + "=" + prop["name"]

    check_dict = ""  # list of all the property expectable in the init_dict
    init_by_dict = ""  # To overwrite the parameter from init_dict
    arg_list = ""  # For the argument with default value
    init_MType = ""  # To initialize the pyleecan Type default (-1)
    for prop in all_properties:
        # To overwrite the parameter from init_dict
        init_by_dict += TAB3 + 'if "' + prop["name"] + '" in list(init_dict.keys()):\n'
        init_by_dict += TAB4 + prop["name"] + ' = init_dict["' + prop["name"] + '"]\n'
        # For the argument with default value
        if prop["type"] in PYTHON_TYPE:
            # Add => ", my_var = 10" to arg_list
            arg_list += (
                ", " + prop["name"] + "=" + get_value_str(prop["value"], prop["type"])
            )
        elif prop["type"] == "ndarray":
            if prop["value"] not in ["", None] and type(prop["value"]) is list:
                # Default value of ndarray are list
                arg_list += ", " + prop["name"] + "=" + str(prop["value"])
            else:
                arg_list += ", " + prop["name"] + "=None"
        elif is_list_pyleecan_type(prop["type"]):
            # List of pyleecan type
            arg_list += ", " + prop["name"] + "=list()"
        elif is_dict_pyleecan_type(prop["type"]):
            # Dict of pyleecan type
            arg_list += ", " + prop["name"] + "=dict()"
        else:  # pyleecan type
            if prop["value"] == "":
                arg_list += ", " + prop["name"] + "=-1"
            else:  # Default value (most likely None)
                arg_list += (
                    ", "
                    + prop["name"]
                    + "="
                    + get_value_str(prop["value"], prop["type"])
                )
            # To initialize the pyleecan Type default (-1)
            init_MType += TAB2 + "if " + prop["name"] + " == -1:\n"
            init_MType += TAB3 + prop["name"] + " = " + prop["type"] + "()\n"
        # For check_init_dict
        if check_dict == "":  # First variable
            check_dict += '"' + prop["name"] + '"'
        else:
            check_dict += ', "' + prop["name"] + '"'

    # Code generation in init_str
    init_str += TAB + "def __init__(self" + arg_list + ", init_dict=None):\n"
    init_str += TAB2 + '"""Constructor of the class. Can be use in two ways ' ":\n"
    init_str += (
        TAB2 + "- __init__ (arg1 = 1, arg3 = 5) every parameters "
        "have name and default values\n"
    )
    init_str += (
        TAB3 + "for Matrix, None will initialise the property with " "an empty Matrix\n"
    )
    init_str += TAB3 + "for pyleecan type, None will call the default " "constructor\n"
    init_str += (
        TAB2 + "- __init__ (init_dict = d) d must be a dictionnary "
        "wiht every properties as keys\n\n"
    )
    init_str += TAB2 + "ndarray or list can be given for Vector and Matrix\n"
    init_str += TAB2 + 'object or dict can be given for pyleecan Object"""\n\n'

    init_str += init_MType
    init_str += TAB2 + "if init_dict is not None:  # Initialisation by dict\n"
    init_str += TAB3 + "check_init_dict(init_dict, [" + check_dict + "])\n"
    init_str += TAB3 + "# Overwrite default value with init_dict content\n"
    init_str += init_by_dict
    init_str += TAB2 + "# Initialisation by argument\n"
    init_str += init_by_var
    # Add the call to super __init__ if needed
    if class_dict["mother"] != "":
        init_str += TAB2 + "# Call " + class_dict["mother"] + " init\n"
        init_str += (
            TAB2 + "super(" + class_name + ", self).__init__(" + mother_arg_list + ")\n"
        )
        init_str += (
            TAB2
            + "# The class is frozen (in "
            + class_dict["mother"]
            + " init), for now it's impossible "
            "to\n" + TAB2 + "# add new "
            "properties\n"
        )
    else:
        init_str += (
            "\n"
            + TAB2
            + "# The class is frozen, for now it's "
            + "impossible to add new properties\n"
        )
        init_str += TAB2 + "self._freeze()\n"

    return init_str


def generate_set_class_by_dict_list(prop_name, prop_type, daug_list):
    """Generate the code to set a list of pyleecan class property with a dictionary

    Parameters
    ----------
    prop_name : str
        Name of the property to set
    prop_type : str
        Type of the property to set
    daug_list : list
        List of the Daughter of the class

    Returns
    -------
    class_dict_str : str
        String containing the code to set a list of pyleecan class property with a dictionary
    """

    class_dict_str = ""
    class_dict_str += TAB4 + "elif isinstance(obj, dict):\n"
    if len(daug_list) > 0:
        if prop_type not in daug_list:
            daug_list.insert(0, prop_type)
        # Add the posibility to call the daughter init
        class_dict_str += (
            TAB5 + "# Check that the type is correct (including daughter)\n"
        )
        class_dict_str += TAB5 + 'class_name = obj.get("__class__")\n'
        class_dict_str += TAB5 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += TAB6 + "raise InitUnKnowClassError(\n"
        class_dict_str += TAB7 + '"Unknow class name "\n'
        class_dict_str += TAB7 + "+ class_name\n"
        class_dict_str += TAB7 + '+ " in init_dict for ' + prop_name + '"\n'
        class_dict_str += TAB6 + ")\n"
        class_dict_str += TAB5 + "# Dynamic import to call the correct constructor\n"
        class_dict_str += TAB5 + "module = __import__(\n"
        class_dict_str += (
            TAB6 + '"pyleecan.Classes." + class_name, fromlist=[class_name]\n'
        )
        class_dict_str += TAB5 + ")\n"
        class_dict_str += TAB5 + "class_obj = getattr(module, class_name)\n"
        class_dict_str += (
            TAB5 + "self." + prop_name + ".append(" + "class_obj(init_dict=obj))\n"
        )
    else:  # No daughter
        class_dict_str += (
            TAB5 + "self." + prop_name + ".append(" + prop_type + "(init_dict=obj))\n"
        )
    return class_dict_str


def generate_set_class_by_dict_dict(prop_name, prop_type, daug_list):
    """Generate the code to set a dict of pyleecan class property with a dictionary

    Parameters
    ----------
    prop_name : str
        Name of the property to set
    prop_type : str
        Type of the property to set
    daug_list : list
        List of the Daughter of the class

    Returns
    -------
    class_dict_str : str
        String containing the code to set a list of pyleecan class property with a dictionary
    """

    class_dict_str = ""
    class_dict_str += TAB4 + "if isinstance(obj, dict):\n"
    if len(daug_list) > 0:
        if prop_type not in daug_list:
            daug_list.insert(0, prop_type)
        # Add the posibility to call the daughter init
        class_dict_str += (
            TAB5 + "# Check that the type is correct (including daughter)\n"
        )
        class_dict_str += TAB5 + "class_name = obj.get('__class__')\n"
        class_dict_str += TAB5 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += (
            TAB6
            + 'raise InitUnKnowClassError("Unknow class name "+class_name+" in init_dict for '
            + prop_name
            + '")\n'
        )
        class_dict_str += TAB5 + "# Dynamic import to call the correct constructor\n"
        class_dict_str += (
            TAB5
            + 'module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])\n'
        )
        class_dict_str += TAB5 + "class_obj = getattr(module,class_name)\n"
        class_dict_str += (
            TAB5 + "self." + prop_name + "[key] = class_obj(init_dict=obj)\n"
        )
    else:  # No daughter
        class_dict_str += (
            TAB5 + "self." + prop_name + "[key] = " + prop_type + "(init_dict=obj))\n"
        )
    return class_dict_str


def generate_set_class_by_dict(prop_name, prop_type, daug_list):
    """Generate the code to set a pyleecan class property with a dictionary

    Parameters
    ----------
    prop_name : str
        Name of the property to set
    prop_type : str
        Type of the property to set
    daug_list : list
        List of the Daughter of the class

    Returns
    -------
    class_dict_str : str
        String containing the code to set a pyleecan class property with a dictionary
    """

    class_dict_str = ""
    class_dict_str += TAB2 + "if isinstance(" + prop_name + ", dict):\n"

    if len(daug_list) > 0:
        if prop_type not in daug_list:
            daug_list.insert(0, prop_type)
        # Add the posibility to call the daughter init
        class_dict_str += (
            TAB3 + "# Check that the type is correct (including daughter)\n"
        )
        class_dict_str += TAB3 + "class_name = " + prop_name + ".get('__class__')\n"
        class_dict_str += TAB3 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += (
            TAB4
            + 'raise InitUnKnowClassError("Unknow class name "+class_name+" in init_dict for '
            + prop_name
            + '")\n'
        )
        class_dict_str += TAB3 + "# Dynamic import to call the correct constructor\n"
        class_dict_str += (
            TAB3
            + 'module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])\n'
        )
        class_dict_str += TAB3 + "class_obj = getattr(module,class_name)\n"
        class_dict_str += (
            TAB3
            + "self."
            + prop_name
            + " = "
            + "class_obj(init_dict="
            + prop_name
            + ")\n"
        )
    else:  # No daughter
        class_dict_str += (
            TAB3
            + "self."
            + prop_name
            + " = "
            + prop_type
            + "(init_dict="
            + prop_name
            + ")\n"
        )
    return class_dict_str


def generate_init_void():
    """Generate the code for the init method with no property

    Returns
    -------
    init_str : str
        String containing the code to initialize a class with no property
    """

    init_str = ""

    init_str += TAB + "def __init__(self, init_dict=None):\n"
    init_str += TAB2 + '"""Constructor of the class. Can be use in two ways ' ":\n"
    init_str += (
        TAB2 + "- __init__ (arg1 = 1, arg3 = 5) every parameters "
        "have name and default values\n"
    )
    init_str += (
        TAB3 + "for Matrix, None will initialise the property with " "an empty Matrix\n"
    )
    init_str += TAB3 + "for pyleecan type, None will call the default " "constructor\n"
    init_str += (
        TAB2 + "- __init__ (init_dict = d) d must be a dictionnary "
        "wiht every properties as keys\n\n"
    )
    init_str += TAB2 + "ndarray or list can be given for Vector and Matrix\n"
    init_str += TAB2 + 'object or dict can be given for pyleecan Object"""\n\n'

    init_str += TAB2 + "if init_dict is not None:  # Initialisation by dict\n"
    init_str += TAB3 + "check_init_dict(init_dict, [])\n"

    init_str += (
        TAB2 + "# The class is frozen, for now it's impossible to "
        "add new properties\n"
    )
    init_str += TAB2 + "self.parent = None\n"
    init_str += TAB2 + "self._freeze()\n"

    return init_str


def generate_str(gen_dict, class_dict):
    """Generate the code for the __str__ method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    str_str : str
        String containing the code for the __str__ method of the class
    """

    class_name = class_dict["name"]
    str_str = ""  # This string is for the generated code

    var_str = ""  # For the creation of the return string (in __str__)

    # Display parent only in the top mother class __str__ method
    if class_dict["mother"] == "":
        var_str += TAB2 + "if self.parent is None:\n"
        var_str += TAB3 + class_name + '_str += "parent = None " + linesep\n'
        var_str += TAB2 + "else:\n"
        var_str += (
            TAB3
            + class_name
            + '_str += "parent = " + '
            + 'str(type(self.parent)) + " object" + linesep\n'
        )

    for ii, prop in enumerate(class_dict["properties"]):
        if prop["type"] == "str":
            # Add => < MyClass_str += 'my_var = "'+self.MyVar+'"' >to var_str
            var_str += (
                TAB2
                + class_name
                + "_str += '"
                + prop["name"]
                + ' = "'
                + "' + str(self."
                + prop["name"]
                + ") + "
                + """'"'"""
            )
        elif prop["type"] in ["int", "float", "bool", "complex", "dict"]:
            # Add => < MyClass_str += "my_var = "+str(self.my_var) >to var_str
            var_str += (
                TAB2
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = " + str(self.'
                + prop["name"]
                + ")"
            )
        elif prop["type"] in ["ndarray", "list"]:
            # For Matrix (skip a line then print the matrix)
            # Add => < MyClass_str += "my_var = "+ linesep + str(
            # self.my_var) >to var_str
            var_str += (
                TAB2
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = " + linesep + str(self.'
                + prop["name"]
                + ")"
            )
        elif is_list_pyleecan_type(prop["type"]):
            var_str += TAB2 + "if len(self." + prop["name"] + ") == 0:\n"
            var_str += TAB3 + class_name + '_str += "' + prop["name"] + ' = []"\n'
            var_str += TAB2 + "for ii in range(len(self." + prop["name"] + ")):\n"
            var_str += (
                TAB3
                + class_name
                + '_str += "'
                + prop["name"]
                + '["+str(ii)+"] = "+str(self.'
                + prop["name"]
                + '[ii].as_dict())+"\\n"'
            )
        elif is_dict_pyleecan_type(prop["type"]):
            var_str += TAB2 + "if len(self." + prop["name"] + ") == 0:\n"
            var_str += TAB3 + class_name + '_str += "' + prop["name"] + ' = dict()"\n'
            var_str += TAB2 + "for key, obj in self." + prop["name"] + ".items():\n"
            var_str += (
                TAB3
                + class_name
                + '_str += "'
                + prop["name"]
                + '["+key+"] = "+str(self.'
                + prop["name"]
                + "[key].as_dict())"
            )
        else:  # For pyleecan type print the dict (from as_dict)
            # Add => < "MyClass = "+str(self.my_var.as_dict()) >to var_str
            var_str += TAB2 + "if self." + prop["name"] + " is not None:\n"
            var_str += (
                TAB3
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = " + str(self.'
                + prop["name"]
                + ".as_dict()) + linesep + linesep\n"
            )
            var_str += TAB2 + "else:\n"
            var_str += TAB3 + class_name + '_str += "' + prop["name"] + ' = None"'

        # Add linesep except for the last line
        if ii == len(class_dict["properties"]) - 1:
            var_str += "\n"
        else:
            if prop["type"] in PYTHON_TYPE:
                var_str += " + linesep\n"
            else:  # Skip two lines for pyleecan type and ndarray
                var_str += " + linesep + linesep\n"
    # Code generation
    str_str += TAB + "def __str__(self):\n"
    str_str += (
        TAB2 + '"""Convert this objet in a readeable string ' + '(for print)"""\n\n'
    )
    str_str += TAB2 + class_name + '_str = ""\n'
    if class_dict["mother"] != "":
        str_str += (
            TAB2 + "# Get the properties inherited from " + class_dict["mother"] + "\n"
        )
        # Add => "Class_str += super(Class, self).__str__() + linesep
        str_str += (
            TAB2
            + class_name
            + "_str += super("
            + class_name
            + ", self).__str__() + linesep\n"
        )
    str_str += var_str
    str_str += TAB2 + "return " + class_name + "_str\n"

    return str_str


def generate_eq(gen_dict, class_dict):
    """Generate the code for the __eq__ method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    eq_str : str
        String containing the code for the __eq__ method of the class
    """

    class_name = class_dict["name"]
    eq_str = ""  # This string is for the generated code

    # Code generation
    eq_str += TAB + "def __eq__(self, other):\n"
    eq_str += TAB2 + '"""Compare two objects (skip parent)"""\n\n'
    # Check the type
    eq_str += TAB2 + "if type(other) != type(self):\n"
    eq_str += TAB3 + "return False\n"
    # Call mother eq
    if class_dict["mother"] != "":
        eq_str += (
            "\n"
            + TAB2
            + "# Check the properties inherited from "
            + class_dict["mother"]
            + "\n"
        )
        eq_str += TAB2 + "if not super(" + class_name + ", self).__eq__(other):\n"
        eq_str += TAB3 + "return False\n"
    # Check that all the propoperties (except parent) are equal
    for prop in class_dict["properties"]:
        if prop["type"] == "ndarray":
            eq_str += (
                TAB2
                + "if not array_equal(other."
                + prop["name"]
                + ", self."
                + prop["name"]
                + "):\n"
            )
            eq_str += TAB3 + "return False\n"
        else:
            eq_str += (
                TAB2 + "if other." + prop["name"] + " != self." + prop["name"] + ":\n"
            )
            eq_str += TAB3 + "return False\n"
    eq_str += TAB2 + "return True\n"

    return eq_str


def generate_as_dict(gen_dict, class_dict):
    """Generate the code for the as_dict method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    dict_str : str
        String containing the code for the as_dict method of the class
    """

    class_name = class_dict["name"]
    dict_str = ""  # This string is for the generated code

    var_str = ""  # For the creation of the return dict (in as_dict)

    for prop in class_dict["properties"]:
        if prop["type"] in PYTHON_TYPE:
            # Add => "class_name ["var_name"] = self.var_name" to var_str
            var_str += (
                TAB2
                + class_name
                + '_dict["'
                + prop["name"]
                + '"] = self.'
                + prop["name"]
                + "\n"
            )
        elif prop["type"] == "ndarray":
            # Add => "class_name ["var_name"] = self.var_name.tolist()" to
            # var_str
            var_str += TAB2 + "if self." + prop["name"] + " is None:\n"
            var_str += TAB3 + class_name + '_dict["' + prop["name"] + '"] = None\n'
            var_str += TAB2 + "else:\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"] = self.'
                + prop["name"]
                + ".tolist()\n"
            )
        elif is_list_pyleecan_type(prop["type"]):
            var_str += TAB2 + class_name + '_dict["' + prop["name"] + '"] = list()\n'
            var_str += TAB2 + "for obj in self." + prop["name"] + ":\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"].append(obj.as_dict())\n'
            )
        elif is_dict_pyleecan_type(prop["type"]):
            var_str += TAB2 + class_name + '_dict["' + prop["name"] + '"] = dict()\n'
            var_str += TAB2 + "for key, obj in self." + prop["name"] + ".items():\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"][key] = obj.as_dict()\n'
            )
        else:
            # Add => "class_name ["var_name"] = self.var_name.as_dict()" to
            # var_str
            var_str += TAB2 + "if self." + prop["name"] + " is None:\n"
            var_str += TAB3 + class_name + '_dict["' + prop["name"] + '"] = None\n'
            var_str += TAB2 + "else:\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"] = self.'
                + prop["name"]
                + ".as_dict()\n"
            )

    # Code generation
    dict_str += TAB + "def as_dict(self):\n"
    dict_str += (
        TAB2 + '"""Convert this objet in a json seriable dict (can '
        "be use in __init__)\n" + TAB2 + '"""\n\n'
    )
    if class_dict["mother"] != "":
        # Get the properties of the mother class (if needed)
        dict_str += (
            TAB2 + "# Get the properties inherited from " + class_dict["mother"] + "\n"
        )
        dict_str += (
            TAB2 + class_name + "_dict = super(" + class_name + ", self).as_dict()\n"
        )
    else:
        dict_str += TAB2 + class_name + "_dict = dict()\n"

    dict_str += var_str
    dict_str += (
        TAB2 + "# The class name is added to the dict for" + "deserialisation purpose\n"
    )
    if class_dict["mother"] != "":
        dict_str += TAB2 + "# Overwrite the mother class name\n"
    dict_str += TAB2 + class_name + '_dict["__class__"] = "' + class_name + '"\n'
    dict_str += TAB2 + "return " + class_name + "_dict\n"

    return dict_str


def generate_set_None(gen_dict, class_dict):
    """Generate the code for the _set_None method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    None_str : str
        String containing the code for the _set_None method of the class
    """

    class_name = class_dict["name"]
    None_str = ""  # This string is for the generated code

    # Code line to set every properties to None (except pyleecan object)
    var_str = ""

    for prop in class_dict["properties"]:
        if prop["type"] in PYTHON_TYPE or prop["type"] == "ndarray":
            var_str += TAB2 + "self." + prop["name"] + " = None\n"
        elif is_list_pyleecan_type(prop["type"]):
            var_str += TAB2 + "for obj in self." + prop["name"] + ":\n"
            var_str += TAB3 + "obj._set_None()\n"
        elif is_dict_pyleecan_type(prop["type"]):
            var_str += TAB2 + "for key, obj in self." + prop["name"] + ".items():\n"
            var_str += TAB3 + "obj._set_None()\n"
        else:  # Pyleecan type
            var_str += TAB2 + "if self." + prop["name"] + " is not None:\n"
            var_str += TAB3 + "self." + prop["name"] + "._set_None()\n"

    # Code generation
    None_str += TAB + "def _set_None(self):\n"
    None_str += (
        TAB2 + '"""Set all the properties to None (except ' + 'pyleecan object)"""\n\n'
    )
    None_str += var_str
    if class_dict["mother"] != "":
        # Get the properties of the mother class (if needed)
        None_str += (
            TAB2
            + "# Set to None the properties inherited from "
            + class_dict["mother"]
            + "\n"
        )
        None_str += TAB2 + "super(" + class_name + ", self)._set_None()\n"

    return None_str


def generate_properties(gen_dict, class_dict):
    """Generate the code for the getter and setter of the properties of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    prop_str : str
        String containing the code for the getter and setter of the properties of the class
    """

    prop_str = ""  # This string is for the generated code

    for prop in class_dict["properties"]:
        # Getter
        prop_str += TAB + "def _get_" + prop["name"] + "(self):\n"
        prop_str += TAB2 + '"""getter of ' + prop["name"] + '"""\n'
        if is_list_pyleecan_type(prop["type"]):
            # TODO: Update the parent should be done only in the setter but
            # their is an issue with .append for list of pyleecan type
            prop_str += TAB2 + "for obj in self._" + prop["name"] + ":\n"
            prop_str += TAB3 + "if obj is not None:\n"
            prop_str += TAB4 + "obj.parent = self\n"
        elif is_dict_pyleecan_type(prop["type"]):
            # TODO: Update the parent should be done only in the setter but
            # their is an issue with .append for list of pyleecan type
            prop_str += TAB2 + "for key, obj in self._" + prop["name"] + ".items():\n"
            prop_str += TAB3 + "if obj is not None:\n"
            prop_str += TAB4 + "obj.parent = self\n"
        prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"

        # Setter
        prop_str += TAB + "def _set_" + prop["name"] + "(self, value):\n"
        prop_str += TAB2 + '"""setter of ' + prop["name"] + '"""\n'
        # Convert ndarray if needed
        if prop["type"] == "ndarray":
            prop_str += TAB2 + "if type(value) is list:\n"
            prop_str += TAB3 + "try:\n"
            prop_str += TAB4 + "value = array(value)\n"
            prop_str += TAB3 + "except:\n"
            prop_str += TAB4 + "pass\n"

        # Add check_var("var_name",value, "var_type", min=var_min, max=var_max)
        prop_str += (
            TAB2 + 'check_var("' + prop["name"] + '", value, "' + prop["type"] + '"'
        )
        # Min and max are added only if needed
        if prop["type"] in ["float", "int", "ndarray"]:
            if str(prop["min"]) is not "":
                prop_str += ", Vmin=" + str(prop["min"])
            if str(prop["max"]) is not "":
                prop_str += ", Vmax=" + str(prop["max"])
        prop_str += ")\n"

        prop_str += TAB2 + "self._" + prop["name"] + " = value\n\n"
        if is_list_pyleecan_type(prop["type"]):
            # List of pyleecan type
            prop_str += TAB2 + "for obj in self._" + prop["name"] + ":\n"
            prop_str += TAB3 + "if obj is not None:\n"
            prop_str += TAB4 + "obj.parent = self\n\n"
        elif (
            prop["type"] not in PYTHON_TYPE
            and prop["type"] != "ndarray"
            and not is_dict_pyleecan_type(prop["type"])
        ):
            # pyleecan type
            prop_str += TAB2 + "if self._" + prop["name"] + " is not None:\n"
            prop_str += TAB3 + "self._" + prop["name"] + ".parent = self\n"

        # Property declaration
        # For doxygen : TODO: still needed for sphinx ?
        prop_str += TAB + "# " + prop["desc"] + "\n"
        prop_str += TAB + "# Type : " + prop["type"]
        if str(prop["min"]) is not "":
            prop_str += ", min = " + str(prop["min"])
        if str(prop["max"]) is not "":
            prop_str += ", max = " + str(prop["max"])
        prop_str += "\n"
        # Add "var_name = property(fget=_get_var_name, fset=_set_var_name,
        # doc = "this is doc")"
        if len(prop["desc"]) > 40:  # PEP8
            # Three lines definition
            prop_str += TAB + prop["name"] + " = property(\n"
            prop_str += TAB2 + "fget=_get_" + prop["name"] + ",\n"
            prop_str += TAB2 + "fset=_set_" + prop["name"] + ",\n"
            prop_str += TAB2 + 'doc=u"""' + prop["desc"] + '""",\n'
            prop_str += TAB + ")\n\n"
        elif len(prop["desc"]) + 2 * len(prop["name"]) > 25:
            prop_str += TAB + prop["name"] + " = property(\n"
            prop_str += TAB2 + "fget=_get_" + prop["name"]
            prop_str += ", fset=_set_" + prop["name"]
            prop_str += ', doc=u"""' + prop["desc"] + '"""\n'
            prop_str += TAB + ")\n\n"
        else:
            # All on one line
            prop_str += TAB + prop["name"] + " = property("
            prop_str += "fget=_get_" + prop["name"]
            prop_str += ", fset=_set_" + prop["name"]
            prop_str += ', doc=u"""' + prop["desc"] + '""")\n\n'

    return prop_str[:-2]  # Remove last \n\n


def get_mother_attr(gen_dict, class_dict, key):
    """Get the list of the key value from the class, including mother ones.
    Used to get all the properties or method of a class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    key : str
        Key to extract from the mother class(es) ("properties" or "methods")

    Returns
    -------
    (all_list, mother_list) : tuple
        all_list: List of all the "key" of the class including mother class(es) ones
        mother_list: List of the "key" from the mother class(es) only
    """
    # Load all the mother properties
    all_list = list(class_dict[key])
    mother_list = list()
    while class_dict["mother"] != "":
        class_dict = gen_dict[class_dict["mother"]]
        mother_list.extend(class_dict[key])
    all_list.extend(mother_list)
    return (all_list, mother_list)
