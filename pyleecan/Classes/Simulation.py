# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Simulation.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Simulation
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Simulation.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .Machine import Machine
from .Input import Input
from .VarSimu import VarSimu


class Simulation(FrozenClass):
    """Abstract class for the simulation"""

    VERSION = 1

    # cf Methods.Simulation.Simulation.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Simulation method run: " + str(run))
            )
        )
    else:
        run = run
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
        name="",
        desc="",
        machine=-1,
        input=-1,
        logger_name="Pyleecan.Simulation",
        var_simu=None,
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
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "var_simu" in list(init_dict.keys()):
                var_simu = init_dict["var_simu"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.desc = desc
        self.machine = machine
        self.input = input
        self.logger_name = logger_name
        self.var_simu = var_simu

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Simulation_str = ""
        if self.parent is None:
            Simulation_str += "parent = None " + linesep
        else:
            Simulation_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Simulation_str += 'name = "' + str(self.name) + '"' + linesep
        Simulation_str += 'desc = "' + str(self.desc) + '"' + linesep
        if self.machine is not None:
            tmp = self.machine.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "machine = " + tmp
        else:
            Simulation_str += "machine = None" + linesep + linesep
        if self.input is not None:
            tmp = self.input.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "input = " + tmp
        else:
            Simulation_str += "input = None" + linesep + linesep
        Simulation_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if self.var_simu is not None:
            tmp = self.var_simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simulation_str += "var_simu = " + tmp
        else:
            Simulation_str += "var_simu = None" + linesep + linesep
        return Simulation_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        if other.machine != self.machine:
            return False
        if other.input != self.input:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.var_simu != self.var_simu:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Simulation_dict = dict()
        Simulation_dict["name"] = self.name
        Simulation_dict["desc"] = self.desc
        if self.machine is None:
            Simulation_dict["machine"] = None
        else:
            Simulation_dict["machine"] = self.machine.as_dict()
        if self.input is None:
            Simulation_dict["input"] = None
        else:
            Simulation_dict["input"] = self.input.as_dict()
        Simulation_dict["logger_name"] = self.logger_name
        if self.var_simu is None:
            Simulation_dict["var_simu"] = None
        else:
            Simulation_dict["var_simu"] = self.var_simu.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Simulation_dict["__class__"] = "Simulation"
        return Simulation_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.desc = None
        if self.machine is not None:
            self.machine._set_None()
        if self.input is not None:
            self.input._set_None()
        self.logger_name = None
        if self.var_simu is not None:
            self.var_simu._set_None()

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the simulation

        :Type: str
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""Simulation description

        :Type: str
        """,
    )

    def _get_machine(self):
        """getter of machine"""
        return self._machine

    def _set_machine(self, value):
        """setter of machine"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "machine"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Machine()
        check_var("machine", value, "Machine")
        self._machine = value

        if self._machine is not None:
            self._machine.parent = self

    machine = property(
        fget=_get_machine,
        fset=_set_machine,
        doc=u"""Machine to simulate

        :Type: Machine
        """,
    )

    def _get_input(self):
        """getter of input"""
        return self._input

    def _set_input(self, value):
        """setter of input"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "input"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Input()
        check_var("input", value, "Input")
        self._input = value

        if self._input is not None:
            self._input.parent = self

    input = property(
        fget=_get_input,
        fset=_set_input,
        doc=u"""Input of the simulation

        :Type: Input
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

    def _get_var_simu(self):
        """getter of var_simu"""
        return self._var_simu

    def _set_var_simu(self, value):
        """setter of var_simu"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "var_simu"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = VarSimu()
        check_var("var_simu", value, "VarSimu")
        self._var_simu = value

        if self._var_simu is not None:
            self._var_simu.parent = self

    var_simu = property(
        fget=_get_var_simu,
        fset=_set_var_simu,
        doc=u"""Multi-simulation definition

        :Type: VarSimu
        """,
    )
