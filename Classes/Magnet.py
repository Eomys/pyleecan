# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Machine.Magnet.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Machine.Magnet.comp_height import comp_height
from pyleecan.Methods.Machine.Magnet.comp_mass import comp_mass
from pyleecan.Methods.Machine.Magnet.comp_ratio_opening import comp_ratio_opening
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface
from pyleecan.Methods.Machine.Magnet.comp_volume import comp_volume
from pyleecan.Methods.Machine.Magnet.is_outwards import is_outwards
from pyleecan.Methods.Machine.Magnet.plot import plot

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class Magnet(FrozenClass):
    """abstract class of magnets"""

    VERSION = 1

    # cf Methods.Machine.Magnet.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Machine.Magnet.comp_height
    comp_height = comp_height
    # cf Methods.Machine.Magnet.comp_mass
    comp_mass = comp_mass
    # cf Methods.Machine.Magnet.comp_ratio_opening
    comp_ratio_opening = comp_ratio_opening
    # cf Methods.Machine.Magnet.comp_surface
    comp_surface = comp_surface
    # cf Methods.Machine.Magnet.comp_volume
    comp_volume = comp_volume
    # cf Methods.Machine.Magnet.is_outwards
    is_outwards = is_outwards
    # cf Methods.Machine.Magnet.plot
    plot = plot
    # save method is available in all object
    save = save

    def __init__(self, mat_type=-1, type_magnetization=0, Lmag=0.95, init_dict=None):
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
            check_init_dict(init_dict, ["mat_type", "type_magnetization", "Lmag"])
            # Overwrite default value with init_dict content
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
            if "Lmag" in list(init_dict.keys()):
                Lmag = init_dict["Lmag"]
        # Initialisation by argument
        self.parent = None
        # mat_type can be None, a Material object or a dict
        if isinstance(mat_type, dict):
            self.mat_type = Material(init_dict=mat_type)
        else:
            self.mat_type = mat_type
        self.type_magnetization = type_magnetization
        self.Lmag = Lmag

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Magnet_str = ""
        if self.parent is None:
            Magnet_str += "parent = None " + linesep
        else:
            Magnet_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Magnet_str += "mat_type = " + str(self.mat_type.as_dict()) + linesep + linesep
        Magnet_str += "type_magnetization = " + str(self.type_magnetization) + linesep
        Magnet_str += "Lmag = " + str(self.Lmag)
        return Magnet_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mat_type != self.mat_type:
            return False
        if other.type_magnetization != self.type_magnetization:
            return False
        if other.Lmag != self.Lmag:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Magnet_dict = dict()
        if self.mat_type is None:
            Magnet_dict["mat_type"] = None
        else:
            Magnet_dict["mat_type"] = self.mat_type.as_dict()
        Magnet_dict["type_magnetization"] = self.type_magnetization
        Magnet_dict["Lmag"] = self.Lmag
        # The class name is added to the dict fordeserialisation purpose
        Magnet_dict["__class__"] = "Magnet"
        return Magnet_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.mat_type is not None:
            self.mat_type._set_None()
        self.type_magnetization = None
        self.Lmag = None

    def _get_mat_type(self):
        """getter of mat_type"""
        return self._mat_type

    def _set_mat_type(self, value):
        """setter of mat_type"""
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    # The Magnet material
    # Type : Material
    mat_type = property(
        fget=_get_mat_type, fset=_set_mat_type, doc=u"""The Magnet material"""
    )

    def _get_type_magnetization(self):
        """getter of type_magnetization"""
        return self._type_magnetization

    def _set_type_magnetization(self, value):
        """setter of type_magnetization"""
        check_var("type_magnetization", value, "int", Vmin=0, Vmax=5)
        self._type_magnetization = value

    # Permanent magnet magnetization type: 0 for radial, 1 for parallel, 2 for HallBach []
    # Type : int, min = 0, max = 5
    type_magnetization = property(
        fget=_get_type_magnetization,
        fset=_set_type_magnetization,
        doc=u"""Permanent magnet magnetization type: 0 for radial, 1 for parallel, 2 for HallBach []""",
    )

    def _get_Lmag(self):
        """getter of Lmag"""
        return self._Lmag

    def _set_Lmag(self, value):
        """setter of Lmag"""
        check_var("Lmag", value, "float", Vmin=0)
        self._Lmag = value

    # Magnet axial length
    # Type : float, min = 0
    Lmag = property(fget=_get_Lmag, fset=_set_Lmag, doc=u"""Magnet axial length""")
