# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

from pyleecan.Methods.Slot.SlotW60._comp_point_coordinate import _comp_point_coordinate
from pyleecan.Methods.Slot.SlotW60.build_geometry import build_geometry
from pyleecan.Methods.Slot.SlotW60.build_geometry_wind import build_geometry_wind
from pyleecan.Methods.Slot.SlotW60.check import check
from pyleecan.Methods.Slot.SlotW60.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotW60.comp_height import comp_height
from pyleecan.Methods.Slot.SlotW60.comp_height_wind import comp_height_wind
from pyleecan.Methods.Slot.SlotW60.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotW60.comp_surface_wind import comp_surface_wind

from pyleecan.Classes.check import InitUnKnowClassError


class SlotW60(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 0

    # cf Methods.Slot.SlotW60._comp_point_coordinate
    _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW60.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.SlotW60.build_geometry_wind
    build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW60.check
    check = check
    # cf Methods.Slot.SlotW60.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW60.comp_height
    comp_height = comp_height
    # cf Methods.Slot.SlotW60.comp_height_wind
    comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW60.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.SlotW60.comp_surface_wind
    comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    def __init__(
        self,
        W1=0.02,
        W2=0.03,
        H1=0.05,
        H2=0.15,
        R1=0.03,
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
                init_dict, ["W1", "W2", "H1", "H2", "R1", "H3", "H4", "W3", "Zs"]
            )
            # Overwrite default value with init_dict content
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "H4" in list(init_dict.keys()):
                H4 = init_dict["H4"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W1 = W1
        self.W2 = W2
        self.H1 = H1
        self.H2 = H2
        self.R1 = R1
        self.H3 = H3
        self.H4 = H4
        self.W3 = W3
        # Call SlotWind init
        super(SlotW60, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW60_str = ""
        # Get the properties inherited from SlotWind
        SlotW60_str += super(SlotW60, self).__str__() + linesep
        SlotW60_str += "W1 = " + str(self.W1) + linesep
        SlotW60_str += "W2 = " + str(self.W2) + linesep
        SlotW60_str += "H1 = " + str(self.H1) + linesep
        SlotW60_str += "H2 = " + str(self.H2) + linesep
        SlotW60_str += "R1 = " + str(self.R1) + linesep
        SlotW60_str += "H3 = " + str(self.H3) + linesep
        SlotW60_str += "H4 = " + str(self.H4) + linesep
        SlotW60_str += "W3 = " + str(self.W3)
        return SlotW60_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW60, self).__eq__(other):
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.H1 != self.H1:
            return False
        if other.H2 != self.H2:
            return False
        if other.R1 != self.R1:
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
        SlotW60_dict = super(SlotW60, self).as_dict()
        SlotW60_dict["W1"] = self.W1
        SlotW60_dict["W2"] = self.W2
        SlotW60_dict["H1"] = self.H1
        SlotW60_dict["H2"] = self.H2
        SlotW60_dict["R1"] = self.R1
        SlotW60_dict["H3"] = self.H3
        SlotW60_dict["H4"] = self.H4
        SlotW60_dict["W3"] = self.W3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW60_dict["__class__"] = "SlotW60"
        return SlotW60_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W1 = None
        self.W2 = None
        self.H1 = None
        self.H2 = None
        self.R1 = None
        self.H3 = None
        self.H4 = None
        self.W3 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW60, self)._set_None()

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

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    # Pole top height
    # Type : float, min = 0
    H1 = property(fget=_get_H1, fset=_set_H1, doc=u"""Pole top height""")

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

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    # Pole top radius
    # Type : float, min = 0
    R1 = property(fget=_get_R1, fset=_set_R1, doc=u"""Pole top radius""")

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
