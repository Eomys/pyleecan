# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/GUI_Option/GUIOption.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/GUIOption/GUIOption
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

from ._check import InitUnKnowClassError
from .Unit import Unit


class GUIOption(FrozenClass):

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, unit=-1, init_dict=None, init_str=None):
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
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.unit = unit

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        GUIOption_str = ""
        if self.parent is None:
            GUIOption_str += "parent = None " + linesep
        else:
            GUIOption_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.unit is not None:
            tmp = self.unit.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            GUIOption_str += "unit = " + tmp
        else:
            GUIOption_str += "unit = None" + linesep + linesep
        return GUIOption_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.unit != self.unit:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.unit)
        return S

    def as_dict(self, keep_function=False):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional input parameter 'keep_function' is for internal use only
        and may prevent json serializability.
        """

        GUIOption_dict = dict()
        if self.unit is None:
            GUIOption_dict["unit"] = None
        else:
            GUIOption_dict["unit"] = self.unit.as_dict()
        # The class name is added to the dict for deserialisation purpose
        GUIOption_dict["__class__"] = "GUIOption"
        return GUIOption_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.unit is not None:
            self.unit._set_None()

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "unit")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Unit()
        check_var("unit", value, "Unit")
        self._unit = value

        if self._unit is not None:
            self._unit.parent = self

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc=u"""Unit options

        :Type: Unit
        """,
    )
