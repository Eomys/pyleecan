# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MachineUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MachineUD
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
from .Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.MachineUD.is_synchronous import is_synchronous
except ImportError as error:
    is_synchronous = error


from ._check import InitUnKnowClassError
from .Lamination import Lamination
from .Frame import Frame
from .Shaft import Shaft


class MachineUD(Machine):
    """User defined Machine with multiple Laminations"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.MachineUD.is_synchronous
    if isinstance(is_synchronous, ImportError):
        is_synchronous = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineUD method is_synchronous: " + str(is_synchronous)
                )
            )
        )
    else:
        is_synchronous = is_synchronous
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        lam_list=-1,
        is_sync=True,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
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
            if "lam_list" in list(init_dict.keys()):
                lam_list = init_dict["lam_list"]
            if "is_sync" in list(init_dict.keys()):
                is_sync = init_dict["is_sync"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.lam_list = lam_list
        self.is_sync = is_sync
        # Call Machine init
        super(MachineUD, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in Machine init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MachineUD_str = ""
        # Get the properties inherited from Machine
        MachineUD_str += super(MachineUD, self).__str__()
        if len(self.lam_list) == 0:
            MachineUD_str += "lam_list = []" + linesep
        for ii in range(len(self.lam_list)):
            tmp = self.lam_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MachineUD_str += "lam_list[" + str(ii) + "] =" + tmp + linesep + linesep
        MachineUD_str += "is_sync = " + str(self.is_sync) + linesep
        return MachineUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Machine
        if not super(MachineUD, self).__eq__(other):
            return False
        if other.lam_list != self.lam_list:
            return False
        if other.is_sync != self.is_sync:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Machine
        diff_list.extend(super(MachineUD, self).compare(other, name=name))
        if (other.lam_list is None and self.lam_list is not None) or (
            other.lam_list is not None and self.lam_list is None
        ):
            diff_list.append(name + ".lam_list None mismatch")
        elif self.lam_list is None:
            pass
        elif len(other.lam_list) != len(self.lam_list):
            diff_list.append("len(" + name + ".lam_list)")
        else:
            for ii in range(len(other.lam_list)):
                diff_list.extend(
                    self.lam_list[ii].compare(
                        other.lam_list[ii], name=name + ".lam_list[" + str(ii) + "]"
                    )
                )
        if other._is_sync != self._is_sync:
            diff_list.append(name + ".is_sync")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Machine
        S += super(MachineUD, self).__sizeof__()
        if self.lam_list is not None:
            for value in self.lam_list:
                S += getsizeof(value)
        S += getsizeof(self.is_sync)
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

        # Get the properties inherited from Machine
        MachineUD_dict = super(MachineUD, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.lam_list is None:
            MachineUD_dict["lam_list"] = None
        else:
            MachineUD_dict["lam_list"] = list()
            for obj in self.lam_list:
                if obj is not None:
                    MachineUD_dict["lam_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    MachineUD_dict["lam_list"].append(None)
        MachineUD_dict["is_sync"] = self.is_sync
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MachineUD_dict["__class__"] = "MachineUD"
        return MachineUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.lam_list = None
        self.is_sync = None
        # Set to None the properties inherited from Machine
        super(MachineUD, self)._set_None()

    def _get_lam_list(self):
        """getter of lam_list"""
        if self._lam_list is not None:
            for obj in self._lam_list:
                if obj is not None:
                    obj.parent = self
        return self._lam_list

    def _set_lam_list(self, value):
        """setter of lam_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "lam_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("lam_list", value, "[Lamination]")
        self._lam_list = value

    lam_list = property(
        fget=_get_lam_list,
        fset=_set_lam_list,
        doc=u"""List of Lamination

        :Type: [Lamination]
        """,
    )

    def _get_is_sync(self):
        """getter of is_sync"""
        return self._is_sync

    def _set_is_sync(self, value):
        """setter of is_sync"""
        check_var("is_sync", value, "bool")
        self._is_sync = value

    is_sync = property(
        fget=_get_is_sync,
        fset=_set_is_sync,
        doc=u"""True if the machine should be handled as a Synchronous machine

        :Type: bool
        """,
    )
