# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Slot/SlotW29.csv
WARNING! All changes made in this file will be lost!
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
    from ..Methods.Slot.SlotW29._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotW29.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotW29.build_geometry_wind import build_geometry_wind
except ImportError as error:
    build_geometry_wind = error

try:
    from ..Methods.Slot.SlotW29.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotW29.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotW29.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotW29.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from ..Methods.Slot.SlotW29.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotW29.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error


from ._check import InitUnKnowClassError


class SlotW29(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW29._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW29.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW29.build_geometry_wind
    if isinstance(build_geometry_wind, ImportError):
        build_geometry_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method build_geometry_wind: "
                    + str(build_geometry_wind)
                )
            )
        )
    else:
        build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW29.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW29 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW29.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW29.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW29 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW29.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW29.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW29.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW29 method comp_surface_wind: "
                    + str(comp_surface_wind)
                )
            )
        )
    else:
        comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=0.05,
        H0=0.001,
        H1=0.0015,
        W1=0.015,
        H2=0.03,
        W2=0.2,
        Zs=36,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object
        - __init__ (init_str = s) s must be a string
        s is the file path to load """

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            W0 = obj.W0
            H0 = obj.H0
            H1 = obj.H1
            W1 = obj.W1
            H2 = obj.H2
            W2 = obj.W2
            Zs = obj.Zs
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W0 = W0
        self.H0 = H0
        self.H1 = H1
        self.W1 = W1
        self.H2 = H2
        self.W2 = W2
        # Call SlotWind init
        super(SlotW29, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW29_str = ""
        # Get the properties inherited from SlotWind
        SlotW29_str += super(SlotW29, self).__str__()
        SlotW29_str += "W0 = " + str(self.W0) + linesep
        SlotW29_str += "H0 = " + str(self.H0) + linesep
        SlotW29_str += "H1 = " + str(self.H1) + linesep
        SlotW29_str += "W1 = " + str(self.W1) + linesep
        SlotW29_str += "H2 = " + str(self.H2) + linesep
        SlotW29_str += "W2 = " + str(self.W2) + linesep
        return SlotW29_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW29, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.W1 != self.W1:
            return False
        if other.H2 != self.H2:
            return False
        if other.W2 != self.W2:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW29_dict = super(SlotW29, self).as_dict()
        SlotW29_dict["W0"] = self.W0
        SlotW29_dict["H0"] = self.H0
        SlotW29_dict["H1"] = self.H1
        SlotW29_dict["W1"] = self.W1
        SlotW29_dict["H2"] = self.H2
        SlotW29_dict["W2"] = self.W2
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW29_dict["__class__"] = "SlotW29"
        return SlotW29_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.H1 = None
        self.W1 = None
        self.H2 = None
        self.W2 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW29, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Slot isthmus width.
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0, doc=u"""Slot isthmus width.""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Slot isthmus height.
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Slot isthmus height.""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Slot middle height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Slot middle height""")

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    # Slot middle width.
    # Type : float, min = 0
    W1 = property(fget=_get_W1, fset=_set_W1, doc=u"""Slot middle width.""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Slot bottom height
    # Type : float, min = 0
    H2 = property(fget=_get_H2, fset=_set_H2, doc=u"""Slot bottom height""")

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    # Slot bottom width.
    # Type : float, min = 0
    W2 = property(fget=_get_W2, fset=_set_W2, doc=u"""Slot bottom width.""")
