# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputFlux.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputFlux
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
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputFlux.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputFlux.comp_felec import comp_felec
except ImportError as error:
    comp_felec = error

try:
    from ..Methods.Simulation.InputFlux.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Input import Input
from .ImportMatrix import ImportMatrix


class InputFlux(Input):
    """Input to skip the magnetic module and start with the structural one"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputFlux.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputFlux.comp_felec
    if isinstance(comp_felec, ImportError):
        comp_felec = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method comp_felec: " + str(comp_felec))
            )
        )
    else:
        comp_felec = comp_felec
    # cf Methods.Simulation.InputFlux.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        per_a=1,
        per_t=1,
        is_antiper_a=False,
        is_antiper_t=False,
        B_dict=None,
        unit=None,
        OP=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
        N0=None,
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
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "per_t" in list(init_dict.keys()):
                per_t = init_dict["per_t"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "is_antiper_t" in list(init_dict.keys()):
                is_antiper_t = init_dict["is_antiper_t"]
            if "B_dict" in list(init_dict.keys()):
                B_dict = init_dict["B_dict"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
        # Set the properties (value check and convertion are done in setter)
        self.per_a = per_a
        self.per_t = per_t
        self.is_antiper_a = is_antiper_a
        self.is_antiper_t = is_antiper_t
        self.B_dict = B_dict
        self.unit = unit
        self.OP = OP
        # Call Input init
        super(InputFlux, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot, N0=N0
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputFlux_str = ""
        # Get the properties inherited from Input
        InputFlux_str += super(InputFlux, self).__str__()
        InputFlux_str += "per_a = " + str(self.per_a) + linesep
        InputFlux_str += "per_t = " + str(self.per_t) + linesep
        InputFlux_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        InputFlux_str += "is_antiper_t = " + str(self.is_antiper_t) + linesep
        InputFlux_str += "B_dict = " + str(self.B_dict) + linesep
        InputFlux_str += 'unit = "' + str(self.unit) + '"' + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "OP = " + tmp
        else:
            InputFlux_str += "OP = None" + linesep + linesep
        return InputFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputFlux, self).__eq__(other):
            return False
        if other.per_a != self.per_a:
            return False
        if other.per_t != self.per_t:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        if other.is_antiper_t != self.is_antiper_t:
            return False
        if other.B_dict != self.B_dict:
            return False
        if other.unit != self.unit:
            return False
        if other.OP != self.OP:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Input
        diff_list.extend(super(InputFlux, self).compare(other, name=name))
        if other._per_a != self._per_a:
            diff_list.append(name + ".per_a")
        if other._per_t != self._per_t:
            diff_list.append(name + ".per_t")
        if other._is_antiper_a != self._is_antiper_a:
            diff_list.append(name + ".is_antiper_a")
        if other._is_antiper_t != self._is_antiper_t:
            diff_list.append(name + ".is_antiper_t")
        if other._B_dict != self._B_dict:
            diff_list.append(name + ".B_dict")
        if other._unit != self._unit:
            diff_list.append(name + ".unit")
        if (other.OP is None and self.OP is not None) or (
            other.OP is not None and self.OP is None
        ):
            diff_list.append(name + ".OP None mismatch")
        elif self.OP is not None:
            diff_list.extend(self.OP.compare(other.OP, name=name + ".OP"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputFlux, self).__sizeof__()
        S += getsizeof(self.per_a)
        S += getsizeof(self.per_t)
        S += getsizeof(self.is_antiper_a)
        S += getsizeof(self.is_antiper_t)
        if self.B_dict is not None:
            for key, value in self.B_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.unit)
        S += getsizeof(self.OP)
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

        # Get the properties inherited from Input
        InputFlux_dict = super(InputFlux, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        InputFlux_dict["per_a"] = self.per_a
        InputFlux_dict["per_t"] = self.per_t
        InputFlux_dict["is_antiper_a"] = self.is_antiper_a
        InputFlux_dict["is_antiper_t"] = self.is_antiper_t
        InputFlux_dict["B_dict"] = (
            self.B_dict.copy() if self.B_dict is not None else None
        )
        InputFlux_dict["unit"] = self.unit
        if self.OP is None:
            InputFlux_dict["OP"] = None
        else:
            InputFlux_dict["OP"] = self.OP.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputFlux_dict["__class__"] = "InputFlux"
        return InputFlux_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.per_a = None
        self.per_t = None
        self.is_antiper_a = None
        self.is_antiper_t = None
        self.B_dict = None
        self.unit = None
        if self.OP is not None:
            self.OP._set_None()
        # Set to None the properties inherited from Input
        super(InputFlux, self)._set_None()

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
        doc=u"""Angle periodicity

        :Type: int
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
        doc=u"""Time periodicity

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
        doc=u"""If angle is antiperiodic

        :Type: bool
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
        doc=u"""If time is antiperiodic

        :Type: bool
        """,
    )

    def _get_B_dict(self):
        """getter of B_dict"""
        return self._B_dict

    def _set_B_dict(self, value):
        """setter of B_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("B_dict", value, "dict")
        self._B_dict = value

    B_dict = property(
        fget=_get_B_dict,
        fset=_set_B_dict,
        doc=u"""Dict of Import objects or lists for each component of the flux

        :Type: dict
        """,
    )

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc=u"""Unit of the flux if not T

        :Type: str
        """,
    )

    def _get_OP(self):
        """getter of OP"""
        return self._OP

    def _set_OP(self, value):
        """setter of OP"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "OP")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Input()
        check_var("OP", value, "Input")
        self._OP = value

        if self._OP is not None:
            self._OP.parent = self

    OP = property(
        fget=_get_OP,
        fset=_set_OP,
        doc=u"""InputCurrent to define Operating Point (not mandatory)

        :Type: Input
        """,
    )
