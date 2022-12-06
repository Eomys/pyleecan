from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6
from ...Generator.read_fct import (
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
    is_list_unknow_type,
)


def generate_properties(gen_dict, class_dict, soft_name="pyleecan"):
    """Generate the code for the getter and setter of the properties of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    class_dict : dict
        dictionary of the class to generate (keys are name, package, properties, methods...)
    soft_name : str
        Name of the software to generate
    Returns
    -------
    prop_str : str
        String containing the code for the getter and setter of the properties of the class
    """

    prop_str = ""  # This string is for the generated code

    for prop in class_dict["properties"]:
        ## Getter
        # Write the getter only if it is not user defined
        if "_get_" + prop["name"] not in class_dict["methods"]:
            prop_str += TAB + "def _get_" + prop["name"] + "(self):\n"
            prop_str += TAB2 + '"""getter of ' + prop["name"] + '"""\n'
            if is_list_pyleecan_type(prop["type"]):
                # TODO: Update the parent should be done only in the setter but
                # their is an issue with .append for list of pyleecan type
                prop_str += TAB2 + "if self._" + prop["name"] + " is not None:\n"
                prop_str += TAB3 + "for obj in self._" + prop["name"] + ":\n"
                prop_str += TAB4 + "if obj is not None:\n"
                prop_str += TAB5 + "obj.parent = self\n"
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"
            elif is_dict_pyleecan_type(prop["type"]) and prop["type"] != "{ndarray}":
                # TODO: Update the parent should be done only in the setter but
                # their is an issue with .append for list of pyleecan type
                prop_str += TAB2 + "if self._" + prop["name"] + " is not None:\n"
                prop_str += (
                    TAB3 + "for key, obj in self._" + prop["name"] + ".items():\n"
                )
                prop_str += TAB4 + "if obj is not None:\n"
                prop_str += TAB5 + "obj.parent = self\n"
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"
            elif prop["type"] == "function":
                prop_str += TAB2 + "return self._" + prop["name"] + "_func\n\n"
            else:
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"

        ## Setter
        # Write the setter only if it is not user defined
        if "_set_" + prop["name"] not in class_dict["methods"]:
            prop_str += generate_prop_setter(
                gen_dict, class_dict, prop, soft_name=soft_name
            )

        ## For sphinx doc
        desc_str = '"""' + prop["desc"]
        # if prop["unit"] != "":
        #     desc_str += " [" + prop["unit"] + "]"
        desc_str += "\n\n"
        desc_str += TAB2 + ":Type: " + prop["type"] + "\n"
        if str(prop["min"]):
            desc_str += TAB2 + ":min: " + str(prop["min"]) + "\n"
        if str(prop["max"]):
            desc_str += TAB2 + ":max: " + str(prop["max"]) + "\n"
        desc_str += TAB2 + '"""'

        # Add "var_name = property(fget=_get_var_name, fset=_set_var_name,
        # doc = "this is doc")"
        # Three lines definition
        prop_str += TAB + prop["name"] + " = property(\n"
        prop_str += TAB2 + "fget=_get_" + prop["name"] + ",\n"
        prop_str += TAB2 + "fset=_set_" + prop["name"] + ",\n"
        prop_str += TAB2 + "doc=u" + desc_str + ",\n"
        prop_str += TAB + ")\n\n"

    return prop_str[:-2]  # Remove last \n\n


def generate_prop_setter(gen_dict, class_dict, prop, soft_name="pyleecan"):
    """Generate the code for the getter and setter of the properties of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    class_dict : dict
        dictionary of the class to generate (keys are name, package, properties, methods...)
    prop_dict: dict
        dictionary of the property to generate the setter
    soft_name : str
        Name of the software to generate

    Returns
    -------
    set_str : str
        String containing the code for the setter of the property of the class
    """
    set_str = ""
    set_str += TAB + "def _set_" + prop["name"] + "(self, value):\n"
    set_str += TAB2 + '"""setter of ' + prop["name"] + '"""\n'

    ## Convertion to correct type
    if prop["type"] == "complex":
        set_str += TAB2 + "if isinstance(value,str):\n"
        set_str += TAB3 + "value = complex(value)\n"
    if prop["type"] == "ndarray":
        set_str += TAB2 + "if type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = array([])\n"
        set_str += TAB2 + "elif type(value) is list:\n"
        set_str += TAB3 + "try:\n"
        set_str += TAB4 + "value = array(value)\n"
        set_str += TAB3 + "except:\n"
        set_str += TAB4 + "pass\n"
    elif prop["type"] == "{ndarray}":
        set_str += TAB2 + "if type(value) is dict:\n"
        set_str += TAB3 + "for key, obj in value.items():\n"
        set_str += TAB4 + "if type(obj) is list:\n"
        set_str += TAB5 + "try:\n"
        set_str += TAB6 + "value[key] = array(obj)\n"
        set_str += TAB5 + "except:\n"
        set_str += TAB6 + "pass\n"
        set_str += TAB2 + "elif type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif prop["type"] == "[ndarray]":
        set_str += TAB2 + "if type(value) is list:\n"
        set_str += TAB3 + "for ii, obj in enumerate(value):\n"
        set_str += TAB4 + "if type(obj) is list:\n"
        set_str += TAB5 + "try:\n"
        set_str += TAB6 + "value[ii] = array(obj)\n"
        set_str += TAB5 + "except:\n"
        set_str += TAB6 + "pass\n"
        set_str += TAB2 + "elif type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = array([])\n"
    elif prop["type"] == "dict":
        set_str += TAB2 + "if type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif prop["type"] == "list":
        set_str += TAB2 + "if type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif prop["type"] == "ImportMatrix":
        set_str += (
            TAB2
            + "ImportMatrix = import_class('"
            + soft_name
            + ".Classes', 'ImportMatrix', '"
            + prop["name"]
            + "')\n"
        )
        set_str += (
            TAB2
            + "ImportMatrixVal = import_class('"
            + soft_name
            + ".Classes', 'ImportMatrixVal', '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB2 + "if isinstance(value, str):  # Load from file\n"
        set_str += TAB3 + "value = load_init_dict(value)[1]\n"
        set_str += TAB2 + "if isinstance(value,ndarray):\n"
        set_str += TAB3 + "value = ImportMatrixVal(value=value)\n"
        set_str += TAB2 + "elif isinstance(value,list):\n"
        set_str += TAB3 + "value = ImportMatrixVal(value=array(value))\n"
        set_str += TAB2 + "elif value == -1:\n"
        set_str += TAB3 + "value = ImportMatrix()\n"
        set_str += TAB2 + "elif isinstance(value,dict):\n"
        set_str += (
            TAB3
            + "class_obj = import_class('pyleecan.Classes', value.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB3 + "value = class_obj(init_dict=value)\n"
    elif is_dict_pyleecan_type(prop["type"]):
        set_str += TAB2 + "if type(value) is dict:\n"
        set_str += TAB3 + "for key, obj in value.items():\n"
        set_str += TAB4 + "if isinstance(obj, str):  # Load from file\n"
        set_str += TAB5 + "try:\n"
        set_str += TAB6 + "obj = load_init_dict(obj)[1]\n"
        set_str += TAB5 + "except Exception as e:\n"
        set_str += (
            TAB6
            + "self.get_logger().error('Error while loading '+obj+', setting None instead')\n"
        )
        set_str += TAB6 + "obj = None\n"
        set_str += TAB6 + "value[key] = None\n"
        set_str += TAB4 + "if type(obj) is dict:\n"
        if "SciDataTool" in prop["type"]:
            set_str += (
                TAB5
                + "class_obj = import_class('SciDataTool.Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        else:
            set_str += (
                TAB5
                + "class_obj = import_class('"
                + soft_name
                + ".Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        set_str += TAB5 + "value[key] = class_obj(init_dict=obj)\n"
        set_str += TAB2 + "if type(value) is int and value == -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif is_list_unknow_type(prop["type"]):
        set_str += TAB2 + "if type(value) is list:\n"
        set_str += TAB3 + "for ii, obj in enumerate(value):\n"
        set_str += TAB4 + "if isinstance(obj, str) and '.json' in obj:\n"
        set_str += TAB5 + "try:  # pyleecan object from file\n"
        set_str += TAB6 + "obj = load_init_dict(obj)[1]\n"
        set_str += TAB5 + "except Exception as e:\n"
        set_str += (
            TAB6
            + "self.get_logger().error('Error while loading '+obj+', setting None instead')\n"
        )
        set_str += TAB6 + "obj = None\n"
        set_str += TAB6 + "value[ii] = None\n"
        set_str += (
            TAB4 + "if type(obj) is dict and '__class__' in obj:  # pyleecan object\n"
        )
        set_str += TAB5 + "try:\n"
        set_str += (
            TAB6
            + "class_obj = import_class('SciDataTool.Classes', obj.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB5 + "except Exception:\n"
        set_str += (
            TAB6
            + "class_obj = import_class('"
            + soft_name
            + ".Classes', obj.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB5 + "value[ii] = class_obj(init_dict=obj)\n"
        set_str += TAB4 + "if value[ii] is not None and hasattr(value[ii], 'parent'):\n"
        set_str += TAB5 + "value[ii].parent = self\n"
        set_str += TAB4 + "if isinstance(obj, list):\n"
        set_str += TAB5 + "try:  # list to array (for list of list use 'list')\n"
        set_str += TAB6 + "value[ii] = array(obj)\n"
        set_str += TAB5 + "except Exception as e:\n"
        set_str += TAB6 + "pass\n"
        set_str += TAB2 + "if value == -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif is_list_pyleecan_type(prop["type"]):
        set_str += TAB2 + "if type(value) is list:\n"
        set_str += TAB3 + "for ii, obj in enumerate(value):\n"
        set_str += TAB4 + "if isinstance(obj, str):  # Load from file\n"
        set_str += TAB5 + "try:\n"
        set_str += TAB6 + "obj = load_init_dict(obj)[1]\n"
        set_str += TAB5 + "except Exception as e:\n"
        set_str += (
            TAB6
            + "self.get_logger().error('Error while loading '+obj+', setting None instead')\n"
        )
        set_str += TAB6 + "obj = None\n"
        set_str += TAB6 + "value[ii] = None\n"
        set_str += TAB4 + "if type(obj) is dict:\n"
        if "SciDataTool" in prop["type"]:
            set_str += (
                TAB5
                + "class_obj = import_class('SciDataTool.Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        else:
            set_str += (
                TAB5
                + "class_obj = import_class('"
                + soft_name
                + ".Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        set_str += TAB5 + "value[ii] = class_obj(init_dict=obj)\n"
        set_str += TAB4 + "if value[ii] is not None:\n"
        set_str += TAB5 + "value[ii].parent = self\n"
        set_str += TAB2 + "if value == -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif prop["type"] in ["", None]:  # No type
        set_str += TAB2 + "if isinstance(value, dict) and '__class__' in value:\n"
        set_str += TAB3 + "try:\n"
        set_str += (
            TAB4
            + "class_obj = import_class('"
            + soft_name
            + ".Classes', value.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB3 + "except:\n"
        set_str += (
            TAB4
            + "class_obj = import_class('SciDataTool.Classes', value.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB3 + "value = class_obj(init_dict=value)\n"
        set_str += TAB2 + "elif type(value) is list:\n"
        set_str += TAB3 + "try:\n"
        set_str += TAB4 + "value = np.array(value)\n"
        set_str += TAB3 + "except:\n"
        set_str += TAB4 + "pass\n"
    elif (
        ("." not in prop["type"] or "SciDataTool" in prop["type"])
        and prop["type"] not in PYTHON_TYPE
        and prop["type"] != "function"
    ):  # pyleecan Type
        set_str += TAB2 + "if isinstance(value, str):  # Load from file\n"
        set_str += TAB3 + "try:\n"
        set_str += TAB4 + "value = load_init_dict(value)[1]\n"
        set_str += TAB3 + "except Exception as e:\n"
        set_str += (
            TAB4
            + "self.get_logger().error('Error while loading '+value+', setting None instead')\n"
        )
        set_str += TAB4 + "value = None\n"
        set_str += TAB2 + "if isinstance(value, dict) and '__class__' in value:\n"
        if "SciDataTool" in prop["type"]:
            set_str += (
                TAB3
                + "class_obj = import_class('SciDataTool.Classes', value.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        else:
            set_str += (
                TAB3
                + "class_obj = import_class('"
                + soft_name
                + ".Classes', value.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        set_str += TAB3 + "value = class_obj(init_dict=value)\n"
        set_str += (
            TAB2 + "elif type(value) is int and value == -1:  # Default constructor\n"
        )
        if prop["value"] is not None and "()" in prop["value"]:
            set_str += (
                TAB3
                + prop["type"]
                + " = import_class('"
                + soft_name
                + ".Classes', '"
                + prop["type"]
                + "', '"
                + prop["name"]
                + "')\n"
            )
            set_str += TAB3 + "value = " + prop["value"] + "\n"
        elif "SciDataTool" in prop["type"]:
            set_str += TAB3 + "value = " + prop["type"].split(".")[-1] + "()\n"
        else:
            set_str += (
                TAB3
                + prop["type"]
                + " = import_class('"
                + soft_name
                + ".Classes', '"
                + prop["type"]
                + "', '"
                + prop["name"]
                + "')\n"
            )
            set_str += TAB3 + "value = " + prop["type"] + "()\n"
    elif "." in prop["type"]:
        set_str += TAB2 + "if value == -1:\n"
        set_str += TAB3 + "value = " + prop["type"].split(".")[-1] + "()\n"

    ## Add check_var("var_name",value, "var_type", min=var_min, max=var_max)
    if prop["type"] == "function":
        # A function can be defined by a callable or a string containing a lambda or a path to a python file
        set_str += TAB2 + "if value is None:\n"
        set_str += TAB3 + "self._" + prop["name"] + "_str = None\n"
        set_str += TAB3 + "self._" + prop["name"] + "_func = None\n"
        set_str += TAB2 + 'elif isinstance(value, str) and "lambda" in value:\n'
        set_str += TAB3 + "self._" + prop["name"] + "_str = value\n"
        set_str += TAB3 + "self._" + prop["name"] + "_func = eval(value)\n"
        set_str += (
            TAB2
            + 'elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":\n'
        )
        set_str += TAB3 + "self._" + prop["name"] + "_str = value\n"
        set_str += TAB3 + 'f = open(value, "r")\n'
        set_str += TAB3 + "exec(f.read(), globals())\n"
        set_str += (
            TAB3 + "self._" + prop["name"] + "_func = eval(basename(value[:-3]))\n"
        )
        set_str += TAB2 + "elif callable(value):\n"
        set_str += TAB3 + "self._" + prop["name"] + "_str = None\n"
        set_str += TAB3 + "self._" + prop["name"] + "_func = value\n"
        set_str += TAB2 + "else:\n"
        set_str += TAB3 + "raise CheckTypeError(\n"
        set_str += (
            TAB4
            + '"For property '
            + prop["name"]
            + ' Expected function or str (path to python file or lambda), got: "\n'
        )
        set_str += TAB4 + "+ str(type(value))\n"
        set_str += TAB3 + ")\n\n"
    else:
        if "." in prop["type"]:
            check_type = prop["type"].split(".")[-1]
            if prop["type"][0] in ["{", "["]:
                check_type = prop["type"][0] + check_type
        else:
            check_type = prop["type"]
        set_str += (
            TAB2 + 'check_var("' + prop["name"] + '", value, "' + check_type + '"'
        )
        # Min and max are added only if needed
        if prop["type"] in ["float", "int", "ndarray"]:
            if str(prop["min"]):
                set_str += ", Vmin=" + str(prop["min"])
            if str(prop["max"]):
                set_str += ", Vmax=" + str(prop["max"])
        set_str += ")\n"
        set_str += TAB2 + "self._" + prop["name"] + " = value\n\n"

    ## Update Parent
    if prop["type"] in ["", None]:
        # No type
        set_str += TAB2 + "if hasattr(self._" + prop["name"] + ", 'parent'):\n"
        set_str += TAB3 + "self._" + prop["name"] + ".parent = self\n"
    elif (
        prop["type"] not in PYTHON_TYPE
        and prop["type"] not in ["ndarray", "function", "{ndarray}", "[ndarray]"]
        and not is_dict_pyleecan_type(prop["type"])
        and not is_list_pyleecan_type(prop["type"])
        and not is_list_unknow_type(prop["type"])
        and "." not in prop["type"]
    ):
        # pyleecan type
        set_str += TAB2 + "if self._" + prop["name"] + " is not None:\n"
        set_str += TAB3 + "self._" + prop["name"] + ".parent = self\n"

    return set_str
