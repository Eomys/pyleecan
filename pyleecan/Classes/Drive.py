# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Drive.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Drive
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


class Drive(FrozenClass):
    """Abstract Drive class"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Umax=800, Imax=800, is_current=False, init_dict=None, init_str=None
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
            if "Umax" in list(init_dict.keys()):
                Umax = init_dict["Umax"]
            if "Imax" in list(init_dict.keys()):
                Imax = init_dict["Imax"]
            if "is_current" in list(init_dict.keys()):
                is_current = init_dict["is_current"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Umax = Umax
        self.Imax = Imax
        self.is_current = is_current

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Drive_str = ""
        if self.parent is None:
            Drive_str += "parent = None " + linesep
        else:
            Drive_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Drive_str += "Umax = " + str(self.Umax) + linesep
        Drive_str += "Imax = " + str(self.Imax) + linesep
        Drive_str += "is_current = " + str(self.is_current) + linesep
        return Drive_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Umax != self.Umax:
            return False
        if other.Imax != self.Imax:
            return False
        if other.is_current != self.is_current:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Umax != self._Umax:
            diff_list.append(name + ".Umax")
        if other._Imax != self._Imax:
            diff_list.append(name + ".Imax")
        if other._is_current != self._is_current:
            diff_list.append(name + ".is_current")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Umax)
        S += getsizeof(self.Imax)
        S += getsizeof(self.is_current)
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

        Drive_dict = dict()
        Drive_dict["Umax"] = self.Umax
        Drive_dict["Imax"] = self.Imax
        Drive_dict["is_current"] = self.is_current
        # The class name is added to the dict for deserialisation purpose
        Drive_dict["__class__"] = "Drive"
        return Drive_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Umax = None
        self.Imax = None
        self.is_current = None

    def _get_Umax(self):
        """getter of Umax"""
        return self._Umax

    def _set_Umax(self, value):
        """setter of Umax"""
        check_var("Umax", value, "float", Vmin=0)
        self._Umax = value

    Umax = property(
        fget=_get_Umax,
        fset=_set_Umax,
        doc=u"""Maximum RMS voltage of the Drive

        :Type: float
        :min: 0
        """,
    )

    def _get_Imax(self):
        """getter of Imax"""
        return self._Imax

    def _set_Imax(self, value):
        """setter of Imax"""
        check_var("Imax", value, "float", Vmin=0)
        self._Imax = value

    Imax = property(
        fget=_get_Imax,
        fset=_set_Imax,
        doc=u"""Maximum RMS current of the Drive

        :Type: float
        :min: 0
        """,
    )

    def _get_is_current(self):
        """getter of is_current"""
        return self._is_current

    def _set_is_current(self, value):
        """setter of is_current"""
        check_var("is_current", value, "bool")
        self._is_current = value

    is_current = property(
        fget=_get_is_current,
        fset=_set_is_current,
        doc=u"""True to generate current waveform, False for voltage

        :Type: bool
        """,
    )
