# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ELUT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ELUT
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ELUT.get_param_dict import get_param_dict
except ImportError as error:
    get_param_dict = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ELUT(FrozenClass):
    """Abstract class for Electrical Look Up Table (ELUT)"""

    VERSION = 1

    # cf Methods.Simulation.ELUT.get_param_dict
    if isinstance(get_param_dict, ImportError):
        get_param_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ELUT method get_param_dict: " + str(get_param_dict)
                )
            )
        )
    else:
        get_param_dict = get_param_dict
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        R1=None,
        L1=None,
        T1_ref=20,
        OP_matrix=None,
        axes_dict=None,
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
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "T1_ref" in list(init_dict.keys()):
                T1_ref = init_dict["T1_ref"]
            if "OP_matrix" in list(init_dict.keys()):
                OP_matrix = init_dict["OP_matrix"]
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.R1 = R1
        self.L1 = L1
        self.T1_ref = T1_ref
        self.OP_matrix = OP_matrix
        self.axes_dict = axes_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ELUT_str = ""
        if self.parent is None:
            ELUT_str += "parent = None " + linesep
        else:
            ELUT_str += "parent = " + str(type(self.parent)) + " object" + linesep
        ELUT_str += "R1 = " + str(self.R1) + linesep
        ELUT_str += "L1 = " + str(self.L1) + linesep
        ELUT_str += "T1_ref = " + str(self.T1_ref) + linesep
        ELUT_str += (
            "OP_matrix = "
            + linesep
            + str(self.OP_matrix).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ELUT_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        return ELUT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.R1 != self.R1:
            return False
        if other.L1 != self.L1:
            return False
        if other.T1_ref != self.T1_ref:
            return False
        if not array_equal(other.OP_matrix, self.OP_matrix):
            return False
        if other.axes_dict != self.axes_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._R1 != self._R1:
            diff_list.append(name + ".R1")
        if other._L1 != self._L1:
            diff_list.append(name + ".L1")
        if other._T1_ref != self._T1_ref:
            diff_list.append(name + ".T1_ref")
        if not array_equal(other.OP_matrix, self.OP_matrix):
            diff_list.append(name + ".OP_matrix")
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key], name=name + ".axes_dict"
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.R1)
        S += getsizeof(self.L1)
        S += getsizeof(self.T1_ref)
        S += getsizeof(self.OP_matrix)
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
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

        ELUT_dict = dict()
        ELUT_dict["R1"] = self.R1
        ELUT_dict["L1"] = self.L1
        ELUT_dict["T1_ref"] = self.T1_ref
        if self.OP_matrix is None:
            ELUT_dict["OP_matrix"] = None
        else:
            if type_handle_ndarray == 0:
                ELUT_dict["OP_matrix"] = self.OP_matrix.tolist()
            elif type_handle_ndarray == 1:
                ELUT_dict["OP_matrix"] = self.OP_matrix.copy()
            elif type_handle_ndarray == 2:
                ELUT_dict["OP_matrix"] = self.OP_matrix
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.axes_dict is None:
            ELUT_dict["axes_dict"] = None
        else:
            ELUT_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    ELUT_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    ELUT_dict["axes_dict"][key] = None
        # The class name is added to the dict for deserialisation purpose
        ELUT_dict["__class__"] = "ELUT"
        return ELUT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.R1 = None
        self.L1 = None
        self.T1_ref = None
        self.OP_matrix = None
        self.axes_dict = None

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float")
        self._R1 = value

    R1 = property(
        fget=_get_R1,
        fset=_set_R1,
        doc=u"""DC phase winding resistance at T1_ref per phase 

        :Type: float
        """,
    )

    def _get_L1(self):
        """getter of L1"""
        return self._L1

    def _set_L1(self, value):
        """setter of L1"""
        check_var("L1", value, "float")
        self._L1 = value

    L1 = property(
        fget=_get_L1,
        fset=_set_L1,
        doc=u"""Phase winding leakage inductance 

        :Type: float
        """,
    )

    def _get_T1_ref(self):
        """getter of T1_ref"""
        return self._T1_ref

    def _set_T1_ref(self, value):
        """setter of T1_ref"""
        check_var("T1_ref", value, "float")
        self._T1_ref = value

    T1_ref = property(
        fget=_get_T1_ref,
        fset=_set_T1_ref,
        doc=u"""Stator winding average temperature associated to R1, L1 parameters

        :Type: float
        """,
    )

    def _get_OP_matrix(self):
        """getter of OP_matrix"""
        return self._OP_matrix

    def _set_OP_matrix(self, value):
        """setter of OP_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("OP_matrix", value, "ndarray")
        self._OP_matrix = value

    OP_matrix = property(
        fget=_get_OP_matrix,
        fset=_set_OP_matrix,
        doc=u"""Array of operating point values of size (N,5) with N the number of operating points (Speed, Id, Iq, Torque, Power). OP values are set to nan if they are not given.

        :Type: ndarray
        """,
    )

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc=u"""Dict containing axes data used for Magnetics

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )
