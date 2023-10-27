# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/Machine_type_mot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/Machine_type_mot
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
    from ..Methods.Converter.Machine_type_mot.get_BPM import get_BPM
except ImportError as error:
    get_BPM = error

try:
    from ..Methods.Converter.Machine_type_mot.get_IM import get_IM
except ImportError as error:
    get_IM = error

try:
    from ..Methods.Converter.Machine_type_mot.get_SRM import get_SRM
except ImportError as error:
    get_SRM = error

try:
    from ..Methods.Converter.Machine_type_mot.get_BPMO import get_BPMO
except ImportError as error:
    get_BPMO = error

try:
    from ..Methods.Converter.Machine_type_mot.get_PMDC import get_PMDC
except ImportError as error:
    get_PMDC = error

try:
    from ..Methods.Converter.Machine_type_mot.get_SYNC import get_SYNC
except ImportError as error:
    get_SYNC = error

try:
    from ..Methods.Converter.Machine_type_mot.get_CLAW import get_CLAW
except ImportError as error:
    get_CLAW = error

try:
    from ..Methods.Converter.Machine_type_mot.get_IM1PH import get_IM1PH
except ImportError as error:
    get_IM1PH = error

try:
    from ..Methods.Converter.Machine_type_mot.get_WFC import get_WFC
except ImportError as error:
    get_WFC = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Machine_type_mot(FrozenClass):
    """All motor type in motor-cad"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.Machine_type_mot.get_BPM
    if isinstance(get_BPM, ImportError):
        get_BPM = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_BPM: " + str(get_BPM)
                )
            )
        )
    else:
        get_BPM = get_BPM
    # cf Methods.Converter.Machine_type_mot.get_IM
    if isinstance(get_IM, ImportError):
        get_IM = property(
            fget=lambda x: raise_(
                ImportError("Can't use Machine_type_mot method get_IM: " + str(get_IM))
            )
        )
    else:
        get_IM = get_IM
    # cf Methods.Converter.Machine_type_mot.get_SRM
    if isinstance(get_SRM, ImportError):
        get_SRM = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_SRM: " + str(get_SRM)
                )
            )
        )
    else:
        get_SRM = get_SRM
    # cf Methods.Converter.Machine_type_mot.get_BPMO
    if isinstance(get_BPMO, ImportError):
        get_BPMO = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_BPMO: " + str(get_BPMO)
                )
            )
        )
    else:
        get_BPMO = get_BPMO
    # cf Methods.Converter.Machine_type_mot.get_PMDC
    if isinstance(get_PMDC, ImportError):
        get_PMDC = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_PMDC: " + str(get_PMDC)
                )
            )
        )
    else:
        get_PMDC = get_PMDC
    # cf Methods.Converter.Machine_type_mot.get_SYNC
    if isinstance(get_SYNC, ImportError):
        get_SYNC = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_SYNC: " + str(get_SYNC)
                )
            )
        )
    else:
        get_SYNC = get_SYNC
    # cf Methods.Converter.Machine_type_mot.get_CLAW
    if isinstance(get_CLAW, ImportError):
        get_CLAW = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_CLAW: " + str(get_CLAW)
                )
            )
        )
    else:
        get_CLAW = get_CLAW
    # cf Methods.Converter.Machine_type_mot.get_IM1PH
    if isinstance(get_IM1PH, ImportError):
        get_IM1PH = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_IM1PH: " + str(get_IM1PH)
                )
            )
        )
    else:
        get_IM1PH = get_IM1PH
    # cf Methods.Converter.Machine_type_mot.get_WFC
    if isinstance(get_WFC, ImportError):
        get_WFC = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Machine_type_mot method get_WFC: " + str(get_WFC)
                )
            )
        )
    else:
        get_WFC = get_WFC
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, mot_dict=-1, rules=-1, init_dict=None, init_str=None):
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
            if "mot_dict" in list(init_dict.keys()):
                mot_dict = init_dict["mot_dict"]
            if "rules" in list(init_dict.keys()):
                rules = init_dict["rules"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.mot_dict = mot_dict
        self.rules = rules

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Machine_type_mot_str = ""
        if self.parent is None:
            Machine_type_mot_str += "parent = None " + linesep
        else:
            Machine_type_mot_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        Machine_type_mot_str += "mot_dict = " + str(self.mot_dict) + linesep
        Machine_type_mot_str += (
            "rules = "
            + linesep
            + str(self.rules).replace(linesep, linesep + "\t")
            + linesep
        )
        return Machine_type_mot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mot_dict != self.mot_dict:
            return False
        if other.rules != self.rules:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._mot_dict != self._mot_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._mot_dict)
                    + ", other="
                    + str(other._mot_dict)
                    + ")"
                )
                diff_list.append(name + ".mot_dict" + val_str)
            else:
                diff_list.append(name + ".mot_dict")
        if other._rules != self._rules:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._rules) + ", other=" + str(other._rules) + ")"
                )
                diff_list.append(name + ".rules" + val_str)
            else:
                diff_list.append(name + ".rules")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.mot_dict is not None:
            for key, value in self.mot_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.rules is not None:
            for value in self.rules:
                S += getsizeof(value)
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

        Machine_type_mot_dict = dict()
        Machine_type_mot_dict["mot_dict"] = (
            self.mot_dict.copy() if self.mot_dict is not None else None
        )
        Machine_type_mot_dict["rules"] = (
            self.rules.copy() if self.rules is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        Machine_type_mot_dict["__class__"] = "Machine_type_mot"
        return Machine_type_mot_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.mot_dict is None:
            mot_dict_val = None
        else:
            mot_dict_val = self.mot_dict.copy()
        if self.rules is None:
            rules_val = None
        else:
            rules_val = self.rules.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(mot_dict=mot_dict_val, rules=rules_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mot_dict = None
        self.rules = None

    def _get_mot_dict(self):
        """getter of mot_dict"""
        return self._mot_dict

    def _set_mot_dict(self, value):
        """setter of mot_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("mot_dict", value, "dict")
        self._mot_dict = value

    mot_dict = property(
        fget=_get_mot_dict,
        fset=_set_mot_dict,
        doc=u"""convertion file .mot in dict

        :Type: dict
        """,
    )

    def _get_rules(self):
        """getter of rules"""
        return self._rules

    def _set_rules(self, value):
        """setter of rules"""
        if type(value) is int and value == -1:
            value = list()
        check_var("rules", value, "list")
        self._rules = value

    rules = property(
        fget=_get_rules,
        fset=_set_rules,
        doc=u"""list differents rules

        :Type: list
        """,
    )
