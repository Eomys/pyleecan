# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputVoltage.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputVoltage
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
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputVoltage.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputVoltage.set_OP_from_array import set_OP_from_array
except ImportError as error:
    set_OP_from_array = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Import import Import
from .ImportGenPWM import ImportGenPWM
from .ImportMatrix import ImportMatrix
from .OP import OP


class InputVoltage(Input):
    """Input to start the electrical module with voltage input"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputVoltage.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputVoltage.set_OP_from_array
    if isinstance(set_OP_from_array, ImportError):
        set_OP_from_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method set_OP_from_array: "
                    + str(set_OP_from_array)
                )
            )
        )
    else:
        set_OP_from_array = set_OP_from_array
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        angle_rotor=None,
        rot_dir=-1,
        angle_rotor_initial=0,
        PWM=None,
        current_dir=-1,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=None,
        Na_tot=2048,
        OP=None,
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
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "PWM" in list(init_dict.keys()):
                PWM = init_dict["PWM"]
            if "current_dir" in list(init_dict.keys()):
                current_dir = init_dict["current_dir"]
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
        # Set the properties (value check and convertion are done in setter)
        self.angle_rotor = angle_rotor
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.PWM = PWM
        self.current_dir = current_dir
        # Call Input init
        super(InputVoltage, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot, OP=OP
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputVoltage_str = ""
        # Get the properties inherited from Input
        InputVoltage_str += super(InputVoltage, self).__str__()
        if self.angle_rotor is not None:
            tmp = (
                self.angle_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            InputVoltage_str += "angle_rotor = " + tmp
        else:
            InputVoltage_str += "angle_rotor = None" + linesep + linesep
        InputVoltage_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputVoltage_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        if self.PWM is not None:
            tmp = self.PWM.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputVoltage_str += "PWM = " + tmp
        else:
            InputVoltage_str += "PWM = None" + linesep + linesep
        InputVoltage_str += "current_dir = " + str(self.current_dir) + linesep
        return InputVoltage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputVoltage, self).__eq__(other):
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.PWM != self.PWM:
            return False
        if other.current_dir != self.current_dir:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Input
        diff_list.extend(super(InputVoltage, self).compare(other, name=name))
        if (other.angle_rotor is None and self.angle_rotor is not None) or (
            other.angle_rotor is not None and self.angle_rotor is None
        ):
            diff_list.append(name + ".angle_rotor None mismatch")
        elif self.angle_rotor is not None:
            diff_list.extend(
                self.angle_rotor.compare(other.angle_rotor, name=name + ".angle_rotor")
            )
        if other._rot_dir != self._rot_dir:
            diff_list.append(name + ".rot_dir")
        if other._angle_rotor_initial != self._angle_rotor_initial:
            diff_list.append(name + ".angle_rotor_initial")
        if (other.PWM is None and self.PWM is not None) or (
            other.PWM is not None and self.PWM is None
        ):
            diff_list.append(name + ".PWM None mismatch")
        elif self.PWM is not None:
            diff_list.extend(self.PWM.compare(other.PWM, name=name + ".PWM"))
        if other._current_dir != self._current_dir:
            diff_list.append(name + ".current_dir")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputVoltage, self).__sizeof__()
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.PWM)
        S += getsizeof(self.current_dir)
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

        # Get the properties inherited from Input
        InputVoltage_dict = super(InputVoltage, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.angle_rotor is None:
            InputVoltage_dict["angle_rotor"] = None
        else:
            InputVoltage_dict["angle_rotor"] = self.angle_rotor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        InputVoltage_dict["rot_dir"] = self.rot_dir
        InputVoltage_dict["angle_rotor_initial"] = self.angle_rotor_initial
        if self.PWM is None:
            InputVoltage_dict["PWM"] = None
        else:
            InputVoltage_dict["PWM"] = self.PWM.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        InputVoltage_dict["current_dir"] = self.current_dir
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputVoltage_dict["__class__"] = "InputVoltage"
        return InputVoltage_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        self.rot_dir = None
        self.angle_rotor_initial = None
        if self.PWM is not None:
            self.PWM._set_None()
        self.current_dir = None
        # Set to None the properties inherited from Input
        super(InputVoltage, self)._set_None()

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "angle_rotor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Import()
        check_var("angle_rotor", value, "Import")
        self._angle_rotor = value

        if self._angle_rotor is not None:
            self._angle_rotor.parent = self

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr) to import

        :Type: Import
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "int", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise

        :Type: int
        :min: -1
        :max: 1
        """,
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0

        :Type: float
        """,
    )

    def _get_PWM(self):
        """getter of PWM"""
        return self._PWM

    def _set_PWM(self, value):
        """setter of PWM"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "PWM")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = ImportGenPWM()
        check_var("PWM", value, "ImportGenPWM")
        self._PWM = value

        if self._PWM is not None:
            self._PWM.parent = self

    PWM = property(
        fget=_get_PWM,
        fset=_set_PWM,
        doc=u"""Object to generate PWM signal

        :Type: ImportGenPWM
        """,
    )

    def _get_current_dir(self):
        """getter of current_dir"""
        return self._current_dir

    def _set_current_dir(self, value):
        """setter of current_dir"""
        check_var("current_dir", value, "int", Vmin=-1, Vmax=1)
        self._current_dir = value

    current_dir = property(
        fget=_get_current_dir,
        fset=_set_current_dir,
        doc=u"""Rotation direction of the stator currents 1 trigo, -1 clockwise

        :Type: int
        :min: -1
        :max: 1
        """,
    )
