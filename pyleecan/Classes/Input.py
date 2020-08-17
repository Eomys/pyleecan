# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Input.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Input
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Input.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.Input.comp_time import comp_time
except ImportError as error:
    comp_time = error


from ._check import InitUnKnowClassError
from .Import import Import


class Input(FrozenClass):
    """Starting data of the simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Input.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use Input method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.Input.comp_time
    if isinstance(comp_time, ImportError):
        comp_time = property(
            fget=lambda x: raise_(
                ImportError("Can't use Input method comp_time: " + str(comp_time))
            )
        )
    else:
        comp_time = comp_time
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
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

        if time == -1:
            time = Import()
        if angle == -1:
            angle = Import()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Nrev = obj.Nrev
            Na_tot = obj.Na_tot
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
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
        # Initialisation by argument
        self.parent = None
        # time can be None, a Import object or a dict
        if isinstance(time, dict):
            # Check that the type is correct (including daughter)
            class_name = time.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for time"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.time = class_obj(init_dict=time)
        elif isinstance(time, str):
            from ..Functions.load import load

            time = load(time)
            # Check that the type is correct (including daughter)
            class_name = time.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for time"
                )
            self.time = time
        else:
            self.time = time
        # angle can be None, a Import object or a dict
        if isinstance(angle, dict):
            # Check that the type is correct (including daughter)
            class_name = angle.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.angle = class_obj(init_dict=angle)
        elif isinstance(angle, str):
            from ..Functions.load import load

            angle = load(angle)
            # Check that the type is correct (including daughter)
            class_name = angle.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle"
                )
            self.angle = angle
        else:
            self.angle = angle
        self.Nt_tot = Nt_tot
        self.Nrev = Nrev
        self.Na_tot = Na_tot

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Input_str = ""
        if self.parent is None:
            Input_str += "parent = None " + linesep
        else:
            Input_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.time is not None:
            tmp = self.time.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "time = " + tmp
        else:
            Input_str += "time = None" + linesep + linesep
        if self.angle is not None:
            tmp = self.angle.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Input_str += "angle = " + tmp
        else:
            Input_str += "angle = None" + linesep + linesep
        Input_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        Input_str += "Nrev = " + str(self.Nrev) + linesep
        Input_str += "Na_tot = " + str(self.Na_tot) + linesep
        return Input_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Nrev != self.Nrev:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Input_dict = dict()
        if self.time is None:
            Input_dict["time"] = None
        else:
            Input_dict["time"] = self.time.as_dict()
        if self.angle is None:
            Input_dict["angle"] = None
        else:
            Input_dict["angle"] = self.angle.as_dict()
        Input_dict["Nt_tot"] = self.Nt_tot
        Input_dict["Nrev"] = self.Nrev
        Input_dict["Na_tot"] = self.Na_tot
        # The class name is added to the dict fordeserialisation purpose
        Input_dict["__class__"] = "Input"
        return Input_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        self.Nt_tot = None
        self.Nrev = None
        self.Na_tot = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        check_var("time", value, "Import")
        self._time = value

        if self._time is not None:
            self._time.parent = self

    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry) to import

        :Type: Import
        """,
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        check_var("angle", value, "Import")
        self._angle = value

        if self._angle is not None:
            self._angle.parent = self

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry) to import

        :Type: Import
        """,
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int", Vmin=1)
        self._Nt_tot = value

    # Time discretization
    # Type : int, min = 1
    Nt_tot = property(
        fget=_get_Nt_tot, fset=_set_Nt_tot, doc=u"""Time discretization"""
    )

    def _get_Nrev(self):
        """getter of Nrev"""
        return self._Nrev

    def _set_Nrev(self, value):
        """setter of Nrev"""
        check_var("Nrev", value, "float", Vmin=0)
        self._Nrev = value

    # Number of rotor revolution (to compute the final time)
    # Type : float, min = 0
    Nrev = property(
        fget=_get_Nrev,
        fset=_set_Nrev,
        doc=u"""Number of rotor revolution (to compute the final time)""",
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int", Vmin=1)
        self._Na_tot = value

    # Angular discretization
    # Type : int, min = 1
    Na_tot = property(
        fget=_get_Na_tot, fset=_set_Na_tot, doc=u"""Angular discretization"""
    )
