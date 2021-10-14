# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiProblem.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiProblem
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

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError
from .Simulation import Simulation
from .OptiDesignVar import OptiDesignVar
from .OptiObjective import OptiObjective
from .OptiConstraint import OptiConstraint
from .DataKeeper import DataKeeper


class OptiProblem(FrozenClass):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        simu=-1,
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
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "simu" in list(init_dict.keys()):
                simu = init_dict["simu"]
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
        self.simu = simu
        self.design_var = design_var
        self.obj_func = obj_func
        self.eval_func = eval_func
        self.constraint = constraint
        self.preprocessing = preprocessing
        self.datakeeper_list = datakeeper_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiProblem_str = ""
        if self.parent is None:
            OptiProblem_str += "parent = None " + linesep
        else:
            OptiProblem_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if self.simu is not None:
            tmp = self.simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OptiProblem_str += "simu = " + tmp
        else:
            OptiProblem_str += "simu = None" + linesep + linesep
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
        if self._eval_func_str is not None:
            OptiProblem_str += "eval_func = " + self._eval_func_str + linesep
        elif self._eval_func_func is not None:
            OptiProblem_str += "eval_func = " + str(self._eval_func_func) + linesep
        else:
            OptiProblem_str += "eval_func = None" + linesep + linesep
        if len(self.constraint) == 0:
            OptiProblem_str += "constraint = []" + linesep
        for ii in range(len(self.constraint)):
            tmp = (
                self.constraint[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            OptiProblem_str += "constraint[" + str(ii) + "] =" + tmp + linesep + linesep
        if self._preprocessing_str is not None:
            OptiProblem_str += "preprocessing = " + self._preprocessing_str + linesep
        elif self._preprocessing_func is not None:
            OptiProblem_str += (
                "preprocessing = " + str(self._preprocessing_func) + linesep
            )
        else:
            OptiProblem_str += "preprocessing = None" + linesep + linesep
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
        if other.simu != self.simu:
            return False
        if other.design_var != self.design_var:
            return False
        if other.obj_func != self.obj_func:
            return False
        if other._eval_func_str != self._eval_func_str:
            return False
        if other.constraint != self.constraint:
            return False
        if other._preprocessing_str != self._preprocessing_str:
            return False
        if other.datakeeper_list != self.datakeeper_list:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.simu is None and self.simu is not None) or (
            other.simu is not None and self.simu is None
        ):
            diff_list.append(name + ".simu None mismatch")
        elif self.simu is not None:
            diff_list.extend(self.simu.compare(other.simu, name=name + ".simu"))
        if (other.design_var is None and self.design_var is not None) or (
            other.design_var is not None and self.design_var is None
        ):
            diff_list.append(name + ".design_var None mismatch")
        elif self.design_var is None:
            pass
        elif len(other.design_var) != len(self.design_var):
            diff_list.append("len(" + name + ".design_var)")
        else:
            for ii in range(len(other.design_var)):
                diff_list.extend(
                    self.design_var[ii].compare(
                        other.design_var[ii], name=name + ".design_var[" + str(ii) + "]"
                    )
                )
        if (other.obj_func is None and self.obj_func is not None) or (
            other.obj_func is not None and self.obj_func is None
        ):
            diff_list.append(name + ".obj_func None mismatch")
        elif self.obj_func is None:
            pass
        elif len(other.obj_func) != len(self.obj_func):
            diff_list.append("len(" + name + ".obj_func)")
        else:
            for ii in range(len(other.obj_func)):
                diff_list.extend(
                    self.obj_func[ii].compare(
                        other.obj_func[ii], name=name + ".obj_func[" + str(ii) + "]"
                    )
                )
        if other._eval_func_str != self._eval_func_str:
            diff_list.append(name + ".eval_func")
        if (other.constraint is None and self.constraint is not None) or (
            other.constraint is not None and self.constraint is None
        ):
            diff_list.append(name + ".constraint None mismatch")
        elif self.constraint is None:
            pass
        elif len(other.constraint) != len(self.constraint):
            diff_list.append("len(" + name + ".constraint)")
        else:
            for ii in range(len(other.constraint)):
                diff_list.extend(
                    self.constraint[ii].compare(
                        other.constraint[ii], name=name + ".constraint[" + str(ii) + "]"
                    )
                )
        if other._preprocessing_str != self._preprocessing_str:
            diff_list.append(name + ".preprocessing")
        if (other.datakeeper_list is None and self.datakeeper_list is not None) or (
            other.datakeeper_list is not None and self.datakeeper_list is None
        ):
            diff_list.append(name + ".datakeeper_list None mismatch")
        elif self.datakeeper_list is None:
            pass
        elif len(other.datakeeper_list) != len(self.datakeeper_list):
            diff_list.append("len(" + name + ".datakeeper_list)")
        else:
            for ii in range(len(other.datakeeper_list)):
                diff_list.extend(
                    self.datakeeper_list[ii].compare(
                        other.datakeeper_list[ii],
                        name=name + ".datakeeper_list[" + str(ii) + "]",
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.simu)
        if self.design_var is not None:
            for value in self.design_var:
                S += getsizeof(value)
        if self.obj_func is not None:
            for value in self.obj_func:
                S += getsizeof(value)
        S += getsizeof(self._eval_func_str)
        if self.constraint is not None:
            for value in self.constraint:
                S += getsizeof(value)
        S += getsizeof(self._preprocessing_str)
        if self.datakeeper_list is not None:
            for value in self.datakeeper_list:
                S += getsizeof(value)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        OptiProblem_dict = dict()
        if self.simu is None:
            OptiProblem_dict["simu"] = None
        else:
            OptiProblem_dict["simu"] = self.simu.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs,
            )
        if self.design_var is None:
            OptiProblem_dict["design_var"] = None
        else:
            OptiProblem_dict["design_var"] = list()
            for obj in self.design_var:
                if obj is not None:
                    OptiProblem_dict["design_var"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs,
                        )
                    )
                else:
                    OptiProblem_dict["design_var"].append(None)
        if self.obj_func is None:
            OptiProblem_dict["obj_func"] = None
        else:
            OptiProblem_dict["obj_func"] = list()
            for obj in self.obj_func:
                if obj is not None:
                    OptiProblem_dict["obj_func"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs,
                        )
                    )
                else:
                    OptiProblem_dict["obj_func"].append(None)
        if self._eval_func_str is not None:
            OptiProblem_dict["eval_func"] = self._eval_func_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiProblem_dict["eval_func"] = self.eval_func
        else:
            OptiProblem_dict["eval_func"] = None
            if self.eval_func is not None:
                self.get_logger().warning(
                    "OptiProblem.as_dict(): "
                    + f"Function {self.eval_func.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self.constraint is None:
            OptiProblem_dict["constraint"] = None
        else:
            OptiProblem_dict["constraint"] = list()
            for obj in self.constraint:
                if obj is not None:
                    OptiProblem_dict["constraint"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs,
                        )
                    )
                else:
                    OptiProblem_dict["constraint"].append(None)
        if self._preprocessing_str is not None:
            OptiProblem_dict["preprocessing"] = self._preprocessing_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiProblem_dict["preprocessing"] = self.preprocessing
        else:
            OptiProblem_dict["preprocessing"] = None
            if self.preprocessing is not None:
                self.get_logger().warning(
                    "OptiProblem.as_dict(): "
                    + f"Function {self.preprocessing.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self.datakeeper_list is None:
            OptiProblem_dict["datakeeper_list"] = None
        else:
            OptiProblem_dict["datakeeper_list"] = list()
            for obj in self.datakeeper_list:
                if obj is not None:
                    OptiProblem_dict["datakeeper_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs,
                        )
                    )
                else:
                    OptiProblem_dict["datakeeper_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        OptiProblem_dict["__class__"] = "OptiProblem"
        return OptiProblem_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.simu is not None:
            self.simu._set_None()
        self.design_var = None
        self.obj_func = None
        self.eval_func = None
        self.constraint = None
        self.preprocessing = None
        self.datakeeper_list = None

    def _get_simu(self):
        """getter of simu"""
        return self._simu

    def _set_simu(self, value):
        """setter of simu"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "simu")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Simulation()
        check_var("simu", value, "Simulation")
        self._simu = value

        if self._simu is not None:
            self._simu.parent = self

    simu = property(
        fget=_get_simu,
        fset=_set_simu,
        doc="""Default simulation

        :Type: Simulation
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
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("design_var", value, "[OptiDesignVar]")
        self._design_var = value

    design_var = property(
        fget=_get_design_var,
        fset=_set_design_var,
        doc="""List of design variables

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
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("obj_func", value, "[OptiObjective]")
        self._obj_func = value

    obj_func = property(
        fget=_get_obj_func,
        fset=_set_obj_func,
        doc="""List of objective functions

        :Type: [OptiObjective]
        """,
    )

    def _get_eval_func(self):
        """getter of eval_func"""
        return self._eval_func_func

    def _set_eval_func(self, value):
        """setter of eval_func"""
        if value is None:
            self._eval_func_str = None
            self._eval_func_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._eval_func_str = value
            self._eval_func_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._eval_func_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._eval_func_func = eval(basename(value[:-3]))
        elif callable(value):
            self._eval_func_str = None
            self._eval_func_func = value
        else:
            raise CheckTypeError(
                "For property eval_func Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    eval_func = property(
        fget=_get_eval_func,
        fset=_set_eval_func,
        doc="""Function to evaluate before computing obj function and constraints

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
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("constraint", value, "[OptiConstraint]")
        self._constraint = value

    constraint = property(
        fget=_get_constraint,
        fset=_set_constraint,
        doc="""List containing the constraints 

        :Type: [OptiConstraint]
        """,
    )

    def _get_preprocessing(self):
        """getter of preprocessing"""
        return self._preprocessing_func

    def _set_preprocessing(self, value):
        """setter of preprocessing"""
        if value is None:
            self._preprocessing_str = None
            self._preprocessing_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._preprocessing_str = value
            self._preprocessing_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._preprocessing_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._preprocessing_func = eval(basename(value[:-3]))
        elif callable(value):
            self._preprocessing_str = None
            self._preprocessing_func = value
        else:
            raise CheckTypeError(
                "For property preprocessing Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    preprocessing = property(
        fget=_get_preprocessing,
        fset=_set_preprocessing,
        doc="""Function to execute a preprocessing on the simulation right before it is run.

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
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("datakeeper_list", value, "[DataKeeper]")
        self._datakeeper_list = value

    datakeeper_list = property(
        fget=_get_datakeeper_list,
        fset=_set_datakeeper_list,
        doc="""List of DataKeepers to run on every output

        :Type: [DataKeeper]
        """,
    )
