# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ParamExplorer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ParamExplorer
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
    from ..Methods.Simulation.ParamExplorer._set_setter import _set_setter
except ImportError as error:
    _set_setter = error

try:
    from ..Methods.Simulation.ParamExplorer._set_getter import _set_getter
except ImportError as error:
    _set_getter = error

try:
    from ..Methods.Simulation.ParamExplorer.get_desc import get_desc
except ImportError as error:
    get_desc = error


from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class ParamExplorer(FrozenClass):
    """Abstract class for the multi-simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ParamExplorer._set_setter
    if isinstance(_set_setter, ImportError):
        _set_setter = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorer method _set_setter: " + str(_set_setter)
                )
            )
        )
    else:
        _set_setter = _set_setter
    # cf Methods.Simulation.ParamExplorer._set_getter
    if isinstance(_set_getter, ImportError):
        _set_getter = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorer method _set_getter: " + str(_set_getter)
                )
            )
        )
    else:
        _set_getter = _set_getter
    # cf Methods.Simulation.ParamExplorer.get_desc
    if isinstance(get_desc, ImportError):
        get_desc = property(
            fget=lambda x: raise_(
                ImportError("Can't use ParamExplorer method get_desc: " + str(get_desc))
            )
        )
    else:
        get_desc = get_desc
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        symbol="",
        unit="",
        setter=None,
        getter=None,
        init_dict=None,
        init_str=None,
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
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "setter" in list(init_dict.keys()):
                setter = init_dict["setter"]
            if "getter" in list(init_dict.keys()):
                getter = init_dict["getter"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.symbol = symbol
        self.unit = unit
        self.setter = setter
        self.getter = getter

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ParamExplorer_str = ""
        if self.parent is None:
            ParamExplorer_str += "parent = None " + linesep
        else:
            ParamExplorer_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        ParamExplorer_str += 'name = "' + str(self.name) + '"' + linesep
        ParamExplorer_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        ParamExplorer_str += 'unit = "' + str(self.unit) + '"' + linesep
        if self._setter_str is not None:
            ParamExplorer_str += "setter = " + self._setter_str + linesep
        elif self._setter_func is not None:
            ParamExplorer_str += "setter = " + str(self._setter_func) + linesep
        else:
            ParamExplorer_str += "setter = None" + linesep + linesep
        if self._getter_str is not None:
            ParamExplorer_str += "getter = " + self._getter_str + linesep
        elif self._getter_func is not None:
            ParamExplorer_str += "getter = " + str(self._getter_func) + linesep
        else:
            ParamExplorer_str += "getter = None" + linesep + linesep
        return ParamExplorer_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.symbol != self.symbol:
            return False
        if other.unit != self.unit:
            return False
        if other._setter_str != self._setter_str:
            return False
        if other._getter_str != self._getter_str:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name != self._name:
            diff_list.append(name + ".name")
        if other._symbol != self._symbol:
            diff_list.append(name + ".symbol")
        if other._unit != self._unit:
            diff_list.append(name + ".unit")
        if other._setter_str != self._setter_str:
            diff_list.append(name + ".setter")
        if other._getter_str != self._getter_str:
            diff_list.append(name + ".getter")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.symbol)
        S += getsizeof(self.unit)
        S += getsizeof(self._setter_str)
        S += getsizeof(self._getter_str)
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

        ParamExplorer_dict = dict()
        ParamExplorer_dict["name"] = self.name
        ParamExplorer_dict["symbol"] = self.symbol
        ParamExplorer_dict["unit"] = self.unit
        if self._setter_str is not None:
            ParamExplorer_dict["setter"] = self._setter_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            ParamExplorer_dict["setter"] = self.setter
        else:
            ParamExplorer_dict["setter"] = None
            if self.setter is not None:
                self.get_logger().warning(
                    "ParamExplorer.as_dict(): "
                    + f"Function {self.setter.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self._getter_str is not None:
            ParamExplorer_dict["getter"] = self._getter_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            ParamExplorer_dict["getter"] = self.getter
        else:
            ParamExplorer_dict["getter"] = None
            if self.getter is not None:
                self.get_logger().warning(
                    "ParamExplorer.as_dict(): "
                    + f"Function {self.getter.__name__} is not serializable "
                    + "and will be converted to None."
                )
        # The class name is added to the dict for deserialisation purpose
        ParamExplorer_dict["__class__"] = "ParamExplorer"
        return ParamExplorer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.symbol = None
        self.unit = None
        self.setter = None
        self.getter = None

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
        doc="""Parameter name

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
        doc="""Parameter symbol

        :Type: str
        """,
    )

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc="""Parameter unit

        :Type: str
        """,
    )

    def _get_setter(self):
        """getter of setter"""
        return self._setter_func

    setter = property(
        fget=_get_setter,
        fset=_set_setter,
        doc="""Function that takes a Simulation and a value in argument and modifiers the simulation

        :Type: function
        """,
    )

    def _get_getter(self):
        """getter of getter"""
        return self._getter_func

    getter = property(
        fget=_get_getter,
        fset=_set_getter,
        doc="""Function to return the reference value (simulation as argument)

        :Type: function
        """,
    )
