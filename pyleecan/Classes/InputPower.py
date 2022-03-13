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
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputPower.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError


class InputPower(Input):
    """Input to start the electrical module with power input"""

    VERSION = 1

    # cf Methods.Simulation.InputPower.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputPower method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        rot_dir=None,
        phase_dir=None,
        current_dir=None,
        is_periodicity_t=False,
        is_periodicity_a=False,
        U_max=None,
        J_max=None,
        I_max=None,
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
            if "phase_dir" in list(init_dict.keys()):
                phase_dir = init_dict["phase_dir"]
            if "current_dir" in list(init_dict.keys()):
                current_dir = init_dict["current_dir"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "U_max" in list(init_dict.keys()):
                U_max = init_dict["U_max"]
            if "J_max" in list(init_dict.keys()):
                J_max = init_dict["J_max"]
            if "I_max" in list(init_dict.keys()):
                I_max = init_dict["I_max"]
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
        self.phase_dir = phase_dir
        self.current_dir = current_dir
        self.is_periodicity_t = is_periodicity_t
        self.is_periodicity_a = is_periodicity_a
        self.U_max = U_max
        self.J_max = J_max
        self.I_max = I_max
        # Call Input init
        super(InputPower, self).__init__(
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

        InputPower_str = ""
        # Get the properties inherited from Input
        InputPower_str += super(InputPower, self).__str__()
        InputPower_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputPower_str += "phase_dir = " + str(self.phase_dir) + linesep
        InputPower_str += "current_dir = " + str(self.current_dir) + linesep
        InputPower_str += "is_periodicity_t = " + str(self.is_periodicity_t) + linesep
        InputPower_str += "is_periodicity_a = " + str(self.is_periodicity_a) + linesep
        InputPower_str += "U_max = " + str(self.U_max) + linesep
        InputPower_str += "J_max = " + str(self.J_max) + linesep
        InputPower_str += "I_max = " + str(self.I_max) + linesep
        return InputPower_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputPower, self).__eq__(other):
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.phase_dir != self.phase_dir:
            return False
        if other.current_dir != self.current_dir:
            return False
        if other.is_periodicity_t != self.is_periodicity_t:
            return False
        if other.is_periodicity_a != self.is_periodicity_a:
            return False
        if other.U_max != self.U_max:
            return False
        if other.J_max != self.J_max:
            return False
        if other.I_max != self.I_max:
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
        diff_list.extend(super(InputPower, self).compare(other, name=name))
        if other._rot_dir != self._rot_dir:
            diff_list.append(name + ".rot_dir")
        if other._phase_dir != self._phase_dir:
            diff_list.append(name + ".phase_dir")
        if other._current_dir != self._current_dir:
            diff_list.append(name + ".current_dir")
        if other._is_periodicity_t != self._is_periodicity_t:
            diff_list.append(name + ".is_periodicity_t")
        if other._is_periodicity_a != self._is_periodicity_a:
            diff_list.append(name + ".is_periodicity_a")
        if other._U_max != self._U_max:
            diff_list.append(name + ".U_max")
        if other._J_max != self._J_max:
            diff_list.append(name + ".J_max")
        if other._I_max != self._I_max:
            diff_list.append(name + ".I_max")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputPower, self).__sizeof__()
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.phase_dir)
        S += getsizeof(self.current_dir)
        S += getsizeof(self.is_periodicity_t)
        S += getsizeof(self.is_periodicity_a)
        S += getsizeof(self.U_max)
        S += getsizeof(self.J_max)
        S += getsizeof(self.I_max)
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
        InputPower_dict = super(InputPower, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        InputPower_dict["rot_dir"] = self.rot_dir
        InputPower_dict["phase_dir"] = self.phase_dir
        InputPower_dict["current_dir"] = self.current_dir
        InputPower_dict["is_periodicity_t"] = self.is_periodicity_t
        InputPower_dict["is_periodicity_a"] = self.is_periodicity_a
        InputPower_dict["U_max"] = self.U_max
        InputPower_dict["J_max"] = self.J_max
        InputPower_dict["I_max"] = self.I_max
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputPower_dict["__class__"] = "InputPower"
        return InputPower_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rot_dir = None
        self.phase_dir = None
        self.current_dir = None
        self.is_periodicity_t = None
        self.is_periodicity_a = None
        self.U_max = None
        self.J_max = None
        self.I_max = None
        # Set to None the properties inherited from Input
        super(InputPower, self)._set_None()

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

    def _get_U_max(self):
        """getter of U_max"""
        return self._U_max

    def _set_U_max(self, value):
        """setter of U_max"""
        check_var("U_max", value, "float", Vmin=0)
        self._U_max = value

    U_max = property(
        fget=_get_U_max,
        fset=_set_U_max,
        doc=u"""Maximum phase voltage

        :Type: float
        :min: 0
        """,
    )

    def _get_J_max(self):
        """getter of J_max"""
        return self._J_max

    def _set_J_max(self, value):
        """setter of J_max"""
        check_var("J_max", value, "float", Vmin=0)
        self._J_max = value

    J_max = property(
        fget=_get_J_max,
        fset=_set_J_max,
        doc=u"""Maximum current density in slot

        :Type: float
        :min: 0
        """,
    )

    def _get_I_max(self):
        """getter of I_max"""
        return self._I_max

    def _set_I_max(self, value):
        """setter of I_max"""
        check_var("I_max", value, "float", Vmin=0)
        self._I_max = value

    I_max = property(
        fget=_get_I_max,
        fset=_set_I_max,
        doc=u"""Maximum phase current

        :Type: float
        :min: 0
        """,
    )
