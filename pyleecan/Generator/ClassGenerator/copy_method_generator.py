from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type
from ...Generator.ClassGenerator.init_method_generator import get_mother_attr

T1 = "\n" + TAB
T2 = "\n" + TAB2
T3 = "\n" + TAB3
T4 = "\n" + TAB4
T5 = "\n" + TAB5
T6 = "\n" + TAB6
T7 = "\n" + TAB7


def generate_copy(gen_dict, class_dict):
    """Generate the code for the copy method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        dictionary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    copy_str : str
        String containing the code for the copy method of the class
    """

    # Load all the properties including mother ones
    (all_properties, mother_prop_list) = get_mother_attr(
        gen_dict, class_dict, "properties"
    )

    var_str = ""  # For the copy code of each property
    for prop_dict in all_properties:
        prop = prop_dict["name"]
        prop_type = prop_dict["type"]
        if "as_dict" in prop_dict and prop_dict["as_dict"] == "1":
            # Property set to None both in as_dict and copy
            var_str += T2 + prop + "_val = None"
        elif "as_dict" in prop_dict and prop_dict["as_dict"] == "2":
            # Property set to None in as_dict and pointer in copy
            var_str += T2 + prop + "_val = self." + prop
        elif prop_type in list(set(PYTHON_TYPE) - set(["dict", "list"])):
            var_str += T2 + prop + "_val = self." + prop
        elif prop_type in ["ndarray", "list", "dict"]:
            var_str += T2 + "if self." + prop + " is None:"
            var_str += T3 + prop + "_val = None"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = self." + prop + ".copy()"
        elif prop_type in ["[ndarray]", "{ndarray}"]:
            var_str += T2 + "if self." + prop + " is None:"
            var_str += T3 + prop + "_val = None"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = deepcopy(self." + prop + ")"
        elif prop_type in [None, ""]:
            var_str += T2 + "if hasattr(self." + prop + ", 'copy'):"
            var_str += T3 + prop + "_val = self." + prop + ".copy()"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = self." + prop
        elif is_list_pyleecan_type(prop_type):
            var_str += T2 + "if self." + prop + " is None:"
            var_str += T3 + prop + "_val = None"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = list()"
            var_str += T3 + "for obj in self." + prop + ":"
            var_str += T4 + prop + "_val.append(obj.copy())"
        elif is_dict_pyleecan_type(prop_type):
            var_str += T2 + "if self." + prop + " is None:"
            var_str += T3 + prop + "_val = None"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = dict()"
            var_str += T3 + "for key, obj in self." + prop + ".items():"
            var_str += T4 + prop + "_val[key] = obj.copy()"
        elif prop_type == "function":
            var_str += T2 + "if self._" + prop + "_str is not None:"
            var_str += T3 + prop + "_val = self._" + prop + "_str"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = self._" + prop + "_func"
        else:  # SciDataTool or pyleecan type
            var_str += T2 + "if self." + prop + " is None:"
            var_str += T3 + prop + "_val = None"
            var_str += T2 + "else:"
            var_str += T3 + prop + "_val = self." + prop + ".copy()"

    # Code generation
    copy_str = ""  # This string is for the all generated code
    copy_str += T1 + "def copy(self):"
    copy_str += T2 + '"""Creates a deepcopy of the object"""\n'
    copy_str += T2 + "# Handle deepcopy of all the properties"
    copy_str += var_str
    copy_str += T2 + "# Creates new object of the same type with the copied properties"
    copy_str += T2 + "obj_copy = type(self)("
    for prop_dict in all_properties:
        copy_str += prop_dict["name"] + "=" + prop_dict["name"] + "_val,"
    if len(all_properties) > 0:
        copy_str = copy_str[:-1]  # Remove last comma
    copy_str += ")"
    copy_str += T2 + "return obj_copy\n"

    return copy_str
