# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Segment.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Segment
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
from .Line import Line

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Geometry.Segment.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.Segment.comp_distance import comp_distance
except ImportError as error:
    comp_distance = error

try:
    from ..Methods.Geometry.Segment.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.Segment.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.Segment.draw_FEMM import draw_FEMM
except ImportError as error:
    draw_FEMM = error

try:
    from ..Methods.Geometry.Segment.get_begin import get_begin
except ImportError as error:
    get_begin = error

try:
    from ..Methods.Geometry.Segment.get_end import get_end
except ImportError as error:
    get_end = error

try:
    from ..Methods.Geometry.Segment.get_middle import get_middle
except ImportError as error:
    get_middle = error

try:
    from ..Methods.Geometry.Segment.intersect_line import intersect_line
except ImportError as error:
    intersect_line = error

try:
    from ..Methods.Geometry.Segment.is_on_line import is_on_line
except ImportError as error:
    is_on_line = error

try:
    from ..Methods.Geometry.Segment.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Geometry.Segment.reverse import reverse
except ImportError as error:
    reverse = error

try:
    from ..Methods.Geometry.Segment.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.Segment.scale import scale
except ImportError as error:
    scale = error

try:
    from ..Methods.Geometry.Segment.split_half import split_half
except ImportError as error:
    split_half = error

try:
    from ..Methods.Geometry.Segment.split_line import split_line
except ImportError as error:
    split_line = error

try:
    from ..Methods.Geometry.Segment.translate import translate
except ImportError as error:
    translate = error


from ._check import InitUnKnowClassError


class Segment(Line):
    """A segment between two points"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Segment.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Segment.comp_distance
    if isinstance(comp_distance, ImportError):
        comp_distance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Segment method comp_distance: " + str(comp_distance)
                )
            )
        )
    else:
        comp_distance = comp_distance
    # cf Methods.Geometry.Segment.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Segment.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Segment.draw_FEMM
    if isinstance(draw_FEMM, ImportError):
        draw_FEMM = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method draw_FEMM: " + str(draw_FEMM))
            )
        )
    else:
        draw_FEMM = draw_FEMM
    # cf Methods.Geometry.Segment.get_begin
    if isinstance(get_begin, ImportError):
        get_begin = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method get_begin: " + str(get_begin))
            )
        )
    else:
        get_begin = get_begin
    # cf Methods.Geometry.Segment.get_end
    if isinstance(get_end, ImportError):
        get_end = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method get_end: " + str(get_end))
            )
        )
    else:
        get_end = get_end
    # cf Methods.Geometry.Segment.get_middle
    if isinstance(get_middle, ImportError):
        get_middle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method get_middle: " + str(get_middle))
            )
        )
    else:
        get_middle = get_middle
    # cf Methods.Geometry.Segment.intersect_line
    if isinstance(intersect_line, ImportError):
        intersect_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Segment method intersect_line: " + str(intersect_line)
                )
            )
        )
    else:
        intersect_line = intersect_line
    # cf Methods.Geometry.Segment.is_on_line
    if isinstance(is_on_line, ImportError):
        is_on_line = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method is_on_line: " + str(is_on_line))
            )
        )
    else:
        is_on_line = is_on_line
    # cf Methods.Geometry.Segment.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Geometry.Segment.reverse
    if isinstance(reverse, ImportError):
        reverse = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method reverse: " + str(reverse))
            )
        )
    else:
        reverse = reverse
    # cf Methods.Geometry.Segment.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Segment.scale
    if isinstance(scale, ImportError):
        scale = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method scale: " + str(scale))
            )
        )
    else:
        scale = scale
    # cf Methods.Geometry.Segment.split_half
    if isinstance(split_half, ImportError):
        split_half = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method split_half: " + str(split_half))
            )
        )
    else:
        split_half = split_half
    # cf Methods.Geometry.Segment.split_line
    if isinstance(split_line, ImportError):
        split_line = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method split_line: " + str(split_line))
            )
        )
    else:
        split_line = split_line
    # cf Methods.Geometry.Segment.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Segment method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, begin=0, end=0, prop_dict=None, init_dict=None, init_str=None):
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
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "end" in list(init_dict.keys()):
                end = init_dict["end"]
            if "prop_dict" in list(init_dict.keys()):
                prop_dict = init_dict["prop_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.begin = begin
        self.end = end
        # Call Line init
        super(Segment, self).__init__(prop_dict=prop_dict)
        # The class is frozen (in Line init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Segment_str = ""
        # Get the properties inherited from Line
        Segment_str += super(Segment, self).__str__()
        Segment_str += "begin = " + str(self.begin) + linesep
        Segment_str += "end = " + str(self.end) + linesep
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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Line
        diff_list.extend(super(Segment, self).compare(other, name=name))
        if other._begin != self._begin:
            diff_list.append(name + ".begin")
        if other._end != self._end:
            diff_list.append(name + ".end")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Line
        S += super(Segment, self).__sizeof__()
        S += getsizeof(self.begin)
        S += getsizeof(self.end)
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

        # Get the properties inherited from Line
        Segment_dict = super(Segment, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.begin is None:
            Segment_dict["begin"] = None
        elif isinstance(self.begin, float):
            Segment_dict["begin"] = self.begin
        else:
            Segment_dict["begin"] = str(self.begin)
        if self.end is None:
            Segment_dict["end"] = None
        elif isinstance(self.end, float):
            Segment_dict["end"] = self.end
        else:
            Segment_dict["end"] = str(self.end)
        # The class name is added to the dict for deserialisation purpose
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
        if isinstance(value, str):
            value = complex(value)
        check_var("begin", value, "complex")
        self._begin = value

    begin = property(
        fget=_get_begin,
        fset=_set_begin,
        doc=u"""begin point of the line

        :Type: complex
        """,
    )

    def _get_end(self):
        """getter of end"""
        return self._end

    def _set_end(self, value):
        """setter of end"""
        if isinstance(value, str):
            value = complex(value)
        check_var("end", value, "complex")
        self._end = value

    end = property(
        fget=_get_end,
        fset=_set_end,
        doc=u"""end point of the line

        :Type: complex
        """,
    )
