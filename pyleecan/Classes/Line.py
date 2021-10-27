# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Line.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Line
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
    from ..Methods.Geometry.Line.comp_normal import comp_normal
except ImportError as error:
    comp_normal = error


from ._check import InitUnKnowClassError


class Line(FrozenClass):
    """Abstract geometry class (A line between two points)"""

    VERSION = 1

    # cf Methods.Geometry.Line.comp_normal
    if isinstance(comp_normal, ImportError):
        comp_normal = property(
            fget=lambda x: raise_(
                ImportError("Can't use Line method comp_normal: " + str(comp_normal))
            )
        )
    else:
        comp_normal = comp_normal
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, prop_dict=None, init_dict=None, init_str=None):
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
            if "prop_dict" in list(init_dict.keys()):
                prop_dict = init_dict["prop_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.prop_dict = prop_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Line_str = ""
        if self.parent is None:
            Line_str += "parent = None " + linesep
        else:
            Line_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Line_str += "prop_dict = " + str(self.prop_dict) + linesep
        return Line_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.prop_dict != self.prop_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._prop_dict != self._prop_dict:
            diff_list.append(name + ".prop_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.prop_dict is not None:
            for key, value in self.prop_dict.items():
                S += getsizeof(value) + getsizeof(key)
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

        Line_dict = dict()
        Line_dict["prop_dict"] = (
            self.prop_dict.copy() if self.prop_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        Line_dict["__class__"] = "Line"
        return Line_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.prop_dict = None

    def _get_prop_dict(self):
        """getter of prop_dict"""
        return self._prop_dict

    def _set_prop_dict(self, value):
        """setter of prop_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("prop_dict", value, "dict")
        self._prop_dict = value

    prop_dict = property(
        fget=_get_prop_dict,
        fset=_set_prop_dict,
        doc=u"""Property dictionary

        :Type: dict
        """,
    )
