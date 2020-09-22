# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotW12.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotW12
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotW12.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotW12.build_geometry_wind import build_geometry_wind
except ImportError as error:
    build_geometry_wind = error

try:
    from ..Methods.Slot.SlotW12.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotW12.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotW12.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotW12.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from ..Methods.Slot.SlotW12.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotW12.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error


from ._check import InitUnKnowClassError


class SlotW12(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW12.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW12.build_geometry_wind
    if isinstance(build_geometry_wind, ImportError):
        build_geometry_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method build_geometry_wind: "
                    + str(build_geometry_wind)
                )
            )
        )
    else:
        build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW12.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW12 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW12.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW12.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW12 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW12.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW12.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW12.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW12 method comp_surface_wind: "
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
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, H0=0.003, H1=0, R1=0.001, R2=0.001, Zs=36, init_dict=None, init_str=None
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "R2" in list(init_dict.keys()):
                R2 = init_dict["R2"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Set the properties (value check and convertion are done in setter)
        self.H0 = H0
        self.H1 = H1
        self.R1 = R1
        self.R2 = R2
        # Call SlotWind init
        super(SlotW12, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW12_str = ""
        # Get the properties inherited from SlotWind
        SlotW12_str += super(SlotW12, self).__str__()
        SlotW12_str += "H0 = " + str(self.H0) + linesep
        SlotW12_str += "H1 = " + str(self.H1) + linesep
        SlotW12_str += "R1 = " + str(self.R1) + linesep
        SlotW12_str += "R2 = " + str(self.R2) + linesep
        return SlotW12_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW12, self).__eq__(other):
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.R1 != self.R1:
            return False
        if other.R2 != self.R2:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW12_dict = super(SlotW12, self).as_dict()
        SlotW12_dict["H0"] = self.H0
        SlotW12_dict["H1"] = self.H1
        SlotW12_dict["R1"] = self.R1
        SlotW12_dict["R2"] = self.R2
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW12_dict["__class__"] = "SlotW12"
        return SlotW12_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.H0 = None
        self.H1 = None
        self.R1 = None
        self.R2 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW12, self)._set_None()

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
        doc=u"""Slot isthmus height.

        :Type: float
        :min: 0
        """,
    )

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    H1 = property(
        fget=_get_H1,
        fset=_set_H1,
        doc=u"""Slot middle height

        :Type: float
        :min: 0
        """,
    )

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    R1 = property(
        fget=_get_R1,
        fset=_set_R1,
        doc=u"""Wedges radius

        :Type: float
        :min: 0
        """,
    )

    def _get_R2(self):
        """getter of R2"""
        return self._R2

    def _set_R2(self, value):
        """setter of R2"""
        check_var("R2", value, "float", Vmin=0)
        self._R2 = value

    R2 = property(
        fget=_get_R2,
        fset=_set_R2,
        doc=u"""Slot bottom radius

        :Type: float
        :min: 0
        """,
    )
