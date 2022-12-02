# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiDesignVarSet.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiDesignVarSet
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
from .OptiDesignVar import OptiDesignVar

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from numpy import isnan
from ._check import InitUnKnowClassError


class OptiDesignVarSet(OptiDesignVar):
    """Optimization"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        space=[0, 1],
        get_value=None,
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
            if "space" in list(init_dict.keys()):
                space = init_dict["space"]
            if "get_value" in list(init_dict.keys()):
                get_value = init_dict["get_value"]
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
        # Call OptiDesignVar init
        super(OptiDesignVarSet, self).__init__(
            space=space,
            get_value=get_value,
            name=name,
            symbol=symbol,
            unit=unit,
            setter=setter,
            getter=getter,
        )
        # The class is frozen (in OptiDesignVar init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiDesignVarSet_str = ""
        # Get the properties inherited from OptiDesignVar
        OptiDesignVarSet_str += super(OptiDesignVarSet, self).__str__()
        return OptiDesignVarSet_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiDesignVar
        if not super(OptiDesignVarSet, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiDesignVar
        diff_list.extend(
            super(OptiDesignVarSet, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiDesignVar
        S += super(OptiDesignVarSet, self).__sizeof__()
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

        # Get the properties inherited from OptiDesignVar
        OptiDesignVarSet_dict = super(OptiDesignVarSet, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiDesignVarSet_dict["__class__"] = "OptiDesignVarSet"
        return OptiDesignVarSet_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.space is None:
            space_val = None
        else:
            space_val = self.space.copy()
        if self._get_value_str is not None:
            get_value_val = self._get_value_str
        else:
            get_value_val = self._get_value_func
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
            space=space_val,
            get_value=get_value_val,
            name=name_val,
            symbol=symbol_val,
            unit=unit_val,
            setter=setter_val,
            getter=getter_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from OptiDesignVar
        super(OptiDesignVarSet, self)._set_None()
