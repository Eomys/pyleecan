# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutStruct.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutStruct
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
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError
from .MeshSolution import MeshSolution


class OutStruct(FrozenClass):
    """Gather the structural module outputs"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Time=None,
        Angle=None,
        Nt_tot=None,
        Na_tot=None,
        logger_name="Pyleecan.Structural",
        Yr=None,
        Vr=None,
        Ar=None,
        meshsolution=-1,
        FEA_dict=None,
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
            if "Time" in list(init_dict.keys()):
                Time = init_dict["Time"]
            if "Angle" in list(init_dict.keys()):
                Angle = init_dict["Angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Yr" in list(init_dict.keys()):
                Yr = init_dict["Yr"]
            if "Vr" in list(init_dict.keys()):
                Vr = init_dict["Vr"]
            if "Ar" in list(init_dict.keys()):
                Ar = init_dict["Ar"]
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "FEA_dict" in list(init_dict.keys()):
                FEA_dict = init_dict["FEA_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Time = Time
        self.Angle = Angle
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot
        self.logger_name = logger_name
        self.Yr = Yr
        self.Vr = Vr
        self.Ar = Ar
        self.meshsolution = meshsolution
        self.FEA_dict = FEA_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutStruct_str = ""
        if self.parent is None:
            OutStruct_str += "parent = None " + linesep
        else:
            OutStruct_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutStruct_str += "Time = " + str(self.Time) + linesep + linesep
        OutStruct_str += "Angle = " + str(self.Angle) + linesep + linesep
        OutStruct_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutStruct_str += "Na_tot = " + str(self.Na_tot) + linesep
        OutStruct_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutStruct_str += "Yr = " + str(self.Yr) + linesep + linesep
        OutStruct_str += "Vr = " + str(self.Vr) + linesep + linesep
        OutStruct_str += "Ar = " + str(self.Ar) + linesep + linesep
        if self.meshsolution is not None:
            tmp = (
                self.meshsolution.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OutStruct_str += "meshsolution = " + tmp
        else:
            OutStruct_str += "meshsolution = None" + linesep + linesep
        OutStruct_str += "FEA_dict = " + str(self.FEA_dict) + linesep
        return OutStruct_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Time != self.Time:
            return False
        if other.Angle != self.Angle:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.Yr != self.Yr:
            return False
        if other.Vr != self.Vr:
            return False
        if other.Ar != self.Ar:
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.FEA_dict != self.FEA_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.Time is None and self.Time is not None) or (
            other.Time is not None and self.Time is None
        ):
            diff_list.append(name + ".Time None mismatch")
        elif self.Time is not None:
            diff_list.extend(self.Time.compare(other.Time, name=name + ".Time"))
        if (other.Angle is None and self.Angle is not None) or (
            other.Angle is not None and self.Angle is None
        ):
            diff_list.append(name + ".Angle None mismatch")
        elif self.Angle is not None:
            diff_list.extend(self.Angle.compare(other.Angle, name=name + ".Angle"))
        if other._Nt_tot != self._Nt_tot:
            diff_list.append(name + ".Nt_tot")
        if other._Na_tot != self._Na_tot:
            diff_list.append(name + ".Na_tot")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if (other.Yr is None and self.Yr is not None) or (
            other.Yr is not None and self.Yr is None
        ):
            diff_list.append(name + ".Yr None mismatch")
        elif self.Yr is not None:
            diff_list.extend(self.Yr.compare(other.Yr, name=name + ".Yr"))
        if (other.Vr is None and self.Vr is not None) or (
            other.Vr is not None and self.Vr is None
        ):
            diff_list.append(name + ".Vr None mismatch")
        elif self.Vr is not None:
            diff_list.extend(self.Vr.compare(other.Vr, name=name + ".Vr"))
        if (other.Ar is None and self.Ar is not None) or (
            other.Ar is not None and self.Ar is None
        ):
            diff_list.append(name + ".Ar None mismatch")
        elif self.Ar is not None:
            diff_list.extend(self.Ar.compare(other.Ar, name=name + ".Ar"))
        if (other.meshsolution is None and self.meshsolution is not None) or (
            other.meshsolution is not None and self.meshsolution is None
        ):
            diff_list.append(name + ".meshsolution None mismatch")
        elif self.meshsolution is not None:
            diff_list.extend(
                self.meshsolution.compare(
                    other.meshsolution, name=name + ".meshsolution"
                )
            )
        if other._FEA_dict != self._FEA_dict:
            diff_list.append(name + ".FEA_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Time)
        S += getsizeof(self.Angle)
        S += getsizeof(self.Nt_tot)
        S += getsizeof(self.Na_tot)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.Yr)
        S += getsizeof(self.Vr)
        S += getsizeof(self.Ar)
        S += getsizeof(self.meshsolution)
        if self.FEA_dict is not None:
            for key, value in self.FEA_dict.items():
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

        OutStruct_dict = dict()
        if self.Time is None:
            OutStruct_dict["Time"] = None
        else:
            OutStruct_dict["Time"] = self.Time.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Angle is None:
            OutStruct_dict["Angle"] = None
        else:
            OutStruct_dict["Angle"] = self.Angle.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutStruct_dict["Nt_tot"] = self.Nt_tot
        OutStruct_dict["Na_tot"] = self.Na_tot
        OutStruct_dict["logger_name"] = self.logger_name
        if self.Yr is None:
            OutStruct_dict["Yr"] = None
        else:
            OutStruct_dict["Yr"] = self.Yr.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Vr is None:
            OutStruct_dict["Vr"] = None
        else:
            OutStruct_dict["Vr"] = self.Vr.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Ar is None:
            OutStruct_dict["Ar"] = None
        else:
            OutStruct_dict["Ar"] = self.Ar.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.meshsolution is None:
            OutStruct_dict["meshsolution"] = None
        else:
            OutStruct_dict["meshsolution"] = self.meshsolution.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutStruct_dict["FEA_dict"] = (
            self.FEA_dict.copy() if self.FEA_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        OutStruct_dict["__class__"] = "OutStruct"
        return OutStruct_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Time = None
        self.Angle = None
        self.Nt_tot = None
        self.Na_tot = None
        self.logger_name = None
        self.Yr = None
        self.Vr = None
        self.Ar = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.FEA_dict = None

    def _get_Time(self):
        """getter of Time"""
        return self._Time

    def _set_Time(self, value):
        """setter of Time"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Time"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Data()
        check_var("Time", value, "Data")
        self._Time = value

    Time = property(
        fget=_get_Time,
        fset=_set_Time,
        doc=u"""Structural time Data object

        :Type: SciDataTool.Classes.DataND.Data
        """,
    )

    def _get_Angle(self):
        """getter of Angle"""
        return self._Angle

    def _set_Angle(self, value):
        """setter of Angle"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Angle"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Data()
        check_var("Angle", value, "Data")
        self._Angle = value

    Angle = property(
        fget=_get_Angle,
        fset=_set_Angle,
        doc=u"""Structural position Data object

        :Type: SciDataTool.Classes.DataND.Data
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Length of the time vector

        :Type: int
        """,
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int")
        self._Na_tot = value

    Na_tot = property(
        fget=_get_Na_tot,
        fset=_set_Na_tot,
        doc=u"""Length of the angle vector

        :Type: int
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_Yr(self):
        """getter of Yr"""
        return self._Yr

    def _set_Yr(self, value):
        """setter of Yr"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Yr"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Yr", value, "DataND")
        self._Yr = value

    Yr = property(
        fget=_get_Yr,
        fset=_set_Yr,
        doc=u"""Displacement output

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Vr(self):
        """getter of Vr"""
        return self._Vr

    def _set_Vr(self, value):
        """setter of Vr"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Vr"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Vr", value, "DataND")
        self._Vr = value

    Vr = property(
        fget=_get_Vr,
        fset=_set_Vr,
        doc=u"""Velocity output

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Ar(self):
        """getter of Ar"""
        return self._Ar

    def _set_Ar(self, value):
        """setter of Ar"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Ar"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Ar", value, "DataND")
        self._Ar = value

    Ar = property(
        fget=_get_Ar,
        fset=_set_Ar,
        doc=u"""Acceleration output

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "meshsolution"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MeshSolution()
        check_var("meshsolution", value, "MeshSolution")
        self._meshsolution = value

        if self._meshsolution is not None:
            self._meshsolution.parent = self

    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""FEA software mesh and solution

        :Type: MeshSolution
        """,
    )

    def _get_FEA_dict(self):
        """getter of FEA_dict"""
        return self._FEA_dict

    def _set_FEA_dict(self, value):
        """setter of FEA_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEA_dict", value, "dict")
        self._FEA_dict = value

    FEA_dict = property(
        fget=_get_FEA_dict,
        fset=_set_FEA_dict,
        doc=u"""dictionary containing the main FEA parameter

        :Type: dict
        """,
    )
