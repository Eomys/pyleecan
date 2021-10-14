# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Magnetics.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Magnetics
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Magnetics.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Magnetics.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error


from ._check import InitUnKnowClassError


class Magnetics(FrozenClass):
    """Magnetic module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Magnetics.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Magnetics method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Magnetics.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Magnetics method comp_axes: " + str(comp_axes))
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
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_vent=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=False,
        angle_stator_shift=0,
        angle_rotor_shift=0,
        logger_name="Pyleecan.Magnetics",
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
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_vent" in list(init_dict.keys()):
                is_remove_vent = init_dict["is_remove_vent"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "angle_stator_shift" in list(init_dict.keys()):
                angle_stator_shift = init_dict["angle_stator_shift"]
            if "angle_rotor_shift" in list(init_dict.keys()):
                angle_rotor_shift = init_dict["angle_rotor_shift"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_remove_slotS = is_remove_slotS
        self.is_remove_slotR = is_remove_slotR
        self.is_remove_vent = is_remove_vent
        self.is_mmfs = is_mmfs
        self.is_mmfr = is_mmfr
        self.type_BH_stator = type_BH_stator
        self.type_BH_rotor = type_BH_rotor
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a
        self.angle_stator_shift = angle_stator_shift
        self.angle_rotor_shift = angle_rotor_shift
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Magnetics_str = ""
        if self.parent is None:
            Magnetics_str += "parent = None " + linesep
        else:
            Magnetics_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Magnetics_str += "is_remove_slotS = " + str(self.is_remove_slotS) + linesep
        Magnetics_str += "is_remove_slotR = " + str(self.is_remove_slotR) + linesep
        Magnetics_str += "is_remove_vent = " + str(self.is_remove_vent) + linesep
        Magnetics_str += "is_mmfs = " + str(self.is_mmfs) + linesep
        Magnetics_str += "is_mmfr = " + str(self.is_mmfr) + linesep
        Magnetics_str += "type_BH_stator = " + str(self.type_BH_stator) + linesep
        Magnetics_str += "type_BH_rotor = " + str(self.type_BH_rotor) + linesep
        Magnetics_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        Magnetics_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        Magnetics_str += (
            "angle_stator_shift = " + str(self.angle_stator_shift) + linesep
        )
        Magnetics_str += "angle_rotor_shift = " + str(self.angle_rotor_shift) + linesep
        Magnetics_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return Magnetics_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_remove_slotS != self.is_remove_slotS:
            return False
        if other.is_remove_slotR != self.is_remove_slotR:
            return False
        if other.is_remove_vent != self.is_remove_vent:
            return False
        if other.is_mmfs != self.is_mmfs:
            return False
        if other.is_mmfr != self.is_mmfr:
            return False
        if other.type_BH_stator != self.type_BH_stator:
            return False
        if other.type_BH_rotor != self.type_BH_rotor:
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.angle_stator_shift != self.angle_stator_shift:
            return False
        if other.angle_rotor_shift != self.angle_rotor_shift:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._is_remove_slotS != self._is_remove_slotS:
            diff_list.append(name + ".is_remove_slotS")
        if other._is_remove_slotR != self._is_remove_slotR:
            diff_list.append(name + ".is_remove_slotR")
        if other._is_remove_vent != self._is_remove_vent:
            diff_list.append(name + ".is_remove_vent")
        if other._is_mmfs != self._is_mmfs:
            diff_list.append(name + ".is_mmfs")
        if other._is_mmfr != self._is_mmfr:
            diff_list.append(name + ".is_mmfr")
        if other._type_BH_stator != self._type_BH_stator:
            diff_list.append(name + ".type_BH_stator")
        if other._type_BH_rotor != self._type_BH_rotor:
            diff_list.append(name + ".type_BH_rotor")
        if other._is_periodicity_t != self._is_periodicity_t:
            diff_list.append(name + ".is_periodicity_t")
        if other._is_periodicity_a != self._is_periodicity_a:
            diff_list.append(name + ".is_periodicity_a")
        if other._angle_stator_shift != self._angle_stator_shift:
            diff_list.append(name + ".angle_stator_shift")
        if other._angle_rotor_shift != self._angle_rotor_shift:
            diff_list.append(name + ".angle_rotor_shift")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.is_remove_slotS)
        S += getsizeof(self.is_remove_slotR)
        S += getsizeof(self.is_remove_vent)
        S += getsizeof(self.is_mmfs)
        S += getsizeof(self.is_mmfr)
        S += getsizeof(self.type_BH_stator)
        S += getsizeof(self.type_BH_rotor)
        S += getsizeof(self.is_periodicity_t)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.angle_stator_shift)
        S += getsizeof(self.angle_rotor_shift)
        S += getsizeof(self.logger_name)
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

        Magnetics_dict = dict()
        Magnetics_dict["is_remove_slotS"] = self.is_remove_slotS
        Magnetics_dict["is_remove_slotR"] = self.is_remove_slotR
        Magnetics_dict["is_remove_vent"] = self.is_remove_vent
        Magnetics_dict["is_mmfs"] = self.is_mmfs
        Magnetics_dict["is_mmfr"] = self.is_mmfr
        Magnetics_dict["type_BH_stator"] = self.type_BH_stator
        Magnetics_dict["type_BH_rotor"] = self.type_BH_rotor
        Magnetics_dict["is_periodicity_t"] = self.is_periodicity_t
        Magnetics_dict["is_periodicity_a"] = self.is_periodicity_a
        Magnetics_dict["angle_stator_shift"] = self.angle_stator_shift
        Magnetics_dict["angle_rotor_shift"] = self.angle_rotor_shift
        Magnetics_dict["logger_name"] = self.logger_name
        # The class name is added to the dict for deserialisation purpose
        Magnetics_dict["__class__"] = "Magnetics"
        return Magnetics_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_remove_slotS = None
        self.is_remove_slotR = None
        self.is_remove_vent = None
        self.is_mmfs = None
        self.is_mmfr = None
        self.type_BH_stator = None
        self.type_BH_rotor = None
        self.is_periodicity_t = None
        self.is_periodicity_a = None
        self.angle_stator_shift = None
        self.angle_rotor_shift = None
        self.logger_name = None

    def _get_is_remove_slotS(self):
        """getter of is_remove_slotS"""
        return self._is_remove_slotS

    def _set_is_remove_slotS(self, value):
        """setter of is_remove_slotS"""
        check_var("is_remove_slotS", value, "bool")
        self._is_remove_slotS = value

    is_remove_slotS = property(
        fget=_get_is_remove_slotS,
        fset=_set_is_remove_slotS,
        doc=u"""1 to artificially remove stator slotting effects in permeance mmf calculations

        :Type: bool
        """,
    )

    def _get_is_remove_slotR(self):
        """getter of is_remove_slotR"""
        return self._is_remove_slotR

    def _set_is_remove_slotR(self, value):
        """setter of is_remove_slotR"""
        check_var("is_remove_slotR", value, "bool")
        self._is_remove_slotR = value

    is_remove_slotR = property(
        fget=_get_is_remove_slotR,
        fset=_set_is_remove_slotR,
        doc=u"""1 to artificially remove rotor slotting effects in permeance mmf calculations

        :Type: bool
        """,
    )

    def _get_is_remove_vent(self):
        """getter of is_remove_vent"""
        return self._is_remove_vent

    def _set_is_remove_vent(self, value):
        """setter of is_remove_vent"""
        check_var("is_remove_vent", value, "bool")
        self._is_remove_vent = value

    is_remove_vent = property(
        fget=_get_is_remove_vent,
        fset=_set_is_remove_vent,
        doc=u"""1 to artificially remove the ventilations duct

        :Type: bool
        """,
    )

    def _get_is_mmfs(self):
        """getter of is_mmfs"""
        return self._is_mmfs

    def _set_is_mmfs(self, value):
        """setter of is_mmfs"""
        check_var("is_mmfs", value, "bool")
        self._is_mmfs = value

    is_mmfs = property(
        fget=_get_is_mmfs,
        fset=_set_is_mmfs,
        doc=u"""1 to compute the stator magnetomotive force / stator armature magnetic field

        :Type: bool
        """,
    )

    def _get_is_mmfr(self):
        """getter of is_mmfr"""
        return self._is_mmfr

    def _set_is_mmfr(self, value):
        """setter of is_mmfr"""
        check_var("is_mmfr", value, "bool")
        self._is_mmfr = value

    is_mmfr = property(
        fget=_get_is_mmfr,
        fset=_set_is_mmfr,
        doc=u"""1 to compute the rotor magnetomotive force / rotor magnetic field

        :Type: bool
        """,
    )

    def _get_type_BH_stator(self):
        """getter of type_BH_stator"""
        return self._type_BH_stator

    def _set_type_BH_stator(self, value):
        """setter of type_BH_stator"""
        check_var("type_BH_stator", value, "int", Vmin=0, Vmax=2)
        self._type_BH_stator = value

    type_BH_stator = property(
        fget=_get_type_BH_stator,
        fset=_set_type_BH_stator,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)

        :Type: int
        :min: 0
        :max: 2
        """,
    )

    def _get_type_BH_rotor(self):
        """getter of type_BH_rotor"""
        return self._type_BH_rotor

    def _set_type_BH_rotor(self, value):
        """setter of type_BH_rotor"""
        check_var("type_BH_rotor", value, "int", Vmin=0, Vmax=2)
        self._type_BH_rotor = value

    type_BH_rotor = property(
        fget=_get_type_BH_rotor,
        fset=_set_type_BH_rotor,
        doc=u"""0 to use the B(H) curve, 1 to use linear B(H) curve according to mur_lin, 2 to enforce infinite permeability (mur_lin =100000)

        :Type: int
        :min: 0
        :max: 2
        """,
    )

    def _get_is_periodicity_t(self):
        """getter of is_periodicity_t"""
        return self._is_periodicity_t

    def _set_is_periodicity_t(self, value):
        """setter of is_periodicity_t"""
        check_var("is_periodicity_t", value, "bool")
        self._is_periodicity_t = value

    is_periodicity_t = property(
        fget=_get_is_periodicity_t,
        fset=_set_is_periodicity_t,
        doc=u"""True to compute only on one time periodicity (use periodicities defined in output.mag.Time)

        :Type: bool
        """,
    )

    def _get_is_periodicity_a(self):
        """getter of is_periodicity_a"""
        return self._is_periodicity_a

    def _set_is_periodicity_a(self, value):
        """setter of is_periodicity_a"""
        check_var("is_periodicity_a", value, "bool")
        self._is_periodicity_a = value

    is_periodicity_a = property(
        fget=_get_is_periodicity_a,
        fset=_set_is_periodicity_a,
        doc=u"""True to compute only on one angle periodicity (use periodicities defined in output.mag.Angle)

        :Type: bool
        """,
    )

    def _get_angle_stator_shift(self):
        """getter of angle_stator_shift"""
        return self._angle_stator_shift

    def _set_angle_stator_shift(self, value):
        """setter of angle_stator_shift"""
        check_var("angle_stator_shift", value, "float")
        self._angle_stator_shift = value

    angle_stator_shift = property(
        fget=_get_angle_stator_shift,
        fset=_set_angle_stator_shift,
        doc=u"""Shift angle to appy to the stator in magnetic model

        :Type: float
        """,
    )

    def _get_angle_rotor_shift(self):
        """getter of angle_rotor_shift"""
        return self._angle_rotor_shift

    def _set_angle_rotor_shift(self, value):
        """setter of angle_rotor_shift"""
        check_var("angle_rotor_shift", value, "float")
        self._angle_rotor_shift = value

    angle_rotor_shift = property(
        fget=_get_angle_rotor_shift,
        fset=_set_angle_rotor_shift,
        doc=u"""Shift angle to appy to the rotor in magnetic model

        :Type: float
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )
