# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotCirc.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotCirc
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotCirc.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotCirc.build_geometry_wind import build_geometry_wind
except ImportError as error:
    build_geometry_wind = error

try:
    from ..Methods.Slot.SlotCirc.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotCirc.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotCirc.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotCirc.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from ..Methods.Slot.SlotCirc.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotCirc.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error


from ._check import InitUnKnowClassError


class SlotCirc(SlotWind):
    """Circular slot (for notches)"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotCirc.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotCirc.build_geometry_wind
    if isinstance(build_geometry_wind, ImportError):
        build_geometry_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method build_geometry_wind: "
                    + str(build_geometry_wind)
                )
            )
        )
    else:
        build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotCirc.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotCirc method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotCirc.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotCirc.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotCirc.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotCirc.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotCirc.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotCirc method comp_surface_wind: "
                    + str(comp_surface_wind)
                )
            )
        )
    else:
        comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, W0=0.01, H0=0.03, Zs=36, init_dict=None, init_str=None):
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
            W0 = obj.W0
            H0 = obj.H0
            Zs = obj.Zs
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W0 = W0
        self.H0 = H0
        # Call SlotWind init
        super(SlotCirc, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotCirc_str = ""
        # Get the properties inherited from SlotWind
        SlotCirc_str += super(SlotCirc, self).__str__()
        SlotCirc_str += "W0 = " + str(self.W0) + linesep
        SlotCirc_str += "H0 = " + str(self.H0) + linesep
        return SlotCirc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotCirc, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from SlotWind
        SlotCirc_dict = super(SlotCirc, self).as_dict()
        SlotCirc_dict["W0"] = self.W0
        SlotCirc_dict["H0"] = self.H0
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotCirc_dict["__class__"] = "SlotCirc"
        return SlotCirc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        # Set to None the properties inherited from SlotWind
        super(SlotCirc, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc=u"""Slot isthmus width.

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
        doc=u"""Slot height

        :Type: float
        :min: 0
        """,
    )
