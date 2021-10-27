# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutPost.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutPost
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


class OutPost(FrozenClass):
    """Gather the parameters for the post-processings"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, legend_name="", line_color="", init_dict=None, init_str=None):
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
            if "legend_name" in list(init_dict.keys()):
                legend_name = init_dict["legend_name"]
            if "line_color" in list(init_dict.keys()):
                line_color = init_dict["line_color"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.legend_name = legend_name
        self.line_color = line_color

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutPost_str = ""
        if self.parent is None:
            OutPost_str += "parent = None " + linesep
        else:
            OutPost_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutPost_str += 'legend_name = "' + str(self.legend_name) + '"' + linesep
        OutPost_str += 'line_color = "' + str(self.line_color) + '"' + linesep
        return OutPost_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.legend_name != self.legend_name:
            return False
        if other.line_color != self.line_color:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._legend_name != self._legend_name:
            diff_list.append(name + ".legend_name")
        if other._line_color != self._line_color:
            diff_list.append(name + ".line_color")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.legend_name)
        S += getsizeof(self.line_color)
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

        OutPost_dict = dict()
        OutPost_dict["legend_name"] = self.legend_name
        OutPost_dict["line_color"] = self.line_color
        # The class name is added to the dict for deserialisation purpose
        OutPost_dict["__class__"] = "OutPost"
        return OutPost_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.legend_name = None
        self.line_color = None

    def _get_legend_name(self):
        """getter of legend_name"""
        return self._legend_name

    def _set_legend_name(self, value):
        """setter of legend_name"""
        check_var("legend_name", value, "str")
        self._legend_name = value

    legend_name = property(
        fget=_get_legend_name,
        fset=_set_legend_name,
        doc=u"""Name to use in the legend in case of comparison

        :Type: str
        """,
    )

    def _get_line_color(self):
        """getter of line_color"""
        return self._line_color

    def _set_line_color(self, value):
        """setter of line_color"""
        check_var("line_color", value, "str")
        self._line_color = value

    line_color = property(
        fget=_get_line_color,
        fset=_set_line_color,
        doc=u"""Color to use in case of comparison

        :Type: str
        """,
    )
