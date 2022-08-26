# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ParamExplorerSet.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ParamExplorerSet
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .ParamExplorer import ParamExplorer

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ParamExplorerSet.get_value import get_value
except ImportError as error:
    get_value = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_min import get_min
except ImportError as error:
    get_min = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_max import get_max
except ImportError as error:
    get_max = error

try:
    from ..Methods.Simulation.ParamExplorerSet.get_N import get_N
except ImportError as error:
    get_N = error


from numpy import array, ndarray
from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from numpy import isnan
from ._check import InitUnKnowClassError


class ParamExplorerSet(ParamExplorer):
    """Define a parameter set (for parameter sweep) from a list"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ParamExplorerSet.get_value
    if isinstance(get_value, ImportError):
        get_value = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_value: " + str(get_value)
                )
            )
        )
    else:
        get_value = get_value
    # cf Methods.Simulation.ParamExplorerSet.get_min
    if isinstance(get_min, ImportError):
        get_min = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_min: " + str(get_min)
                )
            )
        )
    else:
        get_min = get_min
    # cf Methods.Simulation.ParamExplorerSet.get_max
    if isinstance(get_max, ImportError):
        get_max = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamExplorerSet method get_max: " + str(get_max)
                )
            )
        )
    else:
        get_max = get_max
    # cf Methods.Simulation.ParamExplorerSet.get_N
    if isinstance(get_N, ImportError):
        get_N = property(
            fget=lambda x: raise_(
                ImportError("Can't use ParamExplorerSet method get_N: " + str(get_N))
            )
        )
    else:
        get_N = get_N
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        value=-1,
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
            if "value" in list(init_dict.keys()):
                value = init_dict["value"]
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
        self.value = value
        # Call ParamExplorer init
        super(ParamExplorerSet, self).__init__(
            name=name, symbol=symbol, unit=unit, setter=setter, getter=getter
        )
        # The class is frozen (in ParamExplorer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ParamExplorerSet_str = ""
        # Get the properties inherited from ParamExplorer
        ParamExplorerSet_str += super(ParamExplorerSet, self).__str__()
        if self.value is not None:
            tmp = self.value.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            ParamExplorerSet_str += "value = " + tmp
        else:
            ParamExplorerSet_str += "value = None" + linesep + linesep
        return ParamExplorerSet_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ParamExplorer
        if not super(ParamExplorerSet, self).__eq__(other):
            return False
        if other.value != self.value:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ParamExplorer
        diff_list.extend(
            super(ParamExplorerSet, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.value is None and self.value is not None) or (
            other.value is not None and self.value is None
        ):
            diff_list.append(name + ".value None mismatch")
        elif self.value is None:
            pass
        elif len(other.value) != len(self.value):
            diff_list.append("len(" + name + ".value)")
        else:
            for ii in range(len(other.value)):
                if hasattr(self.value[ii], "compare"):
                    diff_list.extend(
                        self.value[ii].compare(
                            other.value[ii],
                            name=name + ".value[" + str(ii) + "]",
                            ignore_list=ignore_list,
                            is_add_value=is_add_value,
                        )
                    )
                elif other._value[ii] != self._value[ii]:
                    diff_list.append(name + ".value[" + str(ii) + "])")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ParamExplorer
        S += super(ParamExplorerSet, self).__sizeof__()
        S += getsizeof(self.value)
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

        # Get the properties inherited from ParamExplorer
        ParamExplorerSet_dict = super(ParamExplorerSet, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.value is None:
            ParamExplorerSet_dict["value"] = None
        else:
            ParamExplorerSet_dict["value"] = list()
            for obj in self.value:
                if obj is None:
                    ParamExplorerSet_dict["value"].append(None)
                elif hasattr(obj, "as_dict"):
                    ParamExplorerSet_dict["value"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                elif isinstance(obj, ndarray):
                    if type_handle_ndarray == 0:
                        ParamExplorerSet_dict["value"].append(obj.tolist())
                    elif type_handle_ndarray == 1:
                        ParamExplorerSet_dict["value"].append(obj.copy())
                    elif type_handle_ndarray == 2:
                        ParamExplorerSet_dict["value"].append(obj)
                else:
                    ParamExplorerSet_dict["value"].append(obj)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ParamExplorerSet_dict["__class__"] = "ParamExplorerSet"
        return ParamExplorerSet_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.value is None:
            value_val = None
        else:
            value_val = self.value.copy()
        name_val = self.name
        symbol_val = self.symbol
        unit_val = self.unit
        if self._setter_str is not None:
            setter_val = self._setter_str
        else:
            setter_val = self._setter_func
        if self._getter_str is not None:
            getter_val = self._getter_str
        else:
            getter_val = self._getter_func
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            value=value_val,
            name=name_val,
            symbol=symbol_val,
            unit=unit_val,
            setter=setter_val,
            getter=getter_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.value = None
        # Set to None the properties inherited from ParamExplorer
        super(ParamExplorerSet, self)._set_None()

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str) and ".json" in obj:
                    try:  # pyleecan object from file
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict and "__class__" in obj:  # pyleecan object
                    try:
                        class_obj = import_class(
                            "SciDataTool.Classes", obj.get("__class__"), "value"
                        )
                    except Exception:
                        class_obj = import_class(
                            "pyleecan.Classes", obj.get("__class__"), "value"
                        )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None and hasattr(value[ii], "parent"):
                    value[ii].parent = self
                if isinstance(obj, list):
                    try:  # list to array (for list of list use 'list')
                        value[ii] = array(obj)
                    except Exception as e:
                        pass
        if value == -1:
            value = list()
        check_var("value", value, "[]")
        self._value = value

    value = property(
        fget=_get_value,
        fset=_set_value,
        doc=u"""List containing the different parameter values to explore

        :Type: []
        """,
    )
