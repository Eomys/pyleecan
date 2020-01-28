# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Slot/Slot.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
import numpy
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Slot.Slot.build_geometry_half_tooth import (
        build_geometry_half_tooth,
    )
except ImportError as error:
    build_geometry_half_tooth = error

try:
    from pyleecan.Methods.Slot.Slot.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from pyleecan.Methods.Slot.Slot.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Slot.Slot.get_is_stator import get_is_stator
except ImportError as error:
    get_is_stator = error

try:
    from pyleecan.Methods.Slot.Slot.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from pyleecan.Methods.Slot.Slot.get_surface import get_surface
except ImportError as error:
    get_surface = error

try:
    from pyleecan.Methods.Slot.Slot.get_surface_tooth import get_surface_tooth
except ImportError as error:
    get_surface_tooth = error

try:
    from pyleecan.Methods.Slot.Slot.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error

try:
    from pyleecan.Methods.Slot.Slot.plot import plot
except ImportError as error:
    plot = error


from pyleecan.Classes._check import InitUnKnowClassError


class Slot(FrozenClass):
    """Generic class for slot (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.Slot.build_geometry_half_tooth
    if isinstance(build_geometry_half_tooth, ImportError):
        build_geometry_half_tooth = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method build_geometry_half_tooth: "
                    + str(build_geometry_half_tooth)
                )
            )
        )
    else:
        build_geometry_half_tooth = build_geometry_half_tooth
    # cf Methods.Slot.Slot.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.Slot.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.Slot.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.Slot.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.Slot.get_is_stator
    if isinstance(get_is_stator, ImportError):
        get_is_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method get_is_stator: " + str(get_is_stator)
                )
            )
        )
    else:
        get_is_stator = get_is_stator
    # cf Methods.Slot.Slot.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Slot.Slot.get_surface
    if isinstance(get_surface, ImportError):
        get_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_surface: " + str(get_surface))
            )
        )
    else:
        get_surface = get_surface
    # cf Methods.Slot.Slot.get_surface_tooth
    if isinstance(get_surface_tooth, ImportError):
        get_surface_tooth = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method get_surface_tooth: " + str(get_surface_tooth)
                )
            )
        )
    else:
        get_surface_tooth = get_surface_tooth
    # cf Methods.Slot.Slot.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # cf Methods.Slot.Slot.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method plot: " + str(plot))
            )
        )
    else:
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
