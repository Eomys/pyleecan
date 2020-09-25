from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type


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
        ## Getter
        # Write the getter only if it is not user defined
        if "_get_" + prop["name"] not in class_dict["methods"]:
            prop_str += TAB + "def _get_" + prop["name"] + "(self):\n"
            prop_str += TAB2 + '"""getter of ' + prop["name"] + '"""\n'
            if is_list_pyleecan_type(prop["type"]):
                # TODO: Update the parent should be done only in the setter but
                # their is an issue with .append for list of pyleecan type
                prop_str += TAB2 + "for obj in self._" + prop["name"] + ":\n"
                prop_str += TAB3 + "if obj is not None:\n"
                prop_str += TAB4 + "obj.parent = self\n"
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"
            elif is_dict_pyleecan_type(prop["type"]) and prop["type"] != "{ndarray}":
                # TODO: Update the parent should be done only in the setter but
                # their is an issue with .append for list of pyleecan type
                prop_str += (
                    TAB2 + "for key, obj in self._" + prop["name"] + ".items():\n"
                )
                prop_str += TAB3 + "if obj is not None:\n"
                prop_str += TAB4 + "obj.parent = self\n"
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"
            elif prop["type"] == "function":
                prop_str += TAB2 + "return self._" + prop["name"] + "[0]\n\n"
            else:
                prop_str += TAB2 + "return self._" + prop["name"] + "\n\n"

        ## Setter
        # Write the setter only if it is not user defined
        if "_set_" + prop["name"] not in class_dict["methods"]:
            prop_str += generate_prop_setter(gen_dict, class_dict, prop)

        ## For sphinx doc
        desc_str = '"""' + prop["desc"] + "\n\n"
        desc_str += TAB2 + ":Type: " + prop["type"] + "\n"
        if str(prop["min"]) is not "":
            desc_str += TAB2 + ":min: " + str(prop["min"]) + "\n"
        if str(prop["max"]) is not "":
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


def generate_prop_setter(gen_dict, class_dict, prop):
    """Generate the code for the getter and setter of the properties of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)
    prop_dict: dict
        Dictionnary of the property to generate the setter

    Returns
    -------
    set_str : str
        String containing the code for the setter of the property of the class
    """
    set_str = ""
    set_str += TAB + "def _set_" + prop["name"] + "(self, value):\n"
    set_str += TAB2 + '"""setter of ' + prop["name"] + '"""\n'

    ## Convertion to correct type
    if prop["type"] == "ndarray":
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = list()\n"
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
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif prop["type"] == "[ndarray]":
        set_str += TAB2 + "if type(value) is list:\n"
        set_str += TAB3 + "for ii, obj in enumerate(value):\n"
        set_str += TAB4 + "if type(obj) is list:\n"
        set_str += TAB5 + "try:\n"
        set_str += TAB6 + "value[ii] = array(obj)\n"
        set_str += TAB5 + "except:\n"
        set_str += TAB6 + "pass\n"
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif prop["type"] == "dict":
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif prop["type"] == "list":
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif prop["type"] == "ImportMatrix":
        set_str += TAB2 + "if isinstance(value, str):  # Load from file\n"
        set_str += TAB3 + "value = load_init_dict(value)[1]\n"
        set_str += TAB2 + "if isinstance(value,ndarray):\n"
        set_str += TAB3 + "value = ImportMatrixVal(value=value)\n"
        set_str += TAB2 + "elif isinstance(value,list):\n"
        set_str += TAB3 + "value = ImportMatrixVal(value=array(value))\n"
        set_str += TAB2 + "elif value is -1:\n"
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
        set_str += TAB4 + "if type(obj) is dict:\n"
        if "SciDataTool" in prop["type"]:
            set_str += (
                TAB5
                + "class_obj = import_class('SciDataTool.Classes.'+obj.get('__class__'), obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        else:
            set_str += (
                TAB5
                + "class_obj = import_class('pyleecan.Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        set_str += TAB5 + "value[key] = class_obj(init_dict=obj)\n"
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = dict()\n"
    elif is_list_pyleecan_type(prop["type"]):
        set_str += TAB2 + "if type(value) is list:\n"
        set_str += TAB3 + "for ii, obj in enumerate(value):\n"
        set_str += TAB4 + "if type(obj) is dict:\n"
        if "SciDataTool" in prop["type"]:
            set_str += (
                TAB5
                + "class_obj = import_class('SciDataTool.Classes.'+obj.get('__class__'), obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        else:
            set_str += (
                TAB5
                + "class_obj = import_class('pyleecan.Classes', obj.get('__class__'), '"
                + prop["name"]
                + "')\n"
            )
        set_str += TAB5 + "value[ii] = class_obj(init_dict=obj)\n"
        set_str += TAB2 + "if value is -1:\n"
        set_str += TAB3 + "value = list()\n"
    elif "." not in prop["type"] and prop["type"] not in PYTHON_TYPE:  # pyleecan Type
        set_str += TAB2 + "if isinstance(value, str):  # Load from file\n"
        set_str += TAB3 + "value = load_init_dict(value)[1]\n"
        set_str += TAB2 + "if isinstance(value, dict) and '__class__' in value:\n"
        set_str += (
            TAB3
            + "class_obj = import_class('pyleecan.Classes', value.get('__class__'), '"
            + prop["name"]
            + "')\n"
        )
        set_str += TAB3 + "value = class_obj(init_dict=value)\n"
        set_str += TAB2 + "elif value is -1:  # Default constructor\n"
        set_str += TAB3 + "value = " + prop["type"] + "()\n"

    ## Add check_var("var_name",value, "var_type", min=var_min, max=var_max)
    if prop["type"] == "function":
        # A function can be defined by a callable or a list containing the serialized callable and its sourcecode
        set_str += TAB2 + "try:\n"
        set_str += TAB3 + 'check_var("' + prop["name"] + '", value, "list")\n'
        set_str += TAB2 + "except CheckTypeError:\n"
        set_str += (
            TAB3 + 'check_var("' + prop["name"] + '", value, "' + prop["type"] + '")\n'
        )
        set_str += TAB2 + "if isinstance(value,list): # Load function from saved dict\n"
        set_str += (
            TAB3
            + "self._"
            + prop["name"]
            + " = [loads(value[0].encode('ISO-8859-2')),value[1]]\n"
        )
        set_str += TAB2 + "elif value is None:\n"
        set_str += TAB3 + "self._" + prop["name"] + " = [None,None]\n"
        set_str += TAB2 + "elif callable(value):\n"
        set_str += TAB3 + "self._" + prop["name"] + " = [value,getsource(value)]\n"
        set_str += TAB2 + "else:\n"
        set_str += (
            TAB3
            + "raise TypeError('Expected function or list from a saved file, got: '+str(type(value))) \n"
        )

    elif "." in prop["type"] and not prop["type"].endswith(
        "]"
    ):  # Import from another package
        set_str += TAB2 + "try: # Check the type \n"
        set_str += TAB3 + 'check_var("' + prop["name"] + '", value, "dict")\n'
        set_str += TAB2 + "except CheckTypeError:\n"
        set_str += (
            TAB3 + 'check_var("' + prop["name"] + '", value, "' + prop["type"] + '")\n'
        )
        set_str += TAB3 + "# property can be set from a list to handle loads\n"
        set_str += (
            TAB2
            + 'if type(value) == dict: # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]\n'
        )
        set_str += (
            TAB3
            + "self._"
            + prop["name"]
            + " = loads(value[\"serialized\"].encode('ISO-8859-2'))\n"
        )
        set_str += TAB2 + "else: \n"
        set_str += TAB3 + "self._" + prop["name"] + "= value \n"

    elif "." in prop["type"]:  # List of type from external package
        set_str += (
            TAB2
            + 'if isinstance(value, dict): # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)] \n'
        )
        set_str += TAB3 + "value = loads(value[\"serialized\"].encode('ISO-8859-2'))\n"
        set_str += TAB2 + "elif value == None:\n"
        set_str += TAB3 + "value = []\n"
        set_str += TAB2 + 'check_var("' + prop["name"] + '", value, "list")\n'
        set_str += TAB2 + "for i, element in enumerate(value):\n"
        set_str += (
            TAB3
            + 'check_var("'
            + prop["name"]
            + '[{}]".format(i), element, "'
            + prop["type"][1:-1]
            + '")\n'
        )
        set_str += TAB2 + "self._" + prop["name"] + "= value \n"
    else:
        set_str += (
            TAB2 + 'check_var("' + prop["name"] + '", value, "' + prop["type"] + '"'
        )
        # Min and max are added only if needed
        if prop["type"] in ["float", "int", "ndarray"]:
            if str(prop["min"]) is not "":
                set_str += ", Vmin=" + str(prop["min"])
            if str(prop["max"]) is not "":
                set_str += ", Vmax=" + str(prop["max"])
        set_str += ")\n"
        set_str += TAB2 + "self._" + prop["name"] + " = value\n\n"

    ## Update Parent
    if is_list_pyleecan_type(prop["type"]):
        # List of pyleecan type
        set_str += TAB2 + "for obj in self._" + prop["name"] + ":\n"
        set_str += TAB3 + "if obj is not None:\n"
        set_str += TAB4 + "obj.parent = self\n\n"
    elif (
        prop["type"] not in PYTHON_TYPE
        and prop["type"] not in ["ndarray", "function", "{ndarray}"]
        and not is_dict_pyleecan_type(prop["type"])
        and "." not in prop["type"]
    ):
        # pyleecan type
        set_str += TAB2 + "if self._" + prop["name"] + " is not None:\n"
        set_str += TAB3 + "self._" + prop["name"] + ".parent = self\n"

    return set_str
