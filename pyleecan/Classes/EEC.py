# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC
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
    from ..Methods.Simulation.EEC.get_machine_from_parent import get_machine_from_parent
except ImportError as error:
    get_machine_from_parent = error

try:
    from ..Methods.Simulation.EEC.comp_R1 import comp_R1
except ImportError as error:
    comp_R1 = error

try:
    from ..Methods.Simulation.EEC.comp_skin_effect import comp_skin_effect
except ImportError as error:
    comp_skin_effect = error

try:
    from ..Methods.Simulation.EEC.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC.update_from_ref import update_from_ref
except ImportError as error:
    update_from_ref = error

try:
    from ..Methods.Simulation.EEC.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC.solve_PWM import solve_PWM
except ImportError as error:
    solve_PWM = error

try:
    from ..Methods.Simulation.EEC.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error

try:
    from ..Methods.Simulation.EEC.comp_fluxlinkage import comp_fluxlinkage
except ImportError as error:
    comp_fluxlinkage = error


from ._check import InitUnKnowClassError


class EEC(FrozenClass):
    """Equivalent Electrical Circuit abstract class"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC.get_machine_from_parent
    if isinstance(get_machine_from_parent, ImportError):
        get_machine_from_parent = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method get_machine_from_parent: "
                    + str(get_machine_from_parent)
                )
            )
        )
    else:
        get_machine_from_parent = get_machine_from_parent
    # cf Methods.Simulation.EEC.comp_R1
    if isinstance(comp_R1, ImportError):
        comp_R1 = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC method comp_R1: " + str(comp_R1))
            )
        )
    else:
        comp_R1 = comp_R1
    # cf Methods.Simulation.EEC.comp_skin_effect
    if isinstance(comp_skin_effect, ImportError):
        comp_skin_effect = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method comp_skin_effect: " + str(comp_skin_effect)
                )
            )
        )
    else:
        comp_skin_effect = comp_skin_effect
    # cf Methods.Simulation.EEC.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method comp_parameters: " + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC.update_from_ref
    if isinstance(update_from_ref, ImportError):
        update_from_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method update_from_ref: " + str(update_from_ref)
                )
            )
        )
    else:
        update_from_ref = update_from_ref
    # cf Methods.Simulation.EEC.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.EEC.solve_PWM
    if isinstance(solve_PWM, ImportError):
        solve_PWM = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC method solve_PWM: " + str(solve_PWM))
            )
        )
    else:
        solve_PWM = solve_PWM
    # cf Methods.Simulation.EEC.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method comp_joule_losses: " + str(comp_joule_losses)
                )
            )
        )
    else:
        comp_joule_losses = comp_joule_losses
    # cf Methods.Simulation.EEC.comp_fluxlinkage
    if isinstance(comp_fluxlinkage, ImportError):
        comp_fluxlinkage = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC method comp_fluxlinkage: " + str(comp_fluxlinkage)
                )
            )
        )
    else:
        comp_fluxlinkage = comp_fluxlinkage
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_skin_effect=1,
        OP=None,
        Tsta=20,
        Trot=20,
        Xkr_skinS=1,
        Xke_skinS=1,
        Xkr_skinR=1,
        Xke_skinR=1,
        R1=None,
        fluxlink=None,
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
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "Xkr_skinS" in list(init_dict.keys()):
                Xkr_skinS = init_dict["Xkr_skinS"]
            if "Xke_skinS" in list(init_dict.keys()):
                Xke_skinS = init_dict["Xke_skinS"]
            if "Xkr_skinR" in list(init_dict.keys()):
                Xkr_skinR = init_dict["Xkr_skinR"]
            if "Xke_skinR" in list(init_dict.keys()):
                Xke_skinR = init_dict["Xke_skinR"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.type_skin_effect = type_skin_effect
        self.OP = OP
        self.Tsta = Tsta
        self.Trot = Trot
        self.Xkr_skinS = Xkr_skinS
        self.Xke_skinS = Xke_skinS
        self.Xkr_skinR = Xkr_skinR
        self.Xke_skinR = Xke_skinR
        self.R1 = R1
        self.fluxlink = fluxlink

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_str = ""
        if self.parent is None:
            EEC_str += "parent = None " + linesep
        else:
            EEC_str += "parent = " + str(type(self.parent)) + " object" + linesep
        EEC_str += "type_skin_effect = " + str(self.type_skin_effect) + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_str += "OP = " + tmp
        else:
            EEC_str += "OP = None" + linesep + linesep
        EEC_str += "Tsta = " + str(self.Tsta) + linesep
        EEC_str += "Trot = " + str(self.Trot) + linesep
        EEC_str += "Xkr_skinS = " + str(self.Xkr_skinS) + linesep
        EEC_str += "Xke_skinS = " + str(self.Xke_skinS) + linesep
        EEC_str += "Xkr_skinR = " + str(self.Xkr_skinR) + linesep
        EEC_str += "Xke_skinR = " + str(self.Xke_skinR) + linesep
        EEC_str += "R1 = " + str(self.R1) + linesep
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_str += "fluxlink = " + tmp
        else:
            EEC_str += "fluxlink = None" + linesep + linesep
        return EEC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_skin_effect != self.type_skin_effect:
            return False
        if other.OP != self.OP:
            return False
        if other.Tsta != self.Tsta:
            return False
        if other.Trot != self.Trot:
            return False
        if other.Xkr_skinS != self.Xkr_skinS:
            return False
        if other.Xke_skinS != self.Xke_skinS:
            return False
        if other.Xkr_skinR != self.Xkr_skinR:
            return False
        if other.Xke_skinR != self.Xke_skinR:
            return False
        if other.R1 != self.R1:
            return False
        if other.fluxlink != self.fluxlink:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._type_skin_effect != self._type_skin_effect:
            diff_list.append(name + ".type_skin_effect")
        if (other.OP is None and self.OP is not None) or (
            other.OP is not None and self.OP is None
        ):
            diff_list.append(name + ".OP None mismatch")
        elif self.OP is not None:
            diff_list.extend(self.OP.compare(other.OP, name=name + ".OP"))
        if other._Tsta != self._Tsta:
            diff_list.append(name + ".Tsta")
        if other._Trot != self._Trot:
            diff_list.append(name + ".Trot")
        if other._Xkr_skinS != self._Xkr_skinS:
            diff_list.append(name + ".Xkr_skinS")
        if other._Xke_skinS != self._Xke_skinS:
            diff_list.append(name + ".Xke_skinS")
        if other._Xkr_skinR != self._Xkr_skinR:
            diff_list.append(name + ".Xkr_skinR")
        if other._Xke_skinR != self._Xke_skinR:
            diff_list.append(name + ".Xke_skinR")
        if other._R1 != self._R1:
            diff_list.append(name + ".R1")
        if (other.fluxlink is None and self.fluxlink is not None) or (
            other.fluxlink is not None and self.fluxlink is None
        ):
            diff_list.append(name + ".fluxlink None mismatch")
        elif self.fluxlink is not None:
            diff_list.extend(
                self.fluxlink.compare(other.fluxlink, name=name + ".fluxlink")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.type_skin_effect)
        S += getsizeof(self.OP)
        S += getsizeof(self.Tsta)
        S += getsizeof(self.Trot)
        S += getsizeof(self.Xkr_skinS)
        S += getsizeof(self.Xke_skinS)
        S += getsizeof(self.Xkr_skinR)
        S += getsizeof(self.Xke_skinR)
        S += getsizeof(self.R1)
        S += getsizeof(self.fluxlink)
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

        EEC_dict = dict()
        EEC_dict["type_skin_effect"] = self.type_skin_effect
        if self.OP is None:
            EEC_dict["OP"] = None
        else:
            EEC_dict["OP"] = self.OP.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        EEC_dict["Tsta"] = self.Tsta
        EEC_dict["Trot"] = self.Trot
        EEC_dict["Xkr_skinS"] = self.Xkr_skinS
        EEC_dict["Xke_skinS"] = self.Xke_skinS
        EEC_dict["Xkr_skinR"] = self.Xkr_skinR
        EEC_dict["Xke_skinR"] = self.Xke_skinR
        EEC_dict["R1"] = self.R1
        if self.fluxlink is None:
            EEC_dict["fluxlink"] = None
        else:
            EEC_dict["fluxlink"] = self.fluxlink.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        EEC_dict["__class__"] = "EEC"
        return EEC_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_skin_effect = None
        if self.OP is not None:
            self.OP._set_None()
        self.Tsta = None
        self.Trot = None
        self.Xkr_skinS = None
        self.Xke_skinS = None
        self.Xkr_skinR = None
        self.Xke_skinR = None
        self.R1 = None
        if self.fluxlink is not None:
            self.fluxlink._set_None()

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
        doc=u"""Average stator temperature for operational EEC calculation

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
        doc=u"""Average rotor temperature for operational EEC calculation

        :Type: float
        """,
    )

    def _get_Xkr_skinS(self):
        """getter of Xkr_skinS"""
        return self._Xkr_skinS

    def _set_Xkr_skinS(self, value):
        """setter of Xkr_skinS"""
        check_var("Xkr_skinS", value, "float")
        self._Xkr_skinS = value

    Xkr_skinS = property(
        fget=_get_Xkr_skinS,
        fset=_set_Xkr_skinS,
        doc=u"""Skin effect coefficient for resistances at stator side

        :Type: float
        """,
    )

    def _get_Xke_skinS(self):
        """getter of Xke_skinS"""
        return self._Xke_skinS

    def _set_Xke_skinS(self, value):
        """setter of Xke_skinS"""
        check_var("Xke_skinS", value, "float")
        self._Xke_skinS = value

    Xke_skinS = property(
        fget=_get_Xke_skinS,
        fset=_set_Xke_skinS,
        doc=u"""Skin effect coefficient for inductances at stator side

        :Type: float
        """,
    )

    def _get_Xkr_skinR(self):
        """getter of Xkr_skinR"""
        return self._Xkr_skinR

    def _set_Xkr_skinR(self, value):
        """setter of Xkr_skinR"""
        check_var("Xkr_skinR", value, "float")
        self._Xkr_skinR = value

    Xkr_skinR = property(
        fget=_get_Xkr_skinR,
        fset=_set_Xkr_skinR,
        doc=u"""Skin effect coefficient for resistances at rotor side

        :Type: float
        """,
    )

    def _get_Xke_skinR(self):
        """getter of Xke_skinR"""
        return self._Xke_skinR

    def _set_Xke_skinR(self, value):
        """setter of Xke_skinR"""
        check_var("Xke_skinR", value, "float")
        self._Xke_skinR = value

    Xke_skinR = property(
        fget=_get_Xke_skinR,
        fset=_set_Xke_skinR,
        doc=u"""Skin effect coefficient for inductances at rotor side

        :Type: float
        """,
    )

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
        doc=u"""Stator phase resistance

        :Type: float
        """,
    )

    def _get_fluxlink(self):
        """getter of fluxlink"""
        return self._fluxlink

    def _set_fluxlink(self, value):
        """setter of fluxlink"""
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
                "pyleecan.Classes", value.get("__class__"), "fluxlink"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnetics = import_class("pyleecan.Classes", "Magnetics", "fluxlink")
            value = Magnetics()
        check_var("fluxlink", value, "Magnetics")
        self._fluxlink = value

        if self._fluxlink is not None:
            self._fluxlink.parent = self

    fluxlink = property(
        fget=_get_fluxlink,
        fset=_set_fluxlink,
        doc=u"""Magnetic model for flux linkage calculation

        :Type: Magnetics
        """,
    )
