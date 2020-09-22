# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutGeo.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutGeo
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError
from .OutGeoLam import OutGeoLam


class OutGeo(FrozenClass):
    """Gather the geometrical and the global outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

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
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutGeo_dict = dict()
        if self.stator is None:
            OutGeo_dict["stator"] = None
        else:
            OutGeo_dict["stator"] = self.stator.as_dict()
        if self.rotor is None:
            OutGeo_dict["rotor"] = None
        else:
            OutGeo_dict["rotor"] = self.rotor.as_dict()
        OutGeo_dict["Wgap_mec"] = self.Wgap_mec
        OutGeo_dict["Wgap_mag"] = self.Wgap_mag
        OutGeo_dict["Rgap_mec"] = self.Rgap_mec
        OutGeo_dict["Lgap"] = self.Lgap
        OutGeo_dict["logger_name"] = self.logger_name
        OutGeo_dict["angle_offset_initial"] = self.angle_offset_initial
        OutGeo_dict["rot_dir"] = self.rot_dir
        # The class name is added to the dict fordeserialisation purpose
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

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator"
            )
            value = class_obj(init_dict=value)
        elif value == -1:  # Default constructor
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
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor"
            )
            value = class_obj(init_dict=value)
        elif value == -1:  # Default constructor
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
        doc=u"""Rotation direction

        :Type: int
        :min: -1
        :max: 1
        """,
    )
