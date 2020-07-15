# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Output/OutStruct.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from numpy import array, array_equal
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from SciDataTool.Classes.DataND import DataND
except ImportError:
    DataND = ImportError
from ._check import InitUnKnowClassError


class OutStruct(FrozenClass):
    """Gather the structural module outputs"""

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
        time=None,
        angle=None,
        Nt_tot=None,
        Na_tot=None,
        logger_name="Pyleecan.OutStruct",
        Yr=None,
        Vr=None,
        Ar=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Na_tot = obj.Na_tot
            logger_name = obj.logger_name
            Yr = obj.Yr
            Vr = obj.Vr
            Ar = obj.Ar
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Yr" in list(init_dict.keys()):
                Yr = init_dict["Yr"]
            if "Vr" in list(init_dict.keys()):
                Vr = init_dict["Vr"]
            if "Ar" in list(init_dict.keys()):
                Ar = init_dict["Ar"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot
        self.logger_name = logger_name
        # Check if the type DataND has been imported with success
        if isinstance(DataND, ImportError):
            raise ImportError("Unknown type DataND please install SciDataTool")
        self.Yr = Yr
        self.Vr = Vr
        self.Ar = Ar

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutStruct_str = ""
        if self.parent is None:
            OutStruct_str += "parent = None " + linesep
        else:
            OutStruct_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutStruct_str += (
            "time = "
            + linesep
            + str(self.time).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutStruct_str += (
            "angle = "
            + linesep
            + str(self.angle).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutStruct_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutStruct_str += "Na_tot = " + str(self.Na_tot) + linesep
        OutStruct_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutStruct_str += "Yr = " + str(self.Yr) + linesep + linesep
        OutStruct_str += "Vr = " + str(self.Vr) + linesep + linesep
        OutStruct_str += "Ar = " + str(self.Ar) + linesep + linesep
        return OutStruct_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if not array_equal(other.angle, self.angle):
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.Yr != self.Yr:
            return False
        if other.Vr != self.Vr:
            return False
        if other.Ar != self.Ar:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutStruct_dict = dict()
        if self.time is None:
            OutStruct_dict["time"] = None
        else:
            OutStruct_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutStruct_dict["angle"] = None
        else:
            OutStruct_dict["angle"] = self.angle.tolist()
        OutStruct_dict["Nt_tot"] = self.Nt_tot
        OutStruct_dict["Na_tot"] = self.Na_tot
        OutStruct_dict["logger_name"] = self.logger_name
        if self.Yr is None:
            OutStruct_dict["Yr"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutStruct_dict["Yr"] = {
                "__class__": str(type(self._Yr)),
                "__repr__": str(self._Yr.__repr__()),
                "serialized": dumps(self._Yr).decode("ISO-8859-2"),
            }
        if self.Vr is None:
            OutStruct_dict["Vr"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutStruct_dict["Vr"] = {
                "__class__": str(type(self._Vr)),
                "__repr__": str(self._Vr.__repr__()),
                "serialized": dumps(self._Vr).decode("ISO-8859-2"),
            }
        if self.Ar is None:
            OutStruct_dict["Ar"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutStruct_dict["Ar"] = {
                "__class__": str(type(self._Ar)),
                "__repr__": str(self._Ar.__repr__()),
                "serialized": dumps(self._Ar).decode("ISO-8859-2"),
            }
        # The class name is added to the dict fordeserialisation purpose
        OutStruct_dict["__class__"] = "OutStruct"
        return OutStruct_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Nt_tot = None
        self.Na_tot = None
        self.logger_name = None
        self.Yr = None
        self.Vr = None
        self.Ar = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("time", value, "ndarray")
        self._time = value

    # Structural time vector (no symmetry)
    # Type : ndarray
    time = property(
        fget=_get_time, fset=_set_time, doc=u"""Structural time vector (no symmetry)"""
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle", value, "ndarray")
        self._angle = value

    # Structural position vector (no symmetry)
    # Type : ndarray
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Structural position vector (no symmetry)""",
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    # Length of the time vector
    # Type : int
    Nt_tot = property(
        fget=_get_Nt_tot, fset=_set_Nt_tot, doc=u"""Length of the time vector"""
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int")
        self._Na_tot = value

    # Length of the angle vector
    # Type : int
    Na_tot = property(
        fget=_get_Na_tot, fset=_set_Na_tot, doc=u"""Length of the angle vector"""
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    # Name of the logger to use
    # Type : str
    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use""",
    )

    def _get_Yr(self):
        """getter of Yr"""
        return self._Yr

    def _set_Yr(self, value):
        """setter of Yr"""
        try:  # Check the type
            check_var("Yr", value, "dict")
        except CheckTypeError:
            check_var("Yr", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Yr = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._Yr = value

    # Displacement output
    # Type : SciDataTool.Classes.DataND.DataND
    Yr = property(fget=_get_Yr, fset=_set_Yr, doc=u"""Displacement output""")

    def _get_Vr(self):
        """getter of Vr"""
        return self._Vr

    def _set_Vr(self, value):
        """setter of Vr"""
        try:  # Check the type
            check_var("Vr", value, "dict")
        except CheckTypeError:
            check_var("Vr", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Vr = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._Vr = value

    # Velocity output
    # Type : SciDataTool.Classes.DataND.DataND
    Vr = property(fget=_get_Vr, fset=_set_Vr, doc=u"""Velocity output""")

    def _get_Ar(self):
        """getter of Ar"""
        return self._Ar

    def _set_Ar(self, value):
        """setter of Ar"""
        try:  # Check the type
            check_var("Ar", value, "dict")
        except CheckTypeError:
            check_var("Ar", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Ar = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._Ar = value

    # Acceleration output
    # Type : SciDataTool.Classes.DataND.DataND
    Ar = property(fget=_get_Ar, fset=_set_Ar, doc=u"""Acceleration output""")
