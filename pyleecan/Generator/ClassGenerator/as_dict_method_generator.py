from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import is_list_pyleecan_type, is_dict_pyleecan_type

T1 = "\n" + TAB
T2 = "\n" + TAB2
T3 = "\n" + TAB3
T4 = "\n" + TAB4
T5 = "\n" + TAB5
T6 = "\n" + TAB6
T7 = "\n" + TAB7


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

    cls = class_dict["name"]
    cls_mother = class_dict["mother"]

    dict_str = ""  # This string is for the generated code
    var_str = ""  # For the creation of the return dict (in as_dict)

    for prop_dict in class_dict["properties"]:
        prop = prop_dict["name"]
        prop_type = prop_dict["type"]
        if prop_type in list(set(PYTHON_TYPE) - set(["dict", "list", "complex"])):
            var_str += _get_python_type_str(cls, prop)
        elif prop_type == "complex":
            var_str += _get_complex_str(cls, prop)
        elif prop_type in ["dict", "list"]:
            var_str += _get_list_dict_str(cls, prop)
        elif prop_type == "ndarray":
            var_str += _get_ndarray_str(cls, prop)
        elif prop_type == "[ndarray]":
            var_str += _get_list_of_ndarray_str(cls, prop)
        elif prop_type == "{ndarray}":
            var_str += _get_dict_of_ndarray_str(cls, prop)
        elif is_list_pyleecan_type(prop_type):
            var_str += _get_list_of_pyleecan_str(cls, prop)
        elif is_dict_pyleecan_type(prop_type):
            var_str += _get_dict_of_pyleecan_str(cls, prop)
        elif prop_type == "function":
            var_str += _get_function_str(cls, prop)
        elif "." in prop_type and not "SciDataTool" in prop_type:
            var_str += _get_ext_package_str(cls, prop)
        else:
            var_str += _get_else_type_str(cls, prop)

    # Code generation
    dict_str += T1 + "def as_dict(self):"
    dict_str += (
        T2
        + '"""Convert this object in a json seriable dict (can be use in __init__)"""'
        + "\n"
    )
    if cls_mother != "":
        # Get the properties of the mother class (if needed)
        dict_str += T2 + f"# Get the properties inherited from {cls_mother}"
        dict_str += T2 + f"{cls}_dict = super({cls}, self).as_dict()"
    else:
        dict_str += T2 + f"{cls}_dict = dict()"

    dict_str += var_str
    dict_str += T2 + "# The class name is added to the dict for deserialisation purpose"
    if cls_mother != "":
        dict_str += T2 + "# Overwrite the mother class name"

    dict_str += T2 + f'{cls}_dict["__class__"] = "{cls}"'
    dict_str += T2 + f"return {cls}_dict\n"

    return dict_str


def _get_else_type_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.as_dict()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + "else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = self.{prop}.as_dict()'
    return var_str


def _get_ext_package_str(cls, prop):
    # Type from external package
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f"# Store serialized data (using cloudpickle) and str"
    var_str += T3 + f"# to read it in json save files"
    var_str += T3 + f'{cls}_dict["{prop}"] ={{'
    var_str += T4 + f'"__class__": str(type(self._{prop})),'
    var_str += T4 + f'"__repr__": str(self._{prop}.__repr__()),'
    var_str += T4 + f'"serialized": dumps(self._{prop}).decode("ISO-8859-2")'
    var_str += T3 + f"}}"
    return var_str


def _get_function_str(cls, prop):
    # Add => "cls ["var_name"] = self._var_name" to var_str
    var_str = ""
    var_str += T2 + f"if self._{prop}_str is not None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = self._{prop}_str'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    return var_str


def _get_dict_of_pyleecan_str(cls, prop):
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = dict()'
    var_str += T3 + f"for key, obj in self.{prop}.items():"
    var_str += T4 + f"if obj is not None:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = obj.as_dict()'
    var_str += T4 + f"else:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = None'
    return var_str


def _get_list_of_pyleecan_str(cls, prop):
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = list()'
    var_str += T3 + f"for obj in self.{prop}:"
    var_str += T4 + f"if obj is not None:"
    var_str += T5 + f'{cls}_dict["{prop}"].append(obj.as_dict())'
    var_str += T4 + f"else:"
    var_str += T5 + f'{cls}_dict["{prop}"].append(None)'
    return var_str


def _get_dict_of_ndarray_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.tolist()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = dict()'
    var_str += T3 + f"for key, obj in self.{prop}.items():"
    var_str += T4 + f'{cls}_dict["{prop}"][key] = obj.tolist()'
    return var_str


def _get_list_of_ndarray_str(cls, prop):
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = list()'
    var_str += T3 + f"for obj in self.{prop}:"
    var_str += T4 + f'{cls}_dict["{prop}"].append(obj.tolist())'
    return var_str


def _get_ndarray_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.tolist()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = self.{prop}.tolist()'
    return var_str


def _get_list_dict_str(cls, prop):
    # Add => "cls_dict["var_name"] = self.var_name.copy()" to var_str
    var_str = ""
    var_str += T2 + f'{cls}_dict["{prop}"] = ('
    var_str += T3 + f"self.{prop}.copy() if self.{prop} is not None else None"
    var_str += T2 + ")"
    return var_str


def _get_complex_str(cls, prop):
    # complex is not json serializable so it will be converted to string
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"elif isinstance(self.{prop}, float):"
    var_str += T3 + f'{cls}_dict["{prop}"] = self.{prop}'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = str(self.{prop})'
    return var_str


def _get_python_type_str(cls, prop):
    # PYTHON_TYPE excluding list, dict and complex
    # Add => "cls ["var_name"] = self.var_name" to var_str
    var_str = T2 + f'{cls}_dict["{prop}"] = self.{prop}'
    return var_str
