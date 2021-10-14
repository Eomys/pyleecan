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
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class OptiConstraint(FrozenClass):
    """Constraint of the optimization problem"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        type_const="<=",
        value=0,
        get_variable=None,
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
            if "type_const" in list(init_dict.keys()):
                type_const = init_dict["type_const"]
            if "value" in list(init_dict.keys()):
                value = init_dict["value"]
            if "get_variable" in list(init_dict.keys()):
                get_variable = init_dict["get_variable"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.type_const = type_const
        self.value = value
        self.get_variable = get_variable

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiConstraint_str = ""
        if self.parent is None:
            OptiConstraint_str += "parent = None " + linesep
        else:
            OptiConstraint_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        OptiConstraint_str += 'name = "' + str(self.name) + '"' + linesep
        OptiConstraint_str += 'type_const = "' + str(self.type_const) + '"' + linesep
        OptiConstraint_str += "value = " + str(self.value) + linesep
        if self._get_variable_str is not None:
            OptiConstraint_str += "get_variable = " + self._get_variable_str + linesep
        elif self._get_variable_func is not None:
            OptiConstraint_str += (
                "get_variable = " + str(self._get_variable_func) + linesep
            )
        else:
            OptiConstraint_str += "get_variable = None" + linesep + linesep
        return OptiConstraint_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.type_const != self.type_const:
            return False
        if other.value != self.value:
            return False
        if other._get_variable_str != self._get_variable_str:
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
        if other._type_const != self._type_const:
            diff_list.append(name + ".type_const")
        if other._value != self._value:
            diff_list.append(name + ".value")
        if other._get_variable_str != self._get_variable_str:
            diff_list.append(name + ".get_variable")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.type_const)
        S += getsizeof(self.value)
        S += getsizeof(self._get_variable_str)
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

        OptiConstraint_dict = dict()
        OptiConstraint_dict["name"] = self.name
        OptiConstraint_dict["type_const"] = self.type_const
        OptiConstraint_dict["value"] = self.value
        if self._get_variable_str is not None:
            OptiConstraint_dict["get_variable"] = self._get_variable_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiConstraint_dict["get_variable"] = self.get_variable
        else:
            OptiConstraint_dict["get_variable"] = None
            if self.get_variable is not None:
                self.get_logger().warning(
                    "OptiConstraint.as_dict(): "
                    + f"Function {self.get_variable.__name__} is not serializable "
                    + "and will be converted to None."
                )
        # The class name is added to the dict for deserialisation purpose
        OptiConstraint_dict["__class__"] = "OptiConstraint"
        return OptiConstraint_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.type_const = None
        self.value = None
        self.get_variable = None

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
        doc="""name of the design variable

        :Type: str
        """,
    )

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
        doc="""Type of comparison ( "==", "<=", ">=", "<",">")

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
        doc="""Value to compare

        :Type: float
        """,
    )

    def _get_get_variable(self):
        """getter of get_variable"""
        return self._get_variable_func

    def _set_get_variable(self, value):
        """setter of get_variable"""
        if value is None:
            self._get_variable_str = None
            self._get_variable_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._get_variable_str = value
            self._get_variable_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._get_variable_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._get_variable_func = eval(basename(value[:-3]))
        elif callable(value):
            self._get_variable_str = None
            self._get_variable_func = value
        else:
            raise CheckTypeError(
                "For property get_variable Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    get_variable = property(
        fget=_get_get_variable,
        fset=_set_get_variable,
        doc="""Function to get the variable to compare

        :Type: function
        """,
    )
