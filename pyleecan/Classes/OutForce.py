# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutForce.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutForce
"""

from os import linesep
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
    from ..Methods.Output.OutForce.store import store
except ImportError as error:
    store = error


from ._check import InitUnKnowClassError


class OutForce(FrozenClass):
    """Gather the structural module outputs"""

    VERSION = 1

    # cf Methods.Output.OutForce.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutForce method store: " + str(store))
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
        Time=None,
        Angle=None,
        AGSF=None,
        logger_name="Pyleecan.OutForce",
        Rag=None,
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
            if "AGSF" in list(init_dict.keys()):
                AGSF = init_dict["AGSF"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Rag" in list(init_dict.keys()):
                Rag = init_dict["Rag"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Time = Time
        self.Angle = Angle
        self.AGSF = AGSF
        self.logger_name = logger_name
        self.Rag = Rag

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutForce_str = ""
        if self.parent is None:
            OutForce_str += "parent = None " + linesep
        else:
            OutForce_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutForce_str += "Time = " + str(self.Time) + linesep + linesep
        OutForce_str += "Angle = " + str(self.Angle) + linesep + linesep
        OutForce_str += "AGSF = " + str(self.AGSF) + linesep + linesep
        OutForce_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutForce_str += "Rag = " + str(self.Rag) + linesep
        return OutForce_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Time != self.Time:
            return False
        if other.Angle != self.Angle:
            return False
        if other.AGSF != self.AGSF:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.Rag != self.Rag:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        OutForce_dict = dict()
        if self.Time is None:
            OutForce_dict["Time"] = None
        else:
            OutForce_dict["Time"] = self.Time.as_dict()
        if self.Angle is None:
            OutForce_dict["Angle"] = None
        else:
            OutForce_dict["Angle"] = self.Angle.as_dict()
        if self.AGSF is None:
            OutForce_dict["AGSF"] = None
        else:
            OutForce_dict["AGSF"] = self.AGSF.as_dict()
        OutForce_dict["logger_name"] = self.logger_name
        OutForce_dict["Rag"] = self.Rag
        # The class name is added to the dict for deserialisation purpose
        OutForce_dict["__class__"] = "OutForce"
        return OutForce_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Time = None
        self.Angle = None
        self.AGSF = None
        self.logger_name = None
        self.Rag = None

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
        doc=u"""Force time Data object

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
        doc=u"""Force position Data object

        :Type: SciDataTool.Classes.DataND.Data
        """,
    )

    def _get_AGSF(self):
        """getter of AGSF"""
        return self._AGSF

    def _set_AGSF(self, value):
        """setter of AGSF"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "AGSF"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VectorField()
        check_var("AGSF", value, "VectorField")
        self._AGSF = value

    AGSF = property(
        fget=_get_AGSF,
        fset=_set_AGSF,
        doc=u"""Air Gap Surface Force (mainly computed with Maxwell stress tensor)

        :Type: SciDataTool.Classes.VectorField.VectorField
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
