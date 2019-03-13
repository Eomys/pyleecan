# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from numpy import array
from pyleecan.Classes.check import InitUnKnowClassError


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        time=None,
        angle=None,
        Is=None,
        Ir=None,
        angle_rotor=None,
        Nr=None,
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
            check_init_dict(
                init_dict, ["time", "angle", "Is", "Ir", "angle_rotor", "Nr"]
            )
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

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutElec_str = ""
        if self.parent is None:
            OutElec_str += "parent = None " + linesep
        else:
            OutElec_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutElec_str += "time = " + linesep + str(self.time) + linesep + linesep
        OutElec_str += "angle = " + linesep + str(self.angle) + linesep + linesep
        OutElec_str += "Is = " + linesep + str(self.Is) + linesep + linesep
        OutElec_str += "Ir = " + linesep + str(self.Ir) + linesep + linesep
        OutElec_str += (
            "angle_rotor = " + linesep + str(self.angle_rotor) + linesep + linesep
        )
        OutElec_str += "Nr = " + linesep + str(self.Nr)
        return OutElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.Nr != self.Nr:
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
