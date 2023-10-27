# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/Rules_selections.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/Rules_selections
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
    from ..Methods.Converter.Rules_selections.get_slot import get_slot
except ImportError as error:
    get_slot = error

try:
    from ..Methods.Converter.Rules_selections.get_lamination import get_lamination
except ImportError as error:
    get_lamination = error

try:
    from ..Methods.Converter.Rules_selections.get_winding import get_winding
except ImportError as error:
    get_winding = error

try:
    from ..Methods.Converter.Rules_selections.get_conductor import get_conductor
except ImportError as error:
    get_conductor = error

try:
    from ..Methods.Converter.Rules_selections.get_hole import get_hole
except ImportError as error:
    get_hole = error

try:
    from ..Methods.Converter.Rules_selections.get_pole import get_pole
except ImportError as error:
    get_pole = error

try:
    from ..Methods.Converter.Rules_selections.get_magnet import get_magnet
except ImportError as error:
    get_magnet = error

try:
    from ..Methods.Converter.Rules_selections.get_skew import get_skew
except ImportError as error:
    get_skew = error

try:
    from ..Methods.Converter.Rules_selections.get_bar import get_bar
except ImportError as error:
    get_bar = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Rules_selections(FrozenClass):
    """All motor type in motor-cad"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.Rules_selections.get_slot
    if isinstance(get_slot, ImportError):
        get_slot = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_slot: " + str(get_slot)
                )
            )
        )
    else:
        get_slot = get_slot
    # cf Methods.Converter.Rules_selections.get_lamination
    if isinstance(get_lamination, ImportError):
        get_lamination = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_lamination: "
                    + str(get_lamination)
                )
            )
        )
    else:
        get_lamination = get_lamination
    # cf Methods.Converter.Rules_selections.get_winding
    if isinstance(get_winding, ImportError):
        get_winding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_winding: " + str(get_winding)
                )
            )
        )
    else:
        get_winding = get_winding
    # cf Methods.Converter.Rules_selections.get_conductor
    if isinstance(get_conductor, ImportError):
        get_conductor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_conductor: "
                    + str(get_conductor)
                )
            )
        )
    else:
        get_conductor = get_conductor
    # cf Methods.Converter.Rules_selections.get_hole
    if isinstance(get_hole, ImportError):
        get_hole = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_hole: " + str(get_hole)
                )
            )
        )
    else:
        get_hole = get_hole
    # cf Methods.Converter.Rules_selections.get_pole
    if isinstance(get_pole, ImportError):
        get_pole = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_pole: " + str(get_pole)
                )
            )
        )
    else:
        get_pole = get_pole
    # cf Methods.Converter.Rules_selections.get_magnet
    if isinstance(get_magnet, ImportError):
        get_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_magnet: " + str(get_magnet)
                )
            )
        )
    else:
        get_magnet = get_magnet
    # cf Methods.Converter.Rules_selections.get_skew
    if isinstance(get_skew, ImportError):
        get_skew = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_skew: " + str(get_skew)
                )
            )
        )
    else:
        get_skew = get_skew
    # cf Methods.Converter.Rules_selections.get_bar
    if isinstance(get_bar, ImportError):
        get_bar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Rules_selections method get_bar: " + str(get_bar)
                )
            )
        )
    else:
        get_bar = get_bar
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, mot_dict=-1, rules=-1, is_stator=True, init_dict=None, init_str=None
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
            if "mot_dict" in list(init_dict.keys()):
                mot_dict = init_dict["mot_dict"]
            if "rules" in list(init_dict.keys()):
                rules = init_dict["rules"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.mot_dict = mot_dict
        self.rules = rules
        self.is_stator = is_stator

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Rules_selections_str = ""
        if self.parent is None:
            Rules_selections_str += "parent = None " + linesep
        else:
            Rules_selections_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        Rules_selections_str += "mot_dict = " + str(self.mot_dict) + linesep
        Rules_selections_str += (
            "rules = "
            + linesep
            + str(self.rules).replace(linesep, linesep + "\t")
            + linesep
        )
        Rules_selections_str += "is_stator = " + str(self.is_stator) + linesep
        return Rules_selections_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mot_dict != self.mot_dict:
            return False
        if other.rules != self.rules:
            return False
        if other.is_stator != self.is_stator:
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
        if other._is_stator != self._is_stator:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_stator)
                    + ", other="
                    + str(other._is_stator)
                    + ")"
                )
                diff_list.append(name + ".is_stator" + val_str)
            else:
                diff_list.append(name + ".is_stator")
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
        S += getsizeof(self.is_stator)
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

        Rules_selections_dict = dict()
        Rules_selections_dict["mot_dict"] = (
            self.mot_dict.copy() if self.mot_dict is not None else None
        )
        Rules_selections_dict["rules"] = (
            self.rules.copy() if self.rules is not None else None
        )
        Rules_selections_dict["is_stator"] = self.is_stator
        # The class name is added to the dict for deserialisation purpose
        Rules_selections_dict["__class__"] = "Rules_selections"
        return Rules_selections_dict

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
        is_stator_val = self.is_stator
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            mot_dict=mot_dict_val, rules=rules_val, is_stator=is_stator_val
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mot_dict = None
        self.rules = None
        self.is_stator = None

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

    def _get_is_stator(self):
        """getter of is_stator"""
        return self._is_stator

    def _set_is_stator(self, value):
        """setter of is_stator"""
        check_var("is_stator", value, "bool")
        self._is_stator = value

    is_stator = property(
        fget=_get_is_stator,
        fset=_set_is_stator,
        doc=u"""selection rotor or stator, if true = stator else rotor

        :Type: bool
        """,
    )
