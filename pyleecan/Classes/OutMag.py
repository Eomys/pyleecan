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
        emf=None,
        meshsolution=-1,
        logger_name="Pyleecan.OutMag",
        internal=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
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
            if "emf" in list(init_dict.keys()):
                emf = init_dict["emf"]
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "internal" in list(init_dict.keys()):
                internal = init_dict["internal"]
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
        self.emf = emf
        self.meshsolution = meshsolution
        self.logger_name = logger_name
        self.internal = internal

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
        if other.emf != self.emf:
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.internal != self.internal:
            return False
        return True

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
        S += getsizeof(self.emf)
        S += getsizeof(self.meshsolution)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.internal)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        OutMag_dict = dict()
        if self.Time is None:
            OutMag_dict["Time"] = None
        else:
            OutMag_dict["Time"] = self.Time.as_dict()
        if self.Angle is None:
            OutMag_dict["Angle"] = None
        else:
            OutMag_dict["Angle"] = self.Angle.as_dict()
        if self.B is None:
            OutMag_dict["B"] = None
        else:
            OutMag_dict["B"] = self.B.as_dict()
        if self.Tem is None:
            OutMag_dict["Tem"] = None
        else:
            OutMag_dict["Tem"] = self.Tem.as_dict()
        OutMag_dict["Tem_av"] = self.Tem_av
        OutMag_dict["Tem_rip_norm"] = self.Tem_rip_norm
        OutMag_dict["Tem_rip_pp"] = self.Tem_rip_pp
        if self.Phi_wind_stator is None:
            OutMag_dict["Phi_wind_stator"] = None
        else:
            OutMag_dict["Phi_wind_stator"] = self.Phi_wind_stator.as_dict()
        if self.emf is None:
            OutMag_dict["emf"] = None
        else:
            OutMag_dict["emf"] = self.emf.as_dict()
        if self.meshsolution is None:
            OutMag_dict["meshsolution"] = None
        else:
            OutMag_dict["meshsolution"] = self.meshsolution.as_dict()
        OutMag_dict["logger_name"] = self.logger_name
        if self.internal is None:
            OutMag_dict["internal"] = None
        else:
            OutMag_dict["internal"] = self.internal.as_dict()
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
        self.emf = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.logger_name = None
        if self.internal is not None:
            self.internal._set_None()

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
