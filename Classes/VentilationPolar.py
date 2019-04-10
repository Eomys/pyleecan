# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Hole import Hole

from pyleecan.Methods.Slot.VentilationPolar.build_geometry import build_geometry
from pyleecan.Methods.Slot.VentilationPolar.check import check
from pyleecan.Methods.Slot.VentilationPolar.comp_radius import comp_radius
from pyleecan.Methods.Slot.VentilationPolar.comp_surface import comp_surface
from pyleecan.Methods.Slot.VentilationPolar.get_center import get_center

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class VentilationPolar(Hole):
    """Polar axial ventilation duct"""

    VERSION = 1

    # cf Methods.Slot.VentilationPolar.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.VentilationPolar.check
    check = check
    # cf Methods.Slot.VentilationPolar.comp_radius
    comp_radius = comp_radius
    # cf Methods.Slot.VentilationPolar.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.VentilationPolar.get_center
    get_center = get_center
    # save method is available in all object
    save = save

    def __init__(self, Alpha0=0, D0=1, H0=1, W1=1, Zh=36, mat_void=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_void == -1:
            mat_void = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Alpha0", "D0", "H0", "W1", "Zh", "mat_void"])
            # Overwrite default value with init_dict content
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
            if "D0" in list(init_dict.keys()):
                D0 = init_dict["D0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.Alpha0 = Alpha0
        self.D0 = D0
        self.H0 = H0
        self.W1 = W1
        # Call Hole init
        super(VentilationPolar, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        VentilationPolar_str = ""
        # Get the properties inherited from Hole
        VentilationPolar_str += super(VentilationPolar, self).__str__() + linesep
        VentilationPolar_str += "Alpha0 = " + str(self.Alpha0) + linesep
        VentilationPolar_str += "D0 = " + str(self.D0) + linesep
        VentilationPolar_str += "H0 = " + str(self.H0) + linesep
        VentilationPolar_str += "W1 = " + str(self.W1)
        return VentilationPolar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(VentilationPolar, self).__eq__(other):
            return False
        if other.Alpha0 != self.Alpha0:
            return False
        if other.D0 != self.D0:
            return False
        if other.H0 != self.H0:
            return False
        if other.W1 != self.W1:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Hole
        VentilationPolar_dict = super(VentilationPolar, self).as_dict()
        VentilationPolar_dict["Alpha0"] = self.Alpha0
        VentilationPolar_dict["D0"] = self.D0
        VentilationPolar_dict["H0"] = self.H0
        VentilationPolar_dict["W1"] = self.W1
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        VentilationPolar_dict["__class__"] = "VentilationPolar"
        return VentilationPolar_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Alpha0 = None
        self.D0 = None
        self.H0 = None
        self.W1 = None
        # Set to None the properties inherited from Hole
        super(VentilationPolar, self)._set_None()

    def _get_Alpha0(self):
        """getter of Alpha0"""
        return self._Alpha0

    def _set_Alpha0(self, value):
        """setter of Alpha0"""
        check_var("Alpha0", value, "float", Vmin=0, Vmax=6.29)
        self._Alpha0 = value

    # Shift angle of the hole around circumference
    # Type : float, min = 0, max = 6.29
    Alpha0 = property(fget=_get_Alpha0, fset=_set_Alpha0,
                      doc=u"""Shift angle of the hole around circumference""")

    def _get_D0(self):
        """getter of D0"""
        return self._D0

    def _set_D0(self, value):
        """setter of D0"""
        check_var("D0", value, "float", Vmin=0)
        self._D0 = value

    # Height of the hole
    # Type : float, min = 0
    D0 = property(fget=_get_D0, fset=_set_D0,
                  doc=u"""Height of the hole""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Radius of the bottom of Hole
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0,
                  doc=u"""Radius of the bottom of Hole""")

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0, Vmax=6.29)
        self._W1 = value

    # Hole angular width
    # Type : float, min = 0, max = 6.29
    W1 = property(fget=_get_W1, fset=_set_W1,
                  doc=u"""Hole angular width""")
