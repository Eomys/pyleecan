# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from numpy import array
from pyleecan.Classes.check import InitUnKnowClassError


class OutMag(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        time=None,
        angle=None,
        Br=None,
        Bt=None,
        Nt_tot=None,
        Na_tot=None,
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
                init_dict, ["time", "angle", "Br", "Bt", "Nt_tot", "Na_tot"]
            )
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Br" in list(init_dict.keys()):
                Br = init_dict["Br"]
            if "Bt" in list(init_dict.keys()):
                Bt = init_dict["Bt"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        # Br can be None, a ndarray or a list
        set_array(self, "Br", Br)
        # Bt can be None, a ndarray or a list
        set_array(self, "Bt", Bt)
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutMag_str = ""
        if self.parent is None:
            OutMag_str += "parent = None " + linesep
        else:
            OutMag_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutMag_str += "time = " + linesep + str(self.time) + linesep + linesep
        OutMag_str += "angle = " + linesep + str(self.angle) + linesep + linesep
        OutMag_str += "Br = " + linesep + str(self.Br) + linesep + linesep
        OutMag_str += "Bt = " + linesep + str(self.Bt) + linesep + linesep
        OutMag_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutMag_str += "Na_tot = " + str(self.Na_tot)
        return OutMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Br != self.Br:
            return False
        if other.Bt != self.Bt:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutMag_dict = dict()
        if self.time is None:
            OutMag_dict["time"] = None
        else:
            OutMag_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutMag_dict["angle"] = None
        else:
            OutMag_dict["angle"] = self.angle.tolist()
        if self.Br is None:
            OutMag_dict["Br"] = None
        else:
            OutMag_dict["Br"] = self.Br.tolist()
        if self.Bt is None:
            OutMag_dict["Bt"] = None
        else:
            OutMag_dict["Bt"] = self.Bt.tolist()
        OutMag_dict["Nt_tot"] = self.Nt_tot
        OutMag_dict["Na_tot"] = self.Na_tot
        # The class name is added to the dict fordeserialisation purpose
        OutMag_dict["__class__"] = "OutMag"
        return OutMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Br = None
        self.Bt = None
        self.Nt_tot = None
        self.Na_tot = None

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

    # Magnetic time vector (no symmetry)
    # Type : ndarray
    time = property(
        fget=_get_time, fset=_set_time, doc=u"""Magnetic time vector (no symmetry)"""
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

    # Magnetic position vector (no symmetry)
    # Type : ndarray
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Magnetic position vector (no symmetry)""",
    )

    def _get_Br(self):
        """getter of Br"""
        return self._Br

    def _set_Br(self, value):
        """setter of Br"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Br", value, "ndarray")
        self._Br = value

    # Radial airgap flux
    # Type : ndarray
    Br = property(fget=_get_Br, fset=_set_Br, doc=u"""Radial airgap flux""")

    def _get_Bt(self):
        """getter of Bt"""
        return self._Bt

    def _set_Bt(self, value):
        """setter of Bt"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Bt", value, "ndarray")
        self._Bt = value

    # Tanfential airgap flux
    # Type : ndarray
    Bt = property(fget=_get_Bt, fset=_set_Bt, doc=u"""Tanfential airgap flux""")

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
