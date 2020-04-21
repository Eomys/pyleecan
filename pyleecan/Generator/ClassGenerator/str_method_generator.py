from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type


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
        elif prop["type"] == "function":
            # Add => < MyClass_str += "my_var = "+str(self._my_var) >to var_str
            var_str += TAB2 + "if self._" + prop["name"] + "[1] is None:\n"
            var_str += (
                TAB3
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = " + str(self._'
                + prop["name"]
                + "[1])\n"
            )
            var_str += TAB2 + "else:\n"
            var_str += (
                TAB3
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = " + linesep + str(self._'
                + prop["name"]
                + "[1])"
            )
        elif "." in prop["type"]:  # Imported type
            var_str += (
                TAB2
                + class_name
                + '_str += "'
                + prop["name"]
                + ' = "+ str(self.'
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
                + ').replace(linesep, linesep + "\\t")'
            )
        elif is_list_pyleecan_type(prop["type"]):
            var_str += TAB2 + "if len(self." + prop["name"] + ") == 0:\n"
            var_str += (
                TAB3 + class_name + '_str += "' + prop["name"] + ' = []" + linesep\n'
            )
            var_str += TAB2 + "for ii in range(len(self." + prop["name"] + ")):\n"
            var_str += (
                TAB3
                + "tmp = self."
                + prop["name"]
                + '[ii].__str__().replace(linesep, linesep + "\\t") + linesep\n'
            )
            var_str += (
                TAB3 + class_name + '_str += "' + prop["name"] + '["+str(ii)+"] ="+ tmp'
            )
        elif prop["type"] == "{ndarray}":
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
                + "[key])"
            )
        elif is_dict_pyleecan_type(prop["type"]):
            var_str += TAB2 + "if len(self." + prop["name"] + ") == 0:\n"
            var_str += (
                TAB3 + class_name + '_str += "' + prop["name"] + ' = dict()"+linesep\n'
            )
            var_str += TAB2 + "for key, obj in self." + prop["name"] + ".items():\n"
            var_str += (
                TAB3
                + "tmp = self."
                + prop["name"]
                + '[key].__str__().replace(linesep, linesep + "\\t")+ linesep \n'
            )
            var_str += (
                TAB3 + class_name + '_str += "' + prop["name"] + '["+key+"] ="+ tmp'
            )
        else:  # For pyleecan type print the __str__
            # Add => < "MyClass = "+str(self.my_var.as_dict()) >to var_str
            var_str += TAB2 + "if self." + prop["name"] + " is not None:\n"
            var_str += (
                TAB3
                + "tmp = self."
                + prop["name"]
                + '.__str__().replace(linesep, linesep + "\\t").rstrip("\\t")\n'
            )
            var_str += TAB3 + class_name + '_str += "' + prop["name"] + ' = "+ tmp\n'
            var_str += TAB2 + "else:\n"
            var_str += TAB3 + class_name + '_str += "' + prop["name"] + ' = None"'

        # Add linesep except for the last line
        # if ii == len(class_dict["properties"]) - 1:
        #     var_str += "\n"
        # else:
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
            TAB2 + class_name + "_str += super(" + class_name + ", self).__str__()\n"
        )
    str_str += var_str
    str_str += TAB2 + "return " + class_name + "_str\n"

    return str_str
