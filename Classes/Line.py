# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Geometry/Line.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from pyleecan.Classes._check import InitUnKnowClassError


class Line(FrozenClass):
    """Abstract geometry class (A line between two points)"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.parent = None
        self.label = label

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Line_str = ""
        if self.parent is None:
            Line_str += "parent = None " + linesep
        else:
            Line_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Line_str += 'label = "' + str(self.label) + '"' + linesep
        return Line_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.label != self.label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Line_dict = dict()
        Line_dict["label"] = self.label
        # The class name is added to the dict fordeserialisation purpose
        Line_dict["__class__"] = "Line"
        return Line_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.label = None

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    # the label of the Line (EX: Yoke_side)
    # Type : str
    label = property(
        fget=_get_label,
        fset=_set_label,
        doc=u"""the label of the Line (EX: Yoke_side)""",
    )
