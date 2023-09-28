# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutGeoLam.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutGeoLam
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class OutGeoLam(FrozenClass):
    """Gather the geometrical and the global outputs of a lamination"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name_phase=None,
        BH_curve=None,
        Ksfill=None,
        S_slot=None,
        S_slot_wind=None,
        S_wind_act=None,
        per_a=None,
        is_antiper_a=None,
        per_t=None,
        is_antiper_t=None,
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
            if "name_phase" in list(init_dict.keys()):
                name_phase = init_dict["name_phase"]
            if "BH_curve" in list(init_dict.keys()):
                BH_curve = init_dict["BH_curve"]
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "S_slot" in list(init_dict.keys()):
                S_slot = init_dict["S_slot"]
            if "S_slot_wind" in list(init_dict.keys()):
                S_slot_wind = init_dict["S_slot_wind"]
            if "S_wind_act" in list(init_dict.keys()):
                S_wind_act = init_dict["S_wind_act"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "per_t" in list(init_dict.keys()):
                per_t = init_dict["per_t"]
            if "is_antiper_t" in list(init_dict.keys()):
                is_antiper_t = init_dict["is_antiper_t"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name_phase = name_phase
        self.BH_curve = BH_curve
        self.Ksfill = Ksfill
        self.S_slot = S_slot
        self.S_slot_wind = S_slot_wind
        self.S_wind_act = S_wind_act
        self.per_a = per_a
        self.is_antiper_a = is_antiper_a
        self.per_t = per_t
        self.is_antiper_t = is_antiper_t

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutGeoLam_str = ""
        if self.parent is None:
            OutGeoLam_str += "parent = None " + linesep
        else:
            OutGeoLam_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutGeoLam_str += (
            "name_phase = "
            + linesep
            + str(self.name_phase).replace(linesep, linesep + "\t")
            + linesep
        )
        OutGeoLam_str += (
            "BH_curve = "
            + linesep
            + str(self.BH_curve).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutGeoLam_str += "Ksfill = " + str(self.Ksfill) + linesep
        OutGeoLam_str += "S_slot = " + str(self.S_slot) + linesep
        OutGeoLam_str += "S_slot_wind = " + str(self.S_slot_wind) + linesep
        OutGeoLam_str += "S_wind_act = " + str(self.S_wind_act) + linesep
        OutGeoLam_str += "per_a = " + str(self.per_a) + linesep
        OutGeoLam_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        OutGeoLam_str += "per_t = " + str(self.per_t) + linesep
        OutGeoLam_str += "is_antiper_t = " + str(self.is_antiper_t) + linesep
        return OutGeoLam_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name_phase != self.name_phase:
            return False
        if not array_equal(other.BH_curve, self.BH_curve):
            return False
        if other.Ksfill != self.Ksfill:
            return False
        if other.S_slot != self.S_slot:
            return False
        if other.S_slot_wind != self.S_slot_wind:
            return False
        if other.S_wind_act != self.S_wind_act:
            return False
        if other.per_a != self.per_a:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        if other.per_t != self.per_t:
            return False
        if other.is_antiper_t != self.is_antiper_t:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name_phase != self._name_phase:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._name_phase)
                    + ", other="
                    + str(other._name_phase)
                    + ")"
                )
                diff_list.append(name + ".name_phase" + val_str)
            else:
                diff_list.append(name + ".name_phase")
        if not array_equal(other.BH_curve, self.BH_curve):
            diff_list.append(name + ".BH_curve")
        if (
            other._Ksfill is not None
            and self._Ksfill is not None
            and isnan(other._Ksfill)
            and isnan(self._Ksfill)
        ):
            pass
        elif other._Ksfill != self._Ksfill:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Ksfill)
                    + ", other="
                    + str(other._Ksfill)
                    + ")"
                )
                diff_list.append(name + ".Ksfill" + val_str)
            else:
                diff_list.append(name + ".Ksfill")
        if (
            other._S_slot is not None
            and self._S_slot is not None
            and isnan(other._S_slot)
            and isnan(self._S_slot)
        ):
            pass
        elif other._S_slot != self._S_slot:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._S_slot)
                    + ", other="
                    + str(other._S_slot)
                    + ")"
                )
                diff_list.append(name + ".S_slot" + val_str)
            else:
                diff_list.append(name + ".S_slot")
        if (
            other._S_slot_wind is not None
            and self._S_slot_wind is not None
            and isnan(other._S_slot_wind)
            and isnan(self._S_slot_wind)
        ):
            pass
        elif other._S_slot_wind != self._S_slot_wind:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._S_slot_wind)
                    + ", other="
                    + str(other._S_slot_wind)
                    + ")"
                )
                diff_list.append(name + ".S_slot_wind" + val_str)
            else:
                diff_list.append(name + ".S_slot_wind")
        if (
            other._S_wind_act is not None
            and self._S_wind_act is not None
            and isnan(other._S_wind_act)
            and isnan(self._S_wind_act)
        ):
            pass
        elif other._S_wind_act != self._S_wind_act:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._S_wind_act)
                    + ", other="
                    + str(other._S_wind_act)
                    + ")"
                )
                diff_list.append(name + ".S_wind_act" + val_str)
            else:
                diff_list.append(name + ".S_wind_act")
        if other._per_a != self._per_a:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_a) + ", other=" + str(other._per_a) + ")"
                )
                diff_list.append(name + ".per_a" + val_str)
            else:
                diff_list.append(name + ".per_a")
        if other._is_antiper_a != self._is_antiper_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_a)
                    + ", other="
                    + str(other._is_antiper_a)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_a" + val_str)
            else:
                diff_list.append(name + ".is_antiper_a")
        if other._per_t != self._per_t:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_t) + ", other=" + str(other._per_t) + ")"
                )
                diff_list.append(name + ".per_t" + val_str)
            else:
                diff_list.append(name + ".per_t")
        if other._is_antiper_t != self._is_antiper_t:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_t)
                    + ", other="
                    + str(other._is_antiper_t)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_t" + val_str)
            else:
                diff_list.append(name + ".is_antiper_t")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.name_phase is not None:
            for value in self.name_phase:
                S += getsizeof(value)
        S += getsizeof(self.BH_curve)
        S += getsizeof(self.Ksfill)
        S += getsizeof(self.S_slot)
        S += getsizeof(self.S_slot_wind)
        S += getsizeof(self.S_wind_act)
        S += getsizeof(self.per_a)
        S += getsizeof(self.is_antiper_a)
        S += getsizeof(self.per_t)
        S += getsizeof(self.is_antiper_t)
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

        OutGeoLam_dict = dict()
        OutGeoLam_dict["name_phase"] = (
            self.name_phase.copy() if self.name_phase is not None else None
        )
        if self.BH_curve is None:
            OutGeoLam_dict["BH_curve"] = None
        else:
            if type_handle_ndarray == 0:
                OutGeoLam_dict["BH_curve"] = self.BH_curve.tolist()
            elif type_handle_ndarray == 1:
                OutGeoLam_dict["BH_curve"] = self.BH_curve.copy()
            elif type_handle_ndarray == 2:
                OutGeoLam_dict["BH_curve"] = self.BH_curve
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OutGeoLam_dict["Ksfill"] = self.Ksfill
        OutGeoLam_dict["S_slot"] = self.S_slot
        OutGeoLam_dict["S_slot_wind"] = self.S_slot_wind
        OutGeoLam_dict["S_wind_act"] = self.S_wind_act
        OutGeoLam_dict["per_a"] = self.per_a
        OutGeoLam_dict["is_antiper_a"] = self.is_antiper_a
        OutGeoLam_dict["per_t"] = self.per_t
        OutGeoLam_dict["is_antiper_t"] = self.is_antiper_t
        # The class name is added to the dict for deserialisation purpose
        OutGeoLam_dict["__class__"] = "OutGeoLam"
        return OutGeoLam_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.name_phase is None:
            name_phase_val = None
        else:
            name_phase_val = self.name_phase.copy()
        if self.BH_curve is None:
            BH_curve_val = None
        else:
            BH_curve_val = self.BH_curve.copy()
        Ksfill_val = self.Ksfill
        S_slot_val = self.S_slot
        S_slot_wind_val = self.S_slot_wind
        S_wind_act_val = self.S_wind_act
        per_a_val = self.per_a
        is_antiper_a_val = self.is_antiper_a
        per_t_val = self.per_t
        is_antiper_t_val = self.is_antiper_t
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            name_phase=name_phase_val,
            BH_curve=BH_curve_val,
            Ksfill=Ksfill_val,
            S_slot=S_slot_val,
            S_slot_wind=S_slot_wind_val,
            S_wind_act=S_wind_act_val,
            per_a=per_a_val,
            is_antiper_a=is_antiper_a_val,
            per_t=per_t_val,
            is_antiper_t=is_antiper_t_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name_phase = None
        self.BH_curve = None
        self.Ksfill = None
        self.S_slot = None
        self.S_slot_wind = None
        self.S_wind_act = None
        self.per_a = None
        self.is_antiper_a = None
        self.per_t = None
        self.is_antiper_t = None

    def _get_name_phase(self):
        """getter of name_phase"""
        return self._name_phase

    def _set_name_phase(self, value):
        """setter of name_phase"""
        if type(value) is int and value == -1:
            value = list()
        check_var("name_phase", value, "list")
        self._name_phase = value

    name_phase = property(
        fget=_get_name_phase,
        fset=_set_name_phase,
        doc=u"""Name of the phases of the winding (if any)

        :Type: list
        """,
    )

    def _get_BH_curve(self):
        """getter of BH_curve"""
        return self._BH_curve

    def _set_BH_curve(self, value):
        """setter of BH_curve"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("BH_curve", value, "ndarray")
        self._BH_curve = value

    BH_curve = property(
        fget=_get_BH_curve,
        fset=_set_BH_curve,
        doc=u"""B(H) curve (two columns matrix, H and B(H))

        :Type: ndarray
        """,
    )

    def _get_Ksfill(self):
        """getter of Ksfill"""
        return self._Ksfill

    def _set_Ksfill(self, value):
        """setter of Ksfill"""
        check_var("Ksfill", value, "float")
        self._Ksfill = value

    Ksfill = property(
        fget=_get_Ksfill,
        fset=_set_Ksfill,
        doc=u"""Slot fill factor

        :Type: float
        """,
    )

    def _get_S_slot(self):
        """getter of S_slot"""
        return self._S_slot

    def _set_S_slot(self, value):
        """setter of S_slot"""
        check_var("S_slot", value, "float")
        self._S_slot = value

    S_slot = property(
        fget=_get_S_slot,
        fset=_set_S_slot,
        doc=u"""Slot surface

        :Type: float
        """,
    )

    def _get_S_slot_wind(self):
        """getter of S_slot_wind"""
        return self._S_slot_wind

    def _set_S_slot_wind(self, value):
        """setter of S_slot_wind"""
        check_var("S_slot_wind", value, "float")
        self._S_slot_wind = value

    S_slot_wind = property(
        fget=_get_S_slot_wind,
        fset=_set_S_slot_wind,
        doc=u"""Slot winding surface

        :Type: float
        """,
    )

    def _get_S_wind_act(self):
        """getter of S_wind_act"""
        return self._S_wind_act

    def _set_S_wind_act(self, value):
        """setter of S_wind_act"""
        check_var("S_wind_act", value, "float")
        self._S_wind_act = value

    S_wind_act = property(
        fget=_get_S_wind_act,
        fset=_set_S_wind_act,
        doc=u"""Conductor active surface

        :Type: float
        """,
    )

    def _get_per_a(self):
        """getter of per_a"""
        return self._per_a

    def _set_per_a(self, value):
        """setter of per_a"""
        check_var("per_a", value, "int")
        self._per_a = value

    per_a = property(
        fget=_get_per_a,
        fset=_set_per_a,
        doc=u"""Number of spatial periodicities of the lamination

        :Type: int
        """,
    )

    def _get_is_antiper_a(self):
        """getter of is_antiper_a"""
        return self._is_antiper_a

    def _set_is_antiper_a(self, value):
        """setter of is_antiper_a"""
        check_var("is_antiper_a", value, "bool")
        self._is_antiper_a = value

    is_antiper_a = property(
        fget=_get_is_antiper_a,
        fset=_set_is_antiper_a,
        doc=u"""True if an spatial anti-periodicity is possible after the periodicities

        :Type: bool
        """,
    )

    def _get_per_t(self):
        """getter of per_t"""
        return self._per_t

    def _set_per_t(self, value):
        """setter of per_t"""
        check_var("per_t", value, "int")
        self._per_t = value

    per_t = property(
        fget=_get_per_t,
        fset=_set_per_t,
        doc=u"""Number of time periodicities of the lamination

        :Type: int
        """,
    )

    def _get_is_antiper_t(self):
        """getter of is_antiper_t"""
        return self._is_antiper_t

    def _set_is_antiper_t(self, value):
        """setter of is_antiper_t"""
        check_var("is_antiper_t", value, "bool")
        self._is_antiper_t = value

    is_antiper_t = property(
        fget=_get_is_antiper_t,
        fset=_set_is_antiper_t,
        doc=u"""True if an time anti-periodicity is possible after the periodicities

        :Type: bool
        """,
    )
