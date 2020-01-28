# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutStruct.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
import numpy
from pyleecan.Classes._check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from numpy import array, array_equal
from pyleecan.Classes._check import InitUnKnowClassError


class OutStruct(FrozenClass):
    """Gather the structural module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=None,
        Na_tot=None,
        Prad=None,
        Ptan=None,
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
                init_dict, ["time", "angle", "Nt_tot", "Na_tot", "Prad", "Ptan"]
            )
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "Prad" in list(init_dict.keys()):
                Prad = init_dict["Prad"]
            if "Ptan" in list(init_dict.keys()):
                Ptan = init_dict["Ptan"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot
        # Prad can be None, a ndarray or a list
        set_array(self, "Prad", Prad)
        # Ptan can be None, a ndarray or a list
        set_array(self, "Ptan", Ptan)

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutStruct_str = ""
        if self.parent is None:
            OutStruct_str += "parent = None " + linesep
        else:
            OutStruct_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutStruct_str += "time = " + linesep + str(self.time) + linesep + linesep
        OutStruct_str += "angle = " + linesep + str(self.angle) + linesep + linesep
        OutStruct_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutStruct_str += "Na_tot = " + str(self.Na_tot) + linesep
        OutStruct_str += "Prad = " + linesep + str(self.Prad) + linesep + linesep
        OutStruct_str += "Ptan = " + linesep + str(self.Ptan)
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
        if not array_equal(other.Prad, self.Prad):
            return False
        if not array_equal(other.Ptan, self.Ptan):
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
        if self.Prad is None:
            OutStruct_dict["Prad"] = None
        else:
            OutStruct_dict["Prad"] = self.Prad.tolist()
        if self.Ptan is None:
            OutStruct_dict["Ptan"] = None
        else:
            OutStruct_dict["Ptan"] = self.Ptan.tolist()
        # The class name is added to the dict fordeserialisation purpose
        OutStruct_dict["__class__"] = "OutStruct"
        return OutStruct_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Nt_tot = None
        self.Na_tot = None
        self.Prad = None
        self.Ptan = None

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
        if type(value) is list:
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

    def _get_Prad(self):
        """getter of Prad"""
        return self._Prad

    def _set_Prad(self, value):
        """setter of Prad"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Prad", value, "ndarray")
        self._Prad = value

    # Radial magnetic air-gap surface force
    # Type : ndarray
    Prad = property(
        fget=_get_Prad, fset=_set_Prad, doc=u"""Radial magnetic air-gap surface force"""
    )

    def _get_Ptan(self):
        """getter of Ptan"""
        return self._Ptan

    def _set_Ptan(self, value):
        """setter of Ptan"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ptan", value, "ndarray")
        self._Ptan = value

    # Tangential magnetic air-gap surface force
    # Type : ndarray
    Ptan = property(
        fget=_get_Ptan,
        fset=_set_Ptan,
        doc=u"""Tangential magnetic air-gap surface force""",
    )
