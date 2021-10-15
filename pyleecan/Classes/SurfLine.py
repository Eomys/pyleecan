# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/SurfLine.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/SurfLine
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
    from ..Methods.Geometry.SurfLine.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.SurfLine.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.SurfLine.comp_point_ref import comp_point_ref
except ImportError as error:
    comp_point_ref = error

try:
    from ..Methods.Geometry.SurfLine.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Geometry.SurfLine.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.SurfLine.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from ..Methods.Geometry.SurfLine.get_patches import get_patches
except ImportError as error:
    get_patches = error

try:
    from ..Methods.Geometry.SurfLine.plot_lines import plot_lines
except ImportError as error:
    plot_lines = error

try:
    from ..Methods.Geometry.SurfLine.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.SurfLine.scale import scale
except ImportError as error:
    scale = error

try:
    from ..Methods.Geometry.SurfLine.translate import translate
except ImportError as error:
    translate = error


from ._check import InitUnKnowClassError
from .Line import Line


class SurfLine(Surface):
    """SurfLine defined by list of lines that delimit it, label and point reference."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.SurfLine.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.SurfLine.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.SurfLine.comp_point_ref
    if isinstance(comp_point_ref, ImportError):
        comp_point_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method comp_point_ref: " + str(comp_point_ref)
                )
            )
        )
    else:
        comp_point_ref = comp_point_ref
    # cf Methods.Geometry.SurfLine.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.SurfLine.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.SurfLine.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.SurfLine.get_patches
    if isinstance(get_patches, ImportError):
        get_patches = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfLine method get_patches: " + str(get_patches)
                )
            )
        )
    else:
        get_patches = get_patches
    # cf Methods.Geometry.SurfLine.plot_lines
    if isinstance(plot_lines, ImportError):
        plot_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method plot_lines: " + str(plot_lines))
            )
        )
    else:
        plot_lines = plot_lines
    # cf Methods.Geometry.SurfLine.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.SurfLine.scale
    if isinstance(scale, ImportError):
        scale = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method scale: " + str(scale))
            )
        )
    else:
        scale = scale
    # cf Methods.Geometry.SurfLine.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfLine method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, line_list=-1, point_ref=0, label="", init_dict=None, init_str=None
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
            if "line_list" in list(init_dict.keys()):
                line_list = init_dict["line_list"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Set the properties (value check and convertion are done in setter)
        self.line_list = line_list
        # Call Surface init
        super(SurfLine, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SurfLine_str = ""
        # Get the properties inherited from Surface
        SurfLine_str += super(SurfLine, self).__str__()
        if len(self.line_list) == 0:
            SurfLine_str += "line_list = []" + linesep
        for ii in range(len(self.line_list)):
            tmp = (
                self.line_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            SurfLine_str += "line_list[" + str(ii) + "] =" + tmp + linesep + linesep
        return SurfLine_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(SurfLine, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
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
        diff_list.extend(super(SurfLine, self).compare(other, name=name))
        if (other.line_list is None and self.line_list is not None) or (
            other.line_list is not None and self.line_list is None
        ):
            diff_list.append(name + ".line_list None mismatch")
        elif self.line_list is None:
            pass
        elif len(other.line_list) != len(self.line_list):
            diff_list.append("len(" + name + ".line_list)")
        else:
            for ii in range(len(other.line_list)):
                diff_list.extend(
                    self.line_list[ii].compare(
                        other.line_list[ii], name=name + ".line_list[" + str(ii) + "]"
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Surface
        S += super(SurfLine, self).__sizeof__()
        if self.line_list is not None:
            for value in self.line_list:
                S += getsizeof(value)
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
        SurfLine_dict = super(SurfLine, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.line_list is None:
            SurfLine_dict["line_list"] = None
        else:
            SurfLine_dict["line_list"] = list()
            for obj in self.line_list:
                if obj is not None:
                    SurfLine_dict["line_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    SurfLine_dict["line_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SurfLine_dict["__class__"] = "SurfLine"
        return SurfLine_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.line_list = None
        # Set to None the properties inherited from Surface
        super(SurfLine, self)._set_None()

    def _get_line_list(self):
        """getter of line_list"""
        if self._line_list is not None:
            for obj in self._line_list:
                if obj is not None:
                    obj.parent = self
        return self._line_list

    def _set_line_list(self, value):
        """setter of line_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "line_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("line_list", value, "[Line]")
        self._line_list = value

    line_list = property(
        fget=_get_line_list,
        fset=_set_line_list,
        doc=u"""List of Lines 

        :Type: [Line]
        """,
    )
