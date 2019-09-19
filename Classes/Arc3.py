# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Arc import Arc

from pyleecan.Methods.Geometry.Arc3.check import check
from pyleecan.Methods.Geometry.Arc3.comp_length import comp_length
from pyleecan.Methods.Geometry.Arc3.comp_radius import comp_radius
from pyleecan.Methods.Geometry.Arc3.discretize import discretize
from pyleecan.Methods.Geometry.Arc3.get_angle import get_angle
from pyleecan.Methods.Geometry.Arc3.get_begin import get_begin
from pyleecan.Methods.Geometry.Arc3.get_center import get_center
from pyleecan.Methods.Geometry.Arc3.get_end import get_end
from pyleecan.Methods.Geometry.Arc3.get_middle import get_middle
from pyleecan.Methods.Geometry.Arc3.reverse import reverse
from pyleecan.Methods.Geometry.Arc3.rotate import rotate
from pyleecan.Methods.Geometry.Arc3.split_half import split_half
from pyleecan.Methods.Geometry.Arc3.translate import translate

from pyleecan.Classes.check import InitUnKnowClassError


class Arc3(Arc):
    """Half circle define by two points"""

    VERSION = 1

    # cf Methods.Geometry.Arc3.check
    check = check
    # cf Methods.Geometry.Arc3.comp_length
    comp_length = comp_length
    # cf Methods.Geometry.Arc3.comp_radius
    comp_radius = comp_radius
    # cf Methods.Geometry.Arc3.discretize
    discretize = discretize
    # cf Methods.Geometry.Arc3.get_angle
    get_angle = get_angle
    # cf Methods.Geometry.Arc3.get_begin
    get_begin = get_begin
    # cf Methods.Geometry.Arc3.get_center
    get_center = get_center
    # cf Methods.Geometry.Arc3.get_end
    get_end = get_end
    # cf Methods.Geometry.Arc3.get_middle
    get_middle = get_middle
    # cf Methods.Geometry.Arc3.reverse
    reverse = reverse
    # cf Methods.Geometry.Arc3.rotate
    rotate = rotate
    # cf Methods.Geometry.Arc3.split_half
    split_half = split_half
    # cf Methods.Geometry.Arc3.translate
    translate = translate
    # save method is available in all object
    save = save

    def __init__(self, begin=0, end=0, is_trigo_direction=False, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["begin", "end", "is_trigo_direction", "label"])
            # Overwrite default value with init_dict content
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "end" in list(init_dict.keys()):
                end = init_dict["end"]
            if "is_trigo_direction" in list(init_dict.keys()):
                is_trigo_direction = init_dict["is_trigo_direction"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.begin = begin
        self.end = end
        self.is_trigo_direction = is_trigo_direction
        # Call Arc init
        super(Arc3, self).__init__(label=label)
        # The class is frozen (in Arc init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Arc3_str = ""
        # Get the properties inherited from Arc
        Arc3_str += super(Arc3, self).__str__() + linesep
        Arc3_str += "begin = " + str(self.begin) + linesep
        Arc3_str += "end = " + str(self.end) + linesep
        Arc3_str += "is_trigo_direction = " + str(self.is_trigo_direction)
        return Arc3_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Arc
        if not super(Arc3, self).__eq__(other):
            return False
        if other.begin != self.begin:
            return False
        if other.end != self.end:
            return False
        if other.is_trigo_direction != self.is_trigo_direction:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Arc
        Arc3_dict = super(Arc3, self).as_dict()
        Arc3_dict["begin"] = self.begin
        Arc3_dict["end"] = self.end
        Arc3_dict["is_trigo_direction"] = self.is_trigo_direction
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Arc3_dict["__class__"] = "Arc3"
        return Arc3_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.begin = None
        self.end = None
        self.is_trigo_direction = None
        # Set to None the properties inherited from Arc
        super(Arc3, self)._set_None()

    def _get_begin(self):
        """getter of begin"""
        return self._begin

    def _set_begin(self, value):
        """setter of begin"""
        check_var("begin", value, "complex")
        self._begin = value

    # begin point of the arc
    # Type : complex
    begin = property(fget=_get_begin, fset=_set_begin,
                     doc=u"""begin point of the arc""")

    def _get_end(self):
        """getter of end"""
        return self._end

    def _set_end(self, value):
        """setter of end"""
        check_var("end", value, "complex")
        self._end = value

    # end of the arc
    # Type : complex
    end = property(fget=_get_end, fset=_set_end,
                   doc=u"""end of the arc""")

    def _get_is_trigo_direction(self):
        """getter of is_trigo_direction"""
        return self._is_trigo_direction

    def _set_is_trigo_direction(self, value):
        """setter of is_trigo_direction"""
        check_var("is_trigo_direction", value, "bool")
        self._is_trigo_direction = value

    # Rotation direction of the arc
    # Type : bool
    is_trigo_direction = property(fget=_get_is_trigo_direction, fset=_set_is_trigo_direction,
                                  doc=u"""Rotation direction of the arc""")
