# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiDesignVar.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiDesignVar
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
from .ParamExplorer import ParamExplorer

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class OptiDesignVar(ParamExplorer):
    """Optimization"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_var="interval",
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
            if "type_var" in list(init_dict.keys()):
                type_var = init_dict["type_var"]
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
        self.type_var = type_var
        self.space = space
        self.get_value = get_value
        # Call ParamExplorer init
        super(OptiDesignVar, self).__init__(
            name=name, symbol=symbol, unit=unit, setter=setter, getter=getter
        )
        # The class is frozen (in ParamExplorer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiDesignVar_str = ""
        # Get the properties inherited from ParamExplorer
        OptiDesignVar_str += super(OptiDesignVar, self).__str__()
        OptiDesignVar_str += 'type_var = "' + str(self.type_var) + '"' + linesep
        OptiDesignVar_str += (
            "space = "
            + linesep
            + str(self.space).replace(linesep, linesep + "\t")
            + linesep
        )
        if self._get_value_str is not None:
            OptiDesignVar_str += "get_value = " + self._get_value_str + linesep
        elif self._get_value_func is not None:
            OptiDesignVar_str += "get_value = " + str(self._get_value_func) + linesep
        else:
            OptiDesignVar_str += "get_value = None" + linesep + linesep
        return OptiDesignVar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ParamExplorer
        if not super(OptiDesignVar, self).__eq__(other):
            return False
        if other.type_var != self.type_var:
            return False
        if other.space != self.space:
            return False
        if other._get_value_str != self._get_value_str:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ParamExplorer
        diff_list.extend(super(OptiDesignVar, self).compare(other, name=name))
        if other._type_var != self._type_var:
            diff_list.append(name + ".type_var")
        if other._space != self._space:
            diff_list.append(name + ".space")
        if other._get_value_str != self._get_value_str:
            diff_list.append(name + ".get_value")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ParamExplorer
        S += super(OptiDesignVar, self).__sizeof__()
        S += getsizeof(self.type_var)
        if self.space is not None:
            for value in self.space:
                S += getsizeof(value)
        S += getsizeof(self._get_value_str)
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
        OptiDesignVar_dict = super(OptiDesignVar, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs,
        )
        OptiDesignVar_dict["type_var"] = self.type_var
        OptiDesignVar_dict["space"] = (
            self.space.copy() if self.space is not None else None
        )
        if self._get_value_str is not None:
            OptiDesignVar_dict["get_value"] = self._get_value_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiDesignVar_dict["get_value"] = self.get_value
        else:
            OptiDesignVar_dict["get_value"] = None
            if self.get_value is not None:
                self.get_logger().warning(
                    "OptiDesignVar.as_dict(): "
                    + f"Function {self.get_value.__name__} is not serializable "
                    + "and will be converted to None."
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiDesignVar_dict["__class__"] = "OptiDesignVar"
        return OptiDesignVar_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_var = None
        self.space = None
        self.get_value = None
        # Set to None the properties inherited from ParamExplorer
        super(OptiDesignVar, self)._set_None()

    def _get_type_var(self):
        """getter of type_var"""
        return self._type_var

    def _set_type_var(self, value):
        """setter of type_var"""
        check_var("type_var", value, "str")
        self._type_var = value

    type_var = property(
        fget=_get_type_var,
        fset=_set_type_var,
        doc="""Type of the variable interval or set.

        :Type: str
        """,
    )

    def _get_space(self):
        """getter of space"""
        return self._space

    def _set_space(self, value):
        """setter of space"""
        if type(value) is int and value == -1:
            value = list()
        check_var("space", value, "list")
        self._space = value

    space = property(
        fget=_get_space,
        fset=_set_space,
        doc="""Space of the variable

        :Type: list
        """,
    )

    def _get_get_value(self):
        """getter of get_value"""
        return self._get_value_func

    def _set_get_value(self, value):
        """setter of get_value"""
        if value is None:
            self._get_value_str = None
            self._get_value_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._get_value_str = value
            self._get_value_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._get_value_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._get_value_func = eval(basename(value[:-3]))
        elif callable(value):
            self._get_value_str = None
            self._get_value_func = value
        else:
            raise CheckTypeError(
                "For property get_value Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    get_value = property(
        fget=_get_get_value,
        fset=_set_get_value,
        doc="""Function of the space to initiate the variable

        :Type: function
        """,
    )
