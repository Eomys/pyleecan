# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/DataKeeper.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/DataKeeper
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.DataKeeper._set_keeper import _set_keeper
except ImportError as error:
    _set_keeper = error


from numpy import array, ndarray
from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from numpy import isnan
from ._check import InitUnKnowClassError


class DataKeeper(FrozenClass):
    """Class for defining data to keep on a multi-simulation"""

    VERSION = 1

    # cf Methods.Simulation.DataKeeper._set_keeper
    if isinstance(_set_keeper, ImportError):
        _set_keeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use DataKeeper method _set_keeper: " + str(_set_keeper)
                )
            )
        )
    else:
        _set_keeper = _set_keeper
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        symbol="",
        unit="",
        keeper=None,
        error_keeper=None,
        result=-1,
        result_ref=None,
        physic=None,
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
            if "keeper" in list(init_dict.keys()):
                keeper = init_dict["keeper"]
            if "error_keeper" in list(init_dict.keys()):
                error_keeper = init_dict["error_keeper"]
            if "result" in list(init_dict.keys()):
                result = init_dict["result"]
            if "result_ref" in list(init_dict.keys()):
                result_ref = init_dict["result_ref"]
            if "physic" in list(init_dict.keys()):
                physic = init_dict["physic"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.symbol = symbol
        self.unit = unit
        self.keeper = keeper
        self.error_keeper = error_keeper
        self.result = result
        self.result_ref = result_ref
        self.physic = physic

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        DataKeeper_str = ""
        if self.parent is None:
            DataKeeper_str += "parent = None " + linesep
        else:
            DataKeeper_str += "parent = " + str(type(self.parent)) + " object" + linesep
        DataKeeper_str += 'name = "' + str(self.name) + '"' + linesep
        DataKeeper_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        DataKeeper_str += 'unit = "' + str(self.unit) + '"' + linesep
        if self._keeper_str is not None:
            DataKeeper_str += "keeper = " + self._keeper_str + linesep
        elif self._keeper_func is not None:
            DataKeeper_str += "keeper = " + str(self._keeper_func) + linesep
        else:
            DataKeeper_str += "keeper = None" + linesep + linesep
        if self._error_keeper_str is not None:
            DataKeeper_str += "error_keeper = " + self._error_keeper_str + linesep
        elif self._error_keeper_func is not None:
            DataKeeper_str += "error_keeper = " + str(self._error_keeper_func) + linesep
        else:
            DataKeeper_str += "error_keeper = None" + linesep + linesep
        if self.result is not None:
            tmp = self.result.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            DataKeeper_str += "result = " + tmp
        else:
            DataKeeper_str += "result = None" + linesep + linesep
        DataKeeper_str += "result_ref = " + str(self.result_ref) + linesep + linesep
        DataKeeper_str += 'physic = "' + str(self.physic) + '"' + linesep
        return DataKeeper_str

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
        if other._keeper_str != self._keeper_str:
            return False
        if other._error_keeper_str != self._error_keeper_str:
            return False
        if other.result != self.result:
            return False
        if isinstance(self.result_ref, np.ndarray) and not np.array_equal(
            other.result_ref, self.result_ref
        ):
            return False
        elif other.result_ref != self.result_ref:
            return False
        if other.physic != self.physic:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        if other._symbol != self._symbol:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._symbol)
                    + ", other="
                    + str(other._symbol)
                    + ")"
                )
                diff_list.append(name + ".symbol" + val_str)
            else:
                diff_list.append(name + ".symbol")
        if other._unit != self._unit:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._unit) + ", other=" + str(other._unit) + ")"
                )
                diff_list.append(name + ".unit" + val_str)
            else:
                diff_list.append(name + ".unit")
        if other._keeper_str != self._keeper_str:
            diff_list.append(name + ".keeper")
        if other._error_keeper_str != self._error_keeper_str:
            diff_list.append(name + ".error_keeper")
        if (other.result is None and self.result is not None) or (
            other.result is not None and self.result is None
        ):
            diff_list.append(name + ".result None mismatch")
        elif self.result is None:
            pass
        elif len(other.result) != len(self.result):
            diff_list.append("len(" + name + ".result)")
        else:
            for ii in range(len(other.result)):
                if hasattr(self.result[ii], "compare"):
                    diff_list.extend(
                        self.result[ii].compare(
                            other.result[ii],
                            name=name + ".result[" + str(ii) + "]",
                            ignore_list=ignore_list,
                            is_add_value=is_add_value,
                        )
                    )
                elif other._result[ii] != self._result[ii]:
                    diff_list.append(name + ".result[" + str(ii) + "])")
        if (other.result_ref is None and self.result_ref is not None) or (
            other.result_ref is not None and self.result_ref is None
        ):
            diff_list.append(name + ".result_ref")
        elif self.result_ref is None:
            pass
        elif isinstance(self.result_ref, np.ndarray) and not np.array_equal(
            other.result_ref, self.result_ref
        ):
            diff_list.append(name + ".result_ref")
        elif hasattr(self.result_ref, "compare"):
            diff_list.extend(
                self.result_ref.compare(
                    other.result_ref,
                    name=name + ".result_ref",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        elif other._result_ref != self._result_ref:
            diff_list.append(name + ".result_ref")
        if other._physic != self._physic:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._physic)
                    + ", other="
                    + str(other._physic)
                    + ")"
                )
                diff_list.append(name + ".physic" + val_str)
            else:
                diff_list.append(name + ".physic")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.symbol)
        S += getsizeof(self.unit)
        S += getsizeof(self._keeper_str)
        S += getsizeof(self._error_keeper_str)
        S += getsizeof(self.result)
        S += getsizeof(self.result_ref)
        S += getsizeof(self.physic)
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

        DataKeeper_dict = dict()
        DataKeeper_dict["name"] = self.name
        DataKeeper_dict["symbol"] = self.symbol
        DataKeeper_dict["unit"] = self.unit
        if self._keeper_str is not None:
            DataKeeper_dict["keeper"] = self._keeper_str
        elif keep_function:
            DataKeeper_dict["keeper"] = self.keeper
        else:
            DataKeeper_dict["keeper"] = None
            if self.keeper is not None:
                self.get_logger().warning(
                    "DataKeeper.as_dict(): "
                    + f"Function {self.keeper.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self._error_keeper_str is not None:
            DataKeeper_dict["error_keeper"] = self._error_keeper_str
        elif keep_function:
            DataKeeper_dict["error_keeper"] = self.error_keeper
        else:
            DataKeeper_dict["error_keeper"] = None
            if self.error_keeper is not None:
                self.get_logger().warning(
                    "DataKeeper.as_dict(): "
                    + f"Function {self.error_keeper.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self.result is None:
            DataKeeper_dict["result"] = None
        else:
            DataKeeper_dict["result"] = list()
            for obj in self.result:
                if obj is None:
                    DataKeeper_dict["result"].append(None)
                elif hasattr(obj, "as_dict"):
                    DataKeeper_dict["result"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs,
                        )
                    )
                elif isinstance(obj, ndarray):
                    if type_handle_ndarray == 0:
                        DataKeeper_dict["result"].append(obj.tolist())
                    elif type_handle_ndarray == 1:
                        DataKeeper_dict["result"].append(obj.copy())
                    elif type_handle_ndarray == 2:
                        DataKeeper_dict["result"].append(obj)
                else:
                    DataKeeper_dict["result"].append(obj)
        if self.result_ref is None:
            DataKeeper_dict["result_ref"] = None
        elif isinstance(self.result_ref, np.ndarray):
            if type_handle_ndarray == 0:
                DataKeeper_dict["result_ref"] = self.result_ref.tolist()
            elif type_handle_ndarray == 1:
                DataKeeper_dict["result_ref"] = self.result_ref.copy()
            elif type_handle_ndarray == 2:
                DataKeeper_dict["result_ref"] = self.result_ref
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        elif hasattr(self.result_ref, "as_dict"):
            DataKeeper_dict["result_ref"] = self.result_ref.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs,
            )
        else:
            DataKeeper_dict["result_ref"] = self.result_ref
        DataKeeper_dict["physic"] = self.physic
        # The class name is added to the dict for deserialisation purpose
        DataKeeper_dict["__class__"] = "DataKeeper"
        return DataKeeper_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        name_val = self.name
        symbol_val = self.symbol
        unit_val = self.unit
        if self._keeper_str is not None:
            keeper_val = self._keeper_str
        else:
            keeper_val = self._keeper_func
        if self._error_keeper_str is not None:
            error_keeper_val = self._error_keeper_str
        else:
            error_keeper_val = self._error_keeper_func
        if self.result is None:
            result_val = None
        else:
            result_val = self.result.copy()
        if hasattr(self.result_ref, "copy"):
            result_ref_val = self.result_ref.copy()
        else:
            result_ref_val = self.result_ref
        physic_val = self.physic
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            name=name_val,
            symbol=symbol_val,
            unit=unit_val,
            keeper=keeper_val,
            error_keeper=error_keeper_val,
            result=result_val,
            result_ref=result_ref_val,
            physic=physic_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.symbol = None
        self.unit = None
        self.keeper = None
        self.error_keeper = None
        self.result = None
        if hasattr(self.result_ref, "_set_None"):
            self.result_ref._set_None()
        else:
            self.result_ref = None
        self.physic = None

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
        doc="""Data name

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
        doc="""Data symbol

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
        doc="""Data unit

        :Type: str
        """,
    )

    def _get_keeper(self):
        """getter of keeper"""
        return self._keeper_func

    keeper = property(
        fget=_get_keeper,
        fset=_set_keeper,
        doc="""Function that takes an Output in argument and return a value

        :Type: function
        """,
    )

    def _get_error_keeper(self):
        """getter of error_keeper"""
        return self._error_keeper_func

    def _set_error_keeper(self, value):
        """setter of error_keeper"""
        if value is None:
            self._error_keeper_str = None
            self._error_keeper_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._error_keeper_str = value
            self._error_keeper_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._error_keeper_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._error_keeper_func = eval(basename(value[:-3]))
        elif callable(value):
            self._error_keeper_str = None
            self._error_keeper_func = value
        else:
            raise CheckTypeError(
                "For property error_keeper Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    error_keeper = property(
        fget=_get_error_keeper,
        fset=_set_error_keeper,
        doc="""Function that takes a Simulation in argument and returns a value, this attribute enables to handle errors and to put NaN values in the result matrices

        :Type: function
        """,
    )

    def _get_result(self):
        """getter of result"""
        return self._result

    def _set_result(self, value):
        """setter of result"""
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
                            "SciDataTool.Classes", obj.get("__class__"), "result"
                        )
                    except Exception:
                        class_obj = import_class(
                            "pyleecan.Classes", obj.get("__class__"), "result"
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
        check_var("result", value, "[]")
        self._result = value

    result = property(
        fget=_get_result,
        fset=_set_result,
        doc="""List containing datakeeper results for each simulation

        :Type: []
        """,
    )

    def _get_result_ref(self):
        """getter of result_ref"""
        return self._result_ref

    def _set_result_ref(self, value):
        """setter of result_ref"""
        if isinstance(value, dict) and "__class__" in value:
            try:
                class_obj = import_class(
                    "pyleecan.Classes", value.get("__class__"), "result_ref"
                )
            except:
                class_obj = import_class(
                    "SciDataTool.Classes", value.get("__class__"), "result_ref"
                )
            value = class_obj(init_dict=value)
        elif type(value) is list:
            try:
                value = np.array(value)
            except:
                pass
        check_var("result_ref", value, "")
        self._result_ref = value

        if hasattr(self._result_ref, "parent"):
            self._result_ref.parent = self

    result_ref = property(
        fget=_get_result_ref,
        fset=_set_result_ref,
        doc="""Result for the reference simulation

        :Type: 
        """,
    )

    def _get_physic(self):
        """getter of physic"""
        return self._physic

    def _set_physic(self, value):
        """setter of physic"""
        check_var("physic", value, "str")
        self._physic = value

    physic = property(
        fget=_get_physic,
        fset=_set_physic,
        doc="""Physic of the tracked quantity

        :Type: str
        """,
    )
