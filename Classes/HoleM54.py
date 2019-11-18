# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.HoleM54.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Slot.HoleM54.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Slot.HoleM54.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from pyleecan.Methods.Slot.HoleM54.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Slot.HoleM54.get_height_magnet import get_height_magnet
except ImportError as error:
    get_height_magnet = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material



class HoleM54(Hole):
    """Arc Hole for SyRM"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleM54.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(fget=lambda x: raise_(ImportError("Can't use HoleM54 method build_geometry: " + str(build_geometry))))
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleM54.check
    if isinstance(check, ImportError):
        check = property(fget=lambda x: raise_(ImportError("Can't use HoleM54 method check: " + str(check))))
    else:
        check = check
    # cf Methods.Slot.HoleM54.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(fget=lambda x: raise_(ImportError("Can't use HoleM54 method comp_radius: " + str(comp_radius))))
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.HoleM54.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(fget=lambda x: raise_(ImportError("Can't use HoleM54 method comp_surface: " + str(comp_surface))))
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.HoleM54.get_height_magnet
    if isinstance(get_height_magnet, ImportError):
        get_height_magnet = property(fget=lambda x: raise_(ImportError("Can't use HoleM54 method get_height_magnet: " + str(get_height_magnet))))
    else:
        get_height_magnet = get_height_magnet
    # save method is available in all object
    save = save

    def __init__(self, H0=0.003, H1=0, W0=0.013, R1=0.02, Zh=36, mat_void=-1, init_dict=None):
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
            check_init_dict(init_dict, ["H0", "H1", "W0", "R1", "Zh", "mat_void"])
            # Overwrite default value with init_dict content
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.H0 = H0
        self.H1 = H1
        self.W0 = W0
        self.R1 = R1
        # Call Hole init
        super(HoleM54, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleM54_str = ""
        # Get the properties inherited from Hole
        HoleM54_str += super(HoleM54, self).__str__() + linesep
        HoleM54_str += "H0 = " + str(self.H0) + linesep
        HoleM54_str += "H1 = " + str(self.H1) + linesep
        HoleM54_str += "W0 = " + str(self.W0) + linesep
        HoleM54_str += "R1 = " + str(self.R1)
        return HoleM54_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(HoleM54, self).__eq__(other):
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.W0 != self.W0:
            return False
        if other.R1 != self.R1:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Hole
        HoleM54_dict = super(HoleM54, self).as_dict()
        HoleM54_dict["H0"] = self.H0
        HoleM54_dict["H1"] = self.H1
        HoleM54_dict["W0"] = self.W0
        HoleM54_dict["R1"] = self.R1
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleM54_dict["__class__"] = "HoleM54"
        return HoleM54_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H0 = None
        self.H1 = None
        self.W0 = None
        self.R1 = None
        # Set to None the properties inherited from Hole
        super(HoleM54, self)._set_None()

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Hole depth
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0,
                  doc=u"""Hole depth""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Hole width
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1,
                  doc=u"""Hole width""")

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Hole angular width
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0,
                  doc=u"""Hole angular width""")

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    # Hole radius
    # Type : float, min = 0
    R1 = property(fget=_get_R1, fset=_set_R1,
                  doc=u"""Hole radius""")
