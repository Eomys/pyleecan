# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Line import Line

from pyleecan.Methods.Geometry.Segment.check import check
from pyleecan.Methods.Geometry.Segment.comp_length import comp_length
from pyleecan.Methods.Geometry.Segment.discretize import discretize
from pyleecan.Methods.Geometry.Segment.draw_FEMM import draw_FEMM
from pyleecan.Methods.Geometry.Segment.get_begin import get_begin
from pyleecan.Methods.Geometry.Segment.get_end import get_end
from pyleecan.Methods.Geometry.Segment.get_middle import get_middle
from pyleecan.Methods.Geometry.Segment.intersect_line import intersect_line
from pyleecan.Methods.Geometry.Segment.reverse import reverse
from pyleecan.Methods.Geometry.Segment.rotate import rotate
from pyleecan.Methods.Geometry.Segment.split_half import split_half
from pyleecan.Methods.Geometry.Segment.split_line import split_line
from pyleecan.Methods.Geometry.Segment.translate import translate

from pyleecan.Classes.check import InitUnKnowClassError


class Segment(Line):
    """A segment between two points"""

    VERSION = 1

    # cf Methods.Geometry.Segment.check
    check = check
    # cf Methods.Geometry.Segment.comp_length
    comp_length = comp_length
    # cf Methods.Geometry.Segment.discretize
    discretize = discretize
    # cf Methods.Geometry.Segment.draw_FEMM
    draw_FEMM = draw_FEMM
    # cf Methods.Geometry.Segment.get_begin
    get_begin = get_begin
    # cf Methods.Geometry.Segment.get_end
    get_end = get_end
    # cf Methods.Geometry.Segment.get_middle
    get_middle = get_middle
    # cf Methods.Geometry.Segment.intersect_line
    intersect_line = intersect_line
    # cf Methods.Geometry.Segment.reverse
    reverse = reverse
    # cf Methods.Geometry.Segment.rotate
    rotate = rotate
    # cf Methods.Geometry.Segment.split_half
    split_half = split_half
    # cf Methods.Geometry.Segment.split_line
    split_line = split_line
    # cf Methods.Geometry.Segment.translate
    translate = translate
    # save method is available in all object
    save = save

    def __init__(self, begin=0, end=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["begin", "end", "label"])
            # Overwrite default value with init_dict content
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "end" in list(init_dict.keys()):
                end = init_dict["end"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.begin = begin
        self.end = end
        # Call Line init
        super(Segment, self).__init__(label=label)
        # The class is frozen (in Line init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Segment_str = ""
        # Get the properties inherited from Line
        Segment_str += super(Segment, self).__str__() + linesep
        Segment_str += "begin = " + str(self.begin) + linesep
        Segment_str += "end = " + str(self.end)
        return Segment_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Line
        if not super(Segment, self).__eq__(other):
            return False
        if other.begin != self.begin:
            return False
        if other.end != self.end:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Line
        Segment_dict = super(Segment, self).as_dict()
        Segment_dict["begin"] = self.begin
        Segment_dict["end"] = self.end
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Segment_dict["__class__"] = "Segment"
        return Segment_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.begin = None
        self.end = None
        # Set to None the properties inherited from Line
        super(Segment, self)._set_None()

    def _get_begin(self):
        """getter of begin"""
        return self._begin

    def _set_begin(self, value):
        """setter of begin"""
        check_var("begin", value, "complex")
        self._begin = value

    # begin point of the line
    # Type : complex
    begin = property(
        fget=_get_begin, fset=_set_begin, doc=u"""begin point of the line"""
    )

    def _get_end(self):
        """getter of end"""
        return self._end

    def _set_end(self, value):
        """setter of end"""
        check_var("end", value, "complex")
        self._end = value

    # end point of the line
    # Type : complex
    end = property(fget=_get_end, fset=_set_end, doc=u"""end point of the line""")
