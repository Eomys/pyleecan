# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Slot.Slot.check import check
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.get_is_stator import get_is_stator
from pyleecan.Methods.Slot.Slot.get_Rbo import get_Rbo
from pyleecan.Methods.Slot.Slot.get_surface import get_surface
from pyleecan.Methods.Slot.Slot.is_outwards import is_outwards
from pyleecan.Methods.Slot.Slot.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError


class Slot(FrozenClass):
    """Generic class for slot (abstract)"""

    VERSION = 1

    # cf Methods.Slot.Slot.check
    check = check
    # cf Methods.Slot.Slot.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.Slot.comp_height
    comp_height = comp_height
    # cf Methods.Slot.Slot.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.Slot.get_is_stator
    get_is_stator = get_is_stator
    # cf Methods.Slot.Slot.get_Rbo
    get_Rbo = get_Rbo
    # cf Methods.Slot.Slot.get_surface
    get_surface = get_surface
    # cf Methods.Slot.Slot.is_outwards
    is_outwards = is_outwards
    # cf Methods.Slot.Slot.plot
    plot = plot
    # save method is available in all object
    save = save

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
        self.parent = None
        self.Zs = Zs

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Slot_str = ""
        if self.parent is None:
            Slot_str += "parent = None " + linesep
        else:
            Slot_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Slot_str += "Zs = " + str(self.Zs)
        return Slot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Zs != self.Zs:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Slot_dict = dict()
        Slot_dict["Zs"] = self.Zs
        # The class name is added to the dict fordeserialisation purpose
        Slot_dict["__class__"] = "Slot"
        return Slot_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Zs = None

    def _get_Zs(self):
        """getter of Zs"""
        return self._Zs

    def _set_Zs(self, value):
        """setter of Zs"""
        check_var("Zs", value, "int", Vmin=0, Vmax=1000)
        self._Zs = value

    # slot number
    # Type : int, min = 0, max = 1000
    Zs = property(fget=_get_Zs, fset=_set_Zs, doc=u"""slot number""")
