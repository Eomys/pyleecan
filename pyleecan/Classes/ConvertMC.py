# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/ConvertMC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/ConvertMC
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
from .Convert import Convert

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.ConvertMC.convert_mot_to_dict import convert_mot_to_dict
except ImportError as error:
    convert_mot_to_dict = error

try:
    from ..Methods.Converter.ConvertMC.selection_machine_type import (
        selection_machine_type,
    )
except ImportError as error:
    selection_machine_type = error

try:
    from ..Methods.Converter.ConvertMC.convert import convert
except ImportError as error:
    convert = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_BPM_rules import (
        selection_BPM_rules,
    )
except ImportError as error:
    selection_BPM_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_IM_rules import (
        selection_IM_rules,
    )
except ImportError as error:
    selection_IM_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_SRM_rules import (
        selection_SRM_rules,
    )
except ImportError as error:
    selection_SRM_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules import (
        selection_BPMO_rules,
    )
except ImportError as error:
    selection_BPMO_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_PMDC_rules import (
        selection_PMDC_rules,
    )
except ImportError as error:
    selection_PMDC_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_SYNC_rules import (
        selection_SYNC_rules,
    )
except ImportError as error:
    selection_SYNC_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_CLAW_rules import (
        selection_CLAW_rules,
    )
except ImportError as error:
    selection_CLAW_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_IM1PH_rules import (
        selection_IM1PH_rules,
    )
except ImportError as error:
    selection_IM1PH_rules = error

try:
    from ..Methods.Converter.ConvertMC.machine_type.selection_WFC_rules import (
        selection_WFC_rules,
    )
except ImportError as error:
    selection_WFC_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_slot_rules import (
        selection_slot_rules,
    )
except ImportError as error:
    selection_slot_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_lamination_rules import (
        selection_lamination_rules,
    )
except ImportError as error:
    selection_lamination_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_winding_rules import (
        selection_winding_rules,
    )
except ImportError as error:
    selection_winding_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_conductor_rules import (
        selection_conductor_rules,
    )
except ImportError as error:
    selection_conductor_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_hole_rules import (
        selection_hole_rules,
    )
except ImportError as error:
    selection_hole_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_pole_rules import (
        selection_pole_rules,
    )
except ImportError as error:
    selection_pole_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_magnet_rules import (
        selection_magnet_rules,
    )
except ImportError as error:
    selection_magnet_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_skew_rules import (
        selection_skew_rules,
    )
except ImportError as error:
    selection_skew_rules = error

try:
    from ..Methods.Converter.ConvertMC.Step.selection_bar_rules import (
        selection_bar_rules,
    )
except ImportError as error:
    selection_bar_rules = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_parallel_tooth_slotW11 import (
        add_rule_parallel_tooth_slotW11,
    )
except ImportError as error:
    add_rule_parallel_tooth_slotW11 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_machine_select import (
        add_rule_machine_select,
    )
except ImportError as error:
    add_rule_machine_select = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_machine_type import (
        add_rule_machine_type,
    )
except ImportError as error:
    add_rule_machine_type = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_rotor_parallel_tooth_slotW11 import (
        add_rule_rotor_parallel_tooth_slotW11,
    )
except ImportError as error:
    add_rule_rotor_parallel_tooth_slotW11 = error


from numpy import isnan
from ._check import InitUnKnowClassError


class ConvertMC(Convert):
    """convertorMC abstract"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.ConvertMC.convert_mot_to_dict
    if isinstance(convert_mot_to_dict, ImportError):
        convert_mot_to_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_mot_to_dict: "
                    + str(convert_mot_to_dict)
                )
            )
        )
    else:
        convert_mot_to_dict = convert_mot_to_dict
    # cf Methods.Converter.ConvertMC.selection_machine_type
    if isinstance(selection_machine_type, ImportError):
        selection_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_machine_type: "
                    + str(selection_machine_type)
                )
            )
        )
    else:
        selection_machine_type = selection_machine_type
    # cf Methods.Converter.ConvertMC.convert
    if isinstance(convert, ImportError):
        convert = property(
            fget=lambda x: raise_(
                ImportError("Can't use ConvertMC method convert: " + str(convert))
            )
        )
    else:
        convert = convert
    # cf Methods.Converter.ConvertMC.machine_type.selection_BPM_rules
    if isinstance(selection_BPM_rules, ImportError):
        selection_BPM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_BPM_rules: "
                    + str(selection_BPM_rules)
                )
            )
        )
    else:
        selection_BPM_rules = selection_BPM_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_IM_rules
    if isinstance(selection_IM_rules, ImportError):
        selection_IM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_IM_rules: "
                    + str(selection_IM_rules)
                )
            )
        )
    else:
        selection_IM_rules = selection_IM_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_SRM_rules
    if isinstance(selection_SRM_rules, ImportError):
        selection_SRM_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_SRM_rules: "
                    + str(selection_SRM_rules)
                )
            )
        )
    else:
        selection_SRM_rules = selection_SRM_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules
    if isinstance(selection_BPMO_rules, ImportError):
        selection_BPMO_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_BPMO_rules: "
                    + str(selection_BPMO_rules)
                )
            )
        )
    else:
        selection_BPMO_rules = selection_BPMO_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_PMDC_rules
    if isinstance(selection_PMDC_rules, ImportError):
        selection_PMDC_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_PMDC_rules: "
                    + str(selection_PMDC_rules)
                )
            )
        )
    else:
        selection_PMDC_rules = selection_PMDC_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_SYNC_rules
    if isinstance(selection_SYNC_rules, ImportError):
        selection_SYNC_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_SYNC_rules: "
                    + str(selection_SYNC_rules)
                )
            )
        )
    else:
        selection_SYNC_rules = selection_SYNC_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_CLAW_rules
    if isinstance(selection_CLAW_rules, ImportError):
        selection_CLAW_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_CLAW_rules: "
                    + str(selection_CLAW_rules)
                )
            )
        )
    else:
        selection_CLAW_rules = selection_CLAW_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_IM1PH_rules
    if isinstance(selection_IM1PH_rules, ImportError):
        selection_IM1PH_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_IM1PH_rules: "
                    + str(selection_IM1PH_rules)
                )
            )
        )
    else:
        selection_IM1PH_rules = selection_IM1PH_rules
    # cf Methods.Converter.ConvertMC.machine_type.selection_WFC_rules
    if isinstance(selection_WFC_rules, ImportError):
        selection_WFC_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_WFC_rules: "
                    + str(selection_WFC_rules)
                )
            )
        )
    else:
        selection_WFC_rules = selection_WFC_rules
    # cf Methods.Converter.ConvertMC.Step.selection_slot_rules
    if isinstance(selection_slot_rules, ImportError):
        selection_slot_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_slot_rules: "
                    + str(selection_slot_rules)
                )
            )
        )
    else:
        selection_slot_rules = selection_slot_rules
    # cf Methods.Converter.ConvertMC.Step.selection_lamination_rules
    if isinstance(selection_lamination_rules, ImportError):
        selection_lamination_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_lamination_rules: "
                    + str(selection_lamination_rules)
                )
            )
        )
    else:
        selection_lamination_rules = selection_lamination_rules
    # cf Methods.Converter.ConvertMC.Step.selection_winding_rules
    if isinstance(selection_winding_rules, ImportError):
        selection_winding_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_winding_rules: "
                    + str(selection_winding_rules)
                )
            )
        )
    else:
        selection_winding_rules = selection_winding_rules
    # cf Methods.Converter.ConvertMC.Step.selection_conductor_rules
    if isinstance(selection_conductor_rules, ImportError):
        selection_conductor_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_conductor_rules: "
                    + str(selection_conductor_rules)
                )
            )
        )
    else:
        selection_conductor_rules = selection_conductor_rules
    # cf Methods.Converter.ConvertMC.Step.selection_hole_rules
    if isinstance(selection_hole_rules, ImportError):
        selection_hole_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_hole_rules: "
                    + str(selection_hole_rules)
                )
            )
        )
    else:
        selection_hole_rules = selection_hole_rules
    # cf Methods.Converter.ConvertMC.Step.selection_pole_rules
    if isinstance(selection_pole_rules, ImportError):
        selection_pole_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_pole_rules: "
                    + str(selection_pole_rules)
                )
            )
        )
    else:
        selection_pole_rules = selection_pole_rules
    # cf Methods.Converter.ConvertMC.Step.selection_magnet_rules
    if isinstance(selection_magnet_rules, ImportError):
        selection_magnet_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_magnet_rules: "
                    + str(selection_magnet_rules)
                )
            )
        )
    else:
        selection_magnet_rules = selection_magnet_rules
    # cf Methods.Converter.ConvertMC.Step.selection_skew_rules
    if isinstance(selection_skew_rules, ImportError):
        selection_skew_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_skew_rules: "
                    + str(selection_skew_rules)
                )
            )
        )
    else:
        selection_skew_rules = selection_skew_rules
    # cf Methods.Converter.ConvertMC.Step.selection_bar_rules
    if isinstance(selection_bar_rules, ImportError):
        selection_bar_rules = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method selection_bar_rules: "
                    + str(selection_bar_rules)
                )
            )
        )
    else:
        selection_bar_rules = selection_bar_rules
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_parallel_tooth_slotW11
    if isinstance(add_rule_parallel_tooth_slotW11, ImportError):
        add_rule_parallel_tooth_slotW11 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_parallel_tooth_slotW11: "
                    + str(add_rule_parallel_tooth_slotW11)
                )
            )
        )
    else:
        add_rule_parallel_tooth_slotW11 = add_rule_parallel_tooth_slotW11
    # cf Methods.Converter.ConvertMC.Rules.add_rule_machine_select
    if isinstance(add_rule_machine_select, ImportError):
        add_rule_machine_select = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_machine_select: "
                    + str(add_rule_machine_select)
                )
            )
        )
    else:
        add_rule_machine_select = add_rule_machine_select
    # cf Methods.Converter.ConvertMC.Rules.add_rule_machine_type
    if isinstance(add_rule_machine_type, ImportError):
        add_rule_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_machine_type: "
                    + str(add_rule_machine_type)
                )
            )
        )
    else:
        add_rule_machine_type = add_rule_machine_type
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_rotor_parallel_tooth_slotW11
    if isinstance(add_rule_rotor_parallel_tooth_slotW11, ImportError):
        add_rule_rotor_parallel_tooth_slotW11 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_parallel_tooth_slotW11: "
                    + str(add_rule_rotor_parallel_tooth_slotW11)
                )
            )
        )
    else:
        add_rule_rotor_parallel_tooth_slotW11 = add_rule_rotor_parallel_tooth_slotW11
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        other_dict=None,
        machine=None,
        rules_list=None,
        P_to_other=False,
        file_path="0",
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
            if "other_dict" in list(init_dict.keys()):
                other_dict = init_dict["other_dict"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "rules_list" in list(init_dict.keys()):
                rules_list = init_dict["rules_list"]
            if "P_to_other" in list(init_dict.keys()):
                P_to_other = init_dict["P_to_other"]
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
        # Set the properties (value check and convertion are done in setter)
        self.other_dict = other_dict
        self.machine = machine
        self.rules_list = rules_list
        self.P_to_other = P_to_other
        # Call Convert init
        super(ConvertMC, self).__init__(file_path=file_path)
        # The class is frozen (in Convert init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ConvertMC_str = ""
        # Get the properties inherited from Convert
        ConvertMC_str += super(ConvertMC, self).__str__()
        ConvertMC_str += "other_dict = " + str(self.other_dict) + linesep
        if self.machine is not None:
            tmp = self.machine.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            ConvertMC_str += "machine = " + tmp
        else:
            ConvertMC_str += "machine = None" + linesep + linesep
        ConvertMC_str += (
            "rules_list = "
            + linesep
            + str(self.rules_list).replace(linesep, linesep + "\t")
            + linesep
        )
        ConvertMC_str += "P_to_other = " + str(self.P_to_other) + linesep
        return ConvertMC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Convert
        if not super(ConvertMC, self).__eq__(other):
            return False
        if other.other_dict != self.other_dict:
            return False
        if other.machine != self.machine:
            return False
        if other.rules_list != self.rules_list:
            return False
        if other.P_to_other != self.P_to_other:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Convert
        diff_list.extend(
            super(ConvertMC, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
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
        if other._P_to_other != self._P_to_other:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._P_to_other)
                    + ", other="
                    + str(other._P_to_other)
                    + ")"
                )
                diff_list.append(name + ".P_to_other" + val_str)
            else:
                diff_list.append(name + ".P_to_other")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Convert
        S += super(ConvertMC, self).__sizeof__()
        if self.other_dict is not None:
            for key, value in self.other_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.machine)
        if self.rules_list is not None:
            for value in self.rules_list:
                S += getsizeof(value)
        S += getsizeof(self.P_to_other)
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

        # Get the properties inherited from Convert
        ConvertMC_dict = super(ConvertMC, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ConvertMC_dict["other_dict"] = (
            self.other_dict.copy() if self.other_dict is not None else None
        )
        if self.machine is None:
            ConvertMC_dict["machine"] = None
        else:
            ConvertMC_dict["machine"] = self.machine.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        ConvertMC_dict["rules_list"] = (
            self.rules_list.copy() if self.rules_list is not None else None
        )
        ConvertMC_dict["P_to_other"] = self.P_to_other
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ConvertMC_dict["__class__"] = "ConvertMC"
        return ConvertMC_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
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
        P_to_other_val = self.P_to_other
        file_path_val = self.file_path
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            other_dict=other_dict_val,
            machine=machine_val,
            rules_list=rules_list_val,
            P_to_other=P_to_other_val,
            file_path=file_path_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.other_dict = None
        if self.machine is not None:
            self.machine._set_None()
        self.rules_list = None
        self.P_to_other = None
        # Set to None the properties inherited from Convert
        super(ConvertMC, self)._set_None()

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
            machine = import_class("pyleecan.Classes", "machine", "machine")
            value = machine()
        check_var("machine", value, "machine")
        self._machine = value

        if self._machine is not None:
            self._machine.parent = self

    machine = property(
        fget=_get_machine,
        fset=_set_machine,
        doc=u"""machine pyleecan

        :Type: machine
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

    def _get_P_to_other(self):
        """getter of P_to_other"""
        return self._P_to_other

    def _set_P_to_other(self, value):
        """setter of P_to_other"""
        check_var("P_to_other", value, "bool")
        self._P_to_other = value

    P_to_other = property(
        fget=_get_P_to_other,
        fset=_set_P_to_other,
        doc=u"""booleen to select the direction of conversion

        :Type: bool
        """,
    )
