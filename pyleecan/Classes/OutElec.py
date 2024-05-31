# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutElec.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutElec
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutElec.get_Nr import get_Nr
except ImportError as error:
    get_Nr = error

try:
    from ..Methods.Output.OutElec.get_Is import get_Is
except ImportError as error:
    get_Is = error

try:
    from ..Methods.Output.OutElec.get_Us import get_Us
except ImportError as error:
    get_Us = error

try:
    from ..Methods.Output.OutElec.store import store
except ImportError as error:
    store = error

try:
    from ..Methods.Output.OutElec.get_electrical import get_electrical
except ImportError as error:
    get_electrical = error

try:
    from ..Methods.Output.OutElec.get_Jrms import get_Jrms
except ImportError as error:
    get_Jrms = error


from numpy import isnan
from ._check import InitUnKnowClassError


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutElec.get_Nr
    if isinstance(get_Nr, ImportError):
        get_Nr = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Nr: " + str(get_Nr))
            )
        )
    else:
        get_Nr = get_Nr
    # cf Methods.Output.OutElec.get_Is
    if isinstance(get_Is, ImportError):
        get_Is = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Is: " + str(get_Is))
            )
        )
    else:
        get_Is = get_Is
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
    # cf Methods.Output.OutElec.get_electrical
    if isinstance(get_electrical, ImportError):
        get_electrical = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutElec method get_electrical: " + str(get_electrical)
                )
            )
        )
    else:
        get_electrical = get_electrical
    # cf Methods.Output.OutElec.get_Jrms
    if isinstance(get_Jrms, ImportError):
        get_Jrms = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Jrms: " + str(get_Jrms))
            )
        )
    else:
        get_Jrms = get_Jrms
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        axes_dict=None,
        Is=None,
        Ir=None,
        logger_name="pyleecan.Electrical",
        Pj_losses=None,
        Us=None,
        internal=None,
        OP=None,
        Pem_av=None,
        Tem_av=None,
        phase_dir=None,
        current_dir=None,
        PWM=None,
        eec=None,
        P_out=None,
        Jrms=None,
        P_in=None,
        Arms=None,
        Erms=None,
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
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Pj_losses" in list(init_dict.keys()):
                Pj_losses = init_dict["Pj_losses"]
            if "Us" in list(init_dict.keys()):
                Us = init_dict["Us"]
            if "internal" in list(init_dict.keys()):
                internal = init_dict["internal"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "Pem_av" in list(init_dict.keys()):
                Pem_av = init_dict["Pem_av"]
            if "Tem_av" in list(init_dict.keys()):
                Tem_av = init_dict["Tem_av"]
            if "phase_dir" in list(init_dict.keys()):
                phase_dir = init_dict["phase_dir"]
            if "current_dir" in list(init_dict.keys()):
                current_dir = init_dict["current_dir"]
            if "PWM" in list(init_dict.keys()):
                PWM = init_dict["PWM"]
            if "eec" in list(init_dict.keys()):
                eec = init_dict["eec"]
            if "P_out" in list(init_dict.keys()):
                P_out = init_dict["P_out"]
            if "Jrms" in list(init_dict.keys()):
                Jrms = init_dict["Jrms"]
            if "P_in" in list(init_dict.keys()):
                P_in = init_dict["P_in"]
            if "Arms" in list(init_dict.keys()):
                Arms = init_dict["Arms"]
            if "Erms" in list(init_dict.keys()):
                Erms = init_dict["Erms"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.axes_dict = axes_dict
        self.Is = Is
        self.Ir = Ir
        self.logger_name = logger_name
        self.Pj_losses = Pj_losses
        self.Us = Us
        self.internal = internal
        self.OP = OP
        self.Pem_av = Pem_av
        self.Tem_av = Tem_av
        self.phase_dir = phase_dir
        self.current_dir = current_dir
        self.PWM = PWM
        self.eec = eec
        self.P_out = P_out
        self.Jrms = Jrms
        self.P_in = P_in
        self.Arms = Arms
        self.Erms = Erms

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
        OutElec_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutElec_str += "Pj_losses = " + str(self.Pj_losses) + linesep
        OutElec_str += "Us = " + str(self.Us) + linesep + linesep
        if self.internal is not None:
            tmp = self.internal.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "internal = " + tmp
        else:
            OutElec_str += "internal = None" + linesep + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "OP = " + tmp
        else:
            OutElec_str += "OP = None" + linesep + linesep
        OutElec_str += "Pem_av = " + str(self.Pem_av) + linesep
        OutElec_str += "Tem_av = " + str(self.Tem_av) + linesep
        OutElec_str += "phase_dir = " + str(self.phase_dir) + linesep
        OutElec_str += "current_dir = " + str(self.current_dir) + linesep
        if self.PWM is not None:
            tmp = self.PWM.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "PWM = " + tmp
        else:
            OutElec_str += "PWM = None" + linesep + linesep
        if self.eec is not None:
            tmp = self.eec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "eec = " + tmp
        else:
            OutElec_str += "eec = None" + linesep + linesep
        OutElec_str += "P_out = " + str(self.P_out) + linesep
        OutElec_str += "Jrms = " + str(self.Jrms) + linesep
        OutElec_str += "P_in = " + str(self.P_in) + linesep
        OutElec_str += "Arms = " + str(self.Arms) + linesep
        OutElec_str += "Erms = " + str(self.Erms) + linesep
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
        if other.logger_name != self.logger_name:
            return False
        if other.Pj_losses != self.Pj_losses:
            return False
        if other.Us != self.Us:
            return False
        if other.internal != self.internal:
            return False
        if other.OP != self.OP:
            return False
        if other.Pem_av != self.Pem_av:
            return False
        if other.Tem_av != self.Tem_av:
            return False
        if other.phase_dir != self.phase_dir:
            return False
        if other.current_dir != self.current_dir:
            return False
        if other.PWM != self.PWM:
            return False
        if other.eec != self.eec:
            return False
        if other.P_out != self.P_out:
            return False
        if other.Jrms != self.Jrms:
            return False
        if other.P_in != self.P_in:
            return False
        if other.Arms != self.Arms:
            return False
        if other.Erms != self.Erms:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
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
                        other.axes_dict[key],
                        name=name + ".axes_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.Is is None and self.Is is not None) or (
            other.Is is not None and self.Is is None
        ):
            diff_list.append(name + ".Is None mismatch")
        elif self.Is is not None:
            diff_list.extend(
                self.Is.compare(
                    other.Is,
                    name=name + ".Is",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.Ir is None and self.Ir is not None) or (
            other.Ir is not None and self.Ir is None
        ):
            diff_list.append(name + ".Ir None mismatch")
        elif self.Ir is not None:
            diff_list.extend(
                self.Ir.compare(
                    other.Ir,
                    name=name + ".Ir",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._logger_name != self._logger_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._logger_name)
                    + ", other="
                    + str(other._logger_name)
                    + ")"
                )
                diff_list.append(name + ".logger_name" + val_str)
            else:
                diff_list.append(name + ".logger_name")
        if (
            other._Pj_losses is not None
            and self._Pj_losses is not None
            and isnan(other._Pj_losses)
            and isnan(self._Pj_losses)
        ):
            pass
        elif other._Pj_losses != self._Pj_losses:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Pj_losses)
                    + ", other="
                    + str(other._Pj_losses)
                    + ")"
                )
                diff_list.append(name + ".Pj_losses" + val_str)
            else:
                diff_list.append(name + ".Pj_losses")
        if (other.Us is None and self.Us is not None) or (
            other.Us is not None and self.Us is None
        ):
            diff_list.append(name + ".Us None mismatch")
        elif self.Us is not None:
            diff_list.extend(
                self.Us.compare(
                    other.Us,
                    name=name + ".Us",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.internal is None and self.internal is not None) or (
            other.internal is not None and self.internal is None
        ):
            diff_list.append(name + ".internal None mismatch")
        elif self.internal is not None:
            diff_list.extend(
                self.internal.compare(
                    other.internal,
                    name=name + ".internal",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.OP is None and self.OP is not None) or (
            other.OP is not None and self.OP is None
        ):
            diff_list.append(name + ".OP None mismatch")
        elif self.OP is not None:
            diff_list.extend(
                self.OP.compare(
                    other.OP,
                    name=name + ".OP",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (
            other._Pem_av is not None
            and self._Pem_av is not None
            and isnan(other._Pem_av)
            and isnan(self._Pem_av)
        ):
            pass
        elif other._Pem_av != self._Pem_av:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Pem_av)
                    + ", other="
                    + str(other._Pem_av)
                    + ")"
                )
                diff_list.append(name + ".Pem_av" + val_str)
            else:
                diff_list.append(name + ".Pem_av")
        if (
            other._Tem_av is not None
            and self._Tem_av is not None
            and isnan(other._Tem_av)
            and isnan(self._Tem_av)
        ):
            pass
        elif other._Tem_av != self._Tem_av:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Tem_av)
                    + ", other="
                    + str(other._Tem_av)
                    + ")"
                )
                diff_list.append(name + ".Tem_av" + val_str)
            else:
                diff_list.append(name + ".Tem_av")
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
        if (other.eec is None and self.eec is not None) or (
            other.eec is not None and self.eec is None
        ):
            diff_list.append(name + ".eec None mismatch")
        elif self.eec is not None:
            diff_list.extend(
                self.eec.compare(
                    other.eec,
                    name=name + ".eec",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (
            other._P_out is not None
            and self._P_out is not None
            and isnan(other._P_out)
            and isnan(self._P_out)
        ):
            pass
        elif other._P_out != self._P_out:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._P_out) + ", other=" + str(other._P_out) + ")"
                )
                diff_list.append(name + ".P_out" + val_str)
            else:
                diff_list.append(name + ".P_out")
        if (
            other._Jrms is not None
            and self._Jrms is not None
            and isnan(other._Jrms)
            and isnan(self._Jrms)
        ):
            pass
        elif other._Jrms != self._Jrms:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Jrms) + ", other=" + str(other._Jrms) + ")"
                )
                diff_list.append(name + ".Jrms" + val_str)
            else:
                diff_list.append(name + ".Jrms")
        if (
            other._P_in is not None
            and self._P_in is not None
            and isnan(other._P_in)
            and isnan(self._P_in)
        ):
            pass
        elif other._P_in != self._P_in:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._P_in) + ", other=" + str(other._P_in) + ")"
                )
                diff_list.append(name + ".P_in" + val_str)
            else:
                diff_list.append(name + ".P_in")
        if (
            other._Arms is not None
            and self._Arms is not None
            and isnan(other._Arms)
            and isnan(self._Arms)
        ):
            pass
        elif other._Arms != self._Arms:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Arms) + ", other=" + str(other._Arms) + ")"
                )
                diff_list.append(name + ".Arms" + val_str)
            else:
                diff_list.append(name + ".Arms")
        if (
            other._Erms is not None
            and self._Erms is not None
            and isnan(other._Erms)
            and isnan(self._Erms)
        ):
            pass
        elif other._Erms != self._Erms:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Erms) + ", other=" + str(other._Erms) + ")"
                )
                diff_list.append(name + ".Erms" + val_str)
            else:
                diff_list.append(name + ".Erms")
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
        S += getsizeof(self.logger_name)
        S += getsizeof(self.Pj_losses)
        S += getsizeof(self.Us)
        S += getsizeof(self.internal)
        S += getsizeof(self.OP)
        S += getsizeof(self.Pem_av)
        S += getsizeof(self.Tem_av)
        S += getsizeof(self.phase_dir)
        S += getsizeof(self.current_dir)
        S += getsizeof(self.PWM)
        S += getsizeof(self.eec)
        S += getsizeof(self.P_out)
        S += getsizeof(self.Jrms)
        S += getsizeof(self.P_in)
        S += getsizeof(self.Arms)
        S += getsizeof(self.Erms)
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
        if self.OP is None:
            OutElec_dict["OP"] = None
        else:
            OutElec_dict["OP"] = self.OP.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutElec_dict["Pem_av"] = self.Pem_av
        OutElec_dict["Tem_av"] = self.Tem_av
        OutElec_dict["phase_dir"] = self.phase_dir
        OutElec_dict["current_dir"] = self.current_dir
        if self.PWM is None:
            OutElec_dict["PWM"] = None
        else:
            OutElec_dict["PWM"] = self.PWM.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.eec is None:
            OutElec_dict["eec"] = None
        else:
            OutElec_dict["eec"] = self.eec.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutElec_dict["P_out"] = self.P_out
        OutElec_dict["Jrms"] = self.Jrms
        OutElec_dict["P_in"] = self.P_in
        OutElec_dict["Arms"] = self.Arms
        OutElec_dict["Erms"] = self.Erms
        # The class name is added to the dict for deserialisation purpose
        OutElec_dict["__class__"] = "OutElec"
        return OutElec_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.axes_dict is None:
            axes_dict_val = None
        else:
            axes_dict_val = dict()
            for key, obj in self.axes_dict.items():
                axes_dict_val[key] = obj.copy()
        if self.Is is None:
            Is_val = None
        else:
            Is_val = self.Is.copy()
        if self.Ir is None:
            Ir_val = None
        else:
            Ir_val = self.Ir.copy()
        logger_name_val = self.logger_name
        Pj_losses_val = self.Pj_losses
        if self.Us is None:
            Us_val = None
        else:
            Us_val = self.Us.copy()
        if self.internal is None:
            internal_val = None
        else:
            internal_val = self.internal.copy()
        if self.OP is None:
            OP_val = None
        else:
            OP_val = self.OP.copy()
        Pem_av_val = self.Pem_av
        Tem_av_val = self.Tem_av
        phase_dir_val = self.phase_dir
        current_dir_val = self.current_dir
        if self.PWM is None:
            PWM_val = None
        else:
            PWM_val = self.PWM.copy()
        if self.eec is None:
            eec_val = None
        else:
            eec_val = self.eec.copy()
        P_out_val = self.P_out
        Jrms_val = self.Jrms
        P_in_val = self.P_in
        Arms_val = self.Arms
        Erms_val = self.Erms
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            axes_dict=axes_dict_val,
            Is=Is_val,
            Ir=Ir_val,
            logger_name=logger_name_val,
            Pj_losses=Pj_losses_val,
            Us=Us_val,
            internal=internal_val,
            OP=OP_val,
            Pem_av=Pem_av_val,
            Tem_av=Tem_av_val,
            phase_dir=phase_dir_val,
            current_dir=current_dir_val,
            PWM=PWM_val,
            eec=eec_val,
            P_out=P_out_val,
            Jrms=Jrms_val,
            P_in=P_in_val,
            Arms=Arms_val,
            Erms=Erms_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.axes_dict = None
        self.Is = None
        self.Ir = None
        self.logger_name = None
        self.Pj_losses = None
        self.Us = None
        if self.internal is not None:
            self.internal._set_None()
        if self.OP is not None:
            self.OP._set_None()
        self.Pem_av = None
        self.Tem_av = None
        self.phase_dir = None
        self.current_dir = None
        if self.PWM is not None:
            self.PWM._set_None()
        if self.eec is not None:
            self.eec._set_None()
        self.P_out = None
        self.Jrms = None
        self.P_in = None
        self.Arms = None
        self.Erms = None

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
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
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
        doc="""Dict containing axes data used for Electrical

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
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
        doc="""Stator currents DataTime object

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
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
        doc="""Rotor currents as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
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
        doc="""Name of the logger to use

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
        doc="""Electrical Joule losses

        :Type: float
        """,
    )

    def _get_Us(self):
        """getter of Us"""
        return self._Us

    def _set_Us(self, value):
        """setter of Us"""
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
        doc="""Stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_internal(self):
        """getter of internal"""
        return self._internal

    def _set_internal(self, value):
        """setter of internal"""
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
                "pyleecan.Classes", value.get("__class__"), "internal"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutInternal = import_class("pyleecan.Classes", "OutInternal", "internal")
            value = OutInternal()
        check_var("internal", value, "OutInternal")
        self._internal = value

        if self._internal is not None:
            self._internal.parent = self

    internal = property(
        fget=_get_internal,
        fset=_set_internal,
        doc="""OutInternal object containg outputs related to a specific model

        :Type: OutInternal
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
        doc="""Operating Point

        :Type: OP
        """,
    )

    def _get_Pem_av(self):
        """getter of Pem_av"""
        return self._Pem_av

    def _set_Pem_av(self, value):
        """setter of Pem_av"""
        check_var("Pem_av", value, "float")
        self._Pem_av = value

    Pem_av = property(
        fget=_get_Pem_av,
        fset=_set_Pem_av,
        doc="""Average Electromagnetic power

        :Type: float
        """,
    )

    def _get_Tem_av(self):
        """getter of Tem_av"""
        return self._Tem_av

    def _set_Tem_av(self, value):
        """setter of Tem_av"""
        check_var("Tem_av", value, "float")
        self._Tem_av = value

    Tem_av = property(
        fget=_get_Tem_av,
        fset=_set_Tem_av,
        doc="""Average Electromagnetic torque

        :Type: float
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
        doc="""Rotation direction of the stator phases (phase_dir*(n-1)*pi/qs, default value given by PHASE_DIR_REF)

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
        doc="""Rotation direction of the stator currents (current_dir*2*pi*felec*time, default value given by CURRENT_DIR_REF)

        :Type: int
        :min: -1
        :max: 1
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
        doc="""Object to generate PWM signal

        :Type: ImportGenPWM
        """,
    )

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
        doc="""Electric Equivalent Circuit used for OP resolution

        :Type: EEC
        """,
    )

    def _get_P_out(self):
        """getter of P_out"""
        return self._P_out

    def _set_P_out(self, value):
        """setter of P_out"""
        check_var("P_out", value, "float")
        self._P_out = value

    P_out = property(
        fget=_get_P_out,
        fset=_set_P_out,
        doc="""Output power

        :Type: float
        """,
    )

    def _get_Jrms(self):
        """getter of Jrms"""
        return self._Jrms

    def _set_Jrms(self, value):
        """setter of Jrms"""
        check_var("Jrms", value, "float", Vmin=0)
        self._Jrms = value

    Jrms = property(
        fget=_get_Jrms,
        fset=_set_Jrms,
        doc="""RMS current density in slots

        :Type: float
        :min: 0
        """,
    )

    def _get_P_in(self):
        """getter of P_in"""
        return self._P_in

    def _set_P_in(self, value):
        """setter of P_in"""
        check_var("P_in", value, "float")
        self._P_in = value

    P_in = property(
        fget=_get_P_in,
        fset=_set_P_in,
        doc="""Input power

        :Type: float
        """,
    )

    def _get_Arms(self):
        """getter of Arms"""
        return self._Arms

    def _set_Arms(self, value):
        """setter of Arms"""
        check_var("Arms", value, "float")
        self._Arms = value

    Arms = property(
        fget=_get_Arms,
        fset=_set_Arms,
        doc="""RMS linear current density along airgap

        :Type: float
        """,
    )

    def _get_Erms(self):
        """getter of Erms"""
        return self._Erms

    def _set_Erms(self, value):
        """setter of Erms"""
        check_var("Erms", value, "float")
        self._Erms = value

    Erms = property(
        fget=_get_Erms,
        fset=_set_Erms,
        doc="""RMS back-emf

        :Type: float
        """,
    )
