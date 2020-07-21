# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/ParamSetter.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ParamSetter._set_setter import _set_setter
except ImportError as error:
    _set_setter = error


from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class ParamSetter(FrozenClass):
    """Abstract class for the multi-simulation"""

    VERSION = 1

    # cf Methods.Simulation.ParamSetter._set_setter
    if isinstance(_set_setter, ImportError):
        _set_setter = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ParamSetter method _set_setter: " + str(_set_setter)
                )
            )
        )
    else:
        _set_setter = _set_setter
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
        self,
        name="",
        symbol="",
        unit="",
        setter=None,
        value_list=[],
        init_dict=None,
        init_str=None,
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
            setter = obj.setter
            value_list = obj.value_list
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
            if "value_list" in list(init_dict.keys()):
                value_list = init_dict["value_list"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.symbol = symbol
        self.unit = unit
        self.setter = setter
        self.value_list = value_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ParamSetter_str = ""
        if self.parent is None:
            ParamSetter_str += "parent = None " + linesep
        else:
            ParamSetter_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        ParamSetter_str += 'name = "' + str(self.name) + '"' + linesep
        ParamSetter_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        ParamSetter_str += 'unit = "' + str(self.unit) + '"' + linesep
        if self._setter[1] is None:
            ParamSetter_str += "setter = " + str(self._setter[1])
        else:
            ParamSetter_str += (
                "setter = " + linesep + str(self._setter[1]) + linesep + linesep
            )
        ParamSetter_str += (
            "value_list = "
            + linesep
            + str(self.value_list).replace(linesep, linesep + "\t")
            + linesep
        )
        return ParamSetter_str

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
        if other.setter != self.setter:
            return False
        if other.value_list != self.value_list:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        ParamSetter_dict = dict()
        ParamSetter_dict["name"] = self.name
        ParamSetter_dict["symbol"] = self.symbol
        ParamSetter_dict["unit"] = self.unit
        if self.setter is None:
            ParamSetter_dict["setter"] = None
        else:
            ParamSetter_dict["setter"] = [
                dumps(self._setter[0]).decode("ISO-8859-2"),
                self._setter[1],
            ]
        ParamSetter_dict["value_list"] = self.value_list
        # The class name is added to the dict fordeserialisation purpose
        ParamSetter_dict["__class__"] = "ParamSetter"
        return ParamSetter_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.symbol = None
        self.unit = None
        self.setter = None
        self.value_list = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Parameter name
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Parameter name""")

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    # Parameter symbol
    # Type : str
    symbol = property(fget=_get_symbol, fset=_set_symbol, doc=u"""Parameter symbol""")

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    # Parameter unit
    # Type : str
    unit = property(fget=_get_unit, fset=_set_unit, doc=u"""Parameter unit""")

    def _get_setter(self):
        """getter of setter"""
        return self._setter[0]

    # Function that takes a Simulation and a value in argument and modifiers the simulation
    # Type : function
    setter = property(
        fget=_get_setter,
        fset=_set_setter,
        doc=u"""Function that takes a Simulation and a value in argument and modifiers the simulation""",
    )

    def _get_value_list(self):
        """getter of value_list"""
        return self._value_list

    def _set_value_list(self, value):
        """setter of value_list"""
        check_var("value_list", value, "list")
        self._value_list = value

    # List containing the different parameter values to explore
    # Type : list
    value_list = property(
        fget=_get_value_list,
        fset=_set_value_list,
        doc=u"""List containing the different parameter values to explore""",
    )
