# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMag
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from numpy import array, array_equal
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from SciDataTool.Classes.VectorField import VectorField
except ImportError:
    VectorField = ImportError
try:
    from SciDataTool.Classes.DataND import DataND
except ImportError:
    DataND = ImportError
from ._check import InitUnKnowClassError
from .MeshSolution import MeshSolution


class OutMag(FrozenClass):
    """Gather the magnetic module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=None,
        Na_tot=None,
        B=None,
        Tem=None,
        Tem_av=None,
        Tem_rip_norm=None,
        Tem_rip_pp=None,
        Phi_wind_stator=None,
        emf=None,
        meshsolution=-1,
        FEMM_dict=None,
        logger_name="Pyleecan.OutMag",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if meshsolution == -1:
            meshsolution = MeshSolution()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Na_tot = obj.Na_tot
            B = obj.B
            Tem = obj.Tem
            Tem_av = obj.Tem_av
            Tem_rip_norm = obj.Tem_rip_norm
            Tem_rip_pp = obj.Tem_rip_pp
            Phi_wind_stator = obj.Phi_wind_stator
            emf = obj.emf
            meshsolution = obj.meshsolution
            FEMM_dict = obj.FEMM_dict
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
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
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot
        # Check if the type VectorField has been imported with success
        if isinstance(VectorField, ImportError):
            raise ImportError("Unknown type VectorField please install SciDataTool")
        self.B = B
        # Check if the type DataND has been imported with success
        if isinstance(DataND, ImportError):
            raise ImportError("Unknown type DataND please install SciDataTool")
        self.Tem = Tem
        self.Tem_av = Tem_av
        self.Tem_rip_norm = Tem_rip_norm
        self.Tem_rip_pp = Tem_rip_pp
        # Phi_wind_stator can be None, a ndarray or a list
        set_array(self, "Phi_wind_stator", Phi_wind_stator)
        # emf can be None, a ndarray or a list
        set_array(self, "emf", emf)
        # meshsolution can be None, a MeshSolution object or a dict
        if isinstance(meshsolution, dict):
            self.meshsolution = MeshSolution(init_dict=meshsolution)
        elif isinstance(meshsolution, str):
            from ..Functions.load import load

            self.meshsolution = load(meshsolution)
        else:
            self.meshsolution = meshsolution
        self.FEMM_dict = FEMM_dict
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutMag_str = ""
        if self.parent is None:
            OutMag_str += "parent = None " + linesep
        else:
            OutMag_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutMag_str += (
            "time = "
            + linesep
            + str(self.time).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutMag_str += (
            "angle = "
            + linesep
            + str(self.angle).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutMag_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutMag_str += "Na_tot = " + str(self.Na_tot) + linesep
        OutMag_str += "B = " + str(self.B) + linesep + linesep
        OutMag_str += "Tem = " + str(self.Tem) + linesep + linesep
        OutMag_str += "Tem_av = " + str(self.Tem_av) + linesep
        OutMag_str += "Tem_rip_norm = " + str(self.Tem_rip_norm) + linesep
        OutMag_str += "Tem_rip_pp = " + str(self.Tem_rip_pp) + linesep
        OutMag_str += (
            "Phi_wind_stator = "
            + linesep
            + str(self.Phi_wind_stator).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutMag_str += (
            "emf = "
            + linesep
            + str(self.emf).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        if self.meshsolution is not None:
            tmp = (
                self.meshsolution.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OutMag_str += "meshsolution = " + tmp
        else:
            OutMag_str += "meshsolution = None" + linesep + linesep
        OutMag_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        OutMag_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OutMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if not array_equal(other.angle, self.angle):
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Na_tot != self.Na_tot:
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
        if not array_equal(other.Phi_wind_stator, self.Phi_wind_stator):
            return False
        if not array_equal(other.emf, self.emf):
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        OutMag_dict = dict()
        if self.time is None:
            OutMag_dict["time"] = None
        else:
            OutMag_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutMag_dict["angle"] = None
        else:
            OutMag_dict["angle"] = self.angle.tolist()
        OutMag_dict["Nt_tot"] = self.Nt_tot
        OutMag_dict["Na_tot"] = self.Na_tot
        if self.B is None:
            OutMag_dict["B"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutMag_dict["B"] = {
                "__class__": str(type(self._B)),
                "__repr__": str(self._B.__repr__()),
                "serialized": dumps(self._B).decode("ISO-8859-2"),
            }
        if self.Tem is None:
            OutMag_dict["Tem"] = None
        else:  # Store serialized data (using cloudpickle) and str to read it in json save files
            OutMag_dict["Tem"] = {
                "__class__": str(type(self._Tem)),
                "__repr__": str(self._Tem.__repr__()),
                "serialized": dumps(self._Tem).decode("ISO-8859-2"),
            }
        OutMag_dict["Tem_av"] = self.Tem_av
        OutMag_dict["Tem_rip_norm"] = self.Tem_rip_norm
        OutMag_dict["Tem_rip_pp"] = self.Tem_rip_pp
        if self.Phi_wind_stator is None:
            OutMag_dict["Phi_wind_stator"] = None
        else:
            OutMag_dict["Phi_wind_stator"] = self.Phi_wind_stator.tolist()
        if self.emf is None:
            OutMag_dict["emf"] = None
        else:
            OutMag_dict["emf"] = self.emf.tolist()
        if self.meshsolution is None:
            OutMag_dict["meshsolution"] = None
        else:
            OutMag_dict["meshsolution"] = self.meshsolution.as_dict()
        OutMag_dict["FEMM_dict"] = self.FEMM_dict
        OutMag_dict["logger_name"] = self.logger_name
        # The class name is added to the dict fordeserialisation purpose
        OutMag_dict["__class__"] = "OutMag"
        return OutMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Nt_tot = None
        self.Na_tot = None
        self.B = None
        self.Tem = None
        self.Tem_av = None
        self.Tem_rip_norm = None
        self.Tem_rip_pp = None
        self.Phi_wind_stator = None
        self.emf = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.FEMM_dict = None
        self.logger_name = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("time", value, "ndarray")
        self._time = value

    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Magnetic time vector (no symmetry)

        :Type: ndarray
        """,
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle", value, "ndarray")
        self._angle = value

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Magnetic position vector (no symmetry)

        :Type: ndarray
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Length of the time vector

        :Type: int
        """,
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int")
        self._Na_tot = value

    Na_tot = property(
        fget=_get_Na_tot,
        fset=_set_Na_tot,
        doc=u"""Length of the angle vector

        :Type: int
        """,
    )

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        try:  # Check the type
            check_var("B", value, "dict")
        except CheckTypeError:
            check_var("B", value, "SciDataTool.Classes.VectorField.VectorField")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._B = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._B = value

    B = property(
        fget=_get_B,
        fset=_set_B,
        doc=u"""Airgap flux density components

        :Type: SciDataTool.Classes.VectorField.VectorField
        """,
    )

    def _get_Tem(self):
        """getter of Tem"""
        return self._Tem

    def _set_Tem(self, value):
        """setter of Tem"""
        try:  # Check the type
            check_var("Tem", value, "dict")
        except CheckTypeError:
            check_var("Tem", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if (
            type(value) == dict
        ):  # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Tem = loads(value["serialized"].encode("ISO-8859-2"))
        else:
            self._Tem = value

    Tem = property(
        fget=_get_Tem,
        fset=_set_Tem,
        doc=u"""Electromagnetic torque

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
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Phi_wind_stator", value, "ndarray")
        self._Phi_wind_stator = value

    Phi_wind_stator = property(
        fget=_get_Phi_wind_stator,
        fset=_set_Phi_wind_stator,
        doc=u"""Stator winding flux

        :Type: ndarray
        """,
    )

    def _get_emf(self):
        """getter of emf"""
        return self._emf

    def _set_emf(self, value):
        """setter of emf"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("emf", value, "ndarray")
        self._emf = value

    emf = property(
        fget=_get_emf,
        fset=_set_emf,
        doc=u"""Electromotive force

        :Type: ndarray
        """,
    )

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
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

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    FEMM_dict = property(
        fget=_get_FEMM_dict,
        fset=_set_FEMM_dict,
        doc=u"""Dictionnary containing the main FEMM parameter

        :Type: dict
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
