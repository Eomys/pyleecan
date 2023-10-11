# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/SubdomainModel.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/SubdomainModel
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

from numpy import isnan
from ._check import InitUnKnowClassError


class SubdomainModel(FrozenClass):
    """Abstract class for all the Subdomain model classes"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, airgap=None, periodicity=None, init_dict=None, init_str=None):
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
            if "airgap" in list(init_dict.keys()):
                airgap = init_dict["airgap"]
            if "periodicity" in list(init_dict.keys()):
                periodicity = init_dict["periodicity"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.airgap = airgap
        self.periodicity = periodicity

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SubdomainModel_str = ""
        if self.parent is None:
            SubdomainModel_str += "parent = None " + linesep
        else:
            SubdomainModel_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if self.airgap is not None:
            tmp = self.airgap.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            SubdomainModel_str += "airgap = " + tmp
        else:
            SubdomainModel_str += "airgap = None" + linesep + linesep
        SubdomainModel_str += "periodicity = " + str(self.periodicity) + linesep
        return SubdomainModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.airgap != self.airgap:
            return False
        if other.periodicity != self.periodicity:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.airgap is None and self.airgap is not None) or (
            other.airgap is not None and self.airgap is None
        ):
            diff_list.append(name + ".airgap None mismatch")
        elif self.airgap is not None:
            diff_list.extend(
                self.airgap.compare(
                    other.airgap,
                    name=name + ".airgap",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._periodicity != self._periodicity:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._periodicity)
                    + ", other="
                    + str(other._periodicity)
                    + ")"
                )
                diff_list.append(name + ".periodicity" + val_str)
            else:
                diff_list.append(name + ".periodicity")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.airgap)
        if self.periodicity is not None:
            for key, value in self.periodicity.items():
                S += getsizeof(value) + getsizeof(key)
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

        SubdomainModel_dict = dict()
        if self.airgap is None:
            SubdomainModel_dict["airgap"] = None
        else:
            SubdomainModel_dict["airgap"] = self.airgap.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        SubdomainModel_dict["periodicity"] = (
            self.periodicity.copy() if self.periodicity is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        SubdomainModel_dict["__class__"] = "SubdomainModel"
        return SubdomainModel_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.airgap is None:
            airgap_val = None
        else:
            airgap_val = self.airgap.copy()
        if self.periodicity is None:
            periodicity_val = None
        else:
            periodicity_val = self.periodicity.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(airgap=airgap_val, periodicity=periodicity_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.airgap is not None:
            self.airgap._set_None()
        self.periodicity = None

    def _get_airgap(self):
        """getter of airgap"""
        return self._airgap

    def _set_airgap(self, value):
        """setter of airgap"""
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
                "pyleecan.Classes", value.get("__class__"), "airgap"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            SubdomainModel = import_class(
                "pyleecan.Classes", "SubdomainModel", "airgap"
            )
            value = SubdomainModel()
        check_var("airgap", value, "SubdomainModel")
        self._airgap = value

        if self._airgap is not None:
            self._airgap.parent = self

    airgap = property(
        fget=_get_airgap,
        fset=_set_airgap,
        doc=u"""Airgap subdomain

        :Type: SubdomainModel
        """,
    )

    def _get_periodicity(self):
        """getter of periodicity"""
        return self._periodicity

    def _set_periodicity(self, value):
        """setter of periodicity"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("periodicity", value, "dict")
        self._periodicity = value

    periodicity = property(
        fget=_get_periodicity,
        fset=_set_periodicity,
        doc=u"""Periodicity

        :Type: dict
        """,
    )
