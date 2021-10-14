# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutGeo.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutGeo
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

from ._check import InitUnKnowClassError
from .OutGeoLam import OutGeoLam


class OutGeo(FrozenClass):
    """Gather the geometrical and the global outputs"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        stator=None,
        rotor=None,
        Wgap_mec=None,
        Wgap_mag=None,
        Rgap_mec=None,
        Lgap=None,
        logger_name="Pyleecan.OutGeo",
        angle_offset_initial=None,
        rot_dir=None,
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
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "Wgap_mec" in list(init_dict.keys()):
                Wgap_mec = init_dict["Wgap_mec"]
            if "Wgap_mag" in list(init_dict.keys()):
                Wgap_mag = init_dict["Wgap_mag"]
            if "Rgap_mec" in list(init_dict.keys()):
                Rgap_mec = init_dict["Rgap_mec"]
            if "Lgap" in list(init_dict.keys()):
                Lgap = init_dict["Lgap"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "angle_offset_initial" in list(init_dict.keys()):
                angle_offset_initial = init_dict["angle_offset_initial"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
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
        self.stator = stator
        self.rotor = rotor
        self.Wgap_mec = Wgap_mec
        self.Wgap_mag = Wgap_mag
        self.Rgap_mec = Rgap_mec
        self.Lgap = Lgap
        self.logger_name = logger_name
        self.angle_offset_initial = angle_offset_initial
        self.rot_dir = rot_dir
        self.per_a = per_a
        self.is_antiper_a = is_antiper_a
        self.per_t = per_t
        self.is_antiper_t = is_antiper_t

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutGeo_str = ""
        if self.parent is None:
            OutGeo_str += "parent = None " + linesep
        else:
            OutGeo_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutGeo_str += "stator = " + tmp
        else:
            OutGeo_str += "stator = None" + linesep + linesep
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutGeo_str += "rotor = " + tmp
        else:
            OutGeo_str += "rotor = None" + linesep + linesep
        OutGeo_str += "Wgap_mec = " + str(self.Wgap_mec) + linesep
        OutGeo_str += "Wgap_mag = " + str(self.Wgap_mag) + linesep
        OutGeo_str += "Rgap_mec = " + str(self.Rgap_mec) + linesep
        OutGeo_str += "Lgap = " + str(self.Lgap) + linesep
        OutGeo_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutGeo_str += (
            "angle_offset_initial = " + str(self.angle_offset_initial) + linesep
        )
        OutGeo_str += "rot_dir = " + str(self.rot_dir) + linesep
        OutGeo_str += "per_a = " + str(self.per_a) + linesep
        OutGeo_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        OutGeo_str += "per_t = " + str(self.per_t) + linesep
        OutGeo_str += "is_antiper_t = " + str(self.is_antiper_t) + linesep
        return OutGeo_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.stator != self.stator:
            return False
        if other.rotor != self.rotor:
            return False
        if other.Wgap_mec != self.Wgap_mec:
            return False
        if other.Wgap_mag != self.Wgap_mag:
            return False
        if other.Rgap_mec != self.Rgap_mec:
            return False
        if other.Lgap != self.Lgap:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.angle_offset_initial != self.angle_offset_initial:
            return False
        if other.rot_dir != self.rot_dir:
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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.stator is None and self.stator is not None) or (
            other.stator is not None and self.stator is None
        ):
            diff_list.append(name + ".stator None mismatch")
        elif self.stator is not None:
            diff_list.extend(self.stator.compare(other.stator, name=name + ".stator"))
        if (other.rotor is None and self.rotor is not None) or (
            other.rotor is not None and self.rotor is None
        ):
            diff_list.append(name + ".rotor None mismatch")
        elif self.rotor is not None:
            diff_list.extend(self.rotor.compare(other.rotor, name=name + ".rotor"))
        if other._Wgap_mec != self._Wgap_mec:
            diff_list.append(name + ".Wgap_mec")
        if other._Wgap_mag != self._Wgap_mag:
            diff_list.append(name + ".Wgap_mag")
        if other._Rgap_mec != self._Rgap_mec:
            diff_list.append(name + ".Rgap_mec")
        if other._Lgap != self._Lgap:
            diff_list.append(name + ".Lgap")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if other._angle_offset_initial != self._angle_offset_initial:
            diff_list.append(name + ".angle_offset_initial")
        if other._rot_dir != self._rot_dir:
            diff_list.append(name + ".rot_dir")
        if other._per_a != self._per_a:
            diff_list.append(name + ".per_a")
        if other._is_antiper_a != self._is_antiper_a:
            diff_list.append(name + ".is_antiper_a")
        if other._per_t != self._per_t:
            diff_list.append(name + ".per_t")
        if other._is_antiper_t != self._is_antiper_t:
            diff_list.append(name + ".is_antiper_t")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.stator)
        S += getsizeof(self.rotor)
        S += getsizeof(self.Wgap_mec)
        S += getsizeof(self.Wgap_mag)
        S += getsizeof(self.Rgap_mec)
        S += getsizeof(self.Lgap)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.angle_offset_initial)
        S += getsizeof(self.rot_dir)
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

        OutGeo_dict = dict()
        if self.stator is None:
            OutGeo_dict["stator"] = None
        else:
            OutGeo_dict["stator"] = self.stator.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.rotor is None:
            OutGeo_dict["rotor"] = None
        else:
            OutGeo_dict["rotor"] = self.rotor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutGeo_dict["Wgap_mec"] = self.Wgap_mec
        OutGeo_dict["Wgap_mag"] = self.Wgap_mag
        OutGeo_dict["Rgap_mec"] = self.Rgap_mec
        OutGeo_dict["Lgap"] = self.Lgap
        OutGeo_dict["logger_name"] = self.logger_name
        OutGeo_dict["angle_offset_initial"] = self.angle_offset_initial
        OutGeo_dict["rot_dir"] = self.rot_dir
        OutGeo_dict["per_a"] = self.per_a
        OutGeo_dict["is_antiper_a"] = self.is_antiper_a
        OutGeo_dict["per_t"] = self.per_t
        OutGeo_dict["is_antiper_t"] = self.is_antiper_t
        # The class name is added to the dict for deserialisation purpose
        OutGeo_dict["__class__"] = "OutGeo"
        return OutGeo_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.stator is not None:
            self.stator._set_None()
        if self.rotor is not None:
            self.rotor._set_None()
        self.Wgap_mec = None
        self.Wgap_mag = None
        self.Rgap_mec = None
        self.Lgap = None
        self.logger_name = None
        self.angle_offset_initial = None
        self.rot_dir = None
        self.per_a = None
        self.is_antiper_a = None
        self.per_t = None
        self.is_antiper_t = None

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = OutGeoLam()
        check_var("stator", value, "OutGeoLam")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    stator = property(
        fget=_get_stator,
        fset=_set_stator,
        doc=u"""Geometry output of the stator

        :Type: OutGeoLam
        """,
    )

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = OutGeoLam()
        check_var("rotor", value, "OutGeoLam")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    rotor = property(
        fget=_get_rotor,
        fset=_set_rotor,
        doc=u"""Geometry output of the rotor

        :Type: OutGeoLam
        """,
    )

    def _get_Wgap_mec(self):
        """getter of Wgap_mec"""
        return self._Wgap_mec

    def _set_Wgap_mec(self, value):
        """setter of Wgap_mec"""
        check_var("Wgap_mec", value, "float")
        self._Wgap_mec = value

    Wgap_mec = property(
        fget=_get_Wgap_mec,
        fset=_set_Wgap_mec,
        doc=u"""mechanical airgap width (minimal distance between the lamination including magnet)

        :Type: float
        """,
    )

    def _get_Wgap_mag(self):
        """getter of Wgap_mag"""
        return self._Wgap_mag

    def _set_Wgap_mag(self, value):
        """setter of Wgap_mag"""
        check_var("Wgap_mag", value, "float")
        self._Wgap_mag = value

    Wgap_mag = property(
        fget=_get_Wgap_mag,
        fset=_set_Wgap_mag,
        doc=u"""the magnetic airgap width (distance beetween the two Laminations bore radius)

        :Type: float
        """,
    )

    def _get_Rgap_mec(self):
        """getter of Rgap_mec"""
        return self._Rgap_mec

    def _set_Rgap_mec(self, value):
        """setter of Rgap_mec"""
        check_var("Rgap_mec", value, "float")
        self._Rgap_mec = value

    Rgap_mec = property(
        fget=_get_Rgap_mec,
        fset=_set_Rgap_mec,
        doc=u"""radius of the center of the mecanical airgap

        :Type: float
        """,
    )

    def _get_Lgap(self):
        """getter of Lgap"""
        return self._Lgap

    def _set_Lgap(self, value):
        """setter of Lgap"""
        check_var("Lgap", value, "float")
        self._Lgap = value

    Lgap = property(
        fget=_get_Lgap,
        fset=_set_Lgap,
        doc=u"""Airgap active length

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

    def _get_angle_offset_initial(self):
        """getter of angle_offset_initial"""
        return self._angle_offset_initial

    def _set_angle_offset_initial(self, value):
        """setter of angle_offset_initial"""
        check_var("angle_offset_initial", value, "float")
        self._angle_offset_initial = value

    angle_offset_initial = property(
        fget=_get_angle_offset_initial,
        fset=_set_angle_offset_initial,
        doc=u"""Difference between the d axis angle of the stator and the rotor

        :Type: float
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "int", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""rotation direction of the magnetic field fundamental !! WARNING: rot_dir = -1 to have positive rotor rotating direction, i.e. rotor position moves towards positive angle

        :Type: int
        :min: -1
        :max: 1
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
        doc=u"""Number of spatial periodicities of the machine

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
        doc=u"""Number of time periodicities of the machine

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
