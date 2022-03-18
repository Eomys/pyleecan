# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Input.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Input
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Input.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Simulation.Input.comp_axis_time import comp_axis_time
except ImportError as error:
    comp_axis_time = error

try:
    from ..Methods.Simulation.Input.comp_axis_angle import comp_axis_angle
except ImportError as error:
    comp_axis_angle = error

try:
    from ..Methods.Simulation.Input.comp_axis_phase import comp_axis_phase
except ImportError as error:
    comp_axis_phase = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError


class Input(FrozenClass):
    """Starting data of the simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Input.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use Input method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Simulation.Input.comp_axis_time
    if isinstance(comp_axis_time, ImportError):
        comp_axis_time = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Input method comp_axis_time: " + str(comp_axis_time)
                )
            )
        )
    else:
        comp_axis_time = comp_axis_time
    # cf Methods.Simulation.Input.comp_axis_angle
    if isinstance(comp_axis_angle, ImportError):
        comp_axis_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Input method comp_axis_angle: " + str(comp_axis_angle)
                )
            )
        )
    else:
        comp_axis_angle = comp_axis_angle
    # cf Methods.Simulation.Input.comp_axis_phase
    if isinstance(comp_axis_phase, ImportError):
        comp_axis_phase = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Input method comp_axis_phase: " + str(comp_axis_phase)
                )
            )
        )
    else:
        comp_axis_phase = comp_axis_phase
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=None,
        Na_tot=2048,
        OP=None,
        t_final=None,
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
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "t_final" in list(init_dict.keys()):
                t_final = init_dict["t_final"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.time = time
        self.angle = angle
        self.Nt_tot = Nt_tot
        self.Nrev = Nrev
        self.Na_tot = Na_tot
        self.OP = OP
        self.t_final = t_final

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Input_str = ""
        if self.parent is None:
            Input_str += "parent = None " + linesep
        else:
            Input_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.time is not None:
            tmp = self.time.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "time = " + tmp
        else:
            Input_str += "time = None" + linesep + linesep
        if self.angle is not None:
            tmp = self.angle.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "angle = " + tmp
        else:
            Input_str += "angle = None" + linesep + linesep
        Input_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        Input_str += "Nrev = " + str(self.Nrev) + linesep
        Input_str += "Na_tot = " + str(self.Na_tot) + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "OP = " + tmp
        else:
            Input_str += "OP = None" + linesep + linesep
        Input_str += "t_final = " + str(self.t_final) + linesep
        return Input_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Nrev != self.Nrev:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        if other.OP != self.OP:
            return False
        if other.t_final != self.t_final:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.time is None and self.time is not None) or (
            other.time is not None and self.time is None
        ):
            diff_list.append(name + ".time None mismatch")
        elif self.time is not None:
            diff_list.extend(self.time.compare(other.time, name=name + ".time"))
        if (other.angle is None and self.angle is not None) or (
            other.angle is not None and self.angle is None
        ):
            diff_list.append(name + ".angle None mismatch")
        elif self.angle is not None:
            diff_list.extend(self.angle.compare(other.angle, name=name + ".angle"))
        if other._Nt_tot != self._Nt_tot:
            diff_list.append(name + ".Nt_tot")
        if other._Nrev != self._Nrev:
            diff_list.append(name + ".Nrev")
        if other._Na_tot != self._Na_tot:
            diff_list.append(name + ".Na_tot")
        if (other.OP is None and self.OP is not None) or (
            other.OP is not None and self.OP is None
        ):
            diff_list.append(name + ".OP None mismatch")
        elif self.OP is not None:
            diff_list.extend(self.OP.compare(other.OP, name=name + ".OP"))
        if other._t_final != self._t_final:
            diff_list.append(name + ".t_final")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.time)
        S += getsizeof(self.angle)
        S += getsizeof(self.Nt_tot)
        S += getsizeof(self.Nrev)
        S += getsizeof(self.Na_tot)
        S += getsizeof(self.OP)
        S += getsizeof(self.t_final)
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

        Input_dict = dict()
        if self.time is None:
            Input_dict["time"] = None
        else:
            Input_dict["time"] = self.time.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.angle is None:
            Input_dict["angle"] = None
        else:
            Input_dict["angle"] = self.angle.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Input_dict["Nt_tot"] = self.Nt_tot
        Input_dict["Nrev"] = self.Nrev
        Input_dict["Na_tot"] = self.Na_tot
        if self.OP is None:
            Input_dict["OP"] = None
        else:
            Input_dict["OP"] = self.OP.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Input_dict["t_final"] = self.t_final
        # The class name is added to the dict for deserialisation purpose
        Input_dict["__class__"] = "Input"
        return Input_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        self.Nt_tot = None
        self.Nrev = None
        self.Na_tot = None
        if self.OP is not None:
            self.OP._set_None()
        self.t_final = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "time")
        ImportMatrixVal = import_class("pyleecan.Classes", "ImportMatrixVal", "time")
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "time")
            value = class_obj(init_dict=value)
        check_var("time", value, "ImportMatrix")
        self._time = value

        if self._time is not None:
            self._time.parent = self

    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry) to import

        :Type: ImportMatrix
        """,
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "angle")
        ImportMatrixVal = import_class("pyleecan.Classes", "ImportMatrixVal", "angle")
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "angle"
            )
            value = class_obj(init_dict=value)
        check_var("angle", value, "ImportMatrix")
        self._angle = value

        if self._angle is not None:
            self._angle.parent = self

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int", Vmin=1)
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Time discretization

        :Type: int
        :min: 1
        """,
    )

    def _get_Nrev(self):
        """getter of Nrev"""
        return self._Nrev

    def _set_Nrev(self, value):
        """setter of Nrev"""
        check_var("Nrev", value, "float", Vmin=0)
        self._Nrev = value

    Nrev = property(
        fget=_get_Nrev,
        fset=_set_Nrev,
        doc=u"""Number of rotor revolution (to compute the final time)

        :Type: float
        :min: 0
        """,
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int", Vmin=1)
        self._Na_tot = value

    Na_tot = property(
        fget=_get_Na_tot,
        fset=_set_Na_tot,
        doc=u"""Angular discretization

        :Type: int
        :min: 1
        """,
    )

    def _get_OP(self):
        """getter of OP"""
        return self._OP

    def _set_OP(self, value):
        """setter of OP"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "OP")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OP = import_class("pyleecan.Classes", "OP", "OP")
            value = OP()
        check_var("OP", value, "OP")
        self._OP = value

        if self._OP is not None:
            self._OP.parent = self

    OP = property(
        fget=_get_OP,
        fset=_set_OP,
        doc=u"""Operating Point

        :Type: OP
        """,
    )

    def _get_t_final(self):
        """getter of t_final"""
        return self._t_final

    def _set_t_final(self, value):
        """setter of t_final"""
        check_var("t_final", value, "float")
        self._t_final = value

    t_final = property(
        fget=_get_t_final,
        fset=_set_t_final,
        doc=u"""To enforce final time

        :Type: float
        """,
    )
