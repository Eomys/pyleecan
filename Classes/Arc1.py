# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Arc import Arc

from pyleecan.Methods.Geometry.Arc1.check import check
from pyleecan.Methods.Geometry.Arc1.comp_length import comp_length
from pyleecan.Methods.Geometry.Arc1.discretize import discretize
from pyleecan.Methods.Geometry.Arc1.get_begin import get_begin
from pyleecan.Methods.Geometry.Arc1.get_center import get_center
from pyleecan.Methods.Geometry.Arc1.get_end import get_end
from pyleecan.Methods.Geometry.Arc1.get_middle import get_middle
from pyleecan.Methods.Geometry.Arc1.rotate import rotate
from pyleecan.Methods.Geometry.Arc1.translate import translate
from pyleecan.Methods.Geometry.Arc1.get_angle import get_angle

from pyleecan.Classes.check import InitUnKnowClassError


class Arc1(Arc):
    """An arc between two points (defined by a radius)"""

    VERSION = 1

    # cf Methods.Geometry.Arc1.check
    check = check
    # cf Methods.Geometry.Arc1.comp_length
    comp_length = comp_length
    # cf Methods.Geometry.Arc1.discretize
    discretize = discretize
    # cf Methods.Geometry.Arc1.get_begin
    get_begin = get_begin
    # cf Methods.Geometry.Arc1.get_center
    get_center = get_center
    # cf Methods.Geometry.Arc1.get_end
    get_end = get_end
    # cf Methods.Geometry.Arc1.get_middle
    get_middle = get_middle
    # cf Methods.Geometry.Arc1.rotate
    rotate = rotate
    # cf Methods.Geometry.Arc1.translate
    translate = translate
    # cf Methods.Geometry.Arc1.get_angle
    get_angle = get_angle
    # save method is available in all object
    save = save

    def __init__(self, begin=0, end=0, radius=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["begin", "end", "radius", "label"])
            # Overwrite default value with init_dict content
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "end" in list(init_dict.keys()):
                end = init_dict["end"]
            if "radius" in list(init_dict.keys()):
                radius = init_dict["radius"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.begin = begin
        self.end = end
        self.radius = radius
        # Call Arc init
        super(Arc1, self).__init__(label=label)
        # The class is frozen (in Arc init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Arc1_str = ""
        # Get the properties inherited from Arc
        Arc1_str += super(Arc1, self).__str__() + linesep
        Arc1_str += "begin = " + str(self.begin) + linesep
        Arc1_str += "end = " + str(self.end) + linesep
        Arc1_str += "radius = " + str(self.radius)
        return Arc1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Arc
        if not super(Arc1, self).__eq__(other):
            return False
        if other.begin != self.begin:
            return False
        if other.end != self.end:
            return False
        if other.radius != self.radius:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Arc
        Arc1_dict = super(Arc1, self).as_dict()
        Arc1_dict["begin"] = self.begin
        Arc1_dict["end"] = self.end
        Arc1_dict["radius"] = self.radius
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Arc1_dict["__class__"] = "Arc1"
        return Arc1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.begin = None
        self.end = None
        self.radius = None
        # Set to None the properties inherited from Arc
        super(Arc1, self)._set_None()

    def _get_begin(self):
        """getter of begin"""
        return self._begin

    def _set_begin(self, value):
        """setter of begin"""
        check_var("begin", value, "complex")
        self._begin = value

    # begin point of the arc
    # Type : complex
    begin = property(
        fget=_get_begin, fset=_set_begin, doc=u"""begin point of the arc"""
    )

    def _get_end(self):
        """getter of end"""
        return self._end

    def _set_end(self, value):
        """setter of end"""
        check_var("end", value, "complex")
        self._end = value

    # end point of the arc
    # Type : complex
    end = property(fget=_get_end, fset=_set_end, doc=u"""end point of the arc""")

    def _get_radius(self):
        """getter of radius"""
        return self._radius

    def _set_radius(self, value):
        """setter of radius"""
        check_var("radius", value, "float")
        self._radius = value

    # Radius of the arc (can be + or -)
    # Type : float
    radius = property(
        fget=_get_radius, fset=_set_radius, doc=u"""Radius of the arc (can be + or -)"""
    )
