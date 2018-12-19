# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Slot.Hole.comp_radius import comp_radius
from pyleecan.Methods.Slot.Hole.comp_surface import comp_surface
from pyleecan.Methods.Slot.Hole.get_is_stator import get_is_stator
from pyleecan.Methods.Slot.Hole.get_Rbo import get_Rbo
from pyleecan.Methods.Slot.Hole.has_magnet import has_magnet
from pyleecan.Methods.Slot.Hole.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class Hole(FrozenClass):
    """Holes for lamination (abstract)"""

    VERSION = 1

    # cf Methods.Slot.Hole.comp_radius
    comp_radius = comp_radius
    # cf Methods.Slot.Hole.comp_surface
    comp_surface = comp_surface
    # cf Methods.Slot.Hole.get_is_stator
    get_is_stator = get_is_stator
    # cf Methods.Slot.Hole.get_Rbo
    get_Rbo = get_Rbo
    # cf Methods.Slot.Hole.has_magnet
    has_magnet = has_magnet
    # cf Methods.Slot.Hole.plot
    plot = plot

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
        self.parent = None
        self.Zh = Zh
        # mat_void can be None, a Material object or a dict
        if isinstance(mat_void, dict):
            self.mat_void = Material(init_dict=mat_void)
        else:
            self.mat_void = mat_void

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Hole_str = ""
        if self.parent is None:
            Hole_str += "parent = None " + linesep
        else:
            Hole_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Hole_str += "Zh = " + str(self.Zh) + linesep
        Hole_str += "mat_void = " + str(self.mat_void.as_dict())
        return Hole_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Zh != self.Zh:
            return False
        if other.mat_void != self.mat_void:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Hole_dict = dict()
        Hole_dict["Zh"] = self.Zh
        if self.mat_void is None:
            Hole_dict["mat_void"] = None
        else:
            Hole_dict["mat_void"] = self.mat_void.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Hole_dict["__class__"] = "Hole"
        return Hole_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Zh = None
        if self.mat_void is not None:
            self.mat_void._set_None()

    def _get_Zh(self):
        """getter of Zh"""
        return self._Zh

    def _set_Zh(self, value):
        """setter of Zh"""
        check_var("Zh", value, "int", Vmin=0, Vmax=1000)
        self._Zh = value

    # Number of Hole around the circumference
    # Type : int, min = 0, max = 1000
    Zh = property(
        fget=_get_Zh, fset=_set_Zh, doc=u"""Number of Hole around the circumference"""
    )

    def _get_mat_void(self):
        """getter of mat_void"""
        return self._mat_void

    def _set_mat_void(self, value):
        """setter of mat_void"""
        check_var("mat_void", value, "Material")
        self._mat_void = value

        if self._mat_void is not None:
            self._mat_void.parent = self

    # Material of the "void" part of the hole (Air in general)
    # Type : Material
    mat_void = property(
        fget=_get_mat_void,
        fset=_set_mat_void,
        doc=u"""Material of the "void" part of the hole (Air in general)""",
    )
