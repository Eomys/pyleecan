# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputCurrent.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputCurrent
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
from .InputVoltage import InputVoltage

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputCurrent.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputCurrent.set_Id_Iq import set_Id_Iq
except ImportError as error:
    set_Id_Iq = error

try:
    from ..Methods.Simulation.InputCurrent.set_OP_from_array import set_OP_from_array
except ImportError as error:
    set_OP_from_array = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError


class InputCurrent(InputVoltage):
    """Input to skip the electrical module and start with the magnetic one"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputCurrent.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputCurrent.set_Id_Iq
    if isinstance(set_Id_Iq, ImportError):
        set_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method set_Id_Iq: " + str(set_Id_Iq)
                )
            )
        )
    else:
        set_Id_Iq = set_Id_Iq
    # cf Methods.Simulation.InputCurrent.set_OP_from_array
    if isinstance(set_OP_from_array, ImportError):
        set_OP_from_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method set_OP_from_array: "
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
        Is=None,
        Ir=None,
        Is_harm=None,
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
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "Is_harm" in list(init_dict.keys()):
                Is_harm = init_dict["Is_harm"]
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
        self.Is = Is
        self.Ir = Ir
        self.Is_harm = Is_harm
        # Call InputVoltage init
        super(InputCurrent, self).__init__(
            rot_dir=rot_dir,
            angle_rotor_initial=angle_rotor_initial,
            PWM=PWM,
            phase_dir=phase_dir,
            current_dir=current_dir,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            is_generator=is_generator,
            time=time,
            angle=angle,
            Nt_tot=Nt_tot,
            Nrev=Nrev,
            Na_tot=Na_tot,
            OP=OP,
            t_final=t_final,
        )
        # The class is frozen (in InputVoltage init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputCurrent_str = ""
        # Get the properties inherited from InputVoltage
        InputCurrent_str += super(InputCurrent, self).__str__()
        if self.Is is not None:
            tmp = self.Is.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Is = " + tmp
        else:
            InputCurrent_str += "Is = None" + linesep + linesep
        if self.Ir is not None:
            tmp = self.Ir.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Ir = " + tmp
        else:
            InputCurrent_str += "Ir = None" + linesep + linesep
        if self.Is_harm is not None:
            tmp = self.Is_harm.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Is_harm = " + tmp
        else:
            InputCurrent_str += "Is_harm = None" + linesep + linesep
        return InputCurrent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from InputVoltage
        if not super(InputCurrent, self).__eq__(other):
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.Is_harm != self.Is_harm:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from InputVoltage
        diff_list.extend(super(InputCurrent, self).compare(other, name=name))
        if (other.Is is None and self.Is is not None) or (
            other.Is is not None and self.Is is None
        ):
            diff_list.append(name + ".Is None mismatch")
        elif self.Is is not None:
            diff_list.extend(self.Is.compare(other.Is, name=name + ".Is"))
        if (other.Ir is None and self.Ir is not None) or (
            other.Ir is not None and self.Ir is None
        ):
            diff_list.append(name + ".Ir None mismatch")
        elif self.Ir is not None:
            diff_list.extend(self.Ir.compare(other.Ir, name=name + ".Ir"))
        if (other.Is_harm is None and self.Is_harm is not None) or (
            other.Is_harm is not None and self.Is_harm is None
        ):
            diff_list.append(name + ".Is_harm None mismatch")
        elif self.Is_harm is not None:
            diff_list.extend(
                self.Is_harm.compare(other.Is_harm, name=name + ".Is_harm")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from InputVoltage
        S += super(InputCurrent, self).__sizeof__()
        S += getsizeof(self.Is)
        S += getsizeof(self.Ir)
        S += getsizeof(self.Is_harm)
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

        # Get the properties inherited from InputVoltage
        InputCurrent_dict = super(InputCurrent, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.Is is None:
            InputCurrent_dict["Is"] = None
        else:
            InputCurrent_dict["Is"] = self.Is.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Ir is None:
            InputCurrent_dict["Ir"] = None
        else:
            InputCurrent_dict["Ir"] = self.Ir.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Is_harm is None:
            InputCurrent_dict["Is_harm"] = None
        else:
            InputCurrent_dict["Is_harm"] = self.Is_harm.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputCurrent_dict["__class__"] = "InputCurrent"
        return InputCurrent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.Is is not None:
            self.Is._set_None()
        if self.Ir is not None:
            self.Ir._set_None()
        if self.Is_harm is not None:
            self.Is_harm._set_None()
        # Set to None the properties inherited from InputVoltage
        super(InputCurrent, self)._set_None()

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "Is")
        ImportMatrixVal = import_class("pyleecan.Classes", "ImportMatrixVal", "Is")
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "Is")
            value = class_obj(init_dict=value)
        check_var("Is", value, "ImportMatrix")
        self._Is = value

        if self._Is is not None:
            self._Is.parent = self

    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        ImportMatrix = import_class("pyleecan.Classes", "ImportMatrix", "Ir")
        ImportMatrixVal = import_class("pyleecan.Classes", "ImportMatrixVal", "Ir")
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "Ir")
            value = class_obj(init_dict=value)
        check_var("Ir", value, "ImportMatrix")
        self._Ir = value

        if self._Ir is not None:
            self._Ir.parent = self

    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Is_harm(self):
        """getter of Is_harm"""
        return self._Is_harm

    def _set_Is_harm(self, value):
        """setter of Is_harm"""
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
                "pyleecan.Classes", value.get("__class__"), "Is_harm"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            ImportData = import_class("pyleecan.Classes", "ImportData", "Is_harm")
            value = ImportData()
        check_var("Is_harm", value, "ImportData")
        self._Is_harm = value

        if self._Is_harm is not None:
            self._Is_harm.parent = self

    Is_harm = property(
        fget=_get_Is_harm,
        fset=_set_Is_harm,
        doc=u"""Stator harmonic currents

        :Type: ImportData
        """,
    )
