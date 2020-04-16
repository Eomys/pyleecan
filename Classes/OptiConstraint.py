# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiConstraint.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class OptiConstraint(FrozenClass):
    """Constraint of the optimization problem"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, name="", type_const="<=", value=0, get_variable=None, init_dict=None
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

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
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.type_const = type_const
        self.value = value
        self.get_variable = get_variable

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
        if self._get_variable[1] is None:
            OptiConstraint_str += "get_variable = " + str(self._get_variable[1])
        else:
            OptiConstraint_str += (
                "get_variable = "
                + linesep
                + str(self._get_variable[1])
                + linesep
                + linesep
            )
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
        if other.get_variable != self.get_variable:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiConstraint_dict = dict()
        OptiConstraint_dict["name"] = self.name
        OptiConstraint_dict["type_const"] = self.type_const
        OptiConstraint_dict["value"] = self.value
        if self.get_variable is None:
            OptiConstraint_dict["get_variable"] = None
        else:
            OptiConstraint_dict["get_variable"] = [
                dumps(self._get_variable[0]).decode("ISO-8859-2"),
                self._get_variable[1],
            ]
        # The class name is added to the dict fordeserialisation purpose
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

    # name of the design variable
    # Type : str
    name = property(
        fget=_get_name, fset=_set_name, doc=u"""name of the design variable"""
    )

    def _get_type_const(self):
        """getter of type_const"""
        return self._type_const

    def _set_type_const(self, value):
        """setter of type_const"""
        check_var("type_const", value, "str")
        self._type_const = value

    # Type of comparison ( "==", "<=", ">=", "<",">")
    # Type : str
    type_const = property(
        fget=_get_type_const,
        fset=_set_type_const,
        doc=u"""Type of comparison ( "==", "<=", ">=", "<",">")""",
    )

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        check_var("value", value, "float")
        self._value = value

    # Value to compare
    # Type : float
    value = property(fget=_get_value, fset=_set_value, doc=u"""Value to compare""")

    def _get_get_variable(self):
        """getter of get_variable"""
        return self._get_variable[0]

    def _set_get_variable(self, value):
        """setter of get_variable"""
        try:
            check_var("get_variable", value, "list")
        except CheckTypeError:
            check_var("get_variable", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._get_variable = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._get_variable = [None, None]
        elif callable(value):
            self._get_variable = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Function to get the variable to compare
    # Type : function
    get_variable = property(
        fget=_get_get_variable,
        fset=_set_get_variable,
        doc=u"""Function to get the variable to compare""",
    )
