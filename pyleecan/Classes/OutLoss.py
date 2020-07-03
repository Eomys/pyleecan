# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Output/OutLoss.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from numpy import array, array_equal
from ._check import InitUnKnowClassError


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

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
        Nt_tot=None,
        Plam_stator=None,
        Plam_rotor=None,
        Pwind_stator=None,
        Pwind_rotor=None,
        Pmag_stator=None,
        Pmag_rotor=None,
        Pwindage=None,
        Pbearing=None,
        Pshaft=None,
        Pframe=None,
        Padd=None,
        logger_name="Pyleecan.OutLoss",
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
            Nt_tot = obj.Nt_tot
            Plam_stator = obj.Plam_stator
            Plam_rotor = obj.Plam_rotor
            Pwind_stator = obj.Pwind_stator
            Pwind_rotor = obj.Pwind_rotor
            Pmag_stator = obj.Pmag_stator
            Pmag_rotor = obj.Pmag_rotor
            Pwindage = obj.Pwindage
            Pbearing = obj.Pbearing
            Pshaft = obj.Pshaft
            Pframe = obj.Pframe
            Padd = obj.Padd
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Plam_stator" in list(init_dict.keys()):
                Plam_stator = init_dict["Plam_stator"]
            if "Plam_rotor" in list(init_dict.keys()):
                Plam_rotor = init_dict["Plam_rotor"]
            if "Pwind_stator" in list(init_dict.keys()):
                Pwind_stator = init_dict["Pwind_stator"]
            if "Pwind_rotor" in list(init_dict.keys()):
                Pwind_rotor = init_dict["Pwind_rotor"]
            if "Pmag_stator" in list(init_dict.keys()):
                Pmag_stator = init_dict["Pmag_stator"]
            if "Pmag_rotor" in list(init_dict.keys()):
                Pmag_rotor = init_dict["Pmag_rotor"]
            if "Pwindage" in list(init_dict.keys()):
                Pwindage = init_dict["Pwindage"]
            if "Pbearing" in list(init_dict.keys()):
                Pbearing = init_dict["Pbearing"]
            if "Pshaft" in list(init_dict.keys()):
                Pshaft = init_dict["Pshaft"]
            if "Pframe" in list(init_dict.keys()):
                Pframe = init_dict["Pframe"]
            if "Padd" in list(init_dict.keys()):
                Padd = init_dict["Padd"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        self.Nt_tot = Nt_tot
        # Plam_stator can be None, a ndarray or a list
        set_array(self, "Plam_stator", Plam_stator)
        # Plam_rotor can be None, a ndarray or a list
        set_array(self, "Plam_rotor", Plam_rotor)
        # Pwind_stator can be None, a ndarray or a list
        set_array(self, "Pwind_stator", Pwind_stator)
        # Pwind_rotor can be None, a ndarray or a list
        set_array(self, "Pwind_rotor", Pwind_rotor)
        # Pmag_stator can be None, a ndarray or a list
        set_array(self, "Pmag_stator", Pmag_stator)
        # Pmag_rotor can be None, a ndarray or a list
        set_array(self, "Pmag_rotor", Pmag_rotor)
        # Pwindage can be None, a ndarray or a list
        set_array(self, "Pwindage", Pwindage)
        # Pbearing can be None, a ndarray or a list
        set_array(self, "Pbearing", Pbearing)
        # Pshaft can be None, a ndarray or a list
        set_array(self, "Pshaft", Pshaft)
        # Pframe can be None, a ndarray or a list
        set_array(self, "Pframe", Pframe)
        # Padd can be None, a ndarray or a list
        set_array(self, "Padd", Padd)
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutLoss_str = ""
        if self.parent is None:
            OutLoss_str += "parent = None " + linesep
        else:
            OutLoss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutLoss_str += (
            "time = "
            + linesep
            + str(self.time).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutLoss_str += (
            "Plam_stator = "
            + linesep
            + str(self.Plam_stator).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Plam_rotor = "
            + linesep
            + str(self.Plam_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pwind_stator = "
            + linesep
            + str(self.Pwind_stator).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pwind_rotor = "
            + linesep
            + str(self.Pwind_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pmag_stator = "
            + linesep
            + str(self.Pmag_stator).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pmag_rotor = "
            + linesep
            + str(self.Pmag_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pwindage = "
            + linesep
            + str(self.Pwindage).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pbearing = "
            + linesep
            + str(self.Pbearing).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pshaft = "
            + linesep
            + str(self.Pshaft).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Pframe = "
            + linesep
            + str(self.Pframe).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += (
            "Padd = "
            + linesep
            + str(self.Padd).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if not array_equal(other.Plam_stator, self.Plam_stator):
            return False
        if not array_equal(other.Plam_rotor, self.Plam_rotor):
            return False
        if not array_equal(other.Pwind_stator, self.Pwind_stator):
            return False
        if not array_equal(other.Pwind_rotor, self.Pwind_rotor):
            return False
        if not array_equal(other.Pmag_stator, self.Pmag_stator):
            return False
        if not array_equal(other.Pmag_rotor, self.Pmag_rotor):
            return False
        if not array_equal(other.Pwindage, self.Pwindage):
            return False
        if not array_equal(other.Pbearing, self.Pbearing):
            return False
        if not array_equal(other.Pshaft, self.Pshaft):
            return False
        if not array_equal(other.Pframe, self.Pframe):
            return False
        if not array_equal(other.Padd, self.Padd):
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutLoss_dict = dict()
        if self.time is None:
            OutLoss_dict["time"] = None
        else:
            OutLoss_dict["time"] = self.time.tolist()
        OutLoss_dict["Nt_tot"] = self.Nt_tot
        if self.Plam_stator is None:
            OutLoss_dict["Plam_stator"] = None
        else:
            OutLoss_dict["Plam_stator"] = self.Plam_stator.tolist()
        if self.Plam_rotor is None:
            OutLoss_dict["Plam_rotor"] = None
        else:
            OutLoss_dict["Plam_rotor"] = self.Plam_rotor.tolist()
        if self.Pwind_stator is None:
            OutLoss_dict["Pwind_stator"] = None
        else:
            OutLoss_dict["Pwind_stator"] = self.Pwind_stator.tolist()
        if self.Pwind_rotor is None:
            OutLoss_dict["Pwind_rotor"] = None
        else:
            OutLoss_dict["Pwind_rotor"] = self.Pwind_rotor.tolist()
        if self.Pmag_stator is None:
            OutLoss_dict["Pmag_stator"] = None
        else:
            OutLoss_dict["Pmag_stator"] = self.Pmag_stator.tolist()
        if self.Pmag_rotor is None:
            OutLoss_dict["Pmag_rotor"] = None
        else:
            OutLoss_dict["Pmag_rotor"] = self.Pmag_rotor.tolist()
        if self.Pwindage is None:
            OutLoss_dict["Pwindage"] = None
        else:
            OutLoss_dict["Pwindage"] = self.Pwindage.tolist()
        if self.Pbearing is None:
            OutLoss_dict["Pbearing"] = None
        else:
            OutLoss_dict["Pbearing"] = self.Pbearing.tolist()
        if self.Pshaft is None:
            OutLoss_dict["Pshaft"] = None
        else:
            OutLoss_dict["Pshaft"] = self.Pshaft.tolist()
        if self.Pframe is None:
            OutLoss_dict["Pframe"] = None
        else:
            OutLoss_dict["Pframe"] = self.Pframe.tolist()
        if self.Padd is None:
            OutLoss_dict["Padd"] = None
        else:
            OutLoss_dict["Padd"] = self.Padd.tolist()
        OutLoss_dict["logger_name"] = self.logger_name
        # The class name is added to the dict fordeserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.Nt_tot = None
        self.Plam_stator = None
        self.Plam_rotor = None
        self.Pwind_stator = None
        self.Pwind_rotor = None
        self.Pmag_stator = None
        self.Pmag_rotor = None
        self.Pwindage = None
        self.Pbearing = None
        self.Pshaft = None
        self.Pframe = None
        self.Padd = None
        self.logger_name = None

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

    def _get_Plam_stator(self):
        """getter of Plam_stator"""
        return self._Plam_stator

    def _set_Plam_stator(self, value):
        """setter of Plam_stator"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Plam_stator", value, "ndarray")
        self._Plam_stator = value

    # Stator Lamination Losses
    # Type : ndarray
    Plam_stator = property(
        fget=_get_Plam_stator,
        fset=_set_Plam_stator,
        doc=u"""Stator Lamination Losses""",
    )

    def _get_Plam_rotor(self):
        """getter of Plam_rotor"""
        return self._Plam_rotor

    def _set_Plam_rotor(self, value):
        """setter of Plam_rotor"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Plam_rotor", value, "ndarray")
        self._Plam_rotor = value

    # Rotor Lamination Losses
    # Type : ndarray
    Plam_rotor = property(
        fget=_get_Plam_rotor, fset=_set_Plam_rotor, doc=u"""Rotor Lamination Losses"""
    )

    def _get_Pwind_stator(self):
        """getter of Pwind_stator"""
        return self._Pwind_stator

    def _set_Pwind_stator(self, value):
        """setter of Pwind_stator"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pwind_stator", value, "ndarray")
        self._Pwind_stator = value

    # Stator Winding Losses
    # Type : ndarray
    Pwind_stator = property(
        fget=_get_Pwind_stator, fset=_set_Pwind_stator, doc=u"""Stator Winding Losses"""
    )

    def _get_Pwind_rotor(self):
        """getter of Pwind_rotor"""
        return self._Pwind_rotor

    def _set_Pwind_rotor(self, value):
        """setter of Pwind_rotor"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pwind_rotor", value, "ndarray")
        self._Pwind_rotor = value

    # Rotor Winding Losses
    # Type : ndarray
    Pwind_rotor = property(
        fget=_get_Pwind_rotor, fset=_set_Pwind_rotor, doc=u"""Rotor Winding Losses"""
    )

    def _get_Pmag_stator(self):
        """getter of Pmag_stator"""
        return self._Pmag_stator

    def _set_Pmag_stator(self, value):
        """setter of Pmag_stator"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pmag_stator", value, "ndarray")
        self._Pmag_stator = value

    # Stator Magnet Losses
    # Type : ndarray
    Pmag_stator = property(
        fget=_get_Pmag_stator, fset=_set_Pmag_stator, doc=u"""Stator Magnet Losses"""
    )

    def _get_Pmag_rotor(self):
        """getter of Pmag_rotor"""
        return self._Pmag_rotor

    def _set_Pmag_rotor(self, value):
        """setter of Pmag_rotor"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pmag_rotor", value, "ndarray")
        self._Pmag_rotor = value

    # Rotor Magnet Losses
    # Type : ndarray
    Pmag_rotor = property(
        fget=_get_Pmag_rotor, fset=_set_Pmag_rotor, doc=u"""Rotor Magnet Losses"""
    )

    def _get_Pwindage(self):
        """getter of Pwindage"""
        return self._Pwindage

    def _set_Pwindage(self, value):
        """setter of Pwindage"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pwindage", value, "ndarray")
        self._Pwindage = value

    # Windage Losses
    # Type : ndarray
    Pwindage = property(
        fget=_get_Pwindage, fset=_set_Pwindage, doc=u"""Windage Losses"""
    )

    def _get_Pbearing(self):
        """getter of Pbearing"""
        return self._Pbearing

    def _set_Pbearing(self, value):
        """setter of Pbearing"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pbearing", value, "ndarray")
        self._Pbearing = value

    # Bearing Losses
    # Type : ndarray
    Pbearing = property(
        fget=_get_Pbearing, fset=_set_Pbearing, doc=u"""Bearing Losses"""
    )

    def _get_Pshaft(self):
        """getter of Pshaft"""
        return self._Pshaft

    def _set_Pshaft(self, value):
        """setter of Pshaft"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pshaft", value, "ndarray")
        self._Pshaft = value

    # Shaft Iron Losses
    # Type : ndarray
    Pshaft = property(fget=_get_Pshaft, fset=_set_Pshaft, doc=u"""Shaft Iron Losses""")

    def _get_Pframe(self):
        """getter of Pframe"""
        return self._Pframe

    def _set_Pframe(self, value):
        """setter of Pframe"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pframe", value, "ndarray")
        self._Pframe = value

    # Frame Iron Losses
    # Type : ndarray
    Pframe = property(fget=_get_Pframe, fset=_set_Pframe, doc=u"""Frame Iron Losses""")

    def _get_Padd(self):
        """getter of Padd"""
        return self._Padd

    def _set_Padd(self, value):
        """setter of Padd"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Padd", value, "ndarray")
        self._Padd = value

    # Additional Losses
    # Type : ndarray
    Padd = property(fget=_get_Padd, fset=_set_Padd, doc=u"""Additional Losses""")

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
