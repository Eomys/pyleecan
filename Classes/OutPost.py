# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutPost.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
import numpy
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from pyleecan.Classes._check import InitUnKnowClassError


class OutPost(FrozenClass):
    """Gather the parameters for the post-processings"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, legend_name="", line_color="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["legend_name", "line_color"])
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
        OutPost_str += 'line_color = "' + str(self.line_color) + '"'
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

    # Name to use in the legend in case of comparison
    # Type : str
    legend_name = property(
        fget=_get_legend_name,
        fset=_set_legend_name,
        doc=u"""Name to use in the legend in case of comparison""",
    )

    def _get_line_color(self):
        """getter of line_color"""
        return self._line_color

    def _set_line_color(self, value):
        """setter of line_color"""
        check_var("line_color", value, "str")
        self._line_color = value

    # Color to use in case of comparison
    # Type : str
    line_color = property(
        fget=_get_line_color,
        fset=_set_line_color,
        doc=u"""Color to use in case of comparison""",
    )
