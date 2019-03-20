# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Arc import Arc

from pyleecan.Methods.Geometry.Arc2.check import check
from pyleecan.Methods.Geometry.Arc2.comp_length import comp_length
from pyleecan.Methods.Geometry.Arc2.comp_radius import comp_radius
from pyleecan.Methods.Geometry.Arc2.discretize import discretize
from pyleecan.Methods.Geometry.Arc2.get_begin import get_begin
from pyleecan.Methods.Geometry.Arc2.get_center import get_center
from pyleecan.Methods.Geometry.Arc2.get_end import get_end
from pyleecan.Methods.Geometry.Arc2.get_middle import get_middle
from pyleecan.Methods.Geometry.Arc2.rotate import rotate
from pyleecan.Methods.Geometry.Arc2.translate import translate
from pyleecan.Methods.Geometry.Arc2.get_angle import get_angle

from pyleecan.Classes.check import InitUnKnowClassError


class Arc2(Arc):
    """An arc between two points (defined by the begin  point and a center and angle)"""

    VERSION = 1

    # cf Methods.Geometry.Arc2.check
    check = check
    # cf Methods.Geometry.Arc2.comp_length
    comp_length = comp_length
    # cf Methods.Geometry.Arc2.comp_radius
    comp_radius = comp_radius
    # cf Methods.Geometry.Arc2.discretize
    discretize = discretize
    # cf Methods.Geometry.Arc2.get_begin
    get_begin = get_begin
    # cf Methods.Geometry.Arc2.get_center
    get_center = get_center
    # cf Methods.Geometry.Arc2.get_end
    get_end = get_end
    # cf Methods.Geometry.Arc2.get_middle
    get_middle = get_middle
    # cf Methods.Geometry.Arc2.rotate
    rotate = rotate
    # cf Methods.Geometry.Arc2.translate
    translate = translate
    # cf Methods.Geometry.Arc2.get_angle
    get_angle = get_angle
    # save method is available in all object
    save = save

    def __init__(self, begin=0, center=0, angle=1.57079633, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["begin", "center", "angle", "label"])
            # Overwrite default value with init_dict content
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "center" in list(init_dict.keys()):
                center = init_dict["center"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.begin = begin
        self.center = center
        self.angle = angle
        # Call Arc init
        super(Arc2, self).__init__(label=label)
        # The class is frozen (in Arc init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Arc2_str = ""
        # Get the properties inherited from Arc
        Arc2_str += super(Arc2, self).__str__() + linesep
        Arc2_str += "begin = " + str(self.begin) + linesep
        Arc2_str += "center = " + str(self.center) + linesep
        Arc2_str += "angle = " + str(self.angle)
        return Arc2_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Arc
        if not super(Arc2, self).__eq__(other):
            return False
        if other.begin != self.begin:
            return False
        if other.center != self.center:
            return False
        if other.angle != self.angle:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Arc
        Arc2_dict = super(Arc2, self).as_dict()
        Arc2_dict["begin"] = self.begin
        Arc2_dict["center"] = self.center
        Arc2_dict["angle"] = self.angle
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Arc2_dict["__class__"] = "Arc2"
        return Arc2_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.begin = None
        self.center = None
        self.angle = None
        # Set to None the properties inherited from Arc
        super(Arc2, self)._set_None()

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

    def _get_center(self):
        """getter of center"""
        return self._center

    def _set_center(self, value):
        """setter of center"""
        check_var("center", value, "complex")
        self._center = value

    # center of the arc
    # Type : complex
    center = property(fget=_get_center, fset=_set_center, doc=u"""center of the arc""")

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        check_var("angle", value, "float", Vmin=-6.2831853071796, Vmax=6.2831853071796)
        self._angle = value

    # opening angle of the arc
    # Type : float, min = -6.2831853071796, max = 6.2831853071796
    angle = property(
        fget=_get_angle, fset=_set_angle, doc=u"""opening angle of the arc"""
    )
