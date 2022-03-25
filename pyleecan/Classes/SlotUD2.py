# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotUD2.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotUD2
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
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotUD2.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotUD2.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error

try:
    from ..Methods.Slot.SlotUD2.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotUD2.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotUD2._set_split_active_surf_dict import (
        _set_split_active_surf_dict,
    )
except ImportError as error:
    _set_split_active_surf_dict = error


from ._check import InitUnKnowClassError


class SlotUD2(Slot):
    """"User defined" Slot from a line list and a surface"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotUD2.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD2 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotUD2.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD2 method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # cf Methods.Slot.SlotUD2.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD2 method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotUD2.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotUD2 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotUD2._set_split_active_surf_dict
    if isinstance(_set_split_active_surf_dict, ImportError):
        _set_split_active_surf_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotUD2 method _set_split_active_surf_dict: "
                    + str(_set_split_active_surf_dict)
                )
            )
        )
    else:
        _set_split_active_surf_dict = _set_split_active_surf_dict
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        line_list=-1,
        active_surf=-1,
        split_active_surf_dict=None,
        name="",
        Zs=36,
        wedge_mat=None,
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
            if "active_surf" in list(init_dict.keys()):
                active_surf = init_dict["active_surf"]
            if "split_active_surf_dict" in list(init_dict.keys()):
                split_active_surf_dict = init_dict["split_active_surf_dict"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.line_list = line_list
        self.active_surf = active_surf
        self.split_active_surf_dict = split_active_surf_dict
        self.name = name
        # Call Slot init
        super(SlotUD2, self).__init__(Zs=Zs, wedge_mat=wedge_mat)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotUD2_str = ""
        # Get the properties inherited from Slot
        SlotUD2_str += super(SlotUD2, self).__str__()
        if len(self.line_list) == 0:
            SlotUD2_str += "line_list = []" + linesep
        for ii in range(len(self.line_list)):
            tmp = (
                self.line_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            SlotUD2_str += "line_list[" + str(ii) + "] =" + tmp + linesep + linesep
        if self.active_surf is not None:
            tmp = (
                self.active_surf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            SlotUD2_str += "active_surf = " + tmp
        else:
            SlotUD2_str += "active_surf = None" + linesep + linesep
        SlotUD2_str += (
            "split_active_surf_dict = " + str(self.split_active_surf_dict) + linesep
        )
        SlotUD2_str += 'name = "' + str(self.name) + '"' + linesep
        return SlotUD2_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotUD2, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
            return False
        if other.active_surf != self.active_surf:
            return False
        if other.split_active_surf_dict != self.split_active_surf_dict:
            return False
        if other.name != self.name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(super(SlotUD2, self).compare(other, name=name))
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
        if (other.active_surf is None and self.active_surf is not None) or (
            other.active_surf is not None and self.active_surf is None
        ):
            diff_list.append(name + ".active_surf None mismatch")
        elif self.active_surf is not None:
            diff_list.extend(
                self.active_surf.compare(other.active_surf, name=name + ".active_surf")
            )
        if other._split_active_surf_dict != self._split_active_surf_dict:
            diff_list.append(name + ".split_active_surf_dict")
        if other._name != self._name:
            diff_list.append(name + ".name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotUD2, self).__sizeof__()
        if self.line_list is not None:
            for value in self.line_list:
                S += getsizeof(value)
        S += getsizeof(self.active_surf)
        if self.split_active_surf_dict is not None:
            for key, value in self.split_active_surf_dict.items():
                S += getsizeof(value) + getsizeof(key)
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
        SlotUD2_dict = super(SlotUD2, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.line_list is None:
            SlotUD2_dict["line_list"] = None
        else:
            SlotUD2_dict["line_list"] = list()
            for obj in self.line_list:
                if obj is not None:
                    SlotUD2_dict["line_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    SlotUD2_dict["line_list"].append(None)
        if self.active_surf is None:
            SlotUD2_dict["active_surf"] = None
        else:
            SlotUD2_dict["active_surf"] = self.active_surf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        SlotUD2_dict["split_active_surf_dict"] = (
            self.split_active_surf_dict.copy()
            if self.split_active_surf_dict is not None
            else None
        )
        SlotUD2_dict["name"] = self.name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotUD2_dict["__class__"] = "SlotUD2"
        return SlotUD2_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.line_list = None
        if self.active_surf is not None:
            self.active_surf._set_None()
        self.split_active_surf_dict = None
        self.name = None
        # Set to None the properties inherited from Slot
        super(SlotUD2, self)._set_None()

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

    def _get_active_surf(self):
        """getter of active_surf"""
        return self._active_surf

    def _set_active_surf(self, value):
        """setter of active_surf"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "active_surf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Surface = import_class("pyleecan.Classes", "Surface", "active_surf")
            value = Surface()
        check_var("active_surf", value, "Surface")
        self._active_surf = value

        if self._active_surf is not None:
            self._active_surf.parent = self

    active_surf = property(
        fget=_get_active_surf,
        fset=_set_active_surf,
        doc=u"""Active surface of the Slot

        :Type: Surface
        """,
    )

    def _get_split_active_surf_dict(self):
        """getter of split_active_surf_dict"""
        return self._split_active_surf_dict

    split_active_surf_dict = property(
        fget=_get_split_active_surf_dict,
        fset=_set_split_active_surf_dict,
        doc=u"""Dictionary to enforced the split active surface (key="Nrad=1, Ntan=2"). Labels set according to list order (loop on Nrad then Ntan)

        :Type: dict
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
