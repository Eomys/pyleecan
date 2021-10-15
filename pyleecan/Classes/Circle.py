# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Circle.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Circle
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
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
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        radius=1,
        center=0,
        prop_dict=-1,
        point_ref=0,
        label="",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "radius" in list(init_dict.keys()):
                radius = init_dict["radius"]
            if "center" in list(init_dict.keys()):
                center = init_dict["center"]
            if "prop_dict" in list(init_dict.keys()):
                prop_dict = init_dict["prop_dict"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Set the properties (value check and convertion are done in setter)
        self.radius = radius
        self.center = center
        self.prop_dict = prop_dict
        # Call Surface init
        super(Circle, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Circle_str = ""
        # Get the properties inherited from Surface
        Circle_str += super(Circle, self).__str__()
        Circle_str += "radius = " + str(self.radius) + linesep
        Circle_str += "center = " + str(self.center) + linesep
        Circle_str += "prop_dict = " + str(self.prop_dict) + linesep
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
        if other.prop_dict != self.prop_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Surface
        diff_list.extend(super(Circle, self).compare(other, name=name))
        if other._radius != self._radius:
            diff_list.append(name + ".radius")
        if other._center != self._center:
            diff_list.append(name + ".center")
        if other._prop_dict != self._prop_dict:
            diff_list.append(name + ".prop_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Surface
        S += super(Circle, self).__sizeof__()
        S += getsizeof(self.radius)
        S += getsizeof(self.center)
        if self.prop_dict is not None:
            for key, value in self.prop_dict.items():
                S += getsizeof(value) + getsizeof(key)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Surface
        Circle_dict = super(Circle, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Circle_dict["radius"] = self.radius
        if self.center is None:
            Circle_dict["center"] = None
        elif isinstance(self.center, float):
            Circle_dict["center"] = self.center
        else:
            Circle_dict["center"] = str(self.center)
        Circle_dict["prop_dict"] = (
            self.prop_dict.copy() if self.prop_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Circle_dict["__class__"] = "Circle"
        return Circle_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.radius = None
        self.center = None
        self.prop_dict = None
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

    def _get_prop_dict(self):
        """getter of prop_dict"""
        return self._prop_dict

    def _set_prop_dict(self, value):
        """setter of prop_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("prop_dict", value, "dict")
        self._prop_dict = value

    prop_dict = property(
        fget=_get_prop_dict,
        fset=_set_prop_dict,
        doc=u"""Property dict to apply on the lines

        :Type: dict
        """,
    )
