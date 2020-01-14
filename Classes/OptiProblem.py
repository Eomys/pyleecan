# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiProblem.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Optimization.OptiProblem.eval_pb import eval_pb
except ImportError as error:
    eval_pb = error


from inspect import getsource
from cloudpickle import dumps, loads
from pyleecan.Classes.check import CheckTypeError
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Output import Output
from pyleecan.Classes.OptiDesignVar import OptiDesignVar
from pyleecan.Classes.OptiObjFunc import OptiObjFunc


class OptiProblem(FrozenClass):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

    # cf Methods.Optimization.OptiProblem.eval_pb
    if isinstance(eval_pb, ImportError):
        eval_pb = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiProblem method eval_pb: " + str(eval_pb))
            )
        )
    else:
        eval_pb = eval_pb
    # save method is available in all object
    save = save

    def __init__(
        self,
        output=-1,
        design_var=dict(),
        obj_func=dict(),
        eval_func=None,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if output == -1:
            output = Output()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict, ["output", "design_var", "obj_func", "eval_func"]
            )
            # Overwrite default value with init_dict content
            if "output" in list(init_dict.keys()):
                output = init_dict["output"]
            if "design_var" in list(init_dict.keys()):
                design_var = init_dict["design_var"]
            if "obj_func" in list(init_dict.keys()):
                obj_func = init_dict["obj_func"]
            if "eval_func" in list(init_dict.keys()):
                eval_func = init_dict["eval_func"]
        # Initialisation by argument
        self.parent = None
        # output can be None, a Output object or a dict
        if isinstance(output, dict):
            self.output = Output(init_dict=output)
        else:
            self.output = output
        # design_var can be None or a dict of OptiDesignVar object
        self.design_var = dict()
        if type(design_var) is dict:
            for key, obj in design_var.items():
                if isinstance(obj, dict):
                    self.design_var[key] = OptiDesignVar(init_dict=obj)
                else:
                    self.design_var[key] = obj
        elif design_var is None:
            self.design_var = dict()
        else:
            self.design_var = design_var  # Should raise an error
        # obj_func can be None or a dict of OptiObjFunc object
        self.obj_func = dict()
        if type(obj_func) is dict:
            for key, obj in obj_func.items():
                if isinstance(obj, dict):
                    self.obj_func[key] = OptiObjFunc(init_dict=obj)
                else:
                    self.obj_func[key] = obj
        elif obj_func is None:
            self.obj_func = dict()
        else:
            self.obj_func = obj_func  # Should raise an error
        self.eval_func = eval_func

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
            OptiProblem_str += (
                "output = " + str(self.output.as_dict()) + linesep + linesep
            )
        else:
            OptiProblem_str += "output = None" + linesep + linesep
        if len(self.design_var) == 0:
            OptiProblem_str += "design_var = dict()"
        for key, obj in self.design_var.items():
            OptiProblem_str += (
                "design_var["
                + key
                + "] = "
                + str(self.design_var[key].as_dict())
                + linesep
                + linesep
            )
        if len(self.obj_func) == 0:
            OptiProblem_str += "obj_func = dict()"
        for key, obj in self.obj_func.items():
            OptiProblem_str += (
                "obj_func["
                + key
                + "] = "
                + str(self.obj_func[key].as_dict())
                + linesep
                + linesep
            )
        if self._eval_func[1] is None:
            OptiProblem_str += "eval_func = " + str(self._eval_func[1])
        else:
            OptiProblem_str += "eval_func = " + linesep + str(self._eval_func[1])
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiProblem_dict = dict()
        if self.output is None:
            OptiProblem_dict["output"] = None
        else:
            OptiProblem_dict["output"] = self.output.as_dict()
        OptiProblem_dict["design_var"] = dict()
        for key, obj in self.design_var.items():
            OptiProblem_dict["design_var"][key] = obj.as_dict()
        OptiProblem_dict["obj_func"] = dict()
        for key, obj in self.obj_func.items():
            OptiProblem_dict["obj_func"][key] = obj.as_dict()
        if self.eval_func is None:
            OptiProblem_dict["eval_func"] = None
        else:
            OptiProblem_dict["eval_func"] = [
                dumps(self._eval_func[0]).decode("ISO-8859-2"),
                self._eval_func[1],
            ]
        # The class name is added to the dict fordeserialisation purpose
        OptiProblem_dict["__class__"] = "OptiProblem"
        return OptiProblem_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.output is not None:
            self.output._set_None()
        for key, obj in self.design_var.items():
            obj._set_None()
        for key, obj in self.obj_func.items():
            obj._set_None()
        self.eval_func = None

    def _get_output(self):
        """getter of output"""
        return self._output

    def _set_output(self, value):
        """setter of output"""
        check_var("output", value, "Output")
        self._output = value

        if self._output is not None:
            self._output.parent = self

    # Default output to define the default simulation.
    # Type : Output
    output = property(
        fget=_get_output,
        fset=_set_output,
        doc=u"""Default output to define the default simulation. """,
    )

    def _get_design_var(self):
        """getter of design_var"""
        for key, obj in self._design_var.items():
            if obj is not None:
                obj.parent = self
        return self._design_var

    def _set_design_var(self, value):
        """setter of design_var"""
        check_var("design_var", value, "{OptiDesignVar}")
        self._design_var = value

    # Dict of design variables
    # Type : {OptiDesignVar}
    design_var = property(
        fget=_get_design_var, fset=_set_design_var, doc=u"""Dict of design variables"""
    )

    def _get_obj_func(self):
        """getter of obj_func"""
        for key, obj in self._obj_func.items():
            if obj is not None:
                obj.parent = self
        return self._obj_func

    def _set_obj_func(self, value):
        """setter of obj_func"""
        check_var("obj_func", value, "{OptiObjFunc}")
        self._obj_func = value

    # Dict of objective functions
    # Type : {OptiObjFunc}
    obj_func = property(
        fget=_get_obj_func, fset=_set_obj_func, doc=u"""Dict of objective functions"""
    )

    def _get_eval_func(self):
        """getter of eval_func"""
        return self._eval_func[0]

    def _set_eval_func(self, value):
        """setter of eval_func"""
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

    # Function to evaluate before computing obj function and constraints
    # Type : function
    eval_func = property(
        fget=_get_eval_func,
        fset=_set_eval_func,
        doc=u"""Function to evaluate before computing obj function and constraints""",
    )
