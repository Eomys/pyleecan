from ...Generator import TAB, TAB2, TAB3, TAB4, TAB5


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
        elif prop["type"] == "[ndarray]":
            eq_str += (
                TAB2
                + "if other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None:\n"
            )
            eq_str += TAB3 + "return False\n"
            eq_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            eq_str += TAB3 + "return False\n"
            eq_str += TAB2 + "else:\n"
            eq_str += TAB3 + "for ii in range(len(other." + prop["name"] + ")):\n"
            eq_str += (
                TAB4
                + "if not array_equal(other."
                + prop["name"]
                + "[ii], self."
                + prop["name"]
                + "[ii]):\n"
            )
            eq_str += TAB5 + "return False\n"
        elif prop["type"] == "{ndarray}":
            eq_str += (
                TAB2
                + "if other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None:\n"
            )
            eq_str += TAB3 + "return False\n"
            eq_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            eq_str += TAB3 + "return False\n"
            eq_str += TAB2 + "else:\n"
            eq_str += TAB3 + "for key in other." + prop["name"] + ":\n"
            eq_str += (
                TAB4
                + "if key not in self."
                + prop["name"]
                + " or not array_equal(other."
                + prop["name"]
                + "[key], self."
                + prop["name"]
                + "[key]):\n"
            )
            eq_str += TAB5 + "return False\n"
        elif prop["type"] == "function":
            eq_str += (
                TAB2
                + "if other._"
                + prop["name"]
                + "_str != self._"
                + prop["name"]
                + "_str:\n"
            )
            eq_str += TAB3 + "return False\n"
        else:
            eq_str += (
                TAB2 + "if other." + prop["name"] + " != self." + prop["name"] + ":\n"
            )
            eq_str += TAB3 + "return False\n"
    eq_str += TAB2 + "return True\n"

    return eq_str
