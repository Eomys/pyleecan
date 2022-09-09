# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Bore.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Bore
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.Bore.merge_slot import merge_slot
except ImportError as error:
    merge_slot = error

try:
    from ..Methods.Machine.Bore.is_yoke import is_yoke
except ImportError as error:
    is_yoke = error

try:
    from ..Methods.Machine.Bore.merge_slot_connect import merge_slot_connect
except ImportError as error:
    merge_slot_connect = error

try:
    from ..Methods.Machine.Bore.merge_slot_intersect import merge_slot_intersect
except ImportError as error:
    merge_slot_intersect = error

try:
    from ..Methods.Machine.Bore.merge_slot_translate import merge_slot_translate
except ImportError as error:
    merge_slot_translate = error

try:
    from ..Methods.Machine.Bore.comp_Rmin import comp_Rmin
except ImportError as error:
    comp_Rmin = error

try:
    from ..Methods.Machine.Bore.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.Bore.get_surface import get_surface
except ImportError as error:
    get_surface = error

try:
    from ..Methods.Machine.Bore.plot import plot
except ImportError as error:
    plot = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Bore(FrozenClass):
    """Abstract class for Bore shape"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Bore.merge_slot
    if isinstance(merge_slot, ImportError):
        merge_slot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method merge_slot: " + str(merge_slot))
            )
        )
    else:
        merge_slot = merge_slot
    # cf Methods.Machine.Bore.is_yoke
    if isinstance(is_yoke, ImportError):
        is_yoke = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method is_yoke: " + str(is_yoke))
            )
        )
    else:
        is_yoke = is_yoke
    # cf Methods.Machine.Bore.merge_slot_connect
    if isinstance(merge_slot_connect, ImportError):
        merge_slot_connect = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Bore method merge_slot_connect: "
                    + str(merge_slot_connect)
                )
            )
        )
    else:
        merge_slot_connect = merge_slot_connect
    # cf Methods.Machine.Bore.merge_slot_intersect
    if isinstance(merge_slot_intersect, ImportError):
        merge_slot_intersect = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Bore method merge_slot_intersect: "
                    + str(merge_slot_intersect)
                )
            )
        )
    else:
        merge_slot_intersect = merge_slot_intersect
    # cf Methods.Machine.Bore.merge_slot_translate
    if isinstance(merge_slot_translate, ImportError):
        merge_slot_translate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Bore method merge_slot_translate: "
                    + str(merge_slot_translate)
                )
            )
        )
    else:
        merge_slot_translate = merge_slot_translate
    # cf Methods.Machine.Bore.comp_Rmin
    if isinstance(comp_Rmin, ImportError):
        comp_Rmin = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method comp_Rmin: " + str(comp_Rmin))
            )
        )
    else:
        comp_Rmin = comp_Rmin
    # cf Methods.Machine.Bore.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.Bore.get_surface
    if isinstance(get_surface, ImportError):
        get_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method get_surface: " + str(get_surface))
            )
        )
    else:
        get_surface = get_surface
    # cf Methods.Machine.Bore.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Bore method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, type_merge_slot=1, init_dict=None, init_str=None):
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
            if "type_merge_slot" in list(init_dict.keys()):
                type_merge_slot = init_dict["type_merge_slot"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.type_merge_slot = type_merge_slot

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Bore_str = ""
        if self.parent is None:
            Bore_str += "parent = None " + linesep
        else:
            Bore_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Bore_str += "type_merge_slot = " + str(self.type_merge_slot) + linesep
        return Bore_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_merge_slot != self.type_merge_slot:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._type_merge_slot != self._type_merge_slot:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_merge_slot)
                    + ", other="
                    + str(other._type_merge_slot)
                    + ")"
                )
                diff_list.append(name + ".type_merge_slot" + val_str)
            else:
                diff_list.append(name + ".type_merge_slot")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.type_merge_slot)
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

        Bore_dict = dict()
        Bore_dict["type_merge_slot"] = self.type_merge_slot
        # The class name is added to the dict for deserialisation purpose
        Bore_dict["__class__"] = "Bore"
        return Bore_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_merge_slot_val = self.type_merge_slot
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(type_merge_slot=type_merge_slot_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_merge_slot = None

    def _get_type_merge_slot(self):
        """getter of type_merge_slot"""
        return self._type_merge_slot

    def _set_type_merge_slot(self, value):
        """setter of type_merge_slot"""
        check_var("type_merge_slot", value, "int", Vmin=0, Vmax=2)
        self._type_merge_slot = value

    type_merge_slot = property(
        fget=_get_type_merge_slot,
        fset=_set_type_merge_slot,
        doc=u"""how to merge slot/notch into the bore radius (0: connect the dot, 1: intersection, 2: translate)

        :Type: int
        :min: 0
        :max: 2
        """,
    )
