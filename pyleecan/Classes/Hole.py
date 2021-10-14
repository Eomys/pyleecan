# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/Hole.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/Hole
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.Hole.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.Hole.comp_magnetization_dict import comp_magnetization_dict
except ImportError as error:
    comp_magnetization_dict = error

try:
    from ..Methods.Slot.Hole.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.Hole.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.Hole.convert_to_UD import convert_to_UD
except ImportError as error:
    convert_to_UD = error

try:
    from ..Methods.Slot.Hole.get_is_stator import get_is_stator
except ImportError as error:
    get_is_stator = error

try:
    from ..Methods.Slot.Hole.get_magnet_by_id import get_magnet_by_id
except ImportError as error:
    get_magnet_by_id = error

try:
    from ..Methods.Slot.Hole.get_magnet_dict import get_magnet_dict
except ImportError as error:
    get_magnet_dict = error

try:
    from ..Methods.Slot.Hole.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Slot.Hole.get_Rext import get_Rext
except ImportError as error:
    get_Rext = error

try:
    from ..Methods.Slot.Hole.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.Hole.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Slot.Hole.set_magnet_by_id import set_magnet_by_id
except ImportError as error:
    set_magnet_by_id = error

try:
    from ..Methods.Slot.Hole.get_R_id import get_R_id
except ImportError as error:
    get_R_id = error


from ._check import InitUnKnowClassError
from .Material import Material


class Hole(FrozenClass):
    """Holes for lamination (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.Hole.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.Hole.comp_magnetization_dict
    if isinstance(comp_magnetization_dict, ImportError):
        comp_magnetization_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method comp_magnetization_dict: "
                    + str(comp_magnetization_dict)
                )
            )
        )
    else:
        comp_magnetization_dict = comp_magnetization_dict
    # cf Methods.Slot.Hole.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.Hole.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.Hole.convert_to_UD
    if isinstance(convert_to_UD, ImportError):
        convert_to_UD = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method convert_to_UD: " + str(convert_to_UD)
                )
            )
        )
    else:
        convert_to_UD = convert_to_UD
    # cf Methods.Slot.Hole.get_is_stator
    if isinstance(get_is_stator, ImportError):
        get_is_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method get_is_stator: " + str(get_is_stator)
                )
            )
        )
    else:
        get_is_stator = get_is_stator
    # cf Methods.Slot.Hole.get_magnet_by_id
    if isinstance(get_magnet_by_id, ImportError):
        get_magnet_by_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method get_magnet_by_id: " + str(get_magnet_by_id)
                )
            )
        )
    else:
        get_magnet_by_id = get_magnet_by_id
    # cf Methods.Slot.Hole.get_magnet_dict
    if isinstance(get_magnet_dict, ImportError):
        get_magnet_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method get_magnet_dict: " + str(get_magnet_dict)
                )
            )
        )
    else:
        get_magnet_dict = get_magnet_dict
    # cf Methods.Slot.Hole.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Slot.Hole.get_Rext
    if isinstance(get_Rext, ImportError):
        get_Rext = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method get_Rext: " + str(get_Rext))
            )
        )
    else:
        get_Rext = get_Rext
    # cf Methods.Slot.Hole.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.Hole.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Slot.Hole.set_magnet_by_id
    if isinstance(set_magnet_by_id, ImportError):
        set_magnet_by_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method set_magnet_by_id: " + str(set_magnet_by_id)
                )
            )
        )
    else:
        set_magnet_by_id = set_magnet_by_id
    # cf Methods.Slot.Hole.get_R_id
    if isinstance(get_R_id, ImportError):
        get_R_id = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method get_R_id: " + str(get_R_id))
            )
        )
    else:
        get_R_id = get_R_id
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Zh=36,
        mat_void=-1,
        magnetization_dict_offset=None,
        Alpha0=0,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
            if "magnetization_dict_offset" in list(init_dict.keys()):
                magnetization_dict_offset = init_dict["magnetization_dict_offset"]
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Zh = Zh
        self.mat_void = mat_void
        self.magnetization_dict_offset = magnetization_dict_offset
        self.Alpha0 = Alpha0

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Hole_str = ""
        if self.parent is None:
            Hole_str += "parent = None " + linesep
        else:
            Hole_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Hole_str += "Zh = " + str(self.Zh) + linesep
        if self.mat_void is not None:
            tmp = self.mat_void.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Hole_str += "mat_void = " + tmp
        else:
            Hole_str += "mat_void = None" + linesep + linesep
        Hole_str += (
            "magnetization_dict_offset = "
            + str(self.magnetization_dict_offset)
            + linesep
        )
        Hole_str += "Alpha0 = " + str(self.Alpha0) + linesep
        return Hole_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Zh != self.Zh:
            return False
        if other.mat_void != self.mat_void:
            return False
        if other.magnetization_dict_offset != self.magnetization_dict_offset:
            return False
        if other.Alpha0 != self.Alpha0:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Zh != self._Zh:
            diff_list.append(name + ".Zh")
        if (other.mat_void is None and self.mat_void is not None) or (
            other.mat_void is not None and self.mat_void is None
        ):
            diff_list.append(name + ".mat_void None mismatch")
        elif self.mat_void is not None:
            diff_list.extend(
                self.mat_void.compare(other.mat_void, name=name + ".mat_void")
            )
        if other._magnetization_dict_offset != self._magnetization_dict_offset:
            diff_list.append(name + ".magnetization_dict_offset")
        if other._Alpha0 != self._Alpha0:
            diff_list.append(name + ".Alpha0")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Zh)
        S += getsizeof(self.mat_void)
        if self.magnetization_dict_offset is not None:
            for key, value in self.magnetization_dict_offset.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Alpha0)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        Hole_dict = dict()
        Hole_dict["Zh"] = self.Zh
        if self.mat_void is None:
            Hole_dict["mat_void"] = None
        else:
            Hole_dict["mat_void"] = self.mat_void.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Hole_dict["magnetization_dict_offset"] = (
            self.magnetization_dict_offset.copy()
            if self.magnetization_dict_offset is not None
            else None
        )
        Hole_dict["Alpha0"] = self.Alpha0
        # The class name is added to the dict for deserialisation purpose
        Hole_dict["__class__"] = "Hole"
        return Hole_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Zh = None
        if self.mat_void is not None:
            self.mat_void._set_None()
        self.magnetization_dict_offset = None
        self.Alpha0 = None

    def _get_Zh(self):
        """getter of Zh"""
        return self._Zh

    def _set_Zh(self, value):
        """setter of Zh"""
        check_var("Zh", value, "int", Vmin=0)
        self._Zh = value

    Zh = property(
        fget=_get_Zh,
        fset=_set_Zh,
        doc=u"""Number of Hole around the circumference

        :Type: int
        :min: 0
        """,
    )

    def _get_mat_void(self):
        """getter of mat_void"""
        return self._mat_void

    def _set_mat_void(self, value):
        """setter of mat_void"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "mat_void"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Material()
        check_var("mat_void", value, "Material")
        self._mat_void = value

        if self._mat_void is not None:
            self._mat_void.parent = self

    mat_void = property(
        fget=_get_mat_void,
        fset=_set_mat_void,
        doc=u"""Material of the void part of the hole (Air in general)

        :Type: Material
        """,
    )

    def _get_magnetization_dict_offset(self):
        """getter of magnetization_dict_offset"""
        return self._magnetization_dict_offset

    def _set_magnetization_dict_offset(self, value):
        """setter of magnetization_dict_offset"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("magnetization_dict_offset", value, "dict")
        self._magnetization_dict_offset = value

    magnetization_dict_offset = property(
        fget=_get_magnetization_dict_offset,
        fset=_set_magnetization_dict_offset,
        doc=u"""Dictionary add an offset to the magnetization direction of the magnets (key=magnet_X, value=angle[rad])

        :Type: dict
        """,
    )

    def _get_Alpha0(self):
        """getter of Alpha0"""
        return self._Alpha0

    def _set_Alpha0(self, value):
        """setter of Alpha0"""
        check_var("Alpha0", value, "float", Vmin=0, Vmax=6.29)
        self._Alpha0 = value

    Alpha0 = property(
        fget=_get_Alpha0,
        fset=_set_Alpha0,
        doc=u"""Shift angle of the holes around circumference

        :Type: float
        :min: 0
        :max: 6.29
        """,
    )
