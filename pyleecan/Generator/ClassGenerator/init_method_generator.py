from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import (
    get_value_str,
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
    find_import_type,
)
from ...definitions import PACKAGE_NAME


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

    # Load all the properties including mother ones
    (all_properties, mother_prop_list) = get_mother_attr(
        gen_dict, class_dict, "properties"
    )

    ################
    # Generate the __init__ argument with default value (all prop)
    arg_list = ""
    for prop in all_properties:
        # For the argument with default value
        if prop["type"] == "ndarray":
            if prop["value"] not in ["", None] and type(prop["value"]) is list:
                # Default value of ndarray are list
                arg_list += ", " + prop["name"] + "=" + str(prop["value"])
            else:
                arg_list += ", " + prop["name"] + "=None"
        elif prop["type"] == "list":
            if (
                prop["value"] not in ["", None]
                and type(prop["value"]) is list
                and len(prop["value"]) > 0
            ):
                # Default value of ndarray are list
                arg_list += ", " + prop["name"] + "=" + str(prop["value"])
            elif prop["value"] is None:
                arg_list += ", " + prop["name"] + "=None"
            else:
                arg_list += ", " + prop["name"] + "=-1"
        elif prop["type"] == "function":
            # Callable type (function or lambda function)
            arg_list += ", " + prop["name"] + "=None"
        elif "." in prop["type"]:
            # Imported type
            if prop["value"] != "":
                arg_list += ", " + prop["name"] + "=" + prop["value"]
            else:
                arg_list += ", " + prop["name"] + "=None"
        elif is_list_pyleecan_type(prop["type"]):
            # List of pyleecan type
            arg_list += ", " + prop["name"] + "=-1"
        elif prop["type"] in ["{ndarray}", "[ndarray]"]:
            # Dict of ndarray
            arg_list += ", " + prop["name"] + "=-1"
        elif is_dict_pyleecan_type(prop["type"]):
            # Dict of pyleecan type
            arg_list += ", " + prop["name"] + "=-1"
        elif prop["type"] in PYTHON_TYPE:
            # Add => ", my_var = 10" to arg_list
            arg_list += (
                ", " + prop["name"] + "=" + get_value_str(prop["value"], prop["type"])
            )
        else:  # pyleecan type
            if prop["value"] == "":
                arg_list += ", " + prop["name"] + "=-1"
            elif type(prop["value"]) is str and "()" in prop["value"]:
                # Initialization by a pyleecan class (different from default one)
                arg_list += ", " + prop["name"] + "=-1"
            else:  # Default value (most likely None)
                arg_list += (
                    ", "
                    + prop["name"]
                    + "="
                    + get_value_str(prop["value"], prop["type"])
                )

    ################
    # To overwrite the parameter from init_dict (all prop)
    init_by_dict = ""
    for prop in all_properties:
        # To overwrite the parameter from init_dict
        init_by_dict += TAB3 + 'if "' + prop["name"] + '" in list(init_dict.keys()):\n'
        init_by_dict += TAB4 + prop["name"] + ' = init_dict["' + prop["name"] + '"]\n'

    ################
    # Generate the setter part (self.a = a) (class prop only)
    setter_str = ""
    # Add the parent property only in the top mother classes
    if class_dict["mother"] == "":
        setter_str += TAB2 + "self.parent = None\n"
    for prop in class_dict["properties"]:
        # Add => "self.my_var = my_var\n" to setter_str
        setter_str += TAB2 + "self." + prop["name"] + " = " + prop["name"] + "\n"

    ##################
    # For the call to super __init__ (mother prop only)
    mother_arg_list = ""
    for prop in mother_prop_list:
        if mother_arg_list != "":  # Avoid the first coma
            # Add => ", my_var = my_var" to mother_arg_list
            mother_arg_list += ", " + prop["name"] + "=" + prop["name"]
        else:
            # Add => "my_var = my_var" to mother_arg_list
            mother_arg_list += prop["name"] + "=" + prop["name"]

    ###############
    # Code generation of init method
    init_str = ""
    ## def
    init_str += (
        TAB + "def __init__(self" + arg_list + ", init_dict = None, init_str = None):\n"
    )
    ## Docstring
    init_str += TAB2 + '"""Constructor of the class. Can be use in three ways ' ":\n"
    init_str += (
        TAB2 + "- __init__ (arg1 = 1, arg3 = 5) every parameters "
        "have name and default values\n"
    )
    init_str += TAB3 + "for pyleecan type, -1 will call the default " "constructor\n"
    init_str += (
        TAB2 + "- __init__ (init_dict = d) d must be a dictionnary "
        "with property names as keys\n"
    )
    init_str += TAB2 + "- __init__ (init_str = s) s must be a string\n"
    init_str += TAB2 + "s is the file path to load\n\n"
    init_str += TAB2 + "ndarray or list can be given for Vector and Matrix\n"
    init_str += TAB2 + 'object or dict can be given for pyleecan Object"""\n\n'
    ## init_str
    init_str += TAB2 + "if init_str is not None:  # Load from a file\n"
    init_str += TAB3 + "init_dict = load_init_dict(init_str)[1]\n"
    ## init_dict
    init_str += TAB2 + "if init_dict is not None:  # Initialisation by dict\n"
    init_str += TAB3 + "assert type(init_dict) is dict\n"
    init_str += TAB3 + "# Overwrite default value with init_dict content\n"
    init_str += init_by_dict
    ## Setter part
    init_str += (
        TAB2 + "# Set the properties (value check and convertion are done in setter)\n"
    )
    init_str += setter_str
    ## Add the call to super __init__ if needed
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
            TAB6
            + '"'
            + PACKAGE_NAME
            + '.Classes." + class_name, fromlist=[class_name]\n'
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
        class_dict_str += TAB5 + 'class_name = obj.get("__class__")\n'
        class_dict_str += TAB5 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += TAB6 + "raise InitUnKnowClassError(\n"
        class_dict_str += TAB7 + '"Unknow class name "\n'
        class_dict_str += TAB7 + "+ class_name\n"
        class_dict_str += TAB7 + '+ " in init_dict for ' + prop_name + '"\n'
        class_dict_str += TAB6 + ")\n"
        class_dict_str += TAB5 + "# Dynamic import to call the correct constructor\n"
        class_dict_str += (
            TAB5
            + 'module = __import__("'
            + PACKAGE_NAME
            + '.Classes."+class_name, fromlist=[class_name])\n'
        )
        class_dict_str += TAB5 + "class_obj = getattr(module,class_name)\n"
        class_dict_str += (
            TAB5 + "self." + prop_name + "[key] = class_obj(init_dict=obj)\n"
        )
    else:  # No daughter
        class_dict_str += (
            TAB5 + "self." + prop_name + "[key] = " + prop_type + "(init_dict=obj)\n"
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
        class_dict_str += TAB3 + "class_name = " + prop_name + '.get("__class__")\n'
        class_dict_str += TAB3 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += TAB4 + "raise InitUnKnowClassError(\n"
        class_dict_str += TAB5 + '"Unknow class name "\n'
        class_dict_str += TAB5 + "+ class_name\n"
        class_dict_str += TAB5 + '+ " in init_dict for ' + prop_name + '"\n'
        class_dict_str += TAB4 + ")\n"
        class_dict_str += TAB3 + "# Dynamic import to call the correct constructor\n"
        class_dict_str += (
            TAB3
            + 'module = __import__("'
            + PACKAGE_NAME
            + '.Classes."+class_name, fromlist=[class_name])\n'
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

    class_dict_str += TAB2 + "elif isinstance(" + prop_name + ", str):\n"
    class_dict_str += TAB3 + "from ..Functions.load import load\n"

    if len(daug_list) > 0:
        class_dict_str += TAB3 + prop_name + " = load(" + prop_name + ")\n"
        class_dict_str += (
            TAB3 + "# Check that the type is correct (including daughter)\n"
        )
        class_dict_str += TAB3 + "class_name = " + prop_name + ".__class__.__name__\n"
        class_dict_str += TAB3 + "if class_name not in " + str(daug_list) + ":\n"
        class_dict_str += TAB4 + "raise InitUnKnowClassError(\n"
        class_dict_str += TAB5 + '"Unknow class name "\n'
        class_dict_str += TAB5 + "+ class_name\n"
        class_dict_str += TAB5 + '+ " in init_dict for ' + prop_name + '"\n'
        class_dict_str += TAB4 + ")\n"
        class_dict_str += TAB3 + "self." + prop_name + "=" + prop_name + "\n"

    else:
        class_dict_str += TAB3 + "self." + prop_name + " = load(" + prop_name + ")\n"
    return class_dict_str


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
