# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportVectorField.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportVectorField
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportVectorField.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError
from .ImportData import ImportData


class ImportVectorField(FrozenClass):
    """Abstract class for Data Import/Generation"""

    VERSION = 1

    # cf Methods.Import.ImportVectorField.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportVectorField method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, components=-1, name="", symbol="", init_dict=None, init_str=None
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "components" in list(init_dict.keys()):
                components = init_dict["components"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.components = components
        self.name = name
        self.symbol = symbol

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportVectorField_str = ""
        if self.parent is None:
            ImportVectorField_str += "parent = None " + linesep
        else:
            ImportVectorField_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if len(self.components) == 0:
            ImportVectorField_str += "components = dict()" + linesep
        for key, obj in self.components.items():
            tmp = (
                self.components[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            ImportVectorField_str += (
                "components[" + key + "] =" + tmp + linesep + linesep
            )
        ImportVectorField_str += 'name = "' + str(self.name) + '"' + linesep
        ImportVectorField_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        return ImportVectorField_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.components != self.components:
            return False
        if other.name != self.name:
            return False
        if other.symbol != self.symbol:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.components is None and self.components is not None) or (
            other.components is not None and self.components is None
        ):
            diff_list.append(name + ".components None mismatch")
        elif self.components is None:
            pass
        elif len(other.components) != len(self.components):
            diff_list.append("len(" + name + "components)")
        else:
            for key in self.components:
                diff_list.extend(
                    self.components[key].compare(
                        other.components[key], name=name + ".components"
                    )
                )
        if other._name != self._name:
            diff_list.append(name + ".name")
        if other._symbol != self._symbol:
            diff_list.append(name + ".symbol")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.components is not None:
            for key, value in self.components.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.name)
        S += getsizeof(self.symbol)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        ImportVectorField_dict = dict()
        if self.components is None:
            ImportVectorField_dict["components"] = None
        else:
            ImportVectorField_dict["components"] = dict()
            for key, obj in self.components.items():
                if obj is not None:
                    ImportVectorField_dict["components"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    ImportVectorField_dict["components"][key] = None
        ImportVectorField_dict["name"] = self.name
        ImportVectorField_dict["symbol"] = self.symbol
        # The class name is added to the dict for deserialisation purpose
        ImportVectorField_dict["__class__"] = "ImportVectorField"
        return ImportVectorField_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.components = None
        self.name = None
        self.symbol = None

    def _get_components(self):
        """getter of components"""
        if self._components is not None:
            for key, obj in self._components.items():
                if obj is not None:
                    obj.parent = self
        return self._components

    def _set_components(self, value):
        """setter of components"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "components"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("components", value, "{ImportData}")
        self._components = value

    components = property(
        fget=_get_components,
        fset=_set_components,
        doc=u"""Dict of components (e.g. {"radial": ImportData})

        :Type: {ImportData}
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the vector field

        :Type: str
        """,
    )

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    symbol = property(
        fget=_get_symbol,
        fset=_set_symbol,
        doc=u"""Symbol of the vector field

        :Type: str
        """,
    )
