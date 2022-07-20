# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotUD
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotUD.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotUD.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotUD.get_surface_opening import get_surface_opening
except ImportError as error:
    get_surface_opening = error

try:
    from ..Methods.Slot.SlotUD.set_from_point_list import set_from_point_list
except ImportError as error:
    set_from_point_list = error


from numpy import isnan
from ._check import InitUnKnowClassError


class SlotUD(Slot):
    """"User defined" Slot from a line list. """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotUD.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotUD method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotUD.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotUD.get_surface_opening
    if isinstance(get_surface_opening, ImportError):
        get_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method get_surface_opening: "
                    + str(get_surface_opening)
                )
            )
        )
    else:
        get_surface_opening = get_surface_opening
    # cf Methods.Slot.SlotUD.set_from_point_list
    if isinstance(set_from_point_list, ImportError):
        set_from_point_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD method set_from_point_list: "
                    + str(set_from_point_list)
                )
            )
        )
    else:
        set_from_point_list = set_from_point_list
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        line_list=-1,
        wind_begin_index=None,
        wind_end_index=None,
        type_line_wind=0,
        name="",
        Zs=36,
        wedge_mat=None,
        is_bore=True,
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
            if "line_list" in list(init_dict.keys()):
                line_list = init_dict["line_list"]
            if "wind_begin_index" in list(init_dict.keys()):
                wind_begin_index = init_dict["wind_begin_index"]
            if "wind_end_index" in list(init_dict.keys()):
                wind_end_index = init_dict["wind_end_index"]
            if "type_line_wind" in list(init_dict.keys()):
                type_line_wind = init_dict["type_line_wind"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.line_list = line_list
        self.wind_begin_index = wind_begin_index
        self.wind_end_index = wind_end_index
        self.type_line_wind = type_line_wind
        self.name = name
        # Call Slot init
        super(SlotUD, self).__init__(Zs=Zs, wedge_mat=wedge_mat, is_bore=is_bore)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotUD_str = ""
        # Get the properties inherited from Slot
        SlotUD_str += super(SlotUD, self).__str__()
        if len(self.line_list) == 0:
            SlotUD_str += "line_list = []" + linesep
        for ii in range(len(self.line_list)):
            tmp = (
                self.line_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            SlotUD_str += "line_list[" + str(ii) + "] =" + tmp + linesep + linesep
        SlotUD_str += "wind_begin_index = " + str(self.wind_begin_index) + linesep
        SlotUD_str += "wind_end_index = " + str(self.wind_end_index) + linesep
        SlotUD_str += "type_line_wind = " + str(self.type_line_wind) + linesep
        SlotUD_str += 'name = "' + str(self.name) + '"' + linesep
        return SlotUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotUD, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
            return False
        if other.wind_begin_index != self.wind_begin_index:
            return False
        if other.wind_end_index != self.wind_end_index:
            return False
        if other.type_line_wind != self.type_line_wind:
            return False
        if other.name != self.name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(
            super(SlotUD, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
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
                        other.line_list[ii],
                        name=name + ".line_list[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if other._wind_begin_index != self._wind_begin_index:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._wind_begin_index)
                    + ", other="
                    + str(other._wind_begin_index)
                    + ")"
                )
                diff_list.append(name + ".wind_begin_index" + val_str)
            else:
                diff_list.append(name + ".wind_begin_index")
        if other._wind_end_index != self._wind_end_index:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._wind_end_index)
                    + ", other="
                    + str(other._wind_end_index)
                    + ")"
                )
                diff_list.append(name + ".wind_end_index" + val_str)
            else:
                diff_list.append(name + ".wind_end_index")
        if other._type_line_wind != self._type_line_wind:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_line_wind)
                    + ", other="
                    + str(other._type_line_wind)
                    + ")"
                )
                diff_list.append(name + ".type_line_wind" + val_str)
            else:
                diff_list.append(name + ".type_line_wind")
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotUD, self).__sizeof__()
        if self.line_list is not None:
            for value in self.line_list:
                S += getsizeof(value)
        S += getsizeof(self.wind_begin_index)
        S += getsizeof(self.wind_end_index)
        S += getsizeof(self.type_line_wind)
        S += getsizeof(self.name)
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

        # Get the properties inherited from Slot
        SlotUD_dict = super(SlotUD, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.line_list is None:
            SlotUD_dict["line_list"] = None
        else:
            SlotUD_dict["line_list"] = list()
            for obj in self.line_list:
                if obj is not None:
                    SlotUD_dict["line_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    SlotUD_dict["line_list"].append(None)
        SlotUD_dict["wind_begin_index"] = self.wind_begin_index
        SlotUD_dict["wind_end_index"] = self.wind_end_index
        SlotUD_dict["type_line_wind"] = self.type_line_wind
        SlotUD_dict["name"] = self.name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotUD_dict["__class__"] = "SlotUD"
        return SlotUD_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.line_list is None:
            line_list_val = None
        else:
            line_list_val = list()
            for obj in self.line_list:
                line_list_val.append(obj.copy())
        wind_begin_index_val = self.wind_begin_index
        wind_end_index_val = self.wind_end_index
        type_line_wind_val = self.type_line_wind
        name_val = self.name
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            line_list=line_list_val,
            wind_begin_index=wind_begin_index_val,
            wind_end_index=wind_end_index_val,
            type_line_wind=type_line_wind_val,
            name=name_val,
            Zs=Zs_val,
            wedge_mat=wedge_mat_val,
            is_bore=is_bore_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.line_list = None
        self.wind_begin_index = None
        self.wind_end_index = None
        self.type_line_wind = None
        self.name = None
        # Set to None the properties inherited from Slot
        super(SlotUD, self)._set_None()

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
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
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
        doc=u"""list of line to draw the edges of the slot

        :Type: [Line]
        """,
    )

    def _get_wind_begin_index(self):
        """getter of wind_begin_index"""
        return self._wind_begin_index

    def _set_wind_begin_index(self, value):
        """setter of wind_begin_index"""
        check_var("wind_begin_index", value, "int")
        self._wind_begin_index = value

    wind_begin_index = property(
        fget=_get_wind_begin_index,
        fset=_set_wind_begin_index,
        doc=u"""Index of the first line to include in the winding

        :Type: int
        """,
    )

    def _get_wind_end_index(self):
        """getter of wind_end_index"""
        return self._wind_end_index

    def _set_wind_end_index(self, value):
        """setter of wind_end_index"""
        check_var("wind_end_index", value, "int")
        self._wind_end_index = value

    wind_end_index = property(
        fget=_get_wind_end_index,
        fset=_set_wind_end_index,
        doc=u"""Index of the last line to include in the winding

        :Type: int
        """,
    )

    def _get_type_line_wind(self):
        """getter of type_line_wind"""
        return self._type_line_wind

    def _set_type_line_wind(self, value):
        """setter of type_line_wind"""
        check_var("type_line_wind", value, "int", Vmin=0, Vmax=1)
        self._type_line_wind = value

    type_line_wind = property(
        fget=_get_type_line_wind,
        fset=_set_type_line_wind,
        doc=u"""0 to close winding with Segment, 1 for Arc1

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the slot (for save)

        :Type: str
        """,
    )
