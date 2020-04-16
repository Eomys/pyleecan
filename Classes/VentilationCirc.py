# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/VentilationCirc.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.VentilationCirc.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.VentilationCirc.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.VentilationCirc.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.VentilationCirc.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.VentilationCirc.get_center import get_center
except ImportError as error:
    get_center = error


from ._check import InitUnKnowClassError
from .Material import Material


class VentilationCirc(Hole):
    """Circular axial ventilation duct"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.VentilationCirc.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationCirc method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.VentilationCirc.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use VentilationCirc method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.VentilationCirc.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationCirc method comp_radius: " + str(comp_radius)
                )
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.VentilationCirc.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationCirc method comp_surface: "
                    + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.VentilationCirc.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationCirc method get_center: " + str(get_center)
                )
            )
        )
    else:
        get_center = get_center
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Alpha0=0, D0=1, H0=1, Zh=36, mat_void=-1, init_dict=None):
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
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
            if "D0" in list(init_dict.keys()):
                D0 = init_dict["D0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.Alpha0 = Alpha0
        self.D0 = D0
        self.H0 = H0
        # Call Hole init
        super(VentilationCirc, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        VentilationCirc_str = ""
        # Get the properties inherited from Hole
        VentilationCirc_str += super(VentilationCirc, self).__str__()
        VentilationCirc_str += "Alpha0 = " + str(self.Alpha0) + linesep
        VentilationCirc_str += "D0 = " + str(self.D0) + linesep
        VentilationCirc_str += "H0 = " + str(self.H0) + linesep
        return VentilationCirc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(VentilationCirc, self).__eq__(other):
            return False
        if other.Alpha0 != self.Alpha0:
            return False
        if other.D0 != self.D0:
            return False
        if other.H0 != self.H0:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Hole
        VentilationCirc_dict = super(VentilationCirc, self).as_dict()
        VentilationCirc_dict["Alpha0"] = self.Alpha0
        VentilationCirc_dict["D0"] = self.D0
        VentilationCirc_dict["H0"] = self.H0
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        VentilationCirc_dict["__class__"] = "VentilationCirc"
        return VentilationCirc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Alpha0 = None
        self.D0 = None
        self.H0 = None
        # Set to None the properties inherited from Hole
        super(VentilationCirc, self)._set_None()

    def _get_Alpha0(self):
        """getter of Alpha0"""
        return self._Alpha0

    def _set_Alpha0(self, value):
        """setter of Alpha0"""
        check_var("Alpha0", value, "float", Vmin=0, Vmax=6.29)
        self._Alpha0 = value

    # Shift angle of the holes around circumference
    # Type : float, min = 0, max = 6.29
    Alpha0 = property(
        fget=_get_Alpha0,
        fset=_set_Alpha0,
        doc=u"""Shift angle of the holes around circumference""",
    )

    def _get_D0(self):
        """getter of D0"""
        return self._D0

    def _set_D0(self, value):
        """setter of D0"""
        check_var("D0", value, "float", Vmin=0)
        self._D0 = value

    # Hole diameters
    # Type : float, min = 0
    D0 = property(fget=_get_D0, fset=_set_D0, doc=u"""Hole diameters""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Diameter of the hole centers
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Diameter of the hole centers""")
