# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.Hole import Hole

from pyleecan.Methods.Slot.HoleMag.has_magnet import has_magnet

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class HoleMag(Hole):
    """Hole with magnets for lamination (abstract)"""

    VERSION = 1

    # cf Methods.Slot.HoleMag.has_magnet
    has_magnet = has_magnet

    def __init__(self, Zh=36, mat_void=-1, init_dict=None):
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
            check_init_dict(init_dict, ["Zh", "mat_void"])
            # Overwrite default value with init_dict content
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        # Call Hole init
        super(HoleMag, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleMag_str = ""
        # Get the properties inherited from Hole
        HoleMag_str += super(HoleMag, self).__str__() + linesep
        return HoleMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(HoleMag, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Hole
        HoleMag_dict = super(HoleMag, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleMag_dict["__class__"] = "HoleMag"
        return HoleMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Hole
        super(HoleMag, self)._set_None()
