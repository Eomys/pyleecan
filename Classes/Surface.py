# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Geometry.Surface.draw_FEMM import draw_FEMM

from pyleecan.Classes.check import InitUnKnowClassError


class Surface(FrozenClass):
    """SurfLine define by list of lines that delimit it, label and point reference."""

    VERSION = 1

    # cf Methods.Geometry.Surface.draw_FEMM
    draw_FEMM = draw_FEMM
    # save method is available in all object
    save = save

    def __init__(self, point_ref=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["point_ref", "label"])
            # Overwrite default value with init_dict content
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.parent = None
        self.point_ref = point_ref
        self.label = label

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Surface_str = ""
        if self.parent is None:
            Surface_str += "parent = None " + linesep
        else:
            Surface_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Surface_str += "point_ref = " + str(self.point_ref) + linesep
        Surface_str += 'label = "' + str(self.label) + '"'
        return Surface_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.point_ref != self.point_ref:
            return False
        if other.label != self.label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Surface_dict = dict()
        Surface_dict["point_ref"] = self.point_ref
        Surface_dict["label"] = self.label
        # The class name is added to the dict fordeserialisation purpose
        Surface_dict["__class__"] = "Surface"
        return Surface_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.point_ref = None
        self.label = None

    def _get_point_ref(self):
        """getter of point_ref"""
        return self._point_ref

    def _set_point_ref(self, value):
        """setter of point_ref"""
        check_var("point_ref", value, "complex")
        self._point_ref = value

    # Center of symmetry
    # Type : complex
    point_ref = property(fget=_get_point_ref, fset=_set_point_ref,
                         doc=u"""Center of symmetry""")

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    # Label of the surface
    # Type : str
    label = property(fget=_get_label, fset=_set_label,
                     doc=u"""Label of the surface""")
