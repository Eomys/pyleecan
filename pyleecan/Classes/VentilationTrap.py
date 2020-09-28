# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/VentilationTrap.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/VentilationTrap
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
    from ..Methods.Slot.VentilationTrap.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.VentilationTrap.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.VentilationTrap.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.VentilationTrap.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.VentilationTrap.get_center import get_center
except ImportError as error:
    get_center = error


from ._check import InitUnKnowClassError
from .Material import Material


class VentilationTrap(Hole):
    """Trapezoidal axial ventilation ducts"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.VentilationTrap.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.VentilationTrap.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use VentilationTrap method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.VentilationTrap.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method comp_radius: " + str(comp_radius)
                )
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.VentilationTrap.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method comp_surface: "
                    + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.VentilationTrap.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationTrap method get_center: " + str(get_center)
                )
            )
        )
    else:
        get_center = get_center
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Alpha0=0,
        D0=1,
        H0=1,
        W1=1,
        W2=1,
        Zh=36,
        mat_void=-1,
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

        if mat_void == -1:
            mat_void = Material()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            Alpha0 = obj.Alpha0
            D0 = obj.D0
            H0 = obj.H0
            W1 = obj.W1
            W2 = obj.W2
            Zh = obj.Zh
            mat_void = obj.mat_void
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
            if "D0" in list(init_dict.keys()):
                D0 = init_dict["D0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        self.Alpha0 = Alpha0
        self.D0 = D0
        self.H0 = H0
        self.W1 = W1
        self.W2 = W2
        # Call Hole init
        super(VentilationTrap, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VentilationTrap_str = ""
        # Get the properties inherited from Hole
        VentilationTrap_str += super(VentilationTrap, self).__str__()
        VentilationTrap_str += "Alpha0 = " + str(self.Alpha0) + linesep
        VentilationTrap_str += "D0 = " + str(self.D0) + linesep
        VentilationTrap_str += "H0 = " + str(self.H0) + linesep
        VentilationTrap_str += "W1 = " + str(self.W1) + linesep
        VentilationTrap_str += "W2 = " + str(self.W2) + linesep
        return VentilationTrap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(VentilationTrap, self).__eq__(other):
            return False
        if other.Alpha0 != self.Alpha0:
            return False
        if other.D0 != self.D0:
            return False
        if other.H0 != self.H0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Hole
        VentilationTrap_dict = super(VentilationTrap, self).as_dict()
        VentilationTrap_dict["Alpha0"] = self.Alpha0
        VentilationTrap_dict["D0"] = self.D0
        VentilationTrap_dict["H0"] = self.H0
        VentilationTrap_dict["W1"] = self.W1
        VentilationTrap_dict["W2"] = self.W2
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        VentilationTrap_dict["__class__"] = "VentilationTrap"
        return VentilationTrap_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Alpha0 = None
        self.D0 = None
        self.H0 = None
        self.W1 = None
        self.W2 = None
        # Set to None the properties inherited from Hole
        super(VentilationTrap, self)._set_None()

    def _get_Alpha0(self):
        """getter of Alpha0"""
        return self._Alpha0

    def _set_Alpha0(self, value):
        """setter of Alpha0"""
        check_var("Alpha0", value, "float", Vmin=0, Vmax=6.29)
        self._Alpha0 = value

    Alpha0 = property(
        fget=_get_Alpha0,
        fset=_set_Alpha0,
        doc=u"""Shift angle of the hole around circumference

        :Type: float
        :min: 0
        :max: 6.29
        """,
    )

    def _get_D0(self):
        """getter of D0"""
        return self._D0

    def _set_D0(self, value):
        """setter of D0"""
        check_var("D0", value, "float", Vmin=0)
        self._D0 = value

    D0 = property(
        fget=_get_D0,
        fset=_set_D0,
        doc=u"""Hole height

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc=u"""Radius of the hole bottom

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc=u"""Hole small basis

        :Type: float
        :min: 0
        """,
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    W2 = property(
        fget=_get_W2,
        fset=_set_W2,
        doc=u"""Hole large basis

        :Type: float
        :min: 0
        """,
    )
