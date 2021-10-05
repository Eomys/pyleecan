# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputFlux.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputFlux
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .InputCurrent import InputCurrent

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputFlux.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix
from .Import import Import


class InputFlux(InputCurrent):
    """Input to skip the magnetic module and start with the structural one"""

    VERSION = 1

    # cf Methods.Simulation.InputFlux.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
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
        slice=None,
        B_enforced=None,
        Is=None,
        Ir=None,
        Id_ref=None,
        Iq_ref=None,
        angle_rotor=None,
        rot_dir=None,
        angle_rotor_initial=0,
        Tem_av_ref=None,
        Ud_ref=None,
        Uq_ref=None,
        felec=None,
        slip_ref=0,
        U0_ref=None,
        Pem_av_ref=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=None,
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
            if "slice" in list(init_dict.keys()):
                slice = init_dict["slice"]
            if "B_enforced" in list(init_dict.keys()):
                B_enforced = init_dict["B_enforced"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "slip_ref" in list(init_dict.keys()):
                slip_ref = init_dict["slip_ref"]
            if "U0_ref" in list(init_dict.keys()):
                U0_ref = init_dict["U0_ref"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
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
        self.slice = slice
        self.B_enforced = B_enforced
        # Call InputCurrent init
        super(InputFlux, self).__init__(
            Is=Is,
            Ir=Ir,
            Id_ref=Id_ref,
            Iq_ref=Iq_ref,
            angle_rotor=angle_rotor,
            rot_dir=rot_dir,
            angle_rotor_initial=angle_rotor_initial,
            Tem_av_ref=Tem_av_ref,
            Ud_ref=Ud_ref,
            Uq_ref=Uq_ref,
            felec=felec,
            slip_ref=slip_ref,
            U0_ref=U0_ref,
            Pem_av_ref=Pem_av_ref,
            time=time,
            angle=angle,
            Nt_tot=Nt_tot,
            Nrev=Nrev,
            Na_tot=Na_tot,
            N0=N0,
        )
        # The class is frozen (in InputCurrent init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputFlux_str = ""
        # Get the properties inherited from InputCurrent
        InputFlux_str += super(InputFlux, self).__str__()
        InputFlux_str += "per_a = " + str(self.per_a) + linesep
        InputFlux_str += "per_t = " + str(self.per_t) + linesep
        InputFlux_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        InputFlux_str += "is_antiper_t = " + str(self.is_antiper_t) + linesep
        InputFlux_str += "B_dict = " + str(self.B_dict) + linesep
        InputFlux_str += 'unit = "' + str(self.unit) + '"' + linesep
        InputFlux_str += (
            "slice = "
            + linesep
            + str(self.slice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        InputFlux_str += "B_enforced = " + str(self.B_enforced) + linesep + linesep
        return InputFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from InputCurrent
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
        if not array_equal(other.slice, self.slice):
            return False
        if other.B_enforced != self.B_enforced:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from InputCurrent
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
        if not array_equal(other.slice, self.slice):
            diff_list.append(name + ".slice")
        if (other.B_enforced is None and self.B_enforced is not None) or (
            other.B_enforced is not None and self.B_enforced is None
        ):
            diff_list.append(name + ".B_enforced None mismatch")
        elif self.B_enforced is not None:
            diff_list.extend(
                self.B_enforced.compare(other.B_enforced, name=name + ".B_enforced")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from InputCurrent
        S += super(InputFlux, self).__sizeof__()
        S += getsizeof(self.per_a)
        S += getsizeof(self.per_t)
        S += getsizeof(self.is_antiper_a)
        S += getsizeof(self.is_antiper_t)
        if self.B_dict is not None:
            for key, value in self.B_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.unit)
        S += getsizeof(self.slice)
        S += getsizeof(self.B_enforced)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from InputCurrent
        InputFlux_dict = super(InputFlux, self).as_dict(**kwargs)
        InputFlux_dict["per_a"] = self.per_a
        InputFlux_dict["per_t"] = self.per_t
        InputFlux_dict["is_antiper_a"] = self.is_antiper_a
        InputFlux_dict["is_antiper_t"] = self.is_antiper_t
        InputFlux_dict["B_dict"] = (
            self.B_dict.copy() if self.B_dict is not None else None
        )
        InputFlux_dict["unit"] = self.unit
        if self.slice is None:
            InputFlux_dict["slice"] = None
        else:
            InputFlux_dict["slice"] = self.slice.tolist()
        if self.B_enforced is None:
            InputFlux_dict["B_enforced"] = None
        else:
            InputFlux_dict["B_enforced"] = self.B_enforced.as_dict()
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
        self.slice = None
        self.B_enforced = None
        # Set to None the properties inherited from InputCurrent
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

    def _get_slice(self):
        """getter of slice"""
        return self._slice

    def _set_slice(self, value):
        """setter of slice"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("slice", value, "ndarray")
        self._slice = value

    slice = property(
        fget=_get_slice,
        fset=_set_slice,
        doc=u"""Slice axis values

        :Type: ndarray
        """,
    )

    def _get_B_enforced(self):
        """getter of B_enforced"""
        return self._B_enforced

    def _set_B_enforced(self, value):
        """setter of B_enforced"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "B_enforced"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VectorField()
        check_var("B_enforced", value, "VectorField")
        self._B_enforced = value

    B_enforced = property(
        fget=_get_B_enforced,
        fset=_set_B_enforced,
        doc=u"""Airgap flux density as VectorField object

        :Type: SciDataTool.Classes.VectorField.VectorField
        """,
    )
