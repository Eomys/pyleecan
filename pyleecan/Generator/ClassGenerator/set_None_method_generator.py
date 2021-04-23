from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type


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
        if (
            prop["type"] in PYTHON_TYPE
            or prop["type"] in ["ndarray", "{ndarray}", "[ndarray]", "function"]
            or "." in prop["type"]
        ):
            var_str += TAB2 + "self." + prop["name"] + " = None\n"
        elif is_list_pyleecan_type(prop["type"]):
            var_str += TAB2 + "self." + prop["name"] + " = None\n"
        elif is_dict_pyleecan_type(prop["type"]):
            var_str += TAB2 + "self." + prop["name"] + " = None\n"
        elif prop["type"] in ["", None]:  # No type
            var_str += TAB2 + "if hasattr(self." + prop["name"] + ", '_set_None'):\n"
            var_str += TAB3 + "self." + prop["name"] + "._set_None()\n"
            var_str += TAB2 + "else:\n"
            var_str += TAB3 + "self." + prop["name"] + " = None\n"
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
    elif len(class_dict["properties"]) == 0:
        # No mother and no proprety => Nothing to do
        None_str = None_str[:-1] + TAB2 + "pass\n"

    return None_str
