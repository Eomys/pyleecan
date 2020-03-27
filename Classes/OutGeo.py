# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutGeo.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.OutGeoLam import OutGeoLam


class OutGeo(FrozenClass):
    """Gather the geometrical and the global outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        stator=None,
        rotor=None,
        Wgap_mec=None,
        Wgap_mag=None,
        Rgap_mec=None,
        Lgap=None,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if stator == -1:
            stator = OutGeoLam()
        if rotor == -1:
            rotor = OutGeoLam()
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
        # Initialisation by argument
        self.parent = None
        # stator can be None, a OutGeoLam object or a dict
        if isinstance(stator, dict):
            self.stator = OutGeoLam(init_dict=stator)
        else:
            self.stator = stator
        # rotor can be None, a OutGeoLam object or a dict
        if isinstance(rotor, dict):
            self.rotor = OutGeoLam(init_dict=rotor)
        else:
            self.rotor = rotor
        self.Wgap_mec = Wgap_mec
        self.Wgap_mag = Wgap_mag
        self.Rgap_mec = Rgap_mec
        self.Lgap = Lgap

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

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        check_var("stator", value, "OutGeoLam")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    # Geometry output of the stator
    # Type : OutGeoLam
    stator = property(
        fget=_get_stator, fset=_set_stator, doc=u"""Geometry output of the stator"""
    )

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        check_var("rotor", value, "OutGeoLam")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    # Geometry output of the rotor
    # Type : OutGeoLam
    rotor = property(
        fget=_get_rotor, fset=_set_rotor, doc=u"""Geometry output of the rotor"""
    )

    def _get_Wgap_mec(self):
        """getter of Wgap_mec"""
        return self._Wgap_mec

    def _set_Wgap_mec(self, value):
        """setter of Wgap_mec"""
        check_var("Wgap_mec", value, "float")
        self._Wgap_mec = value

    # mechanical airgap width (minimal distance between the lamination including magnet)
    # Type : float
    Wgap_mec = property(
        fget=_get_Wgap_mec,
        fset=_set_Wgap_mec,
        doc=u"""mechanical airgap width (minimal distance between the lamination including magnet)""",
    )

    def _get_Wgap_mag(self):
        """getter of Wgap_mag"""
        return self._Wgap_mag

    def _set_Wgap_mag(self, value):
        """setter of Wgap_mag"""
        check_var("Wgap_mag", value, "float")
        self._Wgap_mag = value

    # the magnetic airgap width (distance beetween the two Laminations bore radius)
    # Type : float
    Wgap_mag = property(
        fget=_get_Wgap_mag,
        fset=_set_Wgap_mag,
        doc=u"""the magnetic airgap width (distance beetween the two Laminations bore radius)""",
    )

    def _get_Rgap_mec(self):
        """getter of Rgap_mec"""
        return self._Rgap_mec

    def _set_Rgap_mec(self, value):
        """setter of Rgap_mec"""
        check_var("Rgap_mec", value, "float")
        self._Rgap_mec = value

    # radius of the center of the mecanical airgap
    # Type : float
    Rgap_mec = property(
        fget=_get_Rgap_mec,
        fset=_set_Rgap_mec,
        doc=u"""radius of the center of the mecanical airgap""",
    )

    def _get_Lgap(self):
        """getter of Lgap"""
        return self._Lgap

    def _set_Lgap(self, value):
        """setter of Lgap"""
        check_var("Lgap", value, "float")
        self._Lgap = value

    # Airgap active length
    # Type : float
    Lgap = property(fget=_get_Lgap, fset=_set_Lgap, doc=u"""Airgap active length""")
