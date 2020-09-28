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
from .Post import Post


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
        """Return a copy of the class"""
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
        postproc_list=list(),
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

        if machine == -1:
            machine = Machine()
        if input == -1:
            input = Input()
        if var_simu == -1:
            var_simu = VarSimu()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            name = obj.name
            desc = obj.desc
            machine = obj.machine
            input = obj.input
            logger_name = obj.logger_name
            var_simu = obj.var_simu
            postproc_list = obj.postproc_list
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
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
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
        elif isinstance(machine, str):
            from ..Functions.load import load

            machine = load(machine)
            # Check that the type is correct (including daughter)
            class_name = machine.__class__.__name__
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
            self.machine = machine
        else:
            self.machine = machine
        # input can be None, a Input object or a dict
        if isinstance(input, dict):
            # Check that the type is correct (including daughter)
            class_name = input.get("__class__")
            if class_name not in [
                "Input",
                "InputCurrent",
                "InputElec",
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
        elif isinstance(input, str):
            from ..Functions.load import load

            input = load(input)
            # Check that the type is correct (including daughter)
            class_name = input.__class__.__name__
            if class_name not in [
                "Input",
                "InputCurrent",
                "InputElec",
                "InputFlux",
                "InputForce",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for input"
                )
            self.input = input
        else:
            self.input = input
        self.logger_name = logger_name
        # var_simu can be None, a VarSimu object or a dict
        if isinstance(var_simu, dict):
            # Check that the type is correct (including daughter)
            class_name = var_simu.get("__class__")
            if class_name not in ["VarSimu", "VarLoad", "VarLoadCurrent", "VarParam"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for var_simu"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.var_simu = class_obj(init_dict=var_simu)
        elif isinstance(var_simu, str):
            from ..Functions.load import load

            var_simu = load(var_simu)
            # Check that the type is correct (including daughter)
            class_name = var_simu.__class__.__name__
            if class_name not in ["VarSimu", "VarLoad", "VarLoadCurrent", "VarParam"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for var_simu"
                )
            self.var_simu = var_simu
        else:
            self.var_simu = var_simu
        # postproc_list can be None or a list of Post object or a list of dict
        if type(postproc_list) is list:
            # Check if the list is only composed of Post
            if len(postproc_list) > 0 and all(
                isinstance(obj, Post) for obj in postproc_list
            ):
                # set the list to keep pointer reference
                self.postproc_list = postproc_list
            else:
                self.postproc_list = list()
                for obj in postproc_list:
                    if not isinstance(obj, dict):  # Default value
                        self.postproc_list.append(obj)
                    elif isinstance(obj, dict):
                        # Check that the type is correct (including daughter)
                        class_name = obj.get("__class__")
                        if class_name not in ["Post", "PostFunction", "PostMethod"]:
                            raise InitUnKnowClassError(
                                "Unknow class name "
                                + class_name
                                + " in init_dict for postproc_list"
                            )
                        # Dynamic import to call the correct constructor
                        module = __import__(
                            "pyleecan.Classes." + class_name, fromlist=[class_name]
                        )
                        class_obj = getattr(module, class_name)
                        self.postproc_list.append(class_obj(init_dict=obj))

        elif postproc_list is None:
            self.postproc_list = list()
        else:
            self.postproc_list = postproc_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

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
        if len(self.postproc_list) == 0:
            Simulation_str += "postproc_list = []" + linesep
        for ii in range(len(self.postproc_list)):
            tmp = (
                self.postproc_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            Simulation_str += (
                "postproc_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
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
        if other.postproc_list != self.postproc_list:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

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
        Simulation_dict["postproc_list"] = list()
        for obj in self.postproc_list:
            Simulation_dict["postproc_list"].append(obj.as_dict())
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
        for obj in self.postproc_list:
            obj._set_None()

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

    def _get_postproc_list(self):
        """getter of postproc_list"""
        for obj in self._postproc_list:
            if obj is not None:
                obj.parent = self
        return self._postproc_list

    def _set_postproc_list(self, value):
        """setter of postproc_list"""
        check_var("postproc_list", value, "[Post]")
        self._postproc_list = value

        for obj in self._postproc_list:
            if obj is not None:
                obj.parent = self

    postproc_list = property(
        fget=_get_postproc_list,
        fset=_set_postproc_list,
        doc=u"""List of postprocessings to run on Output after the simulation

        :Type: [Post]
        """,
    )
