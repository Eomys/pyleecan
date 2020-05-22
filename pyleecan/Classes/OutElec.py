# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Output/OutElec.csv
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


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        time=None,
        angle=None,
        Is=None,
        Ir=None,
        angle_rotor=None,
        Nr=None,
        rot_dir=-1,
        angle_rotor_initial=0,
        logger_name="Pyleecan.OutElec",
        mmf_unit=None,
        EEC_dict={},
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "Nr" in list(init_dict.keys()):
                Nr = init_dict["Nr"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "mmf_unit" in list(init_dict.keys()):
                mmf_unit = init_dict["mmf_unit"]
            if "EEC_dict" in list(init_dict.keys()):
                EEC_dict = init_dict["EEC_dict"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        # Is can be None, a ndarray or a list
        set_array(self, "Is", Is)
        # Ir can be None, a ndarray or a list
        set_array(self, "Ir", Ir)
        # angle_rotor can be None, a ndarray or a list
        set_array(self, "angle_rotor", angle_rotor)
        # Nr can be None, a ndarray or a list
        set_array(self, "Nr", Nr)
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.logger_name = logger_name
        # Check if the type DataND has been imported with success
        if isinstance(DataND, ImportError):
            raise ImportError("Unknown type DataND please install SciDataTool")
        self.mmf_unit = mmf_unit
        self.EEC_dict = EEC_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutElec_str = ""
        if self.parent is None:
            OutElec_str += "parent = None " + linesep
        else:
            OutElec_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutElec_str += (
            "time = "
            + linesep
            + str(self.time).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "angle = "
            + linesep
            + str(self.angle).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "Is = "
            + linesep
            + str(self.Is).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "Ir = "
            + linesep
            + str(self.Ir).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "angle_rotor = "
            + linesep
            + str(self.angle_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "Nr = "
            + linesep
            + str(self.Nr).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += "rot_dir = " + str(self.rot_dir) + linesep
        OutElec_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        OutElec_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutElec_str += "mmf_unit = " + str(self.mmf_unit) + linesep + linesep
        OutElec_str += "EEC_dict = " + str(self.EEC_dict) + linesep
        return OutElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if not array_equal(other.angle, self.angle):
            return False
        if not array_equal(other.Is, self.Is):
            return False
        if not array_equal(other.Ir, self.Ir):
            return False
        if not array_equal(other.angle_rotor, self.angle_rotor):
            return False
        if not array_equal(other.Nr, self.Nr):
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.mmf_unit != self.mmf_unit:
            return False
        if other.EEC_dict != self.EEC_dict:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutElec_dict = dict()
        if self.time is None:
            OutElec_dict["time"] = None
        else:
            OutElec_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutElec_dict["angle"] = None
        else:
            OutElec_dict["angle"] = self.angle.tolist()
        if self.Is is None:
            OutElec_dict["Is"] = None
        else:
            OutElec_dict["Is"] = self.Is.tolist()
        if self.Ir is None:
            OutElec_dict["Ir"] = None
        else:
            OutElec_dict["Ir"] = self.Ir.tolist()
        if self.angle_rotor is None:
            OutElec_dict["angle_rotor"] = None
        else:
            OutElec_dict["angle_rotor"] = self.angle_rotor.tolist()
        if self.Nr is None:
            OutElec_dict["Nr"] = None
        else:
            OutElec_dict["Nr"] = self.Nr.tolist()
        OutElec_dict["rot_dir"] = self.rot_dir
        OutElec_dict["angle_rotor_initial"] = self.angle_rotor_initial
        OutElec_dict["logger_name"] = self.logger_name
        if self.mmf_unit is None:
            OutElec_dict["mmf_unit"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutElec_dict["mmf_unit"] = {
                "__class__": str(type(self._mmf_unit)),
                "__repr__": str(self._mmf_unit.__repr__()),
                "serialized": dumps(self._mmf_unit).decode("ISO-8859-2"),
            }
        OutElec_dict["EEC_dict"] = self.EEC_dict
        # The class name is added to the dict fordeserialisation purpose
        OutElec_dict["__class__"] = "OutElec"
        return OutElec_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Is = None
        self.Ir = None
        self.angle_rotor = None
        self.Nr = None
        self.rot_dir = None
        self.angle_rotor_initial = None
        self.logger_name = None
        self.mmf_unit = None
        self.EEC_dict = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("time", value, "ndarray")
        self._time = value

    # Electrical time vector (no symmetry)
    # Type : ndarray
    time = property(
        fget=_get_time, fset=_set_time, doc=u"""Electrical time vector (no symmetry)"""
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle", value, "ndarray")
        self._angle = value

    # Electrical position vector (no symmetry)
    # Type : ndarray
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry)""",
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Is", value, "ndarray")
        self._Is = value

    # Stator currents as a function of time (each column correspond to one phase)
    # Type : ndarray
    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase)""",
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ir", value, "ndarray")
        self._Ir = value

    # Rotor currents as a function of time (each column correspond to one phase)
    # Type : ndarray
    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase)""",
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_rotor", value, "ndarray")
        self._angle_rotor = value

    # Rotor angular position as a function of time (if None computed according to Nr)
    # Type : ndarray
    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr)""",
    )

    def _get_Nr(self):
        """getter of Nr"""
        return self._Nr

    def _set_Nr(self, value):
        """setter of Nr"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Nr", value, "ndarray")
        self._Nr = value

    # Rotor speed as a function of time
    # Type : ndarray
    Nr = property(
        fget=_get_Nr, fset=_set_Nr, doc=u"""Rotor speed as a function of time"""
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    # Rotation direction of the rotor 1 trigo, -1 clockwise
    # Type : float, min = -1, max = 1
    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise""",
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    # Initial angular position of the rotor at t=0
    # Type : float
    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0""",
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

    def _get_mmf_unit(self):
        """getter of mmf_unit"""
        return self._mmf_unit

    def _set_mmf_unit(self, value):
        """setter of mmf_unit"""
        try:  # Check the type
            check_var("mmf_unit", value, "dict")
        except CheckTypeError:
            check_var("mmf_unit", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._mmf_unit = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._mmf_unit = value

    # Unit magnetomotive force
    # Type : SciDataTool.Classes.DataND.DataND
    mmf_unit = property(
        fget=_get_mmf_unit, fset=_set_mmf_unit, doc=u"""Unit magnetomotive force"""
    )

    def _get_EEC_dict(self):
        """getter of EEC_dict"""
        return self._EEC_dict

    def _set_EEC_dict(self, value):
        """setter of EEC_dict"""
        check_var("EEC_dict", value, "dict")
        self._EEC_dict = value

    # Dictionary of the Electrical Equivalent Circuit
    # Type : dict
    EEC_dict = property(
        fget=_get_EEC_dict,
        fset=_set_EEC_dict,
        doc=u"""Dictionary of the Electrical Equivalent Circuit""",
    )
