# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.Slot import Slot

from pyleecan.Methods.Slot.SlotWind.comp_angle_wind_eq import comp_angle_wind_eq
from pyleecan.Methods.Slot.SlotWind.comp_height_wind import comp_height_wind
from pyleecan.Methods.Slot.SlotWind.comp_radius_mid_wind import comp_radius_mid_wind
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotWind.plot_wind import plot_wind

from pyleecan.Classes.check import InitUnKnowClassError


class SlotWind(Slot):
    """Slot for winding (abstract)"""

    VERSION = 1

    # cf Methods.Slot.SlotWind.comp_angle_wind_eq
    comp_angle_wind_eq = comp_angle_wind_eq
    # cf Methods.Slot.SlotWind.comp_height_wind
    comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotWind.comp_radius_mid_wind
    comp_radius_mid_wind = comp_radius_mid_wind
    # cf Methods.Slot.SlotWind.comp_surface_wind
    comp_surface_wind = comp_surface_wind
    # cf Methods.Slot.SlotWind.plot_wind
    plot_wind = plot_wind

    def __init__(self, Zs=36, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Zs"])
            # Overwrite default value with init_dict content
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        # Call Slot init
        super(SlotWind, self).__init__(Zs=Zs)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotWind_str = ""
        # Get the properties inherited from Slot
        SlotWind_str += super(SlotWind, self).__str__() + linesep
        return SlotWind_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotWind, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Slot
        SlotWind_dict = super(SlotWind, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotWind_dict["__class__"] = "SlotWind"
        return SlotWind_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Slot
        super(SlotWind, self)._set_None()
