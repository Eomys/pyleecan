# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiConstraint.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiConstraint
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
from .DataKeeper import DataKeeper

from numpy import array, ndarray
from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from numpy import isnan
from ._check import InitUnKnowClassError


class OptiConstraint(DataKeeper):
    """Constraint of the optimization problem"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_const="<=",
        value=0,
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
            if "type_const" in list(init_dict.keys()):
                type_const = init_dict["type_const"]
            if "value" in list(init_dict.keys()):
                value = init_dict["value"]
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
        self.type_const = type_const
        self.value = value
        # Call DataKeeper init
        super(OptiConstraint, self).__init__(
            name=name,
            symbol=symbol,
            unit=unit,
            keeper=keeper,
            error_keeper=error_keeper,
            result=result,
            result_ref=result_ref,
            physic=physic,
        )
        # The class is frozen (in DataKeeper init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiConstraint_str = ""
        # Get the properties inherited from DataKeeper
        OptiConstraint_str += super(OptiConstraint, self).__str__()
        OptiConstraint_str += 'type_const = "' + str(self.type_const) + '"' + linesep
        OptiConstraint_str += "value = " + str(self.value) + linesep
        return OptiConstraint_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from DataKeeper
        if not super(OptiConstraint, self).__eq__(other):
            return False
        if other.type_const != self.type_const:
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

        # Check the properties inherited from DataKeeper
        diff_list.extend(
            super(OptiConstraint, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._type_const != self._type_const:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_const)
                    + ", other="
                    + str(other._type_const)
                    + ")"
                )
                diff_list.append(name + ".type_const" + val_str)
            else:
                diff_list.append(name + ".type_const")
        if (
            other._value is not None
            and self._value is not None
            and isnan(other._value)
            and isnan(self._value)
        ):
            pass
        elif other._value != self._value:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._value) + ", other=" + str(other._value) + ")"
                )
                diff_list.append(name + ".value" + val_str)
            else:
                diff_list.append(name + ".value")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from DataKeeper
        S += super(OptiConstraint, self).__sizeof__()
        S += getsizeof(self.type_const)
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

        # Get the properties inherited from DataKeeper
        OptiConstraint_dict = super(OptiConstraint, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OptiConstraint_dict["type_const"] = self.type_const
        OptiConstraint_dict["value"] = self.value
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiConstraint_dict["__class__"] = "OptiConstraint"
        return OptiConstraint_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_const_val = self.type_const
        value_val = self.value
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
            type_const=type_const_val,
            value=value_val,
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

        self.type_const = None
        self.value = None
        # Set to None the properties inherited from DataKeeper
        super(OptiConstraint, self)._set_None()

    def _get_type_const(self):
        """getter of type_const"""
        return self._type_const

    def _set_type_const(self, value):
        """setter of type_const"""
        check_var("type_const", value, "str")
        self._type_const = value

    type_const = property(
        fget=_get_type_const,
        fset=_set_type_const,
        doc=u"""Type of comparison ( "==", "<=", ">=", "<",">")

        :Type: str
        """,
    )

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        check_var("value", value, "float")
        self._value = value

    value = property(
        fget=_get_value,
        fset=_set_value,
        doc=u"""Value to compare

        :Type: float
        """,
    )
