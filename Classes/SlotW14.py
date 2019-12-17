# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/SlotW14.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.SlotW14._comp_point_coordinate import (
        _comp_point_coordinate,
    )
except ImportError as error:
    _comp_point_coordinate = error

try:
    from pyleecan.Methods.Slot.SlotW14.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Slot.SlotW14.build_geometry_wind import build_geometry_wind
except ImportError as error:
    build_geometry_wind = error

try:
    from pyleecan.Methods.Slot.SlotW14.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Slot.SlotW14.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from pyleecan.Methods.Slot.SlotW14.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Slot.SlotW14.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from pyleecan.Methods.Slot.SlotW14.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Slot.SlotW14.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error


from pyleecan.Classes.check import InitUnKnowClassError


class SlotW14(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW14._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW14.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW14.build_geometry_wind
    if isinstance(build_geometry_wind, ImportError):
        build_geometry_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method build_geometry_wind: "
                    + str(build_geometry_wind)
                )
            )
        )
    else:
        build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW14.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW14 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW14.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW14.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW14 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW14.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW14.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW14.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW14 method comp_surface_wind: "
                    + str(comp_surface_wind)
                )
            )
        )
    else:
        comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    def __init__(
        self,
        W0=0.0122,
        H0=0.001,
        H1=0.0015,
        H3=0.0122,
        W3=0.0122,
        Zs=36,
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
            check_init_dict(init_dict, ["W0", "H0", "H1", "H3", "W3", "Zs"])
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W0 = W0
        self.H0 = H0
        self.H1 = H1
        self.H3 = H3
        self.W3 = W3
        # Call SlotWind init
        super(SlotW14, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW14_str = ""
        # Get the properties inherited from SlotWind
        SlotW14_str += super(SlotW14, self).__str__() + linesep
        SlotW14_str += "W0 = " + str(self.W0) + linesep
        SlotW14_str += "H0 = " + str(self.H0) + linesep
        SlotW14_str += "H1 = " + str(self.H1) + linesep
        SlotW14_str += "H3 = " + str(self.H3) + linesep
        SlotW14_str += "W3 = " + str(self.W3)
        return SlotW14_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW14, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.H3 != self.H3:
            return False
        if other.W3 != self.W3:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW14_dict = super(SlotW14, self).as_dict()
        SlotW14_dict["W0"] = self.W0
        SlotW14_dict["H0"] = self.H0
        SlotW14_dict["H1"] = self.H1
        SlotW14_dict["H3"] = self.H3
        SlotW14_dict["W3"] = self.W3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW14_dict["__class__"] = "SlotW14"
        return SlotW14_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.H1 = None
        self.H3 = None
        self.W3 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW14, self)._set_None()

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

    # Slot intermediate height.
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Slot intermediate height.""")

    def _get_H3(self):
        """getter of H3"""
        return self._H3

    def _set_H3(self, value):
        """setter of H3"""
        check_var("H3", value, "float", Vmin=0)
        self._H3 = value

    # Tooth height
    # Type : float, min = 0
    H3 = property(fget=_get_H3, fset=_set_H3, doc=u"""Tooth height""")

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Tooth width
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Tooth width""")
