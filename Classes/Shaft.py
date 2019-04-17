# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Machine.Shaft.build_geometry import build_geometry
from pyleecan.Methods.Machine.Shaft.comp_mass import comp_mass
from pyleecan.Methods.Machine.Shaft.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class Shaft(FrozenClass):
    """machine shaft"""

    VERSION = 1

    # cf Methods.Machine.Shaft.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.Shaft.comp_mass
    comp_mass = comp_mass
    # cf Methods.Machine.Shaft.plot
    plot = plot
    # save method is available in all object
    save = save

    def __init__(self, Lshaft=0.442, mat_type=-1, Drsh=0.045, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Lshaft", "mat_type", "Drsh"])
            # Overwrite default value with init_dict content
            if "Lshaft" in list(init_dict.keys()):
                Lshaft = init_dict["Lshaft"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Drsh" in list(init_dict.keys()):
                Drsh = init_dict["Drsh"]
        # Initialisation by argument
        self.parent = None
        self.Lshaft = Lshaft
        # mat_type can be None, a Material object or a dict
        if isinstance(mat_type, dict):
            self.mat_type = Material(init_dict=mat_type)
        else:
            self.mat_type = mat_type
        self.Drsh = Drsh

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Shaft_str = ""
        if self.parent is None:
            Shaft_str += "parent = None " + linesep
        else:
            Shaft_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Shaft_str += "Lshaft = " + str(self.Lshaft) + linesep
        Shaft_str += "mat_type = " + str(self.mat_type.as_dict()) + linesep + linesep
        Shaft_str += "Drsh = " + str(self.Drsh)
        return Shaft_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Lshaft != self.Lshaft:
            return False
        if other.mat_type != self.mat_type:
            return False
        if other.Drsh != self.Drsh:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Shaft_dict = dict()
        Shaft_dict["Lshaft"] = self.Lshaft
        if self.mat_type is None:
            Shaft_dict["mat_type"] = None
        else:
            Shaft_dict["mat_type"] = self.mat_type.as_dict()
        Shaft_dict["Drsh"] = self.Drsh
        # The class name is added to the dict fordeserialisation purpose
        Shaft_dict["__class__"] = "Shaft"
        return Shaft_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Lshaft = None
        if self.mat_type is not None:
            self.mat_type._set_None()
        self.Drsh = None

    def _get_Lshaft(self):
        """getter of Lshaft"""
        return self._Lshaft

    def _set_Lshaft(self, value):
        """setter of Lshaft"""
        check_var("Lshaft", value, "float", Vmin=0, Vmax=100)
        self._Lshaft = value

    # length of the rotor shaft [m] (used for weight & cost estimation only)
    # Type : float, min = 0, max = 100
    Lshaft = property(
        fget=_get_Lshaft,
        fset=_set_Lshaft,
        doc=u"""length of the rotor shaft [m] (used for weight & cost estimation only)""",
    )

    def _get_mat_type(self):
        """getter of mat_type"""
        return self._mat_type

    def _set_mat_type(self, value):
        """setter of mat_type"""
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    # Shaft's Material
    # Type : Material
    mat_type = property(
        fget=_get_mat_type, fset=_set_mat_type, doc=u"""Shaft's Material"""
    )

    def _get_Drsh(self):
        """getter of Drsh"""
        return self._Drsh

    def _set_Drsh(self, value):
        """setter of Drsh"""
        check_var("Drsh", value, "float", Vmin=0, Vmax=8)
        self._Drsh = value

    # diameter of the rotor shaft [m], used to estimate bearing diameter for friction losses
    # Type : float, min = 0, max = 8
    Drsh = property(
        fget=_get_Drsh,
        fset=_set_Drsh,
        doc=u"""diameter of the rotor shaft [m], used to estimate bearing diameter for friction losses""",
    )
