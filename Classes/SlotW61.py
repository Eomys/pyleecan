# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/SlotW61.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
import numpy
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.SlotW61._comp_point_coordinate import (
        _comp_point_coordinate,
    )
except ImportError as error:
    _comp_point_coordinate = error

try:
    from pyleecan.Methods.Slot.SlotW61.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Slot.SlotW61.build_geometry_wind import build_geometry_wind
except ImportError as error:
    build_geometry_wind = error

try:
    from pyleecan.Methods.Slot.SlotW61.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Slot.SlotW61.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from pyleecan.Methods.Slot.SlotW61.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Slot.SlotW61.comp_height_wind import comp_height_wind
except ImportError as error:
    comp_height_wind = error

try:
    from pyleecan.Methods.Slot.SlotW61.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Slot.SlotW61.comp_surface_wind import comp_surface_wind
except ImportError as error:
    comp_surface_wind = error


from pyleecan.Classes._check import InitUnKnowClassError


class SlotW61(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 0

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW61._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW61.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW61.build_geometry_wind
    if isinstance(build_geometry_wind, ImportError):
        build_geometry_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method build_geometry_wind: "
                    + str(build_geometry_wind)
                )
            )
        )
    else:
        build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW61.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW61 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW61.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW61.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW61 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW61.comp_height_wind
    if isinstance(comp_height_wind, ImportError):
        comp_height_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method comp_height_wind: "
                    + str(comp_height_wind)
                )
            )
        )
    else:
        comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW61.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW61.comp_surface_wind
    if isinstance(comp_surface_wind, ImportError):
        comp_surface_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW61 method comp_surface_wind: "
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
        W0=0.314,
        W1=0.02,
        W2=0.03,
        H0=0.003,
        H1=0.05,
        H2=0.15,
        H3=0,
        H4=0,
        W3=0,
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
            check_init_dict(
                init_dict, ["W0", "W1", "W2", "H0", "H1", "H2", "H3", "H4", "W3", "Zs"]
            )
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "H4" in list(init_dict.keys()):
                H4 = init_dict["H4"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W0 = W0
        self.W1 = W1
        self.W2 = W2
        self.H0 = H0
        self.H1 = H1
        self.H2 = H2
        self.H3 = H3
        self.H4 = H4
        self.W3 = W3
        # Call SlotWind init
        super(SlotW61, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW61_str = ""
        # Get the properties inherited from SlotWind
        SlotW61_str += super(SlotW61, self).__str__() + linesep
        SlotW61_str += "W0 = " + str(self.W0) + linesep
        SlotW61_str += "W1 = " + str(self.W1) + linesep
        SlotW61_str += "W2 = " + str(self.W2) + linesep
        SlotW61_str += "H0 = " + str(self.H0) + linesep
        SlotW61_str += "H1 = " + str(self.H1) + linesep
        SlotW61_str += "H2 = " + str(self.H2) + linesep
        SlotW61_str += "H3 = " + str(self.H3) + linesep
        SlotW61_str += "H4 = " + str(self.H4) + linesep
        SlotW61_str += "W3 = " + str(self.W3)
        return SlotW61_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW61, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.H2 != self.H2:
            return False
        if other.H3 != self.H3:
            return False
        if other.H4 != self.H4:
            return False
        if other.W3 != self.W3:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW61_dict = super(SlotW61, self).as_dict()
        SlotW61_dict["W0"] = self.W0
        SlotW61_dict["W1"] = self.W1
        SlotW61_dict["W2"] = self.W2
        SlotW61_dict["H0"] = self.H0
        SlotW61_dict["H1"] = self.H1
        SlotW61_dict["H2"] = self.H2
        SlotW61_dict["H3"] = self.H3
        SlotW61_dict["H4"] = self.H4
        SlotW61_dict["W3"] = self.W3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW61_dict["__class__"] = "SlotW61"
        return SlotW61_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.W1 = None
        self.W2 = None
        self.H0 = None
        self.H1 = None
        self.H2 = None
        self.H3 = None
        self.H4 = None
        self.W3 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW61, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Pole top width
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0, doc=u"""Pole top width""")

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    # Pole top width
    # Type : float, min = 0
    W1 = property(fget=_get_W1, fset=_set_W1, doc=u"""Pole top width""")

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    # Pole bottom width
    # Type : float, min = 0
    W2 = property(fget=_get_W2, fset=_set_W2, doc=u"""Pole bottom width""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Pole top height
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Pole top height""")

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Pole intermediate height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Pole intermediate height""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Pole bottom height
    # Type : float, min = 0
    H2 = property(fget=_get_H2, fset=_set_H2, doc=u"""Pole bottom height""")

    def _get_H3(self):
        """getter of H3"""
        return self._H3

    def _set_H3(self, value):
        """setter of H3"""
        check_var("H3", value, "float", Vmin=0)
        self._H3 = value

    # Top Distance Ploe-coil
    # Type : float, min = 0
    H3 = property(fget=_get_H3, fset=_set_H3, doc=u"""Top Distance Ploe-coil """)

    def _get_H4(self):
        """getter of H4"""
        return self._H4

    def _set_H4(self, value):
        """setter of H4"""
        check_var("H4", value, "float", Vmin=0)
        self._H4 = value

    # Bottom Distance Ploe-coil
    # Type : float, min = 0
    H4 = property(fget=_get_H4, fset=_set_H4, doc=u"""Bottom Distance Ploe-coil """)

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Edge Distance Ploe-coil
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Edge Distance Ploe-coil """)
