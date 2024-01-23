# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/Convert.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/Convert
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.Convert.convert_to_other import convert_to_other
except ImportError as error:
    convert_to_other = error

try:
    from ..Methods.Converter.Convert.convert_to_P import convert_to_P
except ImportError as error:
    convert_to_P = error

try:
    from ..Methods.Converter.Convert.select_LamSlotWind_rules import (
        select_LamSlotWind_rules,
    )
except ImportError as error:
    select_LamSlotWind_rules = error

try:
    from ..Methods.Converter.Convert.select_machine_rules import select_machine_rules
except ImportError as error:
    select_machine_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_slot_rotor_rules import (
        select_slot_rotor_rules,
    )
except ImportError as error:
    select_slot_rotor_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_slot_rules import select_slot_rules
except ImportError as error:
    select_slot_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_lamination_rules import (
        select_lamination_rules,
    )
except ImportError as error:
    select_lamination_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_winding_rules import (
        select_winding_rules,
    )
except ImportError as error:
    select_winding_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_conductor_rules import (
        select_conductor_rules,
    )
except ImportError as error:
    select_conductor_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_hole_rules import select_hole_rules
except ImportError as error:
    select_hole_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_pole_rules import select_pole_rules
except ImportError as error:
    select_pole_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_magnet_rules import select_magnet_rules
except ImportError as error:
    select_magnet_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_skew_rules import select_skew_rules
except ImportError as error:
    select_skew_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_bar_rules import select_bar_rules
except ImportError as error:
    select_bar_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_duct_rules import select_duct_rules
except ImportError as error:
    select_duct_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_notch_rules import select_notch_rules
except ImportError as error:
    select_notch_rules = error

try:
    from ..Methods.Converter.Convert.Step.select_material_rules import (
        select_material_rules,
    )
except ImportError as error:
    select_material_rules = error

try:
    from ..Methods.Converter.Convert.machine_type.select_SIPMSM_rules import (
        select_SIPMSM_rules,
    )
except ImportError as error:
    select_SIPMSM_rules = error

try:
    from ..Methods.Converter.Convert.machine_type.select_IPMSM_rules import (
        select_IPMSM_rules,
    )
except ImportError as error:
    select_IPMSM_rules = error

try:
    from ..Methods.Converter.Convert.machine_type.select_SCIM_rules import (
        select_SCIM_rules,
    )
except ImportError as error:
    select_SCIM_rules = error

try:
    from ..Methods.Converter.Convert.machine_type.select_WRSM_rules import (
        select_WRSM_rules,
    )
except ImportError as error:
    select_WRSM_rules = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Convert(FrozenClass):
    """initialisation of conversion abstract"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.Convert.convert_to_other
    if isinstance(convert_to_other, ImportError):
        convert_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method convert_to_other: "
                    + str(convert_to_other)
                )
            )
        )
    else:
        convert_to_other = convert_to_other
    # cf Methods.Converter.Convert.convert_to_P
    if isinstance(convert_to_P, ImportError):
        convert_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method convert_to_P: " + str(convert_to_P)
                )
            )
        )
    else:
        convert_to_P = convert_to_P
    # cf Methods.Converter.Convert.select_LamSlotWind_rules
    if isinstance(select_LamSlotWind_rules, ImportError):
        select_LamSlotWind_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_LamSlotWind_rules: "
                    + str(select_LamSlotWind_rules)
                )
            )
        )
    else:
        select_LamSlotWind_rules = select_LamSlotWind_rules
    # cf Methods.Converter.Convert.select_machine_rules
    if isinstance(select_machine_rules, ImportError):
        select_machine_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_machine_rules: "
                    + str(select_machine_rules)
                )
            )
        )
    else:
        select_machine_rules = select_machine_rules
    # cf Methods.Converter.Convert.Step.select_slot_rotor_rules
    if isinstance(select_slot_rotor_rules, ImportError):
        select_slot_rotor_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_slot_rotor_rules: "
                    + str(select_slot_rotor_rules)
                )
            )
        )
    else:
        select_slot_rotor_rules = select_slot_rotor_rules
    # cf Methods.Converter.Convert.Step.select_slot_rules
    if isinstance(select_slot_rules, ImportError):
        select_slot_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_slot_rules: "
                    + str(select_slot_rules)
                )
            )
        )
    else:
        select_slot_rules = select_slot_rules
    # cf Methods.Converter.Convert.Step.select_lamination_rules
    if isinstance(select_lamination_rules, ImportError):
        select_lamination_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_lamination_rules: "
                    + str(select_lamination_rules)
                )
            )
        )
    else:
        select_lamination_rules = select_lamination_rules
    # cf Methods.Converter.Convert.Step.select_winding_rules
    if isinstance(select_winding_rules, ImportError):
        select_winding_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_winding_rules: "
                    + str(select_winding_rules)
                )
            )
        )
    else:
        select_winding_rules = select_winding_rules
    # cf Methods.Converter.Convert.Step.select_conductor_rules
    if isinstance(select_conductor_rules, ImportError):
        select_conductor_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_conductor_rules: "
                    + str(select_conductor_rules)
                )
            )
        )
    else:
        select_conductor_rules = select_conductor_rules
    # cf Methods.Converter.Convert.Step.select_hole_rules
    if isinstance(select_hole_rules, ImportError):
        select_hole_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_hole_rules: "
                    + str(select_hole_rules)
                )
            )
        )
    else:
        select_hole_rules = select_hole_rules
    # cf Methods.Converter.Convert.Step.select_pole_rules
    if isinstance(select_pole_rules, ImportError):
        select_pole_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_pole_rules: "
                    + str(select_pole_rules)
                )
            )
        )
    else:
        select_pole_rules = select_pole_rules
    # cf Methods.Converter.Convert.Step.select_magnet_rules
    if isinstance(select_magnet_rules, ImportError):
        select_magnet_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_magnet_rules: "
                    + str(select_magnet_rules)
                )
            )
        )
    else:
        select_magnet_rules = select_magnet_rules
    # cf Methods.Converter.Convert.Step.select_skew_rules
    if isinstance(select_skew_rules, ImportError):
        select_skew_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_skew_rules: "
                    + str(select_skew_rules)
                )
            )
        )
    else:
        select_skew_rules = select_skew_rules
    # cf Methods.Converter.Convert.Step.select_bar_rules
    if isinstance(select_bar_rules, ImportError):
        select_bar_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_bar_rules: "
                    + str(select_bar_rules)
                )
            )
        )
    else:
        select_bar_rules = select_bar_rules
    # cf Methods.Converter.Convert.Step.select_duct_rules
    if isinstance(select_duct_rules, ImportError):
        select_duct_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_duct_rules: "
                    + str(select_duct_rules)
                )
            )
        )
    else:
        select_duct_rules = select_duct_rules
    # cf Methods.Converter.Convert.Step.select_notch_rules
    if isinstance(select_notch_rules, ImportError):
        select_notch_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_notch_rules: "
                    + str(select_notch_rules)
                )
            )
        )
    else:
        select_notch_rules = select_notch_rules
    # cf Methods.Converter.Convert.Step.select_material_rules
    if isinstance(select_material_rules, ImportError):
        select_material_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_material_rules: "
                    + str(select_material_rules)
                )
            )
        )
    else:
        select_material_rules = select_material_rules
    # cf Methods.Converter.Convert.machine_type.select_SIPMSM_rules
    if isinstance(select_SIPMSM_rules, ImportError):
        select_SIPMSM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_SIPMSM_rules: "
                    + str(select_SIPMSM_rules)
                )
            )
        )
    else:
        select_SIPMSM_rules = select_SIPMSM_rules
    # cf Methods.Converter.Convert.machine_type.select_IPMSM_rules
    if isinstance(select_IPMSM_rules, ImportError):
        select_IPMSM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_IPMSM_rules: "
                    + str(select_IPMSM_rules)
                )
            )
        )
    else:
        select_IPMSM_rules = select_IPMSM_rules
    # cf Methods.Converter.Convert.machine_type.select_SCIM_rules
    if isinstance(select_SCIM_rules, ImportError):
        select_SCIM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_SCIM_rules: "
                    + str(select_SCIM_rules)
                )
            )
        )
    else:
        select_SCIM_rules = select_SCIM_rules
    # cf Methods.Converter.Convert.machine_type.select_WRSM_rules
    if isinstance(select_WRSM_rules, ImportError):
        select_WRSM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Convert method select_WRSM_rules: "
                    + str(select_WRSM_rules)
                )
            )
        )
    else:
        select_WRSM_rules = select_WRSM_rules
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        other_unit_dict=-1,
        other_dict=-1,
        machine=None,
        rules_list=-1,
        is_P_to_other=False,
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
            if "other_unit_dict" in list(init_dict.keys()):
                other_unit_dict = init_dict["other_unit_dict"]
            if "other_dict" in list(init_dict.keys()):
                other_dict = init_dict["other_dict"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "rules_list" in list(init_dict.keys()):
                rules_list = init_dict["rules_list"]
            if "is_P_to_other" in list(init_dict.keys()):
                is_P_to_other = init_dict["is_P_to_other"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.other_unit_dict = other_unit_dict
        self.other_dict = other_dict
        self.machine = machine
        self.rules_list = rules_list
        self.is_P_to_other = is_P_to_other

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Convert_str = ""
        if self.parent is None:
            Convert_str += "parent = None " + linesep
        else:
            Convert_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Convert_str += "other_unit_dict = " + str(self.other_unit_dict) + linesep
        Convert_str += "other_dict = " + str(self.other_dict) + linesep
        if self.machine is not None:
            tmp = self.machine.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Convert_str += "machine = " + tmp
        else:
            Convert_str += "machine = None" + linesep + linesep
        Convert_str += (
            "rules_list = "
            + linesep
            + str(self.rules_list).replace(linesep, linesep + "\t")
            + linesep
        )
        Convert_str += "is_P_to_other = " + str(self.is_P_to_other) + linesep
        return Convert_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.other_unit_dict != self.other_unit_dict:
            return False
        if other.other_dict != self.other_dict:
            return False
        if other.machine != self.machine:
            return False
        if other.rules_list != self.rules_list:
            return False
        if other.is_P_to_other != self.is_P_to_other:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._other_unit_dict != self._other_unit_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._other_unit_dict)
                    + ", other="
                    + str(other._other_unit_dict)
                    + ")"
                )
                diff_list.append(name + ".other_unit_dict" + val_str)
            else:
                diff_list.append(name + ".other_unit_dict")
        if other._other_dict != self._other_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._other_dict)
                    + ", other="
                    + str(other._other_dict)
                    + ")"
                )
                diff_list.append(name + ".other_dict" + val_str)
            else:
                diff_list.append(name + ".other_dict")
        if (other.machine is None and self.machine is not None) or (
            other.machine is not None and self.machine is None
        ):
            diff_list.append(name + ".machine None mismatch")
        elif self.machine is not None:
            diff_list.extend(
                self.machine.compare(
                    other.machine,
                    name=name + ".machine",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._rules_list != self._rules_list:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._rules_list)
                    + ", other="
                    + str(other._rules_list)
                    + ")"
                )
                diff_list.append(name + ".rules_list" + val_str)
            else:
                diff_list.append(name + ".rules_list")
        if other._is_P_to_other != self._is_P_to_other:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_P_to_other)
                    + ", other="
                    + str(other._is_P_to_other)
                    + ")"
                )
                diff_list.append(name + ".is_P_to_other" + val_str)
            else:
                diff_list.append(name + ".is_P_to_other")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.other_unit_dict is not None:
            for key, value in self.other_unit_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.other_dict is not None:
            for key, value in self.other_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.machine)
        if self.rules_list is not None:
            for value in self.rules_list:
                S += getsizeof(value)
        S += getsizeof(self.is_P_to_other)
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

        Convert_dict = dict()
        Convert_dict["other_unit_dict"] = (
            self.other_unit_dict.copy() if self.other_unit_dict is not None else None
        )
        Convert_dict["other_dict"] = (
            self.other_dict.copy() if self.other_dict is not None else None
        )
        if self.machine is None:
            Convert_dict["machine"] = None
        else:
            Convert_dict["machine"] = self.machine.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Convert_dict["rules_list"] = (
            self.rules_list.copy() if self.rules_list is not None else None
        )
        Convert_dict["is_P_to_other"] = self.is_P_to_other
        # The class name is added to the dict for deserialisation purpose
        Convert_dict["__class__"] = "Convert"
        return Convert_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.other_unit_dict is None:
            other_unit_dict_val = None
        else:
            other_unit_dict_val = self.other_unit_dict.copy()
        if self.other_dict is None:
            other_dict_val = None
        else:
            other_dict_val = self.other_dict.copy()
        if self.machine is None:
            machine_val = None
        else:
            machine_val = self.machine.copy()
        if self.rules_list is None:
            rules_list_val = None
        else:
            rules_list_val = self.rules_list.copy()
        is_P_to_other_val = self.is_P_to_other
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            other_unit_dict=other_unit_dict_val,
            other_dict=other_dict_val,
            machine=machine_val,
            rules_list=rules_list_val,
            is_P_to_other=is_P_to_other_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.other_unit_dict = None
        self.other_dict = None
        if self.machine is not None:
            self.machine._set_None()
        self.rules_list = None
        self.is_P_to_other = None

    def _get_other_unit_dict(self):
        """getter of other_unit_dict"""
        return self._other_unit_dict

    def _set_other_unit_dict(self, value):
        """setter of other_unit_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("other_unit_dict", value, "dict")
        self._other_unit_dict = value

    other_unit_dict = property(
        fget=_get_other_unit_dict,
        fset=_set_other_unit_dict,
        doc=u"""convertion unit file .mot into unit_dict

        :Type: dict
        """,
    )

    def _get_other_dict(self):
        """getter of other_dict"""
        return self._other_dict

    def _set_other_dict(self, value):
        """setter of other_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("other_dict", value, "dict")
        self._other_dict = value

    other_dict = property(
        fget=_get_other_dict,
        fset=_set_other_dict,
        doc=u"""convertion file .mot in dict

        :Type: dict
        """,
    )

    def _get_machine(self):
        """getter of machine"""
        return self._machine

    def _set_machine(self, value):
        """setter of machine"""
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
                "pyleecan.Classes", value.get("__class__"), "machine"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Machine = import_class("pyleecan.Classes", "Machine", "machine")
            value = Machine()
        check_var("machine", value, "Machine")
        self._machine = value

        if self._machine is not None:
            self._machine.parent = self

    machine = property(
        fget=_get_machine,
        fset=_set_machine,
        doc=u"""machine pyleecan

        :Type: Machine
        """,
    )

    def _get_rules_list(self):
        """getter of rules_list"""
        return self._rules_list

    def _set_rules_list(self, value):
        """setter of rules_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("rules_list", value, "list")
        self._rules_list = value

    rules_list = property(
        fget=_get_rules_list,
        fset=_set_rules_list,
        doc=u"""list differents rules

        :Type: list
        """,
    )

    def _get_is_P_to_other(self):
        """getter of is_P_to_other"""
        return self._is_P_to_other

    def _set_is_P_to_other(self, value):
        """setter of is_P_to_other"""
        check_var("is_P_to_other", value, "bool")
        self._is_P_to_other = value

    is_P_to_other = property(
        fget=_get_is_P_to_other,
        fset=_set_is_P_to_other,
        doc=u"""booleen to select the direction of conversion

        :Type: bool
        """,
    )
