# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiBayesAlgSmoot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiBayesAlgSmoot
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .OptiBayesAlg import OptiBayesAlg

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Optimization.OptiBayesAlgSmoot.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Optimization.OptiBayesAlgSmoot.check_optimization_input import (
        check_optimization_input,
    )
except ImportError as error:
    check_optimization_input = error

try:
    from ..Methods.Optimization.OptiBayesAlgSmoot.evaluate import evaluate
except ImportError as error:
    evaluate = error

try:
    from ..Methods.Optimization.OptiBayesAlgSmoot.plot_pareto import plot_pareto
except ImportError as error:
    plot_pareto = error

try:
    from ..Methods.Optimization.OptiBayesAlgSmoot.eval_const import eval_const
except ImportError as error:
    eval_const = error


from numpy import isnan
from ._check import InitUnKnowClassError


class OptiBayesAlgSmoot(OptiBayesAlg):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Optimization.OptiBayesAlgSmoot.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiBayesAlgSmoot method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Optimization.OptiBayesAlgSmoot.check_optimization_input
    if isinstance(check_optimization_input, ImportError):
        check_optimization_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiBayesAlgSmoot method check_optimization_input: "
                    + str(check_optimization_input)
                )
            )
        )
    else:
        check_optimization_input = check_optimization_input
    # cf Methods.Optimization.OptiBayesAlgSmoot.evaluate
    if isinstance(evaluate, ImportError):
        evaluate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiBayesAlgSmoot method evaluate: " + str(evaluate)
                )
            )
        )
    else:
        evaluate = evaluate
    # cf Methods.Optimization.OptiBayesAlgSmoot.plot_pareto
    if isinstance(plot_pareto, ImportError):
        plot_pareto = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiBayesAlgSmoot method plot_pareto: "
                    + str(plot_pareto)
                )
            )
        )
    else:
        plot_pareto = plot_pareto
    # cf Methods.Optimization.OptiBayesAlgSmoot.eval_const
    if isinstance(eval_const, ImportError):
        eval_const = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiBayesAlgSmoot method eval_const: " + str(eval_const)
                )
            )
        )
    else:
        eval_const = eval_const
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        size_pop=40,
        nb_gen=100,
        nb_iter=15,
        nb_start=300,
        criterion="PI",
        kernel=0,
        problem=-1,
        xoutput=-1,
        logger_name="Pyleecan.OptiSolver",
        is_keep_all_output=False,
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
            if "size_pop" in list(init_dict.keys()):
                size_pop = init_dict["size_pop"]
            if "nb_gen" in list(init_dict.keys()):
                nb_gen = init_dict["nb_gen"]
            if "nb_iter" in list(init_dict.keys()):
                nb_iter = init_dict["nb_iter"]
            if "nb_start" in list(init_dict.keys()):
                nb_start = init_dict["nb_start"]
            if "criterion" in list(init_dict.keys()):
                criterion = init_dict["criterion"]
            if "kernel" in list(init_dict.keys()):
                kernel = init_dict["kernel"]
            if "problem" in list(init_dict.keys()):
                problem = init_dict["problem"]
            if "xoutput" in list(init_dict.keys()):
                xoutput = init_dict["xoutput"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
        # Set the properties (value check and convertion are done in setter)
        self.size_pop = size_pop
        self.nb_gen = nb_gen
        # Call OptiBayesAlg init
        super(OptiBayesAlgSmoot, self).__init__(
            nb_iter=nb_iter,
            nb_start=nb_start,
            criterion=criterion,
            kernel=kernel,
            problem=problem,
            xoutput=xoutput,
            logger_name=logger_name,
            is_keep_all_output=is_keep_all_output,
        )
        # The class is frozen (in OptiBayesAlg init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiBayesAlgSmoot_str = ""
        # Get the properties inherited from OptiBayesAlg
        OptiBayesAlgSmoot_str += super(OptiBayesAlgSmoot, self).__str__()
        OptiBayesAlgSmoot_str += "size_pop = " + str(self.size_pop) + linesep
        OptiBayesAlgSmoot_str += "nb_gen = " + str(self.nb_gen) + linesep
        return OptiBayesAlgSmoot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiBayesAlg
        if not super(OptiBayesAlgSmoot, self).__eq__(other):
            return False
        if other.size_pop != self.size_pop:
            return False
        if other.nb_gen != self.nb_gen:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiBayesAlg
        diff_list.extend(
            super(OptiBayesAlgSmoot, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._size_pop != self._size_pop:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._size_pop)
                    + ", other="
                    + str(other._size_pop)
                    + ")"
                )
                diff_list.append(name + ".size_pop" + val_str)
            else:
                diff_list.append(name + ".size_pop")
        if other._nb_gen != self._nb_gen:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_gen)
                    + ", other="
                    + str(other._nb_gen)
                    + ")"
                )
                diff_list.append(name + ".nb_gen" + val_str)
            else:
                diff_list.append(name + ".nb_gen")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiBayesAlg
        S += super(OptiBayesAlgSmoot, self).__sizeof__()
        S += getsizeof(self.size_pop)
        S += getsizeof(self.nb_gen)
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

        # Get the properties inherited from OptiBayesAlg
        OptiBayesAlgSmoot_dict = super(OptiBayesAlgSmoot, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OptiBayesAlgSmoot_dict["size_pop"] = self.size_pop
        OptiBayesAlgSmoot_dict["nb_gen"] = self.nb_gen
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiBayesAlgSmoot_dict["__class__"] = "OptiBayesAlgSmoot"
        return OptiBayesAlgSmoot_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        size_pop_val = self.size_pop
        nb_gen_val = self.nb_gen
        nb_iter_val = self.nb_iter
        nb_start_val = self.nb_start
        criterion_val = self.criterion
        kernel_val = self.kernel
        if self.problem is None:
            problem_val = None
        else:
            problem_val = self.problem.copy()
        if self.xoutput is None:
            xoutput_val = None
        else:
            xoutput_val = self.xoutput.copy()
        logger_name_val = self.logger_name
        is_keep_all_output_val = self.is_keep_all_output
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            size_pop=size_pop_val,
            nb_gen=nb_gen_val,
            nb_iter=nb_iter_val,
            nb_start=nb_start_val,
            criterion=criterion_val,
            kernel=kernel_val,
            problem=problem_val,
            xoutput=xoutput_val,
            logger_name=logger_name_val,
            is_keep_all_output=is_keep_all_output_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.size_pop = None
        self.nb_gen = None
        # Set to None the properties inherited from OptiBayesAlg
        super(OptiBayesAlgSmoot, self)._set_None()

    def _get_size_pop(self):
        """getter of size_pop"""
        return self._size_pop

    def _set_size_pop(self, value):
        """setter of size_pop"""
        check_var("size_pop", value, "int", Vmin=1)
        self._size_pop = value

    size_pop = property(
        fget=_get_size_pop,
        fset=_set_size_pop,
        doc="""Number of individuals for each generation

        :Type: int
        :min: 1
        """,
    )

    def _get_nb_gen(self):
        """getter of nb_gen"""
        return self._nb_gen

    def _set_nb_gen(self, value):
        """setter of nb_gen"""
        check_var("nb_gen", value, "int", Vmin=1)
        self._nb_gen = value

    nb_gen = property(
        fget=_get_nb_gen,
        fset=_set_nb_gen,
        doc="""Number of generations for the genetic part

        :Type: int
        :min: 1
        """,
    )
