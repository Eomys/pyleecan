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

    def __init__(
        self,
        airgap=None,
        per_a=None,
        machine_polar_eq=None,
        antiper_a=None,
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
            if "airgap" in list(init_dict.keys()):
                airgap = init_dict["airgap"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "machine_polar_eq" in list(init_dict.keys()):
                machine_polar_eq = init_dict["machine_polar_eq"]
            if "antiper_a" in list(init_dict.keys()):
                antiper_a = init_dict["antiper_a"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.airgap = airgap
        self.per_a = per_a
        self.machine_polar_eq = machine_polar_eq
        self.antiper_a = antiper_a

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
        SubdomainModel_str += "per_a = " + str(self.per_a) + linesep
        if self.machine_polar_eq is not None:
            tmp = (
                self.machine_polar_eq.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            SubdomainModel_str += "machine_polar_eq = " + tmp
        else:
            SubdomainModel_str += "machine_polar_eq = None" + linesep + linesep
        SubdomainModel_str += "antiper_a = " + str(self.antiper_a) + linesep
        return SubdomainModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.airgap != self.airgap:
            return False
        if other.per_a != self.per_a:
            return False
        if other.machine_polar_eq != self.machine_polar_eq:
            return False
        if other.antiper_a != self.antiper_a:
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
        if other._per_a != self._per_a:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_a) + ", other=" + str(other._per_a) + ")"
                )
                diff_list.append(name + ".per_a" + val_str)
            else:
                diff_list.append(name + ".per_a")
        if (other.machine_polar_eq is None and self.machine_polar_eq is not None) or (
            other.machine_polar_eq is not None and self.machine_polar_eq is None
        ):
            diff_list.append(name + ".machine_polar_eq None mismatch")
        elif self.machine_polar_eq is not None:
            diff_list.extend(
                self.machine_polar_eq.compare(
                    other.machine_polar_eq,
                    name=name + ".machine_polar_eq",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._antiper_a != self._antiper_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._antiper_a)
                    + ", other="
                    + str(other._antiper_a)
                    + ")"
                )
                diff_list.append(name + ".antiper_a" + val_str)
            else:
                diff_list.append(name + ".antiper_a")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.airgap)
        S += getsizeof(self.per_a)
        S += getsizeof(self.machine_polar_eq)
        S += getsizeof(self.antiper_a)
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
        SubdomainModel_dict["per_a"] = self.per_a
        if self.machine_polar_eq is None:
            SubdomainModel_dict["machine_polar_eq"] = None
        else:
            SubdomainModel_dict["machine_polar_eq"] = self.machine_polar_eq.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        SubdomainModel_dict["antiper_a"] = self.antiper_a
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
        per_a_val = self.per_a
        if self.machine_polar_eq is None:
            machine_polar_eq_val = None
        else:
            machine_polar_eq_val = self.machine_polar_eq.copy()
        antiper_a_val = self.antiper_a
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            airgap=airgap_val,
            per_a=per_a_val,
            machine_polar_eq=machine_polar_eq_val,
            antiper_a=antiper_a_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.airgap is not None:
            self.airgap._set_None()
        self.per_a = None
        if self.machine_polar_eq is not None:
            self.machine_polar_eq._set_None()
        self.antiper_a = None

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
            Subdomain_Airgap = import_class(
                "pyleecan.Classes", "Subdomain_Airgap", "airgap"
            )
            value = Subdomain_Airgap()
        check_var("airgap", value, "Subdomain_Airgap")
        self._airgap = value

        if self._airgap is not None:
            self._airgap.parent = self

    airgap = property(
        fget=_get_airgap,
        fset=_set_airgap,
        doc=u"""Airgap subdomain

        :Type: Subdomain_Airgap
        """,
    )

    def _get_per_a(self):
        """getter of per_a"""
        return self._per_a

    def _set_per_a(self, value):
        """setter of per_a"""
        check_var("per_a", value, "int", Vmin=1)
        self._per_a = value

    per_a = property(
        fget=_get_per_a,
        fset=_set_per_a,
        doc=u"""Spatial periodicity factor

        :Type: int
        :min: 1
        """,
    )

    def _get_machine_polar_eq(self):
        """getter of machine_polar_eq"""
        return self._machine_polar_eq

    def _set_machine_polar_eq(self, value):
        """setter of machine_polar_eq"""
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
                "pyleecan.Classes", value.get("__class__"), "machine_polar_eq"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Machine = import_class("pyleecan.Classes", "Machine", "machine_polar_eq")
            value = Machine()
        check_var("machine_polar_eq", value, "Machine")
        self._machine_polar_eq = value

        if self._machine_polar_eq is not None:
            self._machine_polar_eq.parent = self

    machine_polar_eq = property(
        fget=_get_machine_polar_eq,
        fset=_set_machine_polar_eq,
        doc=u"""Polar equivalent of machine

        :Type: Machine
        """,
    )

    def _get_antiper_a(self):
        """getter of antiper_a"""
        return self._antiper_a

    def _set_antiper_a(self, value):
        """setter of antiper_a"""
        check_var("antiper_a", value, "int", Vmin=1)
        self._antiper_a = value

    antiper_a = property(
        fget=_get_antiper_a,
        fset=_set_antiper_a,
        doc=u"""Spatial anti-periodicity factor

        :Type: int
        :min: 1
        """,
    )
