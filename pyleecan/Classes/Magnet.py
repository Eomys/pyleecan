# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Magnet.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Magnet
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

from ._check import InitUnKnowClassError
from .Material import Material


class Magnet(FrozenClass):
    """Magnet class"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mat_type=-1,
        type_magnetization=0,
        Lmag=0.95,
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
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "type_magnetization" in list(init_dict.keys()):
                type_magnetization = init_dict["type_magnetization"]
            if "Lmag" in list(init_dict.keys()):
                Lmag = init_dict["Lmag"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.mat_type = mat_type
        self.type_magnetization = type_magnetization
        self.Lmag = Lmag

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Magnet_str = ""
        if self.parent is None:
            Magnet_str += "parent = None " + linesep
        else:
            Magnet_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.mat_type is not None:
            tmp = self.mat_type.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Magnet_str += "mat_type = " + tmp
        else:
            Magnet_str += "mat_type = None" + linesep + linesep
        Magnet_str += "type_magnetization = " + str(self.type_magnetization) + linesep
        Magnet_str += "Lmag = " + str(self.Lmag) + linesep
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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.mat_type is None and self.mat_type is not None) or (
            other.mat_type is not None and self.mat_type is None
        ):
            diff_list.append(name + ".mat_type None mismatch")
        elif self.mat_type is not None:
            diff_list.extend(
                self.mat_type.compare(other.mat_type, name=name + ".mat_type")
            )
        if other._type_magnetization != self._type_magnetization:
            diff_list.append(name + ".type_magnetization")
        if other._Lmag != self._Lmag:
            diff_list.append(name + ".Lmag")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.mat_type)
        S += getsizeof(self.type_magnetization)
        S += getsizeof(self.Lmag)
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

        Magnet_dict = dict()
        if self.mat_type is None:
            Magnet_dict["mat_type"] = None
        else:
            Magnet_dict["mat_type"] = self.mat_type.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Magnet_dict["type_magnetization"] = self.type_magnetization
        Magnet_dict["Lmag"] = self.Lmag
        # The class name is added to the dict for deserialisation purpose
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
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "mat_type"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Material()
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    mat_type = property(
        fget=_get_mat_type,
        fset=_set_mat_type,
        doc=u"""The Magnet material

        :Type: Material
        """,
    )

    def _get_type_magnetization(self):
        """getter of type_magnetization"""
        return self._type_magnetization

    def _set_type_magnetization(self, value):
        """setter of type_magnetization"""
        check_var("type_magnetization", value, "int", Vmin=0, Vmax=3)
        self._type_magnetization = value

    type_magnetization = property(
        fget=_get_type_magnetization,
        fset=_set_type_magnetization,
        doc=u"""Permanent magnet magnetization type: 0 for radial, 1 for parallel, 2 for Hallbach, 3 Tangential

        :Type: int
        :min: 0
        :max: 3
        """,
    )

    def _get_Lmag(self):
        """getter of Lmag"""
        return self._Lmag

    def _set_Lmag(self, value):
        """setter of Lmag"""
        check_var("Lmag", value, "float", Vmin=0)
        self._Lmag = value

    Lmag = property(
        fget=_get_Lmag,
        fset=_set_Lmag,
        doc=u"""Magnet axial length

        :Type: float
        :min: 0
        """,
    )
