# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/PolarArc.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/PolarArc
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
    from ..Methods.Geometry.PolarArc.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from ..Methods.Geometry.PolarArc.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.PolarArc.translate import translate
except ImportError as error:
    translate = error

try:
    from ..Methods.Geometry.PolarArc.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.PolarArc.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.PolarArc.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.PolarArc.get_patches import get_patches
except ImportError as error:
    get_patches = error

try:
    from ..Methods.Geometry.PolarArc.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Geometry.PolarArc.comp_point_ref import comp_point_ref
except ImportError as error:
    comp_point_ref = error


from ._check import InitUnKnowClassError


class PolarArc(Surface):
    """PolarArc defined by  the center of object(point_ref), the label, the angle and the height"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.PolarArc.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use PolarArc method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.PolarArc.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use PolarArc method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.PolarArc.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use PolarArc method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.PolarArc.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use PolarArc method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.PolarArc.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PolarArc method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.PolarArc.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use PolarArc method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.PolarArc.get_patches
    if isinstance(get_patches, ImportError):
        get_patches = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PolarArc method get_patches: " + str(get_patches)
                )
            )
        )
    else:
        get_patches = get_patches
    # cf Methods.Geometry.PolarArc.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PolarArc method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.PolarArc.comp_point_ref
    if isinstance(comp_point_ref, ImportError):
        comp_point_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PolarArc method comp_point_ref: " + str(comp_point_ref)
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
        self, angle=1, height=1, point_ref=0, label="", init_dict=None, init_str=None
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
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "height" in list(init_dict.keys()):
                height = init_dict["height"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Set the properties (value check and convertion are done in setter)
        self.angle = angle
        self.height = height
        # Call Surface init
        super(PolarArc, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PolarArc_str = ""
        # Get the properties inherited from Surface
        PolarArc_str += super(PolarArc, self).__str__()
        PolarArc_str += "angle = " + str(self.angle) + linesep
        PolarArc_str += "height = " + str(self.height) + linesep
        return PolarArc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(PolarArc, self).__eq__(other):
            return False
        if other.angle != self.angle:
            return False
        if other.height != self.height:
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
        diff_list.extend(super(PolarArc, self).compare(other, name=name))
        if other._angle != self._angle:
            diff_list.append(name + ".angle")
        if other._height != self._height:
            diff_list.append(name + ".height")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Surface
        S += super(PolarArc, self).__sizeof__()
        S += getsizeof(self.angle)
        S += getsizeof(self.height)
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
        PolarArc_dict = super(PolarArc, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        PolarArc_dict["angle"] = self.angle
        PolarArc_dict["height"] = self.height
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PolarArc_dict["__class__"] = "PolarArc"
        return PolarArc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.angle = None
        self.height = None
        # Set to None the properties inherited from Surface
        super(PolarArc, self)._set_None()

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        check_var("angle", value, "float", Vmin=0)
        self._angle = value

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Polar angle

        :Type: float
        :min: 0
        """,
    )

    def _get_height(self):
        """getter of height"""
        return self._height

    def _set_height(self, value):
        """setter of height"""
        check_var("height", value, "float", Vmin=0)
        self._height = value

    height = property(
        fget=_get_height,
        fset=_set_height,
        doc=u"""The Heigth of the PolarAngle

        :Type: float
        :min: 0
        """,
    )
