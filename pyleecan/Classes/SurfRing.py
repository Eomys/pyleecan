# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/SurfRing.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/SurfRing
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
    from ..Methods.Geometry.SurfRing.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from ..Methods.Geometry.SurfRing.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.SurfRing.translate import translate
except ImportError as error:
    translate = error

try:
    from ..Methods.Geometry.SurfRing.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.SurfRing.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.SurfRing.get_patches import get_patches
except ImportError as error:
    get_patches = error

try:
    from ..Methods.Geometry.SurfRing.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.SurfRing.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Geometry.SurfRing.plot_lines import plot_lines
except ImportError as error:
    plot_lines = error

try:
    from ..Methods.Geometry.SurfRing.comp_point_ref import comp_point_ref
except ImportError as error:
    comp_point_ref = error


from ._check import InitUnKnowClassError
from .Surface import Surface


class SurfRing(Surface):
    """SurfRing is a surface between two closed surfaces (lamination surfaces for instance)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.SurfRing.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.SurfRing.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.SurfRing.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.SurfRing.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.SurfRing.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.SurfRing.get_patches
    if isinstance(get_patches, ImportError):
        get_patches = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method get_patches: " + str(get_patches)
                )
            )
        )
    else:
        get_patches = get_patches
    # cf Methods.Geometry.SurfRing.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.SurfRing.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.SurfRing.plot_lines
    if isinstance(plot_lines, ImportError):
        plot_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method plot_lines: " + str(plot_lines))
            )
        )
    else:
        plot_lines = plot_lines
    # cf Methods.Geometry.SurfRing.comp_point_ref
    if isinstance(comp_point_ref, ImportError):
        comp_point_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method comp_point_ref: " + str(comp_point_ref)
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
        out_surf=-1,
        in_surf=-1,
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
            if "out_surf" in list(init_dict.keys()):
                out_surf = init_dict["out_surf"]
            if "in_surf" in list(init_dict.keys()):
                in_surf = init_dict["in_surf"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Set the properties (value check and convertion are done in setter)
        self.out_surf = out_surf
        self.in_surf = in_surf
        # Call Surface init
        super(SurfRing, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SurfRing_str = ""
        # Get the properties inherited from Surface
        SurfRing_str += super(SurfRing, self).__str__()
        if self.out_surf is not None:
            tmp = self.out_surf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            SurfRing_str += "out_surf = " + tmp
        else:
            SurfRing_str += "out_surf = None" + linesep + linesep
        if self.in_surf is not None:
            tmp = self.in_surf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            SurfRing_str += "in_surf = " + tmp
        else:
            SurfRing_str += "in_surf = None" + linesep + linesep
        return SurfRing_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(SurfRing, self).__eq__(other):
            return False
        if other.out_surf != self.out_surf:
            return False
        if other.in_surf != self.in_surf:
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
        diff_list.extend(super(SurfRing, self).compare(other, name=name))
        if (other.out_surf is None and self.out_surf is not None) or (
            other.out_surf is not None and self.out_surf is None
        ):
            diff_list.append(name + ".out_surf None mismatch")
        elif self.out_surf is not None:
            diff_list.extend(
                self.out_surf.compare(other.out_surf, name=name + ".out_surf")
            )
        if (other.in_surf is None and self.in_surf is not None) or (
            other.in_surf is not None and self.in_surf is None
        ):
            diff_list.append(name + ".in_surf None mismatch")
        elif self.in_surf is not None:
            diff_list.extend(
                self.in_surf.compare(other.in_surf, name=name + ".in_surf")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Surface
        S += super(SurfRing, self).__sizeof__()
        S += getsizeof(self.out_surf)
        S += getsizeof(self.in_surf)
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
        SurfRing_dict = super(SurfRing, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.out_surf is None:
            SurfRing_dict["out_surf"] = None
        else:
            SurfRing_dict["out_surf"] = self.out_surf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.in_surf is None:
            SurfRing_dict["in_surf"] = None
        else:
            SurfRing_dict["in_surf"] = self.in_surf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SurfRing_dict["__class__"] = "SurfRing"
        return SurfRing_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.out_surf is not None:
            self.out_surf._set_None()
        if self.in_surf is not None:
            self.in_surf._set_None()
        # Set to None the properties inherited from Surface
        super(SurfRing, self)._set_None()

    def _get_out_surf(self):
        """getter of out_surf"""
        return self._out_surf

    def _set_out_surf(self, value):
        """setter of out_surf"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "out_surf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Surface()
        check_var("out_surf", value, "Surface")
        self._out_surf = value

        if self._out_surf is not None:
            self._out_surf.parent = self

    out_surf = property(
        fget=_get_out_surf,
        fset=_set_out_surf,
        doc=u"""Outter surface

        :Type: Surface
        """,
    )

    def _get_in_surf(self):
        """getter of in_surf"""
        return self._in_surf

    def _set_in_surf(self, value):
        """setter of in_surf"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "in_surf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Surface()
        check_var("in_surf", value, "Surface")
        self._in_surf = value

        if self._in_surf is not None:
            self._in_surf.parent = self

    in_surf = property(
        fget=_get_in_surf,
        fset=_set_in_surf,
        doc=u"""Inner surface

        :Type: Surface
        """,
    )
