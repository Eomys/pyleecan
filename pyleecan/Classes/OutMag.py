# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMag
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
    from ..Methods.Output.OutMag.store import store
except ImportError as error:
    store = error

try:
    from ..Methods.Output.OutMag.clean import clean
except ImportError as error:
    clean = error

try:
    from ..Methods.Output.OutMag.comp_emf import comp_emf
except ImportError as error:
    comp_emf = error

try:
    from ..Methods.Output.OutMag.get_demag import get_demag
except ImportError as error:
    get_demag = error

try:
    from ..Methods.Output.OutMag.comp_power import comp_power
except ImportError as error:
    comp_power = error


from ._check import InitUnKnowClassError
from .MeshSolution import MeshSolution
from .OutInternal import OutInternal


class OutMag(FrozenClass):
    """Gather the magnetic module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutMag.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMag method store: " + str(store))
            )
        )
    else:
        store = store
    # cf Methods.Output.OutMag.clean
    if isinstance(clean, ImportError):
        clean = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMag method clean: " + str(clean))
            )
        )
    else:
        clean = clean
    # cf Methods.Output.OutMag.comp_emf
    if isinstance(comp_emf, ImportError):
        comp_emf = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMag method comp_emf: " + str(comp_emf))
            )
        )
    else:
        comp_emf = comp_emf
    # cf Methods.Output.OutMag.get_demag
    if isinstance(get_demag, ImportError):
        get_demag = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMag method get_demag: " + str(get_demag))
            )
        )
    else:
        get_demag = get_demag
    # cf Methods.Output.OutMag.comp_power
    if isinstance(comp_power, ImportError):
        comp_power = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutMag method comp_power: " + str(comp_power))
            )
        )
    else:
        comp_power = comp_power
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Time=None,
        Angle=None,
        B=None,
        Tem=None,
        Tem_av=None,
        Tem_rip_norm=None,
        Tem_rip_pp=None,
        Phi_wind_stator=None,
        Phi_wind=None,
        emf=None,
        meshsolution=-1,
        logger_name="Pyleecan.Magnetics",
        internal=None,
        Rag=None,
        Pem_av=None,
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
            if "Time" in list(init_dict.keys()):
                Time = init_dict["Time"]
            if "Angle" in list(init_dict.keys()):
                Angle = init_dict["Angle"]
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "Tem" in list(init_dict.keys()):
                Tem = init_dict["Tem"]
            if "Tem_av" in list(init_dict.keys()):
                Tem_av = init_dict["Tem_av"]
            if "Tem_rip_norm" in list(init_dict.keys()):
                Tem_rip_norm = init_dict["Tem_rip_norm"]
            if "Tem_rip_pp" in list(init_dict.keys()):
                Tem_rip_pp = init_dict["Tem_rip_pp"]
            if "Phi_wind_stator" in list(init_dict.keys()):
                Phi_wind_stator = init_dict["Phi_wind_stator"]
            if "Phi_wind" in list(init_dict.keys()):
                Phi_wind = init_dict["Phi_wind"]
            if "emf" in list(init_dict.keys()):
                emf = init_dict["emf"]
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "internal" in list(init_dict.keys()):
                internal = init_dict["internal"]
            if "Rag" in list(init_dict.keys()):
                Rag = init_dict["Rag"]
            if "Pem_av" in list(init_dict.keys()):
                Pem_av = init_dict["Pem_av"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Time = Time
        self.Angle = Angle
        self.B = B
        self.Tem = Tem
        self.Tem_av = Tem_av
        self.Tem_rip_norm = Tem_rip_norm
        self.Tem_rip_pp = Tem_rip_pp
        self.Phi_wind_stator = Phi_wind_stator
        self.Phi_wind = Phi_wind
        self.emf = emf
        self.meshsolution = meshsolution
        self.logger_name = logger_name
        self.internal = internal
        self.Rag = Rag
        self.Pem_av = Pem_av

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutMag_str = ""
        if self.parent is None:
            OutMag_str += "parent = None " + linesep
        else:
            OutMag_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutMag_str += "Time = " + str(self.Time) + linesep + linesep
        OutMag_str += "Angle = " + str(self.Angle) + linesep + linesep
        OutMag_str += "B = " + str(self.B) + linesep + linesep
        OutMag_str += "Tem = " + str(self.Tem) + linesep + linesep
        OutMag_str += "Tem_av = " + str(self.Tem_av) + linesep
        OutMag_str += "Tem_rip_norm = " + str(self.Tem_rip_norm) + linesep
        OutMag_str += "Tem_rip_pp = " + str(self.Tem_rip_pp) + linesep
        OutMag_str += (
            "Phi_wind_stator = " + str(self.Phi_wind_stator) + linesep + linesep
        )
        OutMag_str += "Phi_wind = " + str(self.Phi_wind) + linesep + linesep
        OutMag_str += "emf = " + str(self.emf) + linesep + linesep
        if self.meshsolution is not None:
            tmp = (
                self.meshsolution.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OutMag_str += "meshsolution = " + tmp
        else:
            OutMag_str += "meshsolution = None" + linesep + linesep
        OutMag_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if self.internal is not None:
            tmp = self.internal.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutMag_str += "internal = " + tmp
        else:
            OutMag_str += "internal = None" + linesep + linesep
        OutMag_str += "Rag = " + str(self.Rag) + linesep
        OutMag_str += "Pem_av = " + str(self.Pem_av) + linesep
        return OutMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Time != self.Time:
            return False
        if other.Angle != self.Angle:
            return False
        if other.B != self.B:
            return False
        if other.Tem != self.Tem:
            return False
        if other.Tem_av != self.Tem_av:
            return False
        if other.Tem_rip_norm != self.Tem_rip_norm:
            return False
        if other.Tem_rip_pp != self.Tem_rip_pp:
            return False
        if other.Phi_wind_stator != self.Phi_wind_stator:
            return False
        if other.Phi_wind != self.Phi_wind:
            return False
        if other.emf != self.emf:
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.internal != self.internal:
            return False
        if other.Rag != self.Rag:
            return False
        if other.Pem_av != self.Pem_av:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.Time is None and self.Time is not None) or (
            other.Time is not None and self.Time is None
        ):
            diff_list.append(name + ".Time None mismatch")
        elif self.Time is not None:
            diff_list.extend(self.Time.compare(other.Time, name=name + ".Time"))
        if (other.Angle is None and self.Angle is not None) or (
            other.Angle is not None and self.Angle is None
        ):
            diff_list.append(name + ".Angle None mismatch")
        elif self.Angle is not None:
            diff_list.extend(self.Angle.compare(other.Angle, name=name + ".Angle"))
        if (other.B is None and self.B is not None) or (
            other.B is not None and self.B is None
        ):
            diff_list.append(name + ".B None mismatch")
        elif self.B is not None:
            diff_list.extend(self.B.compare(other.B, name=name + ".B"))
        if (other.Tem is None and self.Tem is not None) or (
            other.Tem is not None and self.Tem is None
        ):
            diff_list.append(name + ".Tem None mismatch")
        elif self.Tem is not None:
            diff_list.extend(self.Tem.compare(other.Tem, name=name + ".Tem"))
        if other._Tem_av != self._Tem_av:
            diff_list.append(name + ".Tem_av")
        if other._Tem_rip_norm != self._Tem_rip_norm:
            diff_list.append(name + ".Tem_rip_norm")
        if other._Tem_rip_pp != self._Tem_rip_pp:
            diff_list.append(name + ".Tem_rip_pp")
        if (other.Phi_wind_stator is None and self.Phi_wind_stator is not None) or (
            other.Phi_wind_stator is not None and self.Phi_wind_stator is None
        ):
            diff_list.append(name + ".Phi_wind_stator None mismatch")
        elif self.Phi_wind_stator is not None:
            diff_list.extend(
                self.Phi_wind_stator.compare(
                    other.Phi_wind_stator, name=name + ".Phi_wind_stator"
                )
            )
        if (other.Phi_wind is None and self.Phi_wind is not None) or (
            other.Phi_wind is not None and self.Phi_wind is None
        ):
            diff_list.append(name + ".Phi_wind None mismatch")
        elif self.Phi_wind is None:
            pass
        elif len(other.Phi_wind) != len(self.Phi_wind):
            diff_list.append("len(" + name + "Phi_wind)")
        else:
            for key in self.Phi_wind:
                diff_list.extend(
                    self.Phi_wind[key].compare(
                        other.Phi_wind[key], name=name + ".Phi_wind"
                    )
                )
        if (other.emf is None and self.emf is not None) or (
            other.emf is not None and self.emf is None
        ):
            diff_list.append(name + ".emf None mismatch")
        elif self.emf is not None:
            diff_list.extend(self.emf.compare(other.emf, name=name + ".emf"))
        if (other.meshsolution is None and self.meshsolution is not None) or (
            other.meshsolution is not None and self.meshsolution is None
        ):
            diff_list.append(name + ".meshsolution None mismatch")
        elif self.meshsolution is not None:
            diff_list.extend(
                self.meshsolution.compare(
                    other.meshsolution, name=name + ".meshsolution"
                )
            )
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if (other.internal is None and self.internal is not None) or (
            other.internal is not None and self.internal is None
        ):
            diff_list.append(name + ".internal None mismatch")
        elif self.internal is not None:
            diff_list.extend(
                self.internal.compare(other.internal, name=name + ".internal")
            )
        if other._Rag != self._Rag:
            diff_list.append(name + ".Rag")
        if other._Pem_av != self._Pem_av:
            diff_list.append(name + ".Pem_av")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Time)
        S += getsizeof(self.Angle)
        S += getsizeof(self.B)
        S += getsizeof(self.Tem)
        S += getsizeof(self.Tem_av)
        S += getsizeof(self.Tem_rip_norm)
        S += getsizeof(self.Tem_rip_pp)
        S += getsizeof(self.Phi_wind_stator)
        if self.Phi_wind is not None:
            for key, value in self.Phi_wind.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.emf)
        S += getsizeof(self.meshsolution)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.internal)
        S += getsizeof(self.Rag)
        S += getsizeof(self.Pem_av)
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

        OutMag_dict = dict()
        if self.Time is None:
            OutMag_dict["Time"] = None
        else:
            OutMag_dict["Time"] = self.Time.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Angle is None:
            OutMag_dict["Angle"] = None
        else:
            OutMag_dict["Angle"] = self.Angle.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.B is None:
            OutMag_dict["B"] = None
        else:
            OutMag_dict["B"] = self.B.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Tem is None:
            OutMag_dict["Tem"] = None
        else:
            OutMag_dict["Tem"] = self.Tem.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutMag_dict["Tem_av"] = self.Tem_av
        OutMag_dict["Tem_rip_norm"] = self.Tem_rip_norm
        OutMag_dict["Tem_rip_pp"] = self.Tem_rip_pp
        if self.Phi_wind_stator is None:
            OutMag_dict["Phi_wind_stator"] = None
        else:
            OutMag_dict["Phi_wind_stator"] = self.Phi_wind_stator.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Phi_wind is None:
            OutMag_dict["Phi_wind"] = None
        else:
            OutMag_dict["Phi_wind"] = dict()
            for key, obj in self.Phi_wind.items():
                if obj is not None:
                    OutMag_dict["Phi_wind"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutMag_dict["Phi_wind"][key] = None
        if self.emf is None:
            OutMag_dict["emf"] = None
        else:
            OutMag_dict["emf"] = self.emf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.meshsolution is None:
            OutMag_dict["meshsolution"] = None
        else:
            OutMag_dict["meshsolution"] = self.meshsolution.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutMag_dict["logger_name"] = self.logger_name
        if self.internal is None:
            OutMag_dict["internal"] = None
        else:
            OutMag_dict["internal"] = self.internal.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutMag_dict["Rag"] = self.Rag
        OutMag_dict["Pem_av"] = self.Pem_av
        # The class name is added to the dict for deserialisation purpose
        OutMag_dict["__class__"] = "OutMag"
        return OutMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Time = None
        self.Angle = None
        self.B = None
        self.Tem = None
        self.Tem_av = None
        self.Tem_rip_norm = None
        self.Tem_rip_pp = None
        self.Phi_wind_stator = None
        self.Phi_wind = None
        self.emf = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.logger_name = None
        if self.internal is not None:
            self.internal._set_None()
        self.Rag = None
        self.Pem_av = None

    def _get_Time(self):
        """getter of Time"""
        return self._Time

    def _set_Time(self, value):
        """setter of Time"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Time"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Data()
        check_var("Time", value, "Data")
        self._Time = value

    Time = property(
        fget=_get_Time,
        fset=_set_Time,
        doc=u"""Magnetic time Data object

        :Type: SciDataTool.Classes.DataND.Data
        """,
    )

    def _get_Angle(self):
        """getter of Angle"""
        return self._Angle

    def _set_Angle(self, value):
        """setter of Angle"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Angle"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Data()
        check_var("Angle", value, "Data")
        self._Angle = value

    Angle = property(
        fget=_get_Angle,
        fset=_set_Angle,
        doc=u"""Magnetic position Data object

        :Type: SciDataTool.Classes.DataND.Data
        """,
    )

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("SciDataTool.Classes", value.get("__class__"), "B")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VectorField()
        check_var("B", value, "VectorField")
        self._B = value

    B = property(
        fget=_get_B,
        fset=_set_B,
        doc=u"""Airgap flux density VectorField object

        :Type: SciDataTool.Classes.VectorField.VectorField
        """,
    )

    def _get_Tem(self):
        """getter of Tem"""
        return self._Tem

    def _set_Tem(self, value):
        """setter of Tem"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Tem"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Tem", value, "DataND")
        self._Tem = value

    Tem = property(
        fget=_get_Tem,
        fset=_set_Tem,
        doc=u"""Electromagnetic torque DataTime object

        :Type: SciDataTool.Classes.DataND.DataND
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
        doc=u"""Average Electromagnetic torque

        :Type: float
        """,
    )

    def _get_Tem_rip_norm(self):
        """getter of Tem_rip_norm"""
        return self._Tem_rip_norm

    def _set_Tem_rip_norm(self, value):
        """setter of Tem_rip_norm"""
        check_var("Tem_rip_norm", value, "float")
        self._Tem_rip_norm = value

    Tem_rip_norm = property(
        fget=_get_Tem_rip_norm,
        fset=_set_Tem_rip_norm,
        doc=u"""Peak to Peak Torque ripple normalized according to average torque (None if average torque=0)

        :Type: float
        """,
    )

    def _get_Tem_rip_pp(self):
        """getter of Tem_rip_pp"""
        return self._Tem_rip_pp

    def _set_Tem_rip_pp(self, value):
        """setter of Tem_rip_pp"""
        check_var("Tem_rip_pp", value, "float")
        self._Tem_rip_pp = value

    Tem_rip_pp = property(
        fget=_get_Tem_rip_pp,
        fset=_set_Tem_rip_pp,
        doc=u"""Peak to Peak Torque ripple

        :Type: float
        """,
    )

    def _get_Phi_wind_stator(self):
        """getter of Phi_wind_stator"""
        return self._Phi_wind_stator

    def _set_Phi_wind_stator(self, value):
        """setter of Phi_wind_stator"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Phi_wind_stator"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataTime()
        check_var("Phi_wind_stator", value, "DataTime")
        self._Phi_wind_stator = value

    Phi_wind_stator = property(
        fget=_get_Phi_wind_stator,
        fset=_set_Phi_wind_stator,
        doc=u"""Stator winding flux DataTime object

        :Type: SciDataTool.Classes.DataTime.DataTime
        """,
    )

    def _get_Phi_wind(self):
        """getter of Phi_wind"""
        if self._Phi_wind is not None:
            for key, obj in self._Phi_wind.items():
                if obj is not None:
                    obj.parent = self
        return self._Phi_wind

    def _set_Phi_wind(self, value):
        """setter of Phi_wind"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "Phi_wind"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("Phi_wind", value, "{DataTime}")
        self._Phi_wind = value

    Phi_wind = property(
        fget=_get_Phi_wind,
        fset=_set_Phi_wind,
        doc=u"""Dict of lamination winding fluxlinkage DataTime objects

        :Type: {SciDataTool.Classes.DataTime.DataTime}
        """,
    )

    def _get_emf(self):
        """getter of emf"""
        return self._emf

    def _set_emf(self, value):
        """setter of emf"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "emf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataTime()
        check_var("emf", value, "DataTime")
        self._emf = value

    emf = property(
        fget=_get_emf,
        fset=_set_emf,
        doc=u"""Electromotive force DataTime object

        :Type: SciDataTool.Classes.DataTime.DataTime
        """,
    )

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "meshsolution"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = MeshSolution()
        check_var("meshsolution", value, "MeshSolution")
        self._meshsolution = value

        if self._meshsolution is not None:
            self._meshsolution.parent = self

    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""FEA software mesh and solution

        :Type: MeshSolution
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

    def _get_Rag(self):
        """getter of Rag"""
        return self._Rag

    def _set_Rag(self, value):
        """setter of Rag"""
        check_var("Rag", value, "float")
        self._Rag = value

    Rag = property(
        fget=_get_Rag,
        fset=_set_Rag,
        doc=u"""Radius value for air-gap computation

        :Type: float
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
        doc=u"""Average Electromagnetic power

        :Type: float
        """,
    )
