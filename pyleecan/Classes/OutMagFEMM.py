# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMagFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMagFEMM
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
from .OutInternal import OutInternal

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutMagFEMM.clean import clean
except ImportError as error:
    clean = error


from ._check import InitUnKnowClassError
from ._FEMMHandler import _FEMMHandler


class OutMagFEMM(OutInternal):
    """Class to store outputs related to MagFEMM magnetic model"""

    VERSION = 1

    # cf Methods.Output.OutMagFEMM.clean
    if isinstance(clean, ImportError):
        clean = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMagFEMM method clean: " + str(clean))
            )
        )
    else:
        clean = clean
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, FEMM_dict=None, handler_list=-1, init_dict=None, init_str=None):
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
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "handler_list" in list(init_dict.keys()):
                handler_list = init_dict["handler_list"]
        # Set the properties (value check and convertion are done in setter)
        self.FEMM_dict = FEMM_dict
        self.handler_list = handler_list
        # Call OutInternal init
        super(OutMagFEMM, self).__init__()
        # The class is frozen (in OutInternal init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutMagFEMM_str = ""
        # Get the properties inherited from OutInternal
        OutMagFEMM_str += super(OutMagFEMM, self).__str__()
        OutMagFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        if len(self.handler_list) == 0:
            OutMagFEMM_str += "handler_list = []" + linesep
        for ii in range(len(self.handler_list)):
            tmp = (
                self.handler_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            OutMagFEMM_str += (
                "handler_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return OutMagFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutInternal
        if not super(OutMagFEMM, self).__eq__(other):
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.handler_list != self.handler_list:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OutInternal
        diff_list.extend(super(OutMagFEMM, self).compare(other, name=name))
        if other._FEMM_dict != self._FEMM_dict:
            diff_list.append(name + ".FEMM_dict")
        if (other.handler_list is None and self.handler_list is not None) or (
            other.handler_list is not None and self.handler_list is None
        ):
            diff_list.append(name + ".handler_list None mismatch")
        elif self.handler_list is None:
            pass
        elif len(other.handler_list) != len(self.handler_list):
            diff_list.append("len(" + name + ".handler_list)")
        else:
            for ii in range(len(other.handler_list)):
                diff_list.extend(
                    self.handler_list[ii].compare(
                        other.handler_list[ii],
                        name=name + ".handler_list[" + str(ii) + "]",
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OutInternal
        S += super(OutMagFEMM, self).__sizeof__()
        if self.FEMM_dict is not None:
            for key, value in self.FEMM_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.handler_list is not None:
            for value in self.handler_list:
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

        # Get the properties inherited from OutInternal
        OutMagFEMM_dict = super(OutMagFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OutMagFEMM_dict["FEMM_dict"] = (
            self.FEMM_dict.copy() if self.FEMM_dict is not None else None
        )
        if self.handler_list is None:
            OutMagFEMM_dict["handler_list"] = None
        else:
            OutMagFEMM_dict["handler_list"] = list()
            for obj in self.handler_list:
                if obj is not None:
                    OutMagFEMM_dict["handler_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    OutMagFEMM_dict["handler_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutMagFEMM_dict["__class__"] = "OutMagFEMM"
        return OutMagFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEMM_dict = None
        self.handler_list = None
        # Set to None the properties inherited from OutInternal
        super(OutMagFEMM, self)._set_None()

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    FEMM_dict = property(
        fget=_get_FEMM_dict,
        fset=_set_FEMM_dict,
        doc=u"""dictionary containing the main FEMM parameters

        :Type: dict
        """,
    )

    def _get_handler_list(self):
        """getter of handler_list"""
        if self._handler_list is not None:
            for obj in self._handler_list:
                if obj is not None:
                    obj.parent = self
        return self._handler_list

    def _set_handler_list(self, value):
        """setter of handler_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "handler_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("handler_list", value, "[_FEMMHandler]")
        self._handler_list = value

    handler_list = property(
        fget=_get_handler_list,
        fset=_set_handler_list,
        doc=u"""List of FEMM Handler (more than 1 if nb_worker >1)

        :Type: [_FEMMHandler]
        """,
    )
