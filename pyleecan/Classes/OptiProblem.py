# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiProblem.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiProblem
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError
from .Output import Output
from .OptiDesignVar import OptiDesignVar
from .DataKeeper import DataKeeper
from .OptiConstraint import OptiConstraint


class OptiProblem(FrozenClass):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

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
        output=-1,
        design_var=-1,
        obj_func=-1,
        eval_func=None,
        constraint=-1,
        preprocessing=None,
        datakeeper_list=-1,
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
            if "output" in list(init_dict.keys()):
                output = init_dict["output"]
            if "design_var" in list(init_dict.keys()):
                design_var = init_dict["design_var"]
            if "obj_func" in list(init_dict.keys()):
                obj_func = init_dict["obj_func"]
            if "eval_func" in list(init_dict.keys()):
                eval_func = init_dict["eval_func"]
            if "constraint" in list(init_dict.keys()):
                constraint = init_dict["constraint"]
            if "preprocessing" in list(init_dict.keys()):
                preprocessing = init_dict["preprocessing"]
            if "datakeeper_list" in list(init_dict.keys()):
                datakeeper_list = init_dict["datakeeper_list"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.output = output
        self.design_var = design_var
        self.obj_func = obj_func
        self.eval_func = eval_func
        self.constraint = constraint
        self.preprocessing = preprocessing
        self.datakeeper_list = datakeeper_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiProblem_str = ""
        if self.parent is None:
            OptiProblem_str += "parent = None " + linesep
        else:
            OptiProblem_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if self.output is not None:
            tmp = self.output.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OptiProblem_str += "output = " + tmp
        else:
            OptiProblem_str += "output = None" + linesep + linesep
        if len(self.design_var) == 0:
            OptiProblem_str += "design_var = []" + linesep
        for ii in range(len(self.design_var)):
            tmp = (
                self.design_var[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            OptiProblem_str += "design_var[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.obj_func) == 0:
            OptiProblem_str += "obj_func = []" + linesep
        for ii in range(len(self.obj_func)):
            tmp = self.obj_func[ii].__str__().replace(linesep, linesep + "\t") + linesep
            OptiProblem_str += "obj_func[" + str(ii) + "] =" + tmp + linesep + linesep
        if self._eval_func[1] is None:
            OptiProblem_str += "eval_func = " + str(self._eval_func[1])
        else:
            OptiProblem_str += (
                "eval_func = " + linesep + str(self._eval_func[1]) + linesep + linesep
            )
        if len(self.constraint) == 0:
            OptiProblem_str += "constraint = []" + linesep
        for ii in range(len(self.constraint)):
            tmp = (
                self.constraint[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            OptiProblem_str += "constraint[" + str(ii) + "] =" + tmp + linesep + linesep
        if self._preprocessing[1] is None:
            OptiProblem_str += "preprocessing = " + str(self._preprocessing[1])
        else:
            OptiProblem_str += (
                "preprocessing = "
                + linesep
                + str(self._preprocessing[1])
                + linesep
                + linesep
            )
        if len(self.datakeeper_list) == 0:
            OptiProblem_str += "datakeeper_list = []" + linesep
        for ii in range(len(self.datakeeper_list)):
            tmp = (
                self.datakeeper_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            OptiProblem_str += (
                "datakeeper_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return OptiProblem_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.output != self.output:
            return False
        if other.design_var != self.design_var:
            return False
        if other.obj_func != self.obj_func:
            return False
        if other.eval_func != self.eval_func:
            return False
        if other.constraint != self.constraint:
            return False
        if other.preprocessing != self.preprocessing:
            return False
        if other.datakeeper_list != self.datakeeper_list:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiProblem_dict = dict()
        if self.output is None:
            OptiProblem_dict["output"] = None
        else:
            OptiProblem_dict["output"] = self.output.as_dict()
        OptiProblem_dict["design_var"] = list()
        for obj in self.design_var:
            OptiProblem_dict["design_var"].append(obj.as_dict())
        OptiProblem_dict["obj_func"] = list()
        for obj in self.obj_func:
            OptiProblem_dict["obj_func"].append(obj.as_dict())
        if self.eval_func is None:
            OptiProblem_dict["eval_func"] = None
        else:
            OptiProblem_dict["eval_func"] = [
                dumps(self._eval_func[0]).decode("ISO-8859-2"),
                self._eval_func[1],
            ]
        OptiProblem_dict["constraint"] = list()
        for obj in self.constraint:
            OptiProblem_dict["constraint"].append(obj.as_dict())
        if self.preprocessing is None:
            OptiProblem_dict["preprocessing"] = None
        else:
            OptiProblem_dict["preprocessing"] = [
                dumps(self._preprocessing[0]).decode("ISO-8859-2"),
                self._preprocessing[1],
            ]
        OptiProblem_dict["datakeeper_list"] = list()
        for obj in self.datakeeper_list:
            OptiProblem_dict["datakeeper_list"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        OptiProblem_dict["__class__"] = "OptiProblem"
        return OptiProblem_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.output is not None:
            self.output._set_None()
        for obj in self.design_var:
            obj._set_None()
        for obj in self.obj_func:
            obj._set_None()
        self.eval_func = None
        for obj in self.constraint:
            obj._set_None()
        self.preprocessing = None
        for obj in self.datakeeper_list:
            obj._set_None()

    def _get_output(self):
        """getter of output"""
        return self._output

    def _set_output(self, value):
        """setter of output"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "output"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Output()
        check_var("output", value, "Output")
        self._output = value

        if self._output is not None:
            self._output.parent = self

    output = property(
        fget=_get_output,
        fset=_set_output,
        doc=u"""Default output to define the default simulation. 

        :Type: Output
        """,
    )

    def _get_design_var(self):
        """getter of design_var"""
        if self._design_var is not None:
            for obj in self._design_var:
                if obj is not None:
                    obj.parent = self
        return self._design_var

    def _set_design_var(self, value):
        """setter of design_var"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "design_var"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("design_var", value, "[OptiDesignVar]")
        self._design_var = value

    design_var = property(
        fget=_get_design_var,
        fset=_set_design_var,
        doc=u"""List of design variables

        :Type: [OptiDesignVar]
        """,
    )

    def _get_obj_func(self):
        """getter of obj_func"""
        if self._obj_func is not None:
            for obj in self._obj_func:
                if obj is not None:
                    obj.parent = self
        return self._obj_func

    def _set_obj_func(self, value):
        """setter of obj_func"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "obj_func"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("obj_func", value, "[DataKeeper]")
        self._obj_func = value

    obj_func = property(
        fget=_get_obj_func,
        fset=_set_obj_func,
        doc=u"""List of objective functions

        :Type: [DataKeeper]
        """,
    )

    def _get_eval_func(self):
        """getter of eval_func"""
        return self._eval_func[0]

    def _set_eval_func(self, value):
        """setter of eval_func"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "eval_func"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = function()
        try:
            check_var("eval_func", value, "list")
        except CheckTypeError:
            check_var("eval_func", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._eval_func = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._eval_func = [None, None]
        elif callable(value):
            self._eval_func = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    eval_func = property(
        fget=_get_eval_func,
        fset=_set_eval_func,
        doc=u"""Function to evaluate before computing obj function and constraints

        :Type: function
        """,
    )

    def _get_constraint(self):
        """getter of constraint"""
        if self._constraint is not None:
            for obj in self._constraint:
                if obj is not None:
                    obj.parent = self
        return self._constraint

    def _set_constraint(self, value):
        """setter of constraint"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "constraint"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("constraint", value, "[OptiConstraint]")
        self._constraint = value

    constraint = property(
        fget=_get_constraint,
        fset=_set_constraint,
        doc=u"""List containing the constraints 

        :Type: [OptiConstraint]
        """,
    )

    def _get_preprocessing(self):
        """getter of preprocessing"""
        return self._preprocessing[0]

    def _set_preprocessing(self, value):
        """setter of preprocessing"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "preprocessing"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = function()
        try:
            check_var("preprocessing", value, "list")
        except CheckTypeError:
            check_var("preprocessing", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._preprocessing = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._preprocessing = [None, None]
        elif callable(value):
            self._preprocessing = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    preprocessing = property(
        fget=_get_preprocessing,
        fset=_set_preprocessing,
        doc=u"""Function to execute a preprocessing on the simulation right before it is run.

        :Type: function
        """,
    )

    def _get_datakeeper_list(self):
        """getter of datakeeper_list"""
        if self._datakeeper_list is not None:
            for obj in self._datakeeper_list:
                if obj is not None:
                    obj.parent = self
        return self._datakeeper_list

    def _set_datakeeper_list(self, value):
        """setter of datakeeper_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "datakeeper_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("datakeeper_list", value, "[DataKeeper]")
        self._datakeeper_list = value

    datakeeper_list = property(
        fget=_get_datakeeper_list,
        fset=_set_datakeeper_list,
        doc=u"""List of DataKeepers to run on every output

        :Type: [DataKeeper]
        """,
    )
