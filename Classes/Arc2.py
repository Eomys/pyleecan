# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Geometry/Arc2.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Arc import Arc

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Geometry.Arc2.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Geometry.Arc2.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from pyleecan.Methods.Geometry.Arc2.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from pyleecan.Methods.Geometry.Arc2.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from pyleecan.Methods.Geometry.Arc2.get_angle import get_angle
except ImportError as error:
    get_angle = error

try:
    from pyleecan.Methods.Geometry.Arc2.get_begin import get_begin
except ImportError as error:
    get_begin = error

try:
    from pyleecan.Methods.Geometry.Arc2.get_center import get_center
except ImportError as error:
    get_center = error

try:
    from pyleecan.Methods.Geometry.Arc2.get_end import get_end
except ImportError as error:
    get_end = error

try:
    from pyleecan.Methods.Geometry.Arc2.get_middle import get_middle
except ImportError as error:
    get_middle = error

try:
    from pyleecan.Methods.Geometry.Arc2.reverse import reverse
except ImportError as error:
    reverse = error

try:
    from pyleecan.Methods.Geometry.Arc2.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from pyleecan.Methods.Geometry.Arc2.split_half import split_half
except ImportError as error:
    split_half = error

try:
    from pyleecan.Methods.Geometry.Arc2.translate import translate
except ImportError as error:
    translate = error


from pyleecan.Classes._check import InitUnKnowClassError


class Arc2(Arc):
    """An arc between two points (defined by the begin  point and a center and angle)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Arc2.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Arc2.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Arc2.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Geometry.Arc2.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Arc2.get_angle
    if isinstance(get_angle, ImportError):
        get_angle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method get_angle: " + str(get_angle))
            )
        )
    else:
        get_angle = get_angle
    # cf Methods.Geometry.Arc2.get_begin
    if isinstance(get_begin, ImportError):
        get_begin = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method get_begin: " + str(get_begin))
            )
        )
    else:
        get_begin = get_begin
    # cf Methods.Geometry.Arc2.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method get_center: " + str(get_center))
            )
        )
    else:
        get_center = get_center
    # cf Methods.Geometry.Arc2.get_end
    if isinstance(get_end, ImportError):
        get_end = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method get_end: " + str(get_end))
            )
        )
    else:
        get_end = get_end
    # cf Methods.Geometry.Arc2.get_middle
    if isinstance(get_middle, ImportError):
        get_middle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method get_middle: " + str(get_middle))
            )
        )
    else:
        get_middle = get_middle
    # cf Methods.Geometry.Arc2.reverse
    if isinstance(reverse, ImportError):
        reverse = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method reverse: " + str(reverse))
            )
        )
    else:
        reverse = reverse
    # cf Methods.Geometry.Arc2.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Arc2.split_half
    if isinstance(split_half, ImportError):
        split_half = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method split_half: " + str(split_half))
            )
        )
    else:
        split_half = split_half
    # cf Methods.Geometry.Arc2.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc2 method translate: " + str(translate))
            )
        )
    else:
        translate = translate
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
