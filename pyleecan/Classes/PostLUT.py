# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Post/PostLUT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Post/PostLUT
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
from .PostMethod import PostMethod

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Post.PostLUT.run import run
except ImportError as error:
    run = error


from numpy import isnan
from ._check import InitUnKnowClassError


class PostLUT(PostMethod):
    """Class to generate a LUT after the corresponding simulation"""

    VERSION = 1

    # cf Methods.Post.PostLUT.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use PostLUT method run: " + str(run))
            )
        )
    else:
        run = run
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, is_save_LUT=True, file_name="LUT", init_dict=None, init_str=None
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
            if "is_save_LUT" in list(init_dict.keys()):
                is_save_LUT = init_dict["is_save_LUT"]
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
        # Set the properties (value check and convertion are done in setter)
        self.is_save_LUT = is_save_LUT
        self.file_name = file_name
        # Call PostMethod init
        super(PostLUT, self).__init__()
        # The class is frozen (in PostMethod init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PostLUT_str = ""
        # Get the properties inherited from PostMethod
        PostLUT_str += super(PostLUT, self).__str__()
        PostLUT_str += "is_save_LUT = " + str(self.is_save_LUT) + linesep
        PostLUT_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        return PostLUT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from PostMethod
        if not super(PostLUT, self).__eq__(other):
            return False
        if other.is_save_LUT != self.is_save_LUT:
            return False
        if other.file_name != self.file_name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from PostMethod
        diff_list.extend(
            super(PostLUT, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._is_save_LUT != self._is_save_LUT:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_save_LUT)
                    + ", other="
                    + str(other._is_save_LUT)
                    + ")"
                )
                diff_list.append(name + ".is_save_LUT" + val_str)
            else:
                diff_list.append(name + ".is_save_LUT")
        if other._file_name != self._file_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._file_name)
                    + ", other="
                    + str(other._file_name)
                    + ")"
                )
                diff_list.append(name + ".file_name" + val_str)
            else:
                diff_list.append(name + ".file_name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from PostMethod
        S += super(PostLUT, self).__sizeof__()
        S += getsizeof(self.is_save_LUT)
        S += getsizeof(self.file_name)
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
        PostLUT_dict = super(PostLUT, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        PostLUT_dict["is_save_LUT"] = self.is_save_LUT
        PostLUT_dict["file_name"] = self.file_name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PostLUT_dict["__class__"] = "PostLUT"
        return PostLUT_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        is_save_LUT_val = self.is_save_LUT
        file_name_val = self.file_name
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(is_save_LUT=is_save_LUT_val, file_name=file_name_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_save_LUT = None
        self.file_name = None
        # Set to None the properties inherited from PostMethod
        super(PostLUT, self)._set_None()

    def _get_is_save_LUT(self):
        """getter of is_save_LUT"""
        return self._is_save_LUT

    def _set_is_save_LUT(self, value):
        """setter of is_save_LUT"""
        check_var("is_save_LUT", value, "bool")
        self._is_save_LUT = value

    is_save_LUT = property(
        fget=_get_is_save_LUT,
        fset=_set_is_save_LUT,
        doc=u"""True to save LUT in PostLUT

        :Type: bool
        """,
    )

    def _get_file_name(self):
        """getter of file_name"""
        return self._file_name

    def _set_file_name(self, value):
        """setter of file_name"""
        check_var("file_name", value, "str")
        self._file_name = value

    file_name = property(
        fget=_get_file_name,
        fset=_set_file_name,
        doc=u"""File name of the file created if is_save_LUT is True

        :Type: str
        """,
    )
