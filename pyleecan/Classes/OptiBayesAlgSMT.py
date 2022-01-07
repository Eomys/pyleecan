# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiBayesAlgSMT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiBayesAlgSMT
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
from .OptiBayesAlg import OptiBayesAlg

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Optimization.OptiBayesAlgSMT.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Optimization.OptiBayesAlgSMT.check_optimization_input import (
        check_optimization_input,
    )
except ImportError as error:
    check_optimization_input = error


from ._check import InitUnKnowClassError
from .OptiProblem import OptiProblem
from .XOutput import XOutput


class OptiBayesAlgSMT(OptiBayesAlg):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Optimization.OptiBayesAlgSMT.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiBayesAlgSMT method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Optimization.OptiBayesAlgSMT.check_optimization_input
    if isinstance(check_optimization_input, ImportError):
        check_optimization_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiBayesAlgSMT method check_optimization_input: "
                    + str(check_optimization_input)
                )
            )
        )
    else:
        check_optimization_input = check_optimization_input
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        nb_iter=10,
        criteria="EI",
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
            if "criteria" in list(init_dict.keys()):
                criteria = init_dict["criteria"]
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
        # Call OptiBayesAlg init
        super(OptiBayesAlgSMT, self).__init__(
            nb_iter=nb_iter,
            criteria=criteria,
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

        OptiBayesAlgSMT_str = ""
        # Get the properties inherited from OptiBayesAlg
        OptiBayesAlgSMT_str += super(OptiBayesAlgSMT, self).__str__()
        return OptiBayesAlgSMT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiBayesAlg
        if not super(OptiBayesAlgSMT, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiBayesAlg
        diff_list.extend(super(OptiBayesAlgSMT, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiBayesAlg
        S += super(OptiBayesAlgSMT, self).__sizeof__()
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
        OptiBayesAlgSMT_dict = super(OptiBayesAlgSMT, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiBayesAlgSMT_dict["__class__"] = "OptiBayesAlgSMT"
        return OptiBayesAlgSMT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from OptiBayesAlg
        super(OptiBayesAlgSMT, self)._set_None()
