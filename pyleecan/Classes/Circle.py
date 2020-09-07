# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Circle.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Circle
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Surface import Surface

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Geometry.Circle.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.Circle.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.Circle.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Geometry.Circle.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.Circle.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from ..Methods.Geometry.Circle.get_patches import get_patches
except ImportError as error:
    get_patches = error

try:
    from ..Methods.Geometry.Circle.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.Circle.translate import translate
except ImportError as error:
    translate = error

try:
    from ..Methods.Geometry.Circle.comp_point_ref import comp_point_ref
except ImportError as error:
    comp_point_ref = error


from ._check import InitUnKnowClassError


class Circle(Surface):
    """Circle define by  the center of circle(point_ref), the label and the radius"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Circle.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Circle.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Circle.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Circle method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.Circle.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Circle.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.Circle.get_patches
    if isinstance(get_patches, ImportError):
        get_patches = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method get_patches: " + str(get_patches))
            )
        )
    else:
        get_patches = get_patches
    # cf Methods.Geometry.Circle.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Circle.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Circle method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.Circle.comp_point_ref
    if isinstance(comp_point_ref, ImportError):
        comp_point_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Circle method comp_point_ref: " + str(comp_point_ref)
                )
            )
        )
    else:
        comp_point_ref = comp_point_ref
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        radius=1,
        center=0,
        line_label="",
        point_ref=0,
        label="",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            radius = obj.radius
            center = obj.center
            line_label = obj.line_label
            point_ref = obj.point_ref
            label = obj.label
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "radius" in list(init_dict.keys()):
                radius = init_dict["radius"]
            if "center" in list(init_dict.keys()):
                center = init_dict["center"]
            if "line_label" in list(init_dict.keys()):
                line_label = init_dict["line_label"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        self.radius = radius
        self.center = center
        self.line_label = line_label
        # Call Surface init
        super(Circle, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Circle_str = ""
        # Get the properties inherited from Surface
        Circle_str += super(Circle, self).__str__()
        Circle_str += "radius = " + str(self.radius) + linesep
        Circle_str += "center = " + str(self.center) + linesep
        Circle_str += 'line_label = "' + str(self.line_label) + '"' + linesep
        return Circle_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(Circle, self).__eq__(other):
            return False
        if other.radius != self.radius:
            return False
        if other.center != self.center:
            return False
        if other.line_label != self.line_label:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Surface
        Circle_dict = super(Circle, self).as_dict()
        Circle_dict["radius"] = self.radius
        if self.center is None:
            Circle_dict["center"] = None
        else:
            Circle_dict["center"] = str(self.center)
        Circle_dict["line_label"] = self.line_label
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Circle_dict["__class__"] = "Circle"
        return Circle_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.radius = None
        self.center = None
        self.line_label = None
        # Set to None the properties inherited from Surface
        super(Circle, self)._set_None()

    def _get_radius(self):
        """getter of radius"""
        return self._radius

    def _set_radius(self, value):
        """setter of radius"""
        check_var("radius", value, "float", Vmin=0)
        self._radius = value

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        doc=u"""Radius of the circle

        :Type: float
        :min: 0
        """,
    )

    def _get_center(self):
        """getter of center"""
        return self._center

    def _set_center(self, value):
        """setter of center"""
        if isinstance(value, str):
            value = complex(value)
        check_var("center", value, "complex")
        self._center = value

    center = property(
        fget=_get_center,
        fset=_set_center,
        doc=u"""center of the Circle

        :Type: complex
        """,
    )

    def _get_line_label(self):
        """getter of line_label"""
        return self._line_label

    def _set_line_label(self, value):
        """setter of line_label"""
        check_var("line_label", value, "str")
        self._line_label = value

    line_label = property(
        fget=_get_line_label,
        fset=_set_line_label,
        doc=u"""Label to set to the lines

        :Type: str
        """,
    )
