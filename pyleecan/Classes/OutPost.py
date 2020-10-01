# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutPost.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutPost
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class OutPost(FrozenClass):
    """Gather the parameters for the post-processings"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, legend_name="", line_color="", init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None :  # Initialisation by str
            from ..Functions.load import load
            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            legend_name = obj.legend_name
            line_color = obj.line_color
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "legend_name" in list(init_dict.keys()):
                legend_name = init_dict["legend_name"]
            if "line_color" in list(init_dict.keys()):
                line_color = init_dict["line_color"]
        # Initialisation by argument
        self.parent = None
        self.legend_name = legend_name
        self.line_color = line_color

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutPost_dict = dict()
        OutPost_dict["legend_name"] = self.legend_name
        OutPost_dict["line_color"] = self.line_color
        # The class name is added to the dict fordeserialisation purpose
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
