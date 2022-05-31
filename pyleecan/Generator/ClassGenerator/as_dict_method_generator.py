from ...Generator import PYTHON_TYPE, TAB, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7
from ...Generator.read_fct import (
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
    is_list_unknow_type,
)

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
        dictionary of the class to generate (keys are name, package, properties, methods...)

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
        if "as_dict" in prop_dict and prop_dict["as_dict"] == "1":
            # Property set to None both in as_dict and copy
            var_str += T2 + cls + "_dict['" + prop + "'] = None"
        elif "as_dict" in prop_dict and prop_dict["as_dict"] == "2":
            # Property set to None both in as_dict and pointer in copy
            var_str += T2 + cls + "_dict['" + prop + "'] = None"
        elif prop_type in list(set(PYTHON_TYPE) - set(["dict", "list", "complex"])):
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
        elif prop_type in [None, ""]:
            var_str += _get_no_type_str(cls, prop)
        elif is_list_pyleecan_type(prop_type):
            var_str += _get_list_of_pyleecan_str(cls, prop, prop_type)
        elif is_list_unknow_type(prop_type):
            var_str += _get_list_of_unknow_str(cls, prop, prop_type)
        elif is_dict_pyleecan_type(prop_type):
            var_str += _get_dict_of_pyleecan_str(cls, prop, prop_type)
        elif prop_type == "function":
            var_str += _get_function_str(cls, prop)
        elif "." in prop_type and not "SciDataTool" in prop_type:
            var_str += _get_ext_package_str(cls, prop)
        else:
            var_str += _get_pyleecan_type_str(cls, prop, prop_type)

    # Code generation
    dict_str += (
        T1 + "def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):"
    )
    dict_str += (
        T2
        + '"""'
        + T2
        + "Convert this object in a json serializable dict (can be use in __init__)."
        + T2
        + "type_handle_ndarray: int"
        + T3
        + "How to handle ndarray (0: tolist, 1: copy, 2: nothing)"
        + T2
        + "keep_function : bool"
        + T3
        + "True to keep the function object, else return str"
        + T2
        + "Optional keyword input parameter is for internal use only "
        + T2
        + "and may prevent json serializability."
        + T2
        + '"""\n'
    )
    if cls_mother != "":
        # Get the properties of the mother class (if needed)
        dict_str += T2 + f"# Get the properties inherited from {cls_mother}"
        dict_str += (
            T2
            + f"{cls}_dict = super({cls}, self).as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)"
        )
    else:
        dict_str += T2 + f"{cls}_dict = dict()"

    dict_str += var_str
    dict_str += T2 + "# The class name is added to the dict for deserialisation purpose"
    if cls_mother != "":
        dict_str += T2 + "# Overwrite the mother class name"

    dict_str += T2 + f'{cls}_dict["__class__"] = "{cls}"'
    dict_str += T2 + f"return {cls}_dict\n"

    return dict_str


def _get_pyleecan_type_str(cls, prop, prop_type):
    # Add => "cls ["var_name"] = self.var_name.as_dict()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + "else:"

    var_str += (
        T3
        + f'{cls}_dict["{prop}"] = self.{prop}.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)'
    )
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
    var_str += T2 + f'elif "keep_function" in kwargs and kwargs["keep_function"]:'
    var_str += T3 + f'{cls}_dict["{prop}"] = self.{prop}'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T3 + f"if self.{prop} is not None:"
    var_str += T4 + f"self.get_logger().warning("
    var_str += (
        T5
        + f'"{cls}.as_dict(): " +'
        + f'f"Function {{self.{prop}.__name__}} is not serializable " + '
        + '"and will be converted to None."'
    )
    var_str += T4 + ")"
    return var_str


def _get_dict_of_pyleecan_str(cls, prop, prop_type):
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = dict()'
    var_str += T3 + f"for key, obj in self.{prop}.items():"
    var_str += T4 + f"if obj is not None:"
    var_str += (
        T5
        + f'{cls}_dict["{prop}"][key] = obj.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)'
    )
    var_str += T4 + f"else:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = None'
    return var_str


def _get_list_of_pyleecan_str(cls, prop, prop_type):
    var_str = ""
    var_str += T2 + "if self." + prop + " is None:"
    var_str += T3 + cls + "_dict['" + prop + "'] = None"
    var_str += T2 + "else:"
    var_str += T3 + cls + "_dict['" + prop + "'] = list()"
    var_str += T3 + "for obj in self." + prop + ":"
    var_str += T4 + "if obj is not None:"
    var_str += (
        T5
        + cls
        + "_dict['"
        + prop
        + "'].append(obj.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs))"
    )
    var_str += T4 + "else:"
    var_str += T5 + cls + "_dict['" + prop + "'].append(None)"
    return var_str


def _get_list_of_unknow_str(cls, prop, prop_type):
    var_str = ""
    var_str += T2 + "if self." + prop + " is None:"
    var_str += T3 + cls + "_dict['" + prop + "'] = None"
    var_str += T2 + "else:"
    var_str += T3 + cls + "_dict['" + prop + "'] = list()"
    var_str += T3 + "for obj in self." + prop + ":"
    var_str += T4 + "if obj is None:"
    var_str += T5 + cls + "_dict['" + prop + "'].append(None)"
    var_str += T4 + "elif hasattr(obj, as_dict):"
    var_str += (
        T5
        + cls
        + "_dict['"
        + prop
        + "'].append(obj.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs))"
    )
    var_str += T4 + "elif isinstance(obj, ndarray):"
    var_str += T5 + cls + "_dict['" + prop + "'].append(obj.tolist())"
    var_str += T4 + "else:"
    var_str += T5 + cls + "_dict['" + prop + "'].append(obj)"

    return var_str


def _get_dict_of_ndarray_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.tolist()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = dict()'
    var_str += T3 + f"for key, obj in self.{prop}.items():"
    var_str += T4 + "if type_handle_ndarray==0:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = obj.tolist()'
    var_str += T4 + "elif type_handle_ndarray==1:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = obj.copy()'
    var_str += T4 + "elif type_handle_ndarray==2:"
    var_str += T5 + f'{cls}_dict["{prop}"][key] = obj'
    var_str += T4 + "else:"
    var_str += (
        T5
        + "raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))"
    )
    return var_str


def _get_list_of_ndarray_str(cls, prop):
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = list()'
    var_str += T3 + f"for obj in self.{prop}:"
    var_str += T4 + "if type_handle_ndarray==0:"
    var_str += T5 + f'{cls}_dict["{prop}"].append(obj.tolist())'
    var_str += T4 + "elif type_handle_ndarray==1:"
    var_str += T5 + f'{cls}_dict["{prop}"].append(obj.copy())'
    var_str += T4 + "elif type_handle_ndarray==2:"
    var_str += T5 + f'{cls}_dict["{prop}"].append(obj)'
    var_str += T4 + "else:"
    var_str += (
        T5
        + "raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))"
    )
    return var_str


def _get_ndarray_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.tolist()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + "else:"
    var_str += T3 + "if type_handle_ndarray==0:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}.tolist()'
    var_str += T3 + "elif type_handle_ndarray==1:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}.copy()'
    var_str += T3 + "elif type_handle_ndarray==2:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}'
    var_str += T3 + "else:"
    var_str += (
        T4
        + "raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))"
    )
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


def _get_no_type_str(cls, prop):
    # Add => "cls ["var_name"] = self.var_name.tolist()" to var_str
    var_str = ""
    var_str += T2 + f"if self.{prop} is None:"
    var_str += T3 + f'{cls}_dict["{prop}"] = None'
    var_str += T2 + f"elif isinstance(self.{prop}, np.ndarray):"
    var_str += T3 + "if type_handle_ndarray==0:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}.tolist()'
    var_str += T3 + "elif type_handle_ndarray==1:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}.copy()'
    var_str += T3 + "elif type_handle_ndarray==2:"
    var_str += T4 + f'{cls}_dict["{prop}"] = self.{prop}'
    var_str += T3 + "else:"
    var_str += (
        T4
        + "raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))"
    )
    var_str += T2 + f"elif hasattr(self.{prop}, 'as_dict'):"
    var_str += (
        T3
        + f'{cls}_dict["{prop}"] = self.{prop}.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)'
    )
    var_str += T2 + "else:"
    var_str += T3 + f'{cls}_dict["{prop}"] = self.{prop}'
    return var_str
