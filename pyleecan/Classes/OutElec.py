# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutElec.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutElec
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
    from ..Methods.Output.OutElec.get_I_fund import get_I_fund
except ImportError as error:
    get_I_fund = error

try:
    from ..Methods.Output.OutElec.get_I_harm import get_I_harm
except ImportError as error:
    get_I_harm = error

try:
    from ..Methods.Output.OutElec.get_Is import get_Is
except ImportError as error:
    get_Is = error

try:
    from ..Methods.Output.OutElec.get_Nr import get_Nr
except ImportError as error:
    get_Nr = error

try:
    from ..Methods.Output.OutElec.get_Us import get_Us
except ImportError as error:
    get_Us = error

try:
    from ..Methods.Output.OutElec.store import store
except ImportError as error:
    store = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .OutInternal import OutInternal
from .OP import OP


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutElec.get_I_fund
    if isinstance(get_I_fund, ImportError):
        get_I_fund = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_I_fund: " + str(get_I_fund))
            )
        )
    else:
        get_I_fund = get_I_fund
    # cf Methods.Output.OutElec.get_I_harm
    if isinstance(get_I_harm, ImportError):
        get_I_harm = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_I_harm: " + str(get_I_harm))
            )
        )
    else:
        get_I_harm = get_I_harm
    # cf Methods.Output.OutElec.get_Is
    if isinstance(get_Is, ImportError):
        get_Is = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Is: " + str(get_Is))
            )
        )
    else:
        get_Is = get_Is
    # cf Methods.Output.OutElec.get_Nr
    if isinstance(get_Nr, ImportError):
        get_Nr = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Nr: " + str(get_Nr))
            )
        )
    else:
        get_Nr = get_Nr
    # cf Methods.Output.OutElec.get_Us
    if isinstance(get_Us, ImportError):
        get_Us = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Us: " + str(get_Us))
            )
        )
    else:
        get_Us = get_Us
    # cf Methods.Output.OutElec.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method store: " + str(store))
            )
        )
    else:
        store = store
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        axes_dict=None,
        Is=None,
        Ir=None,
        angle_rotor=None,
        angle_rotor_initial=0,
        logger_name="Pyleecan.Electrical",
        Pj_losses=None,
        Us=None,
        internal=None,
        Us_harm=None,
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
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Pj_losses" in list(init_dict.keys()):
                Pj_losses = init_dict["Pj_losses"]
            if "Us" in list(init_dict.keys()):
                Us = init_dict["Us"]
            if "internal" in list(init_dict.keys()):
                internal = init_dict["internal"]
            if "Us_harm" in list(init_dict.keys()):
                Us_harm = init_dict["Us_harm"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.axes_dict = axes_dict
        self.Is = Is
        self.Ir = Ir
        self.angle_rotor = angle_rotor
        self.angle_rotor_initial = angle_rotor_initial
        self.logger_name = logger_name
        self.Pj_losses = Pj_losses
        self.Us = Us
        self.internal = internal
        self.Us_harm = Us_harm
        self.OP = OP

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutElec_str = ""
        if self.parent is None:
            OutElec_str += "parent = None " + linesep
        else:
            OutElec_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutElec_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        OutElec_str += "Is = " + str(self.Is) + linesep + linesep
        OutElec_str += "Ir = " + str(self.Ir) + linesep + linesep
        OutElec_str += (
            "angle_rotor = "
            + linesep
            + str(self.angle_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        OutElec_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutElec_str += "Pj_losses = " + str(self.Pj_losses) + linesep
        OutElec_str += "Us = " + str(self.Us) + linesep + linesep
        if self.internal is not None:
            tmp = self.internal.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "internal = " + tmp
        else:
            OutElec_str += "internal = None" + linesep + linesep
        OutElec_str += "Us_harm = " + str(self.Us_harm) + linesep + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "OP = " + tmp
        else:
            OutElec_str += "OP = None" + linesep + linesep
        return OutElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if not array_equal(other.angle_rotor, self.angle_rotor):
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.Pj_losses != self.Pj_losses:
            return False
        if other.Us != self.Us:
            return False
        if other.internal != self.internal:
            return False
        if other.Us_harm != self.Us_harm:
            return False
        if other.OP != self.OP:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
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
        if not array_equal(other.angle_rotor, self.angle_rotor):
            diff_list.append(name + ".angle_rotor")
        if other._angle_rotor_initial != self._angle_rotor_initial:
            diff_list.append(name + ".angle_rotor_initial")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if other._Pj_losses != self._Pj_losses:
            diff_list.append(name + ".Pj_losses")
        if (other.Us is None and self.Us is not None) or (
            other.Us is not None and self.Us is None
        ):
            diff_list.append(name + ".Us None mismatch")
        elif self.Us is not None:
            diff_list.extend(self.Us.compare(other.Us, name=name + ".Us"))
        if (other.internal is None and self.internal is not None) or (
            other.internal is not None and self.internal is None
        ):
            diff_list.append(name + ".internal None mismatch")
        elif self.internal is not None:
            diff_list.extend(
                self.internal.compare(other.internal, name=name + ".internal")
            )
        if (other.Us_harm is None and self.Us_harm is not None) or (
            other.Us_harm is not None and self.Us_harm is None
        ):
            diff_list.append(name + ".Us_harm None mismatch")
        elif self.Us_harm is not None:
            diff_list.extend(
                self.Us_harm.compare(other.Us_harm, name=name + ".Us_harm")
            )
        if (other.OP is None and self.OP is not None) or (
            other.OP is not None and self.OP is None
        ):
            diff_list.append(name + ".OP None mismatch")
        elif self.OP is not None:
            diff_list.extend(self.OP.compare(other.OP, name=name + ".OP"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Is)
        S += getsizeof(self.Ir)
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.Pj_losses)
        S += getsizeof(self.Us)
        S += getsizeof(self.internal)
        S += getsizeof(self.Us_harm)
        S += getsizeof(self.OP)
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

        OutElec_dict = dict()
        if self.axes_dict is None:
            OutElec_dict["axes_dict"] = None
        else:
            OutElec_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutElec_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutElec_dict["axes_dict"][key] = None
        if self.Is is None:
            OutElec_dict["Is"] = None
        else:
            OutElec_dict["Is"] = self.Is.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Ir is None:
            OutElec_dict["Ir"] = None
        else:
            OutElec_dict["Ir"] = self.Ir.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.angle_rotor is None:
            OutElec_dict["angle_rotor"] = None
        else:
            if type_handle_ndarray == 0:
                OutElec_dict["angle_rotor"] = self.angle_rotor.tolist()
            elif type_handle_ndarray == 1:
                OutElec_dict["angle_rotor"] = self.angle_rotor.copy()
            elif type_handle_ndarray == 2:
                OutElec_dict["angle_rotor"] = self.angle_rotor
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OutElec_dict["angle_rotor_initial"] = self.angle_rotor_initial
        OutElec_dict["logger_name"] = self.logger_name
        OutElec_dict["Pj_losses"] = self.Pj_losses
        if self.Us is None:
            OutElec_dict["Us"] = None
        else:
            OutElec_dict["Us"] = self.Us.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.internal is None:
            OutElec_dict["internal"] = None
        else:
            OutElec_dict["internal"] = self.internal.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Us_harm is None:
            OutElec_dict["Us_harm"] = None
        else:
            OutElec_dict["Us_harm"] = self.Us_harm.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.OP is None:
            OutElec_dict["OP"] = None
        else:
            OutElec_dict["OP"] = self.OP.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        OutElec_dict["__class__"] = "OutElec"
        return OutElec_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.axes_dict = None
        self.Is = None
        self.Ir = None
        self.angle_rotor = None
        self.angle_rotor_initial = None
        self.logger_name = None
        self.Pj_losses = None
        self.Us = None
        if self.internal is not None:
            self.internal._set_None()
        self.Us_harm = None
        if self.OP is not None:
            self.OP._set_None()

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
        doc=u"""Dict containing axes data used for Electrical

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Is"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Is", value, "DataND")
        self._Is = value

    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents DataTime object

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Ir"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Ir", value, "DataND")
        self._Ir = value

    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_rotor", value, "ndarray")
        self._angle_rotor = value

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr)

        :Type: ndarray
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

    def _get_Pj_losses(self):
        """getter of Pj_losses"""
        return self._Pj_losses

    def _set_Pj_losses(self, value):
        """setter of Pj_losses"""
        check_var("Pj_losses", value, "float")
        self._Pj_losses = value

    Pj_losses = property(
        fget=_get_Pj_losses,
        fset=_set_Pj_losses,
        doc=u"""Electrical Joule losses

        :Type: float
        """,
    )

    def _get_Us(self):
        """getter of Us"""
        return self._Us

    def _set_Us(self, value):
        """setter of Us"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Us"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Us", value, "DataND")
        self._Us = value

    Us = property(
        fget=_get_Us,
        fset=_set_Us,
        doc=u"""Stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_internal(self):
        """getter of internal"""
        return self._internal

    def _set_internal(self, value):
        """setter of internal"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "internal"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = OutInternal()
        check_var("internal", value, "OutInternal")
        self._internal = value

        if self._internal is not None:
            self._internal.parent = self

    internal = property(
        fget=_get_internal,
        fset=_set_internal,
        doc=u"""OutInternal object containg outputs related to a specific model

        :Type: OutInternal
        """,
    )

    def _get_Us_harm(self):
        """getter of Us_harm"""
        return self._Us_harm

    def _set_Us_harm(self, value):
        """setter of Us_harm"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Us_harm"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Us_harm", value, "DataND")
        self._Us_harm = value

    Us_harm = property(
        fget=_get_Us_harm,
        fset=_set_Us_harm,
        doc=u"""Harmonic stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_OP(self):
        """getter of OP"""
        return self._OP

    def _set_OP(self, value):
        """setter of OP"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "OP")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
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
