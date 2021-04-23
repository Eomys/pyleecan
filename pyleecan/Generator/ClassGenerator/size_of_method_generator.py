from ...Generator import TAB, TAB2, TAB3, TAB4, TAB5
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type


def generate_size_of(gen_dict, class_dict):
    """Generate the code for the __sizeof__ method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        Dictionnary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    so_str : str
        String containing the code for the __sizeof__ method of the class
    """

    class_name = class_dict["name"]
    so_str = ""  # This string is for the generated code

    # Code generation
    so_str += TAB + "def __sizeof__(self):\n"
    so_str += (
        TAB2
        + '"""Return the size in memory of the object (including all subobject)"""\n\n'
    )
    so_str += TAB2 + "S = 0  # Full size of the object\n"
    # Call mother eq
    if class_dict["mother"] != "":
        so_str += (
            "\n"
            + TAB2
            + "# Get size of the properties inherited from "
            + class_dict["mother"]
            + "\n"
        )

        so_str += TAB2 + "S += super(" + class_name + ", self).__sizeof__()\n"
    # Check that all the propoperties (except parent) are equal
    for prop in class_dict["properties"]:
        if prop["type"] in [
            "float",
            "int",
            "str",
            "bool",
            "complex",
            "ndarray",
            None,
            "",
        ]:
            so_str += TAB2 + "S += getsizeof(self." + prop["name"] + ")\n"
        elif prop["type"] in ["[ndarray]", "list", "tuple"] or is_list_pyleecan_type(
            prop["type"]
        ):
            so_str += TAB2 + "if self." + prop["name"] + " is not None:\n"
            so_str += TAB3 + "for value in self." + prop["name"] + ":\n"
            so_str += TAB4 + "S += getsizeof(value)\n"
        elif prop["type"] in ["{ndarray}", "dict"] or is_dict_pyleecan_type(
            prop["type"]
        ):
            so_str += TAB2 + "if self." + prop["name"] + " is not None:\n"
            so_str += TAB3 + "for key, value in self." + prop["name"] + ".items():\n"
            so_str += TAB4 + "S += getsizeof(value) + getsizeof(key)\n"
        elif prop["type"] == "function":
            so_str += TAB2 + "S += getsizeof(self._" + prop["name"] + "_str)\n"
        else:  # pyleecan type
            so_str += TAB2 + "S += getsizeof(self." + prop["name"] + ")\n"
    so_str += TAB2 + "return S\n"

    return so_str
