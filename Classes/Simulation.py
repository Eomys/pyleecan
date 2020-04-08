# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Simulation/Simulation.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ..Classes._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Classes._frozen import FrozenClass

from ..Classes._check import InitUnKnowClassError
from ..Classes.Machine import Machine
from ..Classes.Input import Input


class Simulation(FrozenClass):
    """Abstract class for the simulation"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        desc="",
        machine=-1,
        input=-1,
        logger_name="Pyleecan.Simulation",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if machine == -1:
            machine = Machine()
        if input == -1:
            input = Input()
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
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.desc = desc
        # machine can be None, a Machine object or a dict
        if isinstance(machine, dict):
            # Check that the type is correct (including daughter)
            class_name = machine.get("__class__")
            if class_name not in [
                "Machine",
                "MachineAsync",
                "MachineDFIM",
                "MachineIPMSM",
                "MachineSCIM",
                "MachineSIPMSM",
                "MachineSRM",
                "MachineSyRM",
                "MachineSync",
                "MachineUD",
                "MachineWRSM",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for machine"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.machine = class_obj(init_dict=machine)
        else:
            self.machine = machine
        # input can be None, a Input object or a dict
        if isinstance(input, dict):
            # Check that the type is correct (including daughter)
            class_name = input.get("__class__")
            if class_name not in [
                "Input",
                "InputCurrent",
                "InputCurrentDQ",
                "InputFlux",
                "InputForce",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for input"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.input = class_obj(init_dict=input)
        else:
            self.input = input
        self.logger_name = logger_name

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

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # Name of the simulation
    # Type : str
    name = property(fget=_get_name, fset=_set_name, doc=u"""Name of the simulation""")

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    # Simulation description
    # Type : str
    desc = property(fget=_get_desc, fset=_set_desc, doc=u"""Simulation description""")

    def _get_machine(self):
        """getter of machine"""
        return self._machine

    def _set_machine(self, value):
        """setter of machine"""
        check_var("machine", value, "Machine")
        self._machine = value

        if self._machine is not None:
            self._machine.parent = self

    # Machine to simulate
    # Type : Machine
    machine = property(
        fget=_get_machine, fset=_set_machine, doc=u"""Machine to simulate"""
    )

    def _get_input(self):
        """getter of input"""
        return self._input

    def _set_input(self, value):
        """setter of input"""
        check_var("input", value, "Input")
        self._input = value

        if self._input is not None:
            self._input.parent = self

    # Input of the simulation
    # Type : Input
    input = property(
        fget=_get_input, fset=_set_input, doc=u"""Input of the simulation"""
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    # Name of the logger to use
    # Type : str
    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use""",
    )
