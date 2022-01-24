# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC
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
from .LUT import LUT
from .Drive import Drive


class EEC(FrozenClass):
    """Equivalent Electrical Circuit abstract class"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        parameters=None,
        LUT_enforced=None,
        drive=None,
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
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "LUT_enforced" in list(init_dict.keys()):
                LUT_enforced = init_dict["LUT_enforced"]
            if "drive" in list(init_dict.keys()):
                drive = init_dict["drive"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.parameters = parameters
        self.LUT_enforced = LUT_enforced
        self.drive = drive

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_str = ""
        if self.parent is None:
            EEC_str += "parent = None " + linesep
        else:
            EEC_str += "parent = " + str(type(self.parent)) + " object" + linesep
        EEC_str += "parameters = " + str(self.parameters) + linesep
        if self.LUT_enforced is not None:
            tmp = (
                self.LUT_enforced.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            EEC_str += "LUT_enforced = " + tmp
        else:
            EEC_str += "LUT_enforced = None" + linesep + linesep
        if self.drive is not None:
            tmp = self.drive.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_str += "drive = " + tmp
        else:
            EEC_str += "drive = None" + linesep + linesep
        return EEC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.parameters != self.parameters:
            return False
        if other.LUT_enforced != self.LUT_enforced:
            return False
        if other.drive != self.drive:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._parameters != self._parameters:
            diff_list.append(name + ".parameters")
        if (other.LUT_enforced is None and self.LUT_enforced is not None) or (
            other.LUT_enforced is not None and self.LUT_enforced is None
        ):
            diff_list.append(name + ".LUT_enforced None mismatch")
        elif self.LUT_enforced is not None:
            diff_list.extend(
                self.LUT_enforced.compare(
                    other.LUT_enforced, name=name + ".LUT_enforced"
                )
            )
        if (other.drive is None and self.drive is not None) or (
            other.drive is not None and self.drive is None
        ):
            diff_list.append(name + ".drive None mismatch")
        elif self.drive is not None:
            diff_list.extend(self.drive.compare(other.drive, name=name + ".drive"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.parameters is not None:
            for key, value in self.parameters.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.LUT_enforced)
        S += getsizeof(self.drive)
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

        EEC_dict = dict()
        EEC_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        if self.LUT_enforced is None:
            EEC_dict["LUT_enforced"] = None
        else:
            EEC_dict["LUT_enforced"] = self.LUT_enforced.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.drive is None:
            EEC_dict["drive"] = None
        else:
            EEC_dict["drive"] = self.drive.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        EEC_dict["__class__"] = "EEC"
        return EEC_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.parameters = None
        if self.LUT_enforced is not None:
            self.LUT_enforced._set_None()
        if self.drive is not None:
            self.drive._set_None()

    def _get_parameters(self):
        """getter of parameters"""
        return self._parameters

    def _set_parameters(self, value):
        """setter of parameters"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("parameters", value, "dict")
        self._parameters = value

    parameters = property(
        fget=_get_parameters,
        fset=_set_parameters,
        doc=u"""Parameters of the EEC: computed if empty, or enforced

        :Type: dict
        """,
    )

    def _get_LUT_enforced(self):
        """getter of LUT_enforced"""
        return self._LUT_enforced

    def _set_LUT_enforced(self, value):
        """setter of LUT_enforced"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "LUT_enforced"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = LUT()
        check_var("LUT_enforced", value, "LUT")
        self._LUT_enforced = value

        if self._LUT_enforced is not None:
            self._LUT_enforced.parent = self

    LUT_enforced = property(
        fget=_get_LUT_enforced,
        fset=_set_LUT_enforced,
        doc=u"""Electrical Look Up Table to be enforced 

        :Type: LUT
        """,
    )

    def _get_drive(self):
        """getter of drive"""
        return self._drive

    def _set_drive(self, value):
        """setter of drive"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "drive"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Drive()
        check_var("drive", value, "Drive")
        self._drive = value

        if self._drive is not None:
            self._drive.parent = self

    drive = property(
        fget=_get_drive,
        fset=_set_drive,
        doc=u"""Drive

        :Type: Drive
        """,
    )
