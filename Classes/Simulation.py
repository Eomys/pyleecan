# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.MachineSync import MachineSync
from pyleecan.Classes.MachineAsync import MachineAsync
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.Input import Input
from pyleecan.Classes.InCurrent import InCurrent


class Simulation(FrozenClass):
    """Abstract class for the simulation"""

    VERSION = 1

    def __init__(self, name="", desc="", machine=-1, input=-1, init_dict=None):
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
            check_init_dict(init_dict, ["name", "desc", "machine", "input"])
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.desc = desc
        # machine can be None, a Machine object or a dict
        if isinstance(machine, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "MachineSync": MachineSync,
                "MachineAsync": MachineAsync,
                "MachineSCIM": MachineSCIM,
                "MachineDFIM": MachineDFIM,
                "MachineSIPMSM": MachineSIPMSM,
                "MachineIPMSM": MachineIPMSM,
                "MachineWRSM": MachineWRSM,
                "MachineSyRM": MachineSyRM,
                "Machine": Machine,
            }
            obj_class = machine.get("__class__")
            if obj_class is None:
                self.machine = Machine(init_dict=machine)
            elif obj_class in list(load_dict.keys()):
                self.machine = load_dict[obj_class](init_dict=machine)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for machine")
        else:
            self.machine = machine
        # input can be None, a Input object or a dict
        if isinstance(input, dict):
            # Call the correct constructor according to the dict
            load_dict = {"InCurrent": InCurrent, "Input": Input}
            obj_class = input.get("__class__")
            if obj_class is None:
                self.input = Input(init_dict=input)
            elif obj_class in list(load_dict.keys()):
                self.input = load_dict[obj_class](init_dict=input)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for input")
        else:
            self.input = input

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
        Simulation_str += "machine = " + str(self.machine.as_dict()) + linesep + linesep
        Simulation_str += "input = " + str(self.input.as_dict())
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
