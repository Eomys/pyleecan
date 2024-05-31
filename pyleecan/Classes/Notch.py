# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Notch.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Notch
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
    from ..Methods.Machine.Notch.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Machine.Notch.get_Ryoke import get_Ryoke
except ImportError as error:
    get_Ryoke = error

try:
    from ..Methods.Machine.Notch.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error

try:
    from ..Methods.Machine.Notch.has_key import has_key
except ImportError as error:
    has_key = error

try:
    from ..Methods.Machine.Notch.get_label import get_label
except ImportError as error:
    get_label = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Notch(FrozenClass):

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Notch.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Machine.Notch.get_Ryoke
    if isinstance(get_Ryoke, ImportError):
        get_Ryoke = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Ryoke: " + str(get_Ryoke))
            )
        )
    else:
        get_Ryoke = get_Ryoke
    # cf Methods.Machine.Notch.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # cf Methods.Machine.Notch.has_key
    if isinstance(has_key, ImportError):
        has_key = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method has_key: " + str(has_key))
            )
        )
    else:
        has_key = has_key
    # cf Methods.Machine.Notch.get_label
    if isinstance(get_label, ImportError):
        get_label = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_label: " + str(get_label))
            )
        )
    else:
        get_label = get_label
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, key_mat=None, init_dict=None, init_str=None):
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
            if "key_mat" in list(init_dict.keys()):
                key_mat = init_dict["key_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.key_mat = key_mat

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Notch_str = ""
        if self.parent is None:
            Notch_str += "parent = None " + linesep
        else:
            Notch_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.key_mat is not None:
            tmp = self.key_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Notch_str += "key_mat = " + tmp
        else:
            Notch_str += "key_mat = None" + linesep + linesep
        return Notch_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.key_mat != self.key_mat:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.key_mat is None and self.key_mat is not None) or (
            other.key_mat is not None and self.key_mat is None
        ):
            diff_list.append(name + ".key_mat None mismatch")
        elif self.key_mat is not None:
            diff_list.extend(
                self.key_mat.compare(
                    other.key_mat,
                    name=name + ".key_mat",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.key_mat)
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

        Notch_dict = dict()
        if self.key_mat is None:
            Notch_dict["key_mat"] = None
        else:
            Notch_dict["key_mat"] = self.key_mat.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        Notch_dict["__class__"] = "Notch"
        return Notch_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.key_mat is None:
            key_mat_val = None
        else:
            key_mat_val = self.key_mat.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(key_mat=key_mat_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.key_mat is not None:
            self.key_mat._set_None()

    def _get_key_mat(self):
        """getter of key_mat"""
        return self._key_mat

    def _set_key_mat(self, value):
        """setter of key_mat"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "key_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Material = import_class("pyleecan.Classes", "Material", "key_mat")
            value = Material()
        check_var("key_mat", value, "Material")
        self._key_mat = value

        if self._key_mat is not None:
            self._key_mat.parent = self

    key_mat = property(
        fget=_get_key_mat,
        fset=_set_key_mat,
        doc="""The material of the key (if None, no key to add)

        :Type: Material
        """,
    )
