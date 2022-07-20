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
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputVoltage.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputVoltage.set_Ud_Uq import set_Ud_Uq
except ImportError as error:
    set_Ud_Uq = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


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
    # cf Methods.Simulation.InputVoltage.set_Ud_Uq
    if isinstance(set_Ud_Uq, ImportError):
        set_Ud_Uq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method set_Ud_Uq: " + str(set_Ud_Uq)
                )
            )
        )
    else:
        set_Ud_Uq = set_Ud_Uq
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        rot_dir=None,
        angle_rotor_initial=0,
        PWM=None,
        phase_dir=None,
        current_dir=None,
        is_periodicity_t=False,
        is_periodicity_a=False,
        is_generator=False,
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
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "PWM" in list(init_dict.keys()):
                PWM = init_dict["PWM"]
            if "phase_dir" in list(init_dict.keys()):
                phase_dir = init_dict["phase_dir"]
            if "current_dir" in list(init_dict.keys()):
                current_dir = init_dict["current_dir"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_generator" in list(init_dict.keys()):
                is_generator = init_dict["is_generator"]
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
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.PWM = PWM
        self.phase_dir = phase_dir
        self.current_dir = current_dir
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a
        self.is_generator = is_generator
        # Call Input init
        super(InputVoltage, self).__init__(
            time=time,
            angle=angle,
            Nt_tot=Nt_tot,
            Nrev=Nrev,
            Na_tot=Na_tot,
            OP=OP,
            t_final=t_final,
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputVoltage_str = ""
        # Get the properties inherited from Input
        InputVoltage_str += super(InputVoltage, self).__str__()
        InputVoltage_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputVoltage_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        if self.PWM is not None:
            tmp = self.PWM.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputVoltage_str += "PWM = " + tmp
        else:
            InputVoltage_str += "PWM = None" + linesep + linesep
        InputVoltage_str += "phase_dir = " + str(self.phase_dir) + linesep
        InputVoltage_str += "current_dir = " + str(self.current_dir) + linesep
        InputVoltage_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        InputVoltage_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        InputVoltage_str += "is_generator = " + str(self.is_generator) + linesep
        return InputVoltage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputVoltage, self).__eq__(other):
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.PWM != self.PWM:
            return False
        if other.phase_dir != self.phase_dir:
            return False
        if other.current_dir != self.current_dir:
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.is_generator != self.is_generator:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Input
        diff_list.extend(
            super(InputVoltage, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._rot_dir != self._rot_dir:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._rot_dir)
                    + ", other="
                    + str(other._rot_dir)
                    + ")"
                )
                diff_list.append(name + ".rot_dir" + val_str)
            else:
                diff_list.append(name + ".rot_dir")
        if (
            other._angle_rotor_initial is not None
            and self._angle_rotor_initial is not None
            and isnan(other._angle_rotor_initial)
            and isnan(self._angle_rotor_initial)
        ):
            pass
        elif other._angle_rotor_initial != self._angle_rotor_initial:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._angle_rotor_initial)
                    + ", other="
                    + str(other._angle_rotor_initial)
                    + ")"
                )
                diff_list.append(name + ".angle_rotor_initial" + val_str)
            else:
                diff_list.append(name + ".angle_rotor_initial")
        if (other.PWM is None and self.PWM is not None) or (
            other.PWM is not None and self.PWM is None
        ):
            diff_list.append(name + ".PWM None mismatch")
        elif self.PWM is not None:
            diff_list.extend(
                self.PWM.compare(
                    other.PWM,
                    name=name + ".PWM",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._phase_dir != self._phase_dir:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._phase_dir)
                    + ", other="
                    + str(other._phase_dir)
                    + ")"
                )
                diff_list.append(name + ".phase_dir" + val_str)
            else:
                diff_list.append(name + ".phase_dir")
        if other._current_dir != self._current_dir:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._current_dir)
                    + ", other="
                    + str(other._current_dir)
                    + ")"
                )
                diff_list.append(name + ".current_dir" + val_str)
            else:
                diff_list.append(name + ".current_dir")
        if other._is_periodicity_t != self._is_periodicity_t:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_periodicity_t)
                    + ", other="
                    + str(other._is_periodicity_t)
                    + ")"
                )
                diff_list.append(name + ".is_periodicity_t" + val_str)
            else:
                diff_list.append(name + ".is_periodicity_t")
        if other._is_periodicity_a != self._is_periodicity_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_periodicity_a)
                    + ", other="
                    + str(other._is_periodicity_a)
                    + ")"
                )
                diff_list.append(name + ".is_periodicity_a" + val_str)
            else:
                diff_list.append(name + ".is_periodicity_a")
        if other._is_generator != self._is_generator:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_generator)
                    + ", other="
                    + str(other._is_generator)
                    + ")"
                )
                diff_list.append(name + ".is_generator" + val_str)
            else:
                diff_list.append(name + ".is_generator")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputVoltage, self).__sizeof__()
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.PWM)
        S += getsizeof(self.phase_dir)
        S += getsizeof(self.current_dir)
        S += getsizeof(self.is_periodicity_t)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.is_generator)
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
        InputVoltage_dict["phase_dir"] = self.phase_dir
        InputVoltage_dict["current_dir"] = self.current_dir
        InputVoltage_dict["is_periodicity_t"] = self.is_periodicity_t
        InputVoltage_dict["is_periodicity_a"] = self.is_periodicity_a
        InputVoltage_dict["is_generator"] = self.is_generator
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputVoltage_dict["__class__"] = "InputVoltage"
        return InputVoltage_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        rot_dir_val = self.rot_dir
        angle_rotor_initial_val = self.angle_rotor_initial
        if self.PWM is None:
            PWM_val = None
        else:
            PWM_val = self.PWM.copy()
        phase_dir_val = self.phase_dir
        current_dir_val = self.current_dir
        is_periodicity_t_val = self.is_periodicity_t
        is_periodicity_a_val = self.is_periodicity_a
        is_generator_val = self.is_generator
        if self.time is None:
            time_val = None
        else:
            time_val = self.time.copy()
        if self.angle is None:
            angle_val = None
        else:
            angle_val = self.angle.copy()
        Nt_tot_val = self.Nt_tot
        Nrev_val = self.Nrev
        Na_tot_val = self.Na_tot
        if self.OP is None:
            OP_val = None
        else:
            OP_val = self.OP.copy()
        t_final_val = self.t_final
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            rot_dir=rot_dir_val,
            angle_rotor_initial=angle_rotor_initial_val,
            PWM=PWM_val,
            phase_dir=phase_dir_val,
            current_dir=current_dir_val,
            is_periodicity_t=is_periodicity_t_val,
            is_periodicity_a=is_periodicity_a_val,
            is_generator=is_generator_val,
            time=time_val,
            angle=angle_val,
            Nt_tot=Nt_tot_val,
            Nrev=Nrev_val,
            Na_tot=Na_tot_val,
            OP=OP_val,
            t_final=t_final_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rot_dir = None
        self.angle_rotor_initial = None
        if self.PWM is not None:
            self.PWM._set_None()
        self.phase_dir = None
        self.current_dir = None
        self.is_periodicity_t = None
        self.is_periodicity_a = None
        self.is_generator = None
        # Set to None the properties inherited from Input
        super(InputVoltage, self)._set_None()

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
        doc=u"""Rotation direction of the rotor (rot_dir*N0, default value given by ROT_DIR_REF)

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
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "PWM")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            ImportGenPWM = import_class("pyleecan.Classes", "ImportGenPWM", "PWM")
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

    def _get_phase_dir(self):
        """getter of phase_dir"""
        return self._phase_dir

    def _set_phase_dir(self, value):
        """setter of phase_dir"""
        check_var("phase_dir", value, "int", Vmin=-1, Vmax=1)
        self._phase_dir = value

    phase_dir = property(
        fget=_get_phase_dir,
        fset=_set_phase_dir,
        doc=u"""Rotation direction of the stator phase (phase_dir*(n-1)*pi/qs, default value given by PHASE_DIR_REF)

        :Type: int
        :min: -1
        :max: 1
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
        doc=u"""Rotation direction of the stator currents (current_dir*2*pi*felec*time, default value given by CURRENT_DIR_REF)

        :Type: int
        :min: -1
        :max: 1
        """,
    )

    def _get_is_periodicity_t(self):
        """getter of is_periodicity_t"""
        return self._is_periodicity_t

    def _set_is_periodicity_t(self, value):
        """setter of is_periodicity_t"""
        check_var("is_periodicity_t", value, "bool")
        self._is_periodicity_t = value

    is_periodicity_t = property(
        fget=_get_is_periodicity_t,
        fset=_set_is_periodicity_t,
        doc=u"""True to compute voltage/currents only on one time periodicity (use periodicities defined in axes_dict[time])

        :Type: bool
        """,
    )

    def _get_is_periodicity_a(self):
        """getter of is_periodicity_a"""
        return self._is_periodicity_a

    def _set_is_periodicity_a(self, value):
        """setter of is_periodicity_a"""
        check_var("is_periodicity_a", value, "bool")
        self._is_periodicity_a = value

    is_periodicity_a = property(
        fget=_get_is_periodicity_a,
        fset=_set_is_periodicity_a,
        doc=u"""True to compute voltage/currents only on one angle periodicity (use periodicities defined in axes_dict[angle])

        :Type: bool
        """,
    )

    def _get_is_generator(self):
        """getter of is_generator"""
        return self._is_generator

    def _set_is_generator(self, value):
        """setter of is_generator"""
        check_var("is_generator", value, "bool")
        self._is_generator = value

    is_generator = property(
        fget=_get_is_generator,
        fset=_set_is_generator,
        doc=u"""True if machine is used as a generator

        :Type: bool
        """,
    )
