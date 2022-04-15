# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputPower.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputPower
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
    from ..Methods.Simulation.InputPower.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputPower.set_OP_from_array import set_OP_from_array
except ImportError as error:
    set_OP_from_array = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError


class InputPower(InputVoltage):
    """Input to start the electrical module with power input"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputPower.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputPower method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputPower.set_OP_from_array
    if isinstance(set_OP_from_array, ImportError):
        set_OP_from_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputPower method set_OP_from_array: "
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
        Urms_max=None,
        Jrms_max=None,
        Irms_max=None,
        is_generator=False,
        rot_dir=None,
        angle_rotor_initial=0,
        PWM=None,
        phase_dir=None,
        current_dir=None,
        is_periodicity_t=False,
        is_periodicity_a=False,
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
            if "Urms_max" in list(init_dict.keys()):
                Urms_max = init_dict["Urms_max"]
            if "Jrms_max" in list(init_dict.keys()):
                Jrms_max = init_dict["Jrms_max"]
            if "Irms_max" in list(init_dict.keys()):
                Irms_max = init_dict["Irms_max"]
            if "is_generator" in list(init_dict.keys()):
                is_generator = init_dict["is_generator"]
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
        self.Urms_max = Urms_max
        self.Jrms_max = Jrms_max
        self.Irms_max = Irms_max
        self.is_generator = is_generator
        # Call InputVoltage init
        super(InputPower, self).__init__(
            rot_dir=rot_dir,
            angle_rotor_initial=angle_rotor_initial,
            PWM=PWM,
            phase_dir=phase_dir,
            current_dir=current_dir,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
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

        InputPower_str = ""
        # Get the properties inherited from InputVoltage
        InputPower_str += super(InputPower, self).__str__()
        InputPower_str += "Urms_max = " + str(self.Urms_max) + linesep
        InputPower_str += "Jrms_max = " + str(self.Jrms_max) + linesep
        InputPower_str += "Irms_max = " + str(self.Irms_max) + linesep
        InputPower_str += "is_generator = " + str(self.is_generator) + linesep
        return InputPower_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from InputVoltage
        if not super(InputPower, self).__eq__(other):
            return False
        if other.Urms_max != self.Urms_max:
            return False
        if other.Jrms_max != self.Jrms_max:
            return False
        if other.Irms_max != self.Irms_max:
            return False
        if other.is_generator != self.is_generator:
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
        diff_list.extend(super(InputPower, self).compare(other, name=name))
        if other._Urms_max != self._Urms_max:
            diff_list.append(name + ".Urms_max")
        if other._Jrms_max != self._Jrms_max:
            diff_list.append(name + ".Jrms_max")
        if other._Irms_max != self._Irms_max:
            diff_list.append(name + ".Irms_max")
        if other._is_generator != self._is_generator:
            diff_list.append(name + ".is_generator")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from InputVoltage
        S += super(InputPower, self).__sizeof__()
        S += getsizeof(self.Urms_max)
        S += getsizeof(self.Jrms_max)
        S += getsizeof(self.Irms_max)
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

        # Get the properties inherited from InputVoltage
        InputPower_dict = super(InputPower, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        InputPower_dict["Urms_max"] = self.Urms_max
        InputPower_dict["Jrms_max"] = self.Jrms_max
        InputPower_dict["Irms_max"] = self.Irms_max
        InputPower_dict["is_generator"] = self.is_generator
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputPower_dict["__class__"] = "InputPower"
        return InputPower_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Urms_max = None
        self.Jrms_max = None
        self.Irms_max = None
        self.is_generator = None
        # Set to None the properties inherited from InputVoltage
        super(InputPower, self)._set_None()

    def _get_Urms_max(self):
        """getter of Urms_max"""
        return self._Urms_max

    def _set_Urms_max(self, value):
        """setter of Urms_max"""
        check_var("Urms_max", value, "float", Vmin=0)
        self._Urms_max = value

    Urms_max = property(
        fget=_get_Urms_max,
        fset=_set_Urms_max,
        doc=u"""Maximum rms phase voltage

        :Type: float
        :min: 0
        """,
    )

    def _get_Jrms_max(self):
        """getter of Jrms_max"""
        return self._Jrms_max

    def _set_Jrms_max(self, value):
        """setter of Jrms_max"""
        check_var("Jrms_max", value, "float", Vmin=0)
        self._Jrms_max = value

    Jrms_max = property(
        fget=_get_Jrms_max,
        fset=_set_Jrms_max,
        doc=u"""Maximum rms current density in slot

        :Type: float
        :min: 0
        """,
    )

    def _get_Irms_max(self):
        """getter of Irms_max"""
        return self._Irms_max

    def _set_Irms_max(self, value):
        """setter of Irms_max"""
        check_var("Irms_max", value, "float", Vmin=0)
        self._Irms_max = value

    Irms_max = property(
        fget=_get_Irms_max,
        fset=_set_Irms_max,
        doc=u"""Maximum rms phase current

        :Type: float
        :min: 0
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
