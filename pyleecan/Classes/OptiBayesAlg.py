# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiBayesAlg.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiBayesAlg
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
from .OptiSolver import OptiSolver

from numpy import isnan
from ._check import InitUnKnowClassError


class OptiBayesAlg(OptiSolver):
    """Bayesian algorithm class"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        self.nb_iter = nb_iter
        self.nb_start = nb_start
        self.criterion = criterion
        self.kernel = kernel
        # Call OptiSolver init
        super(OptiBayesAlg, self).__init__(
            problem=problem,
            xoutput=xoutput,
            logger_name=logger_name,
            is_keep_all_output=is_keep_all_output,
        )
        # The class is frozen (in OptiSolver init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiBayesAlg_str = ""
        # Get the properties inherited from OptiSolver
        OptiBayesAlg_str += super(OptiBayesAlg, self).__str__()
        OptiBayesAlg_str += "nb_iter = " + str(self.nb_iter) + linesep
        OptiBayesAlg_str += "nb_start = " + str(self.nb_start) + linesep
        OptiBayesAlg_str += 'criterion = "' + str(self.criterion) + '"' + linesep
        OptiBayesAlg_str += "kernel = " + str(self.kernel) + linesep
        return OptiBayesAlg_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiSolver
        if not super(OptiBayesAlg, self).__eq__(other):
            return False
        if other.nb_iter != self.nb_iter:
            return False
        if other.nb_start != self.nb_start:
            return False
        if other.criterion != self.criterion:
            return False
        if other.kernel != self.kernel:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiSolver
        diff_list.extend(
            super(OptiBayesAlg, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._nb_iter != self._nb_iter:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_iter)
                    + ", other="
                    + str(other._nb_iter)
                    + ")"
                )
                diff_list.append(name + ".nb_iter" + val_str)
            else:
                diff_list.append(name + ".nb_iter")
        if other._nb_start != self._nb_start:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_start)
                    + ", other="
                    + str(other._nb_start)
                    + ")"
                )
                diff_list.append(name + ".nb_start" + val_str)
            else:
                diff_list.append(name + ".nb_start")
        if other._criterion != self._criterion:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._criterion)
                    + ", other="
                    + str(other._criterion)
                    + ")"
                )
                diff_list.append(name + ".criterion" + val_str)
            else:
                diff_list.append(name + ".criterion")
        if other._kernel != self._kernel:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._kernel)
                    + ", other="
                    + str(other._kernel)
                    + ")"
                )
                diff_list.append(name + ".kernel" + val_str)
            else:
                diff_list.append(name + ".kernel")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiSolver
        S += super(OptiBayesAlg, self).__sizeof__()
        S += getsizeof(self.nb_iter)
        S += getsizeof(self.nb_start)
        S += getsizeof(self.criterion)
        S += getsizeof(self.kernel)
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

        # Get the properties inherited from OptiSolver
        OptiBayesAlg_dict = super(OptiBayesAlg, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OptiBayesAlg_dict["nb_iter"] = self.nb_iter
        OptiBayesAlg_dict["nb_start"] = self.nb_start
        OptiBayesAlg_dict["criterion"] = self.criterion
        OptiBayesAlg_dict["kernel"] = self.kernel
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiBayesAlg_dict["__class__"] = "OptiBayesAlg"
        return OptiBayesAlg_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
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

        self.nb_iter = None
        self.nb_start = None
        self.criterion = None
        self.kernel = None
        # Set to None the properties inherited from OptiSolver
        super(OptiBayesAlg, self)._set_None()

    def _get_nb_iter(self):
        """getter of nb_iter"""
        return self._nb_iter

    def _set_nb_iter(self, value):
        """setter of nb_iter"""
        check_var("nb_iter", value, "int", Vmin=1)
        self._nb_iter = value

    nb_iter = property(
        fget=_get_nb_iter,
        fset=_set_nb_iter,
        doc="""Number of iterations

        :Type: int
        :min: 1
        """,
    )

    def _get_nb_start(self):
        """getter of nb_start"""
        return self._nb_start

    def _set_nb_start(self, value):
        """setter of nb_start"""
        check_var("nb_start", value, "int", Vmin=1)
        self._nb_start = value

    nb_start = property(
        fget=_get_nb_start,
        fset=_set_nb_start,
        doc="""Number of starting points

        :Type: int
        :min: 1
        """,
    )

    def _get_criterion(self):
        """getter of criterion"""
        return self._criterion

    def _set_criterion(self, value):
        """setter of criterion"""
        check_var("criterion", value, "str")
        self._criterion = value

    criterion = property(
        fget=_get_criterion,
        fset=_set_criterion,
        doc="""Point selection criteria

        :Type: str
        """,
    )

    def _get_kernel(self):
        """getter of kernel"""
        return self._kernel

    def _set_kernel(self, value):
        """setter of kernel"""
        check_var("kernel", value, "int", Vmin=0, Vmax=0)
        self._kernel = value

    kernel = property(
        fget=_get_kernel,
        fset=_set_kernel,
        doc="""Type of kernel

        :Type: int
        :min: 0
        :max: 0
        """,
    )
