# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/RuleComplex.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/RuleComplex
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
from .Rules import Rules

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.RuleComplex.convert_to_P import convert_to_P
except ImportError as error:
    convert_to_P = error

try:
    from ..Methods.Converter.RuleComplex.convert_to_mot import convert_to_mot
except ImportError as error:
    convert_to_mot = error

try:
    from ..Methods.Converter.RuleComplex._set_fct_name import _set_fct_name
except ImportError as error:
    _set_fct_name = error


from numpy import isnan
from ._check import InitUnKnowClassError


class RuleComplex(Rules):
    """complex rules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.RuleComplex.convert_to_P
    if isinstance(convert_to_P, ImportError):
        convert_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleComplex method convert_to_P: " + str(convert_to_P)
                )
            )
        )
    else:
        convert_to_P = convert_to_P
    # cf Methods.Converter.RuleComplex.convert_to_mot
    if isinstance(convert_to_mot, ImportError):
        convert_to_mot = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleComplex method convert_to_mot: "
                    + str(convert_to_mot)
                )
            )
        )
    else:
        convert_to_mot = convert_to_mot
    # cf Methods.Converter.RuleComplex._set_fct_name
    if isinstance(_set_fct_name, ImportError):
        _set_fct_name = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RuleComplex method _set_fct_name: " + str(_set_fct_name)
                )
            )
        )
    else:
        _set_fct_name = _set_fct_name
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, fct_name=None, src=None, init_dict=None, init_str=None):
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
            if "fct_name" in list(init_dict.keys()):
                fct_name = init_dict["fct_name"]
            if "src" in list(init_dict.keys()):
                src = init_dict["src"]
        # Set the properties (value check and convertion are done in setter)
        self.fct_name = fct_name
        self.src = src
        # Call Rules init
        super(RuleComplex, self).__init__()
        # The class is frozen (in Rules init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RuleComplex_str = ""
        # Get the properties inherited from Rules
        RuleComplex_str += super(RuleComplex, self).__str__()
        RuleComplex_str += 'fct_name = "' + str(self.fct_name) + '"' + linesep
        RuleComplex_str += 'src = "' + str(self.src) + '"' + linesep
        return RuleComplex_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Rules
        if not super(RuleComplex, self).__eq__(other):
            return False
        if other.fct_name != self.fct_name:
            return False
        if other.src != self.src:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Rules
        diff_list.extend(
            super(RuleComplex, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._fct_name != self._fct_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._fct_name)
                    + ", other="
                    + str(other._fct_name)
                    + ")"
                )
                diff_list.append(name + ".fct_name" + val_str)
            else:
                diff_list.append(name + ".fct_name")
        if other._src != self._src:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._src) + ", other=" + str(other._src) + ")"
                )
                diff_list.append(name + ".src" + val_str)
            else:
                diff_list.append(name + ".src")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Rules
        S += super(RuleComplex, self).__sizeof__()
        S += getsizeof(self.fct_name)
        S += getsizeof(self.src)
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

        # Get the properties inherited from Rules
        RuleComplex_dict = super(RuleComplex, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        RuleComplex_dict["fct_name"] = self.fct_name
        RuleComplex_dict["src"] = self.src
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        RuleComplex_dict["__class__"] = "RuleComplex"
        return RuleComplex_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        fct_name_val = self.fct_name
        src_val = self.src
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(fct_name=fct_name_val, src=src_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.fct_name = None
        self.src = None
        # Set to None the properties inherited from Rules
        super(RuleComplex, self)._set_None()

    def _get_fct_name(self):
        """getter of fct_name"""
        return self._fct_name

    fct_name = property(
        fget=_get_fct_name,
        fset=_set_fct_name,
        doc=u"""fonction name to convert 

        :Type: str
        """,
    )

    def _get_src(self):
        """getter of src"""
        return self._src

    def _set_src(self, value):
        """setter of src"""
        check_var("src", value, "str")
        self._src = value

    src = property(
        fget=_get_src,
        fset=_set_src,
        doc=u"""name source

        :Type: str
        """,
    )
