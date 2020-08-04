# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Optimization/OptiObjFunc.csv
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


class OptiObjFunc(FrozenClass):
    """Optimization"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, name="", symbol="", unit="", func=None, init_dict=None, init_str=None
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            name = obj.name
            symbol = obj.symbol
            unit = obj.unit
            func = obj.func
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "func" in list(init_dict.keys()):
                func = init_dict["func"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.symbol = symbol
        self.unit = unit
        self.func = func

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiObjFunc_str = ""
        if self.parent is None:
            OptiObjFunc_str += "parent = None " + linesep
        else:
            OptiObjFunc_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        OptiObjFunc_str += 'name = "' + str(self.name) + '"' + linesep
        OptiObjFunc_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        OptiObjFunc_str += 'unit = "' + str(self.unit) + '"' + linesep
        if self._func[1] is None:
            OptiObjFunc_str += "func = " + str(self._func[1])
        else:
            OptiObjFunc_str += (
                "func = " + linesep + str(self._func[1]) + linesep + linesep
            )
        return OptiObjFunc_str

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
        if other.func != self.func:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiObjFunc_dict = dict()
        OptiObjFunc_dict["name"] = self.name
        OptiObjFunc_dict["symbol"] = self.symbol
        OptiObjFunc_dict["unit"] = self.unit
        if self.func is None:
            OptiObjFunc_dict["func"] = None
        else:
            OptiObjFunc_dict["func"] = [
                dumps(self._func[0]).decode("ISO-8859-2"),
                self._func[1],
            ]
        # The class name is added to the dict fordeserialisation purpose
        OptiObjFunc_dict["__class__"] = "OptiObjFunc"
        return OptiObjFunc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.symbol = None
        self.unit = None
        self.func = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Data name
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Data name""")

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    # Data symbol
    # Type : str
    symbol = property(fget=_get_symbol, fset=_set_symbol, doc=u"""Data symbol""")

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    # Data unit
    # Type : str
    unit = property(fget=_get_unit, fset=_set_unit, doc=u"""Data unit""")

    def _get_func(self):
        """getter of func"""
        return self._func[0]

    def _set_func(self, value):
        """setter of func"""
        try:
            check_var("func", value, "list")
        except CheckTypeError:
            check_var("func", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._func = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._func = [None, None]
        elif callable(value):
            self._func = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Function to minimize
    # Type : function
    func = property(fget=_get_func, fset=_set_func, doc=u"""Function to minimize""")
