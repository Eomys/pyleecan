# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiGenAlgNsga2Deap.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiGenAlgNsga2Deap
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
from .OptiGenAlg import OptiGenAlg

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.mutate import mutate
except ImportError as error:
    mutate = error

try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.cross import cross
except ImportError as error:
    cross = error

try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.create_toolbox import create_toolbox
except ImportError as error:
    create_toolbox = error

try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.check_optimization_input import (
        check_optimization_input,
    )
except ImportError as error:
    check_optimization_input = error

try:
    from ..Methods.Optimization.OptiGenAlgNsga2Deap.delete_toolbox import delete_toolbox
except ImportError as error:
    delete_toolbox = error


from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from deap.base import Toolbox
except ImportError:
    Toolbox = ImportError
from ._check import InitUnKnowClassError
from .OptiProblem import OptiProblem
from .XOutput import XOutput


class OptiGenAlgNsga2Deap(OptiGenAlg):
    """Multi-objectives optimization problem with some constraints"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiGenAlgNsga2Deap method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.mutate
    if isinstance(mutate, ImportError):
        mutate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiGenAlgNsga2Deap method mutate: " + str(mutate)
                )
            )
        )
    else:
        mutate = mutate
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.cross
    if isinstance(cross, ImportError):
        cross = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiGenAlgNsga2Deap method cross: " + str(cross))
            )
        )
    else:
        cross = cross
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.create_toolbox
    if isinstance(create_toolbox, ImportError):
        create_toolbox = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiGenAlgNsga2Deap method create_toolbox: "
                    + str(create_toolbox)
                )
            )
        )
    else:
        create_toolbox = create_toolbox
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.check_optimization_input
    if isinstance(check_optimization_input, ImportError):
        check_optimization_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiGenAlgNsga2Deap method check_optimization_input: "
                    + str(check_optimization_input)
                )
            )
        )
    else:
        check_optimization_input = check_optimization_input
    # cf Methods.Optimization.OptiGenAlgNsga2Deap.delete_toolbox
    if isinstance(delete_toolbox, ImportError):
        delete_toolbox = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OptiGenAlgNsga2Deap method delete_toolbox: "
                    + str(delete_toolbox)
                )
            )
        )
    else:
        delete_toolbox = delete_toolbox
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        toolbox=None,
        selector=None,
        crossover=None,
        mutator=None,
        p_cross=0.9,
        p_mutate=0.1,
        size_pop=40,
        nb_gen=100,
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
            if "toolbox" in list(init_dict.keys()):
                toolbox = init_dict["toolbox"]
            if "selector" in list(init_dict.keys()):
                selector = init_dict["selector"]
            if "crossover" in list(init_dict.keys()):
                crossover = init_dict["crossover"]
            if "mutator" in list(init_dict.keys()):
                mutator = init_dict["mutator"]
            if "p_cross" in list(init_dict.keys()):
                p_cross = init_dict["p_cross"]
            if "p_mutate" in list(init_dict.keys()):
                p_mutate = init_dict["p_mutate"]
            if "size_pop" in list(init_dict.keys()):
                size_pop = init_dict["size_pop"]
            if "nb_gen" in list(init_dict.keys()):
                nb_gen = init_dict["nb_gen"]
            if "problem" in list(init_dict.keys()):
                problem = init_dict["problem"]
            if "xoutput" in list(init_dict.keys()):
                xoutput = init_dict["xoutput"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
        # Set the properties (value check and convertion are done in setter)
        self.toolbox = toolbox
        # Call OptiGenAlg init
        super(OptiGenAlgNsga2Deap, self).__init__(
            selector=selector,
            crossover=crossover,
            mutator=mutator,
            p_cross=p_cross,
            p_mutate=p_mutate,
            size_pop=size_pop,
            nb_gen=nb_gen,
            problem=problem,
            xoutput=xoutput,
            logger_name=logger_name,
            is_keep_all_output=is_keep_all_output,
        )
        # The class is frozen (in OptiGenAlg init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiGenAlgNsga2Deap_str = ""
        # Get the properties inherited from OptiGenAlg
        OptiGenAlgNsga2Deap_str += super(OptiGenAlgNsga2Deap, self).__str__()
        OptiGenAlgNsga2Deap_str += "toolbox = " + str(self.toolbox) + linesep + linesep
        return OptiGenAlgNsga2Deap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiGenAlg
        if not super(OptiGenAlgNsga2Deap, self).__eq__(other):
            return False
        if other.toolbox != self.toolbox:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiGenAlg
        diff_list.extend(super(OptiGenAlgNsga2Deap, self).compare(other, name=name))
        if (other.toolbox is None and self.toolbox is not None) or (
            other.toolbox is not None and self.toolbox is None
        ):
            diff_list.append(name + ".toolbox None mismatch")
        elif self.toolbox is not None and self.toolbox != other.toolbox:
            diff_list.append(name + ".toolbox")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiGenAlg
        S += super(OptiGenAlgNsga2Deap, self).__sizeof__()
        S += getsizeof(self.toolbox)
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

        # Get the properties inherited from OptiGenAlg
        OptiGenAlgNsga2Deap_dict = super(OptiGenAlgNsga2Deap, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.toolbox is None:
            OptiGenAlgNsga2Deap_dict["toolbox"] = None
        else:
            # Store serialized data (using cloudpickle) and str
            # to read it in json save files
            OptiGenAlgNsga2Deap_dict["toolbox"] = {
                "__class__": str(type(self._toolbox)),
                "__repr__": str(self._toolbox.__repr__()),
                "serialized": dumps(self._toolbox).decode("ISO-8859-2"),
            }
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiGenAlgNsga2Deap_dict["__class__"] = "OptiGenAlgNsga2Deap"
        return OptiGenAlgNsga2Deap_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.toolbox = None
        # Set to None the properties inherited from OptiGenAlg
        super(OptiGenAlgNsga2Deap, self)._set_None()

    def _get_toolbox(self):
        """getter of toolbox"""
        return self._toolbox

    def _set_toolbox(self, value):
        """setter of toolbox"""
        check_var("toolbox", value, "Toolbox")
        self._toolbox = value

    toolbox = property(
        fget=_get_toolbox,
        fset=_set_toolbox,
        doc=u"""DEAP toolbox

        :Type: deap.base.Toolbox
        """,
    )
