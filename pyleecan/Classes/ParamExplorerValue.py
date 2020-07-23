# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/ParamExplorerValue.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .ParamExplorer import ParamExplorer

from numpy import array, array_equal
from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class ParamExplorerValue(ParamExplorer):
    """Abstract class for the multi-simulation"""

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
        self,
        value=[],
        name="",
        symbol="",
        unit="",
        setter=None,
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
            value = obj.value
            name = obj.name
            symbol = obj.symbol
            unit = obj.unit
            setter = obj.setter
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
        # Initialisation by argument
        # value can be None, a ndarray or a list
        set_array(self, "value", value)
        # Call ParamExplorer init
        super(ParamExplorerValue, self).__init__(
            name=name, symbol=symbol, unit=unit, setter=setter
        )
        # The class is frozen (in ParamExplorer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ParamExplorerValue_str = ""
        # Get the properties inherited from ParamExplorer
        ParamExplorerValue_str += super(ParamExplorerValue, self).__str__()
        ParamExplorerValue_str += (
            "value = "
            + linesep
            + str(self.value).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ParamExplorerValue_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ParamExplorer
        if not super(ParamExplorerValue, self).__eq__(other):
            return False
        if not array_equal(other.value, self.value):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ParamExplorer
        ParamExplorerValue_dict = super(ParamExplorerValue, self).as_dict()
        if self.value is None:
            ParamExplorerValue_dict["value"] = None
        else:
            ParamExplorerValue_dict["value"] = self.value.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ParamExplorerValue_dict["__class__"] = "ParamExplorerValue"
        return ParamExplorerValue_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.value = None
        # Set to None the properties inherited from ParamExplorer
        super(ParamExplorerValue, self)._set_None()

    def _get_value(self):
        """getter of value"""
        return self._value

    def _set_value(self, value):
        """setter of value"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("value", value, "ndarray")
        self._value = value

    # List containing the different parameter values to explore
    # Type : ndarray
    value = property(
        fget=_get_value,
        fset=_set_value,
        doc=u"""List containing the different parameter values to explore""",
    )
