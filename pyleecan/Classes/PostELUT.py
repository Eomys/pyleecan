# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Post/PostELUT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Post/PostELUT
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
from .PostMethod import PostMethod

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Post.PostELUT.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .ELUT import ELUT


class PostELUT(PostMethod):
    """Class to generate an ELUT after the corresponding simulation"""

    VERSION = 1

    # cf Methods.Post.PostELUT.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use PostELUT method run: " + str(run))
            )
        )
    else:
        run = run
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        ELUT=None,
        is_save_ELUT=True,
        is_store_ELUT=True,
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
            if "ELUT" in list(init_dict.keys()):
                ELUT = init_dict["ELUT"]
            if "is_save_ELUT" in list(init_dict.keys()):
                is_save_ELUT = init_dict["is_save_ELUT"]
            if "is_store_ELUT" in list(init_dict.keys()):
                is_store_ELUT = init_dict["is_store_ELUT"]
        # Set the properties (value check and convertion are done in setter)
        self.ELUT = ELUT
        self.is_save_ELUT = is_save_ELUT
        self.is_store_ELUT = is_store_ELUT
        # Call PostMethod init
        super(PostELUT, self).__init__()
        # The class is frozen (in PostMethod init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PostELUT_str = ""
        # Get the properties inherited from PostMethod
        PostELUT_str += super(PostELUT, self).__str__()
        if self.ELUT is not None:
            tmp = self.ELUT.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            PostELUT_str += "ELUT = " + tmp
        else:
            PostELUT_str += "ELUT = None" + linesep + linesep
        PostELUT_str += "is_save_ELUT = " + str(self.is_save_ELUT) + linesep
        PostELUT_str += "is_store_ELUT = " + str(self.is_store_ELUT) + linesep
        return PostELUT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from PostMethod
        if not super(PostELUT, self).__eq__(other):
            return False
        if other.ELUT != self.ELUT:
            return False
        if other.is_save_ELUT != self.is_save_ELUT:
            return False
        if other.is_store_ELUT != self.is_store_ELUT:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from PostMethod
        diff_list.extend(super(PostELUT, self).compare(other, name=name))
        if (other.ELUT is None and self.ELUT is not None) or (
            other.ELUT is not None and self.ELUT is None
        ):
            diff_list.append(name + ".ELUT None mismatch")
        elif self.ELUT is not None:
            diff_list.extend(self.ELUT.compare(other.ELUT, name=name + ".ELUT"))
        if other._is_save_ELUT != self._is_save_ELUT:
            diff_list.append(name + ".is_save_ELUT")
        if other._is_store_ELUT != self._is_store_ELUT:
            diff_list.append(name + ".is_store_ELUT")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from PostMethod
        S += super(PostELUT, self).__sizeof__()
        S += getsizeof(self.ELUT)
        S += getsizeof(self.is_save_ELUT)
        S += getsizeof(self.is_store_ELUT)
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

        # Get the properties inherited from PostMethod
        PostELUT_dict = super(PostELUT, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.ELUT is None:
            PostELUT_dict["ELUT"] = None
        else:
            PostELUT_dict["ELUT"] = self.ELUT.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        PostELUT_dict["is_save_ELUT"] = self.is_save_ELUT
        PostELUT_dict["is_store_ELUT"] = self.is_store_ELUT
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PostELUT_dict["__class__"] = "PostELUT"
        return PostELUT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.ELUT is not None:
            self.ELUT._set_None()
        self.is_save_ELUT = None
        self.is_store_ELUT = None
        # Set to None the properties inherited from PostMethod
        super(PostELUT, self)._set_None()

    def _get_ELUT(self):
        """getter of ELUT"""
        return self._ELUT

    def _set_ELUT(self, value):
        """setter of ELUT"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "ELUT")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = ELUT()
        check_var("ELUT", value, "ELUT")
        self._ELUT = value

        if self._ELUT is not None:
            self._ELUT.parent = self

    ELUT = property(
        fget=_get_ELUT,
        fset=_set_ELUT,
        doc=u"""Electrical Look-Up Table to enforce

        :Type: ELUT
        """,
    )

    def _get_is_save_ELUT(self):
        """getter of is_save_ELUT"""
        return self._is_save_ELUT

    def _set_is_save_ELUT(self, value):
        """setter of is_save_ELUT"""
        check_var("is_save_ELUT", value, "bool")
        self._is_save_ELUT = value

    is_save_ELUT = property(
        fget=_get_is_save_ELUT,
        fset=_set_is_save_ELUT,
        doc=u"""True to save ELUT in PostELUT

        :Type: bool
        """,
    )

    def _get_is_store_ELUT(self):
        """getter of is_store_ELUT"""
        return self._is_store_ELUT

    def _set_is_store_ELUT(self, value):
        """setter of is_store_ELUT"""
        check_var("is_store_ELUT", value, "bool")
        self._is_store_ELUT = value

    is_store_ELUT = property(
        fget=_get_is_store_ELUT,
        fset=_set_is_store_ELUT,
        doc=u"""True to store ELUT in PostELUT

        :Type: bool
        """,
    )
