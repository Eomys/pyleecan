# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/GUI_Option/GUIOption.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Unit import Unit


class GUIOption(FrozenClass):

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, unit=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if unit == -1:
            unit = Unit()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["unit"])
            # Overwrite default value with init_dict content
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
        # Initialisation by argument
        self.parent = None
        # unit can be None, a Unit object or a dict
        if isinstance(unit, dict):
            self.unit = Unit(init_dict=unit)
        else:
            self.unit = unit

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        GUIOption_str = ""
        if self.parent is None:
            GUIOption_str += "parent = None " + linesep
        else:
            GUIOption_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.unit is not None:
            GUIOption_str += "unit = " + str(self.unit.as_dict()) + linesep + linesep
        else:
            GUIOption_str += "unit = None"
        return GUIOption_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.unit != self.unit:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        GUIOption_dict = dict()
        if self.unit is None:
            GUIOption_dict["unit"] = None
        else:
            GUIOption_dict["unit"] = self.unit.as_dict()
        # The class name is added to the dict fordeserialisation purpose
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
        check_var("unit", value, "Unit")
        self._unit = value

        if self._unit is not None:
            self._unit.parent = self

    # Unit options
    # Type : Unit
    unit = property(fget=_get_unit, fset=_set_unit, doc=u"""Unit options""")
