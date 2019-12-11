# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.Frame.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.Frame.comp_height_eq import comp_height_eq
except ImportError as error:
    comp_height_eq = error

try:
    from pyleecan.Methods.Machine.Frame.comp_mass import comp_mass
except ImportError as error:
    comp_mass = error

try:
    from pyleecan.Methods.Machine.Frame.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Machine.Frame.comp_volume import comp_volume
except ImportError as error:
    comp_volume = error

try:
    from pyleecan.Methods.Machine.Frame.get_length import get_length
except ImportError as error:
    get_length = error

try:
    from pyleecan.Methods.Machine.Frame.plot import plot
except ImportError as error:
    plot = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material


class Frame(FrozenClass):
    """machine frame"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Frame.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Frame method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.Frame.comp_height_eq
    if isinstance(comp_height_eq, ImportError):
        comp_height_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Frame method comp_height_eq: " + str(comp_height_eq)
                )
            )
        )
    else:
        comp_height_eq = comp_height_eq
    # cf Methods.Machine.Frame.comp_mass
    if isinstance(comp_mass, ImportError):
        comp_mass = property(
            fget=lambda x: raise_(
                ImportError("Can't use Frame method comp_mass: " + str(comp_mass))
            )
        )
    else:
        comp_mass = comp_mass
    # cf Methods.Machine.Frame.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Frame method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.Frame.comp_volume
    if isinstance(comp_volume, ImportError):
        comp_volume = property(
            fget=lambda x: raise_(
                ImportError("Can't use Frame method comp_volume: " + str(comp_volume))
            )
        )
    else:
        comp_volume = comp_volume
    # cf Methods.Machine.Frame.get_length
    if isinstance(get_length, ImportError):
        get_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Frame method get_length: " + str(get_length))
            )
        )
    else:
        get_length = get_length
    # cf Methods.Machine.Frame.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Frame method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # save method is available in all object
    save = save

    def __init__(self, Lfra=0.35, Rint=0.2, Rext=0.2, mat_type=-1, init_dict=None):
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
            check_init_dict(init_dict, ["Lfra", "Rint", "Rext", "mat_type"])
            # Overwrite default value with init_dict content
            if "Lfra" in list(init_dict.keys()):
                Lfra = init_dict["Lfra"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
        # Initialisation by argument
        self.parent = None
        self.Lfra = Lfra
        self.Rint = Rint
        self.Rext = Rext
        # mat_type can be None, a Material object or a dict
        if isinstance(mat_type, dict):
            self.mat_type = Material(init_dict=mat_type)
        else:
            self.mat_type = mat_type

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Frame_str = ""
        if self.parent is None:
            Frame_str += "parent = None " + linesep
        else:
            Frame_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Frame_str += "Lfra = " + str(self.Lfra) + linesep
        Frame_str += "Rint = " + str(self.Rint) + linesep
        Frame_str += "Rext = " + str(self.Rext) + linesep
        if self.mat_type is not None:
            Frame_str += (
                "mat_type = " + str(self.mat_type.as_dict()) + linesep + linesep
            )
        else:
            Frame_str += "mat_type = None"
        return Frame_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Lfra != self.Lfra:
            return False
        if other.Rint != self.Rint:
            return False
        if other.Rext != self.Rext:
            return False
        if other.mat_type != self.mat_type:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Frame_dict = dict()
        Frame_dict["Lfra"] = self.Lfra
        Frame_dict["Rint"] = self.Rint
        Frame_dict["Rext"] = self.Rext
        if self.mat_type is None:
            Frame_dict["mat_type"] = None
        else:
            Frame_dict["mat_type"] = self.mat_type.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Frame_dict["__class__"] = "Frame"
        return Frame_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Lfra = None
        self.Rint = None
        self.Rext = None
        if self.mat_type is not None:
            self.mat_type._set_None()

    def _get_Lfra(self):
        """getter of Lfra"""
        return self._Lfra

    def _set_Lfra(self, value):
        """setter of Lfra"""
        check_var("Lfra", value, "float", Vmin=0)
        self._Lfra = value

    # frame length [m]
    # Type : float, min = 0
    Lfra = property(fget=_get_Lfra, fset=_set_Lfra, doc=u"""frame length [m]""")

    def _get_Rint(self):
        """getter of Rint"""
        return self._Rint

    def _set_Rint(self, value):
        """setter of Rint"""
        check_var("Rint", value, "float", Vmin=0)
        self._Rint = value

    # frame internal radius
    # Type : float, min = 0
    Rint = property(fget=_get_Rint, fset=_set_Rint, doc=u"""frame internal radius""")

    def _get_Rext(self):
        """getter of Rext"""
        return self._Rext

    def _set_Rext(self, value):
        """setter of Rext"""
        check_var("Rext", value, "float", Vmin=0)
        self._Rext = value

    # Frame external radius
    # Type : float, min = 0
    Rext = property(fget=_get_Rext, fset=_set_Rext, doc=u"""Frame external radius""")

    def _get_mat_type(self):
        """getter of mat_type"""
        return self._mat_type

    def _set_mat_type(self, value):
        """setter of mat_type"""
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    # Frame material
    # Type : Material
    mat_type = property(
        fget=_get_mat_type, fset=_set_mat_type, doc=u"""Frame material"""
    )
