# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Electrical.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Electrical
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
    from ..Methods.Simulation.Electrical.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Electrical.comp_power import comp_power
except ImportError as error:
    comp_power = error

try:
    from ..Methods.Simulation.Electrical.comp_torque import comp_torque
except ImportError as error:
    comp_torque = error

try:
    from ..Methods.Simulation.Electrical.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error


from ._check import InitUnKnowClassError


class Electrical(FrozenClass):
    """Electric module object for electrical equivalent circuit simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Electrical.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Electrical method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Electrical.comp_power
    if isinstance(comp_power, ImportError):
        comp_power = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Electrical method comp_power: " + str(comp_power)
                )
            )
        )
    else:
        comp_power = comp_power
    # cf Methods.Simulation.Electrical.comp_torque
    if isinstance(comp_torque, ImportError):
        comp_torque = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Electrical method comp_torque: " + str(comp_torque)
                )
            )
        )
    else:
        comp_torque = comp_torque
    # cf Methods.Simulation.Electrical.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use Electrical method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        eec=None,
        logger_name="Pyleecan.Electrical",
        freq_max=40000,
        LUT_enforced=None,
        Tsta=20,
        Trot=20,
        type_skin_effect=1,
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
            if "eec" in list(init_dict.keys()):
                eec = init_dict["eec"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "freq_max" in list(init_dict.keys()):
                freq_max = init_dict["freq_max"]
            if "LUT_enforced" in list(init_dict.keys()):
                LUT_enforced = init_dict["LUT_enforced"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.eec = eec
        self.logger_name = logger_name
        self.freq_max = freq_max
        self.LUT_enforced = LUT_enforced
        self.Tsta = Tsta
        self.Trot = Trot
        self.type_skin_effect = type_skin_effect

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Electrical_str = ""
        if self.parent is None:
            Electrical_str += "parent = None " + linesep
        else:
            Electrical_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.eec is not None:
            tmp = self.eec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Electrical_str += "eec = " + tmp
        else:
            Electrical_str += "eec = None" + linesep + linesep
        Electrical_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        Electrical_str += "freq_max = " + str(self.freq_max) + linesep
        if self.LUT_enforced is not None:
            tmp = (
                self.LUT_enforced.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            Electrical_str += "LUT_enforced = " + tmp
        else:
            Electrical_str += "LUT_enforced = None" + linesep + linesep
        Electrical_str += "Tsta = " + str(self.Tsta) + linesep
        Electrical_str += "Trot = " + str(self.Trot) + linesep
        Electrical_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        return Electrical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.eec != self.eec:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.freq_max != self.freq_max:
            return False
        if other.LUT_enforced != self.LUT_enforced:
            return False
        if other.Tsta != self.Tsta:
            return False
        if other.Trot != self.Trot:
            return False
        if other.type_skin_effect != self.type_skin_effect:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.eec is None and self.eec is not None) or (
            other.eec is not None and self.eec is None
        ):
            diff_list.append(name + ".eec None mismatch")
        elif self.eec is not None:
            diff_list.extend(self.eec.compare(other.eec, name=name + ".eec"))
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if other._freq_max != self._freq_max:
            diff_list.append(name + ".freq_max")
        if (other.LUT_enforced is None and self.LUT_enforced is not None) or (
            other.LUT_enforced is not None and self.LUT_enforced is None
        ):
            diff_list.append(name + ".LUT_enforced None mismatch")
        elif self.LUT_enforced is not None:
            diff_list.extend(
                self.LUT_enforced.compare(
                    other.LUT_enforced, name=name + ".LUT_enforced"
                )
            )
        if other._Tsta != self._Tsta:
            diff_list.append(name + ".Tsta")
        if other._Trot != self._Trot:
            diff_list.append(name + ".Trot")
        if other._type_skin_effect != self._type_skin_effect:
            diff_list.append(name + ".type_skin_effect")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.eec)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.freq_max)
        S += getsizeof(self.LUT_enforced)
        S += getsizeof(self.Tsta)
        S += getsizeof(self.Trot)
        S += getsizeof(self.type_skin_effect)
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

        Electrical_dict = dict()
        if self.eec is None:
            Electrical_dict["eec"] = None
        else:
            Electrical_dict["eec"] = self.eec.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Electrical_dict["logger_name"] = self.logger_name
        Electrical_dict["freq_max"] = self.freq_max
        if self.LUT_enforced is None:
            Electrical_dict["LUT_enforced"] = None
        else:
            Electrical_dict["LUT_enforced"] = self.LUT_enforced.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Electrical_dict["Tsta"] = self.Tsta
        Electrical_dict["Trot"] = self.Trot
        Electrical_dict["type_skin_effect"] = self.type_skin_effect
        # The class name is added to the dict for deserialisation purpose
        Electrical_dict["__class__"] = "Electrical"
        return Electrical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.eec is not None:
            self.eec._set_None()
        self.logger_name = None
        self.freq_max = None
        if self.LUT_enforced is not None:
            self.LUT_enforced._set_None()
        self.Tsta = None
        self.Trot = None
        self.type_skin_effect = None

    def _get_eec(self):
        """getter of eec"""
        return self._eec

    def _set_eec(self, value):
        """setter of eec"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "eec")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            EEC = import_class("pyleecan.Classes", "EEC", "eec")
            value = EEC()
        check_var("eec", value, "EEC")
        self._eec = value

        if self._eec is not None:
            self._eec.parent = self

    eec = property(
        fget=_get_eec,
        fset=_set_eec,
        doc=u"""Electrical Equivalent Circuit

        :Type: EEC
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

    def _get_freq_max(self):
        """getter of freq_max"""
        return self._freq_max

    def _set_freq_max(self, value):
        """setter of freq_max"""
        check_var("freq_max", value, "float")
        self._freq_max = value

    freq_max = property(
        fget=_get_freq_max,
        fset=_set_freq_max,
        doc=u"""Maximum frequency to calculate voltage and current harmonics

        :Type: float
        """,
    )

    def _get_LUT_enforced(self):
        """getter of LUT_enforced"""
        return self._LUT_enforced

    def _set_LUT_enforced(self, value):
        """setter of LUT_enforced"""
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
                "pyleecan.Classes", value.get("__class__"), "LUT_enforced"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            LUT = import_class("pyleecan.Classes", "LUT", "LUT_enforced")
            value = LUT()
        check_var("LUT_enforced", value, "LUT")
        self._LUT_enforced = value

        if self._LUT_enforced is not None:
            self._LUT_enforced.parent = self

    LUT_enforced = property(
        fget=_get_LUT_enforced,
        fset=_set_LUT_enforced,
        doc=u"""Look-Up Tables to update equivalent circuit parameters

        :Type: LUT
        """,
    )

    def _get_Tsta(self):
        """getter of Tsta"""
        return self._Tsta

    def _set_Tsta(self, value):
        """setter of Tsta"""
        check_var("Tsta", value, "float")
        self._Tsta = value

    Tsta = property(
        fget=_get_Tsta,
        fset=_set_Tsta,
        doc=u"""Average stator temperature for Electrical calculation

        :Type: float
        """,
    )

    def _get_Trot(self):
        """getter of Trot"""
        return self._Trot

    def _set_Trot(self, value):
        """setter of Trot"""
        check_var("Trot", value, "float")
        self._Trot = value

    Trot = property(
        fget=_get_Trot,
        fset=_set_Trot,
        doc=u"""Average rotor temperature for Electrical calculation

        :Type: float
        """,
    )

    def _get_type_skin_effect(self):
        """getter of type_skin_effect"""
        return self._type_skin_effect

    def _set_type_skin_effect(self, value):
        """setter of type_skin_effect"""
        check_var("type_skin_effect", value, "int")
        self._type_skin_effect = value

    type_skin_effect = property(
        fget=_get_type_skin_effect,
        fset=_set_type_skin_effect,
        doc=u"""Skin effect for resistance and inductance

        :Type: int
        """,
    )
