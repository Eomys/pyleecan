# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

from pyleecan.Methods.Slot.SlotW24._comp_point_coordinate import _comp_point_coordinate
from pyleecan.Methods.Slot.SlotW24.build_geometry import build_geometry
from pyleecan.Methods.Slot.SlotW24.build_geometry_wind import build_geometry_wind
from pyleecan.Methods.Slot.SlotW24.check import check
from pyleecan.Methods.Slot.SlotW24.comp_alphas import comp_alphas
from pyleecan.Methods.Slot.SlotW24.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotW24.comp_height import comp_height
from pyleecan.Methods.Slot.SlotW24.comp_height_wind import comp_height_wind
from pyleecan.Methods.Slot.SlotW24.comp_surface import comp_surface
from pyleecan.Methods.Slot.SlotW24.comp_surface_wind import comp_surface_wind

from pyleecan.Classes.check import InitUnKnowClassError


class SlotW24(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # cf Methods.Slot.SlotW24._comp_point_coordinate
    _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW24.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.SlotW24.build_geometry_wind
    build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW24.check
    check = check
    # cf Methods.Slot.SlotW24.comp_alphas
    comp_alphas = comp_alphas
    # cf Methods.Slot.SlotW24.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW24.comp_height
    comp_height = comp_height
    # cf Methods.Slot.SlotW24.comp_height_wind
    comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW24.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.SlotW24.comp_surface_wind
    comp_surface_wind = comp_surface_wind
    # save method is available in all object
    save = save

    def __init__(self, W3=0.003, H2=0.003, Zs=36, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["W3", "H2", "Zs"])
            # Overwrite default value with init_dict content
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W3 = W3
        self.H2 = H2
        # Call SlotWind init
        super(SlotW24, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW24_str = ""
        # Get the properties inherited from SlotWind
        SlotW24_str += super(SlotW24, self).__str__() + linesep
        SlotW24_str += "W3 = " + str(self.W3) + linesep
        SlotW24_str += "H2 = " + str(self.H2)
        return SlotW24_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW24, self).__eq__(other):
            return False
        if other.W3 != self.W3:
            return False
        if other.H2 != self.H2:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW24_dict = super(SlotW24, self).as_dict()
        SlotW24_dict["W3"] = self.W3
        SlotW24_dict["H2"] = self.H2
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW24_dict["__class__"] = "SlotW24"
        return SlotW24_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W3 = None
        self.H2 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW24, self)._set_None()

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Teeth width
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Teeth width""")

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    # Slot height
    # Type : float, min = 0
    H2 = property(fget=_get_H2, fset=_set_H2, doc=u"""Slot height""")
