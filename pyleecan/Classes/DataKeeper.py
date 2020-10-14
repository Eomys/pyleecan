# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/DataKeeper.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/DataKeeper
"""

from os import linesep
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


class DataKeeper(FrozenClass):
    """Abstract class for the multi-simulation"""

    VERSION = 1

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
        keeper=None,
        error_keeper=None,
        result=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.symbol = symbol
        self.unit = unit
        self.keeper = keeper
        self.error_keeper = error_keeper
        self.result = result

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
        DataKeeper_str += (
            "result = "
            + linesep
            + str(self.result).replace(linesep, linesep + "\t")
            + linesep
        )
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
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        DataKeeper_dict = dict()
        DataKeeper_dict["name"] = self.name
        DataKeeper_dict["symbol"] = self.symbol
        DataKeeper_dict["unit"] = self.unit
        if self._keeper_str is not None:
            DataKeeper_dict["keeper"] = self._keeper_str
        else:
            DataKeeper_dict["keeper"] = None
        if self._error_keeper_str is not None:
            DataKeeper_dict["error_keeper"] = self._error_keeper_str
        else:
            DataKeeper_dict["error_keeper"] = None
        DataKeeper_dict["result"] = (
            self.result.copy() if self.result is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        DataKeeper_dict["__class__"] = "DataKeeper"
        return DataKeeper_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.symbol = None
        self.unit = None
        self.keeper = None
        self.error_keeper = None
        self.result = None

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
        doc=u"""Data name

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
        doc=u"""Data symbol

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
        doc=u"""Data unit

        :Type: str
        """,
    )

    def _get_keeper(self):
        """getter of keeper"""
        return self._keeper_func

    def _set_keeper(self, value):
        """setter of keeper"""
        if value is None:
            self._keeper_str = None
            self._keeper_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._keeper_str = value
            self._keeper_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._keeper_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._keeper_func = eval(basename(value[:-3]))
        elif callable(value):
            self._keeper_str = None
            self._keeper_func = value
        else:
            raise CheckTypeError(
                "For property keeper Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    keeper = property(
        fget=_get_keeper,
        fset=_set_keeper,
        doc=u"""Function that takes an Output in argument and return a value

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
        doc=u"""Function that takes a Simulation in argument and returns a value, this attribute enables to handle errors and to put NaN values in the result matrices

        :Type: function
        """,
    )

    def _get_result(self):
        """getter of result"""
        return self._result

    def _set_result(self, value):
        """setter of result"""
        if type(value) is int and value == -1:
            value = list()
        check_var("result", value, "list")
        self._result = value

    result = property(
        fget=_get_result,
        fset=_set_result,
        doc=u"""List containing datakeeper results for each simulation

        :Type: list
        """,
    )
