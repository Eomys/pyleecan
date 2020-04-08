from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type


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
        elif prop["type"] == "function":
            # Add => "class_name ["var_name"] = self._var_name" to
            # var_str
            var_str += TAB2 + "if self." + prop["name"] + " is None:\n"
            var_str += TAB3 + class_name + '_dict["' + prop["name"] + '"] = None\n'
            var_str += TAB2 + "else:\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"] = [dumps(self._'
                + prop["name"]
                + "[0]).decode('ISO-8859-2'), self._"
                + prop["name"]
                + "[1]]\n"
            )
        elif "." in prop["type"]:  # Type from external package
            var_str += TAB2 + "if self." + prop["name"] + " is None:\n"
            var_str += TAB3 + class_name + '_dict["' + prop["name"] + '"] = None\n'
            var_str += (
                TAB2
                + "else: # Store serialized data (using cloudpickle) and str to read it in json save files\n"
            )
            var_str += (
                TAB3
                + class_name
                + "_dict['"
                + prop["name"]
                + '\'] ={"__class__" : str(type(self._'
                + prop["name"]
                + ")),"
                + '"__repr__":str(self._'
                + prop["name"]
                + ".__repr__()),"
                + '"serialized":dumps(self._'
                + prop["name"]
                + ").decode('ISO-8859-2')}\n"
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
        elif prop["type"] == "{ndarray}":
            var_str += TAB2 + class_name + '_dict["' + prop["name"] + '"] = dict()\n'
            var_str += TAB2 + "for key, obj in self." + prop["name"] + ".items():\n"
            var_str += (
                TAB3
                + class_name
                + '_dict["'
                + prop["name"]
                + '"][key] = obj.tolist()\n'
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
