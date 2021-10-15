# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiGenAlg.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiGenAlg
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
from .OptiSolver import OptiSolver

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError
from .OptiProblem import OptiProblem
from .XOutput import XOutput


class OptiGenAlg(OptiSolver):
    """Genetic algorithm class"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        self.selector = selector
        self.crossover = crossover
        self.mutator = mutator
        self.p_cross = p_cross
        self.p_mutate = p_mutate
        self.size_pop = size_pop
        self.nb_gen = nb_gen
        # Call OptiSolver init
        super(OptiGenAlg, self).__init__(
            problem=problem,
            xoutput=xoutput,
            logger_name=logger_name,
            is_keep_all_output=is_keep_all_output,
        )
        # The class is frozen (in OptiSolver init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OptiGenAlg_str = ""
        # Get the properties inherited from OptiSolver
        OptiGenAlg_str += super(OptiGenAlg, self).__str__()
        if self._selector_str is not None:
            OptiGenAlg_str += "selector = " + self._selector_str + linesep
        elif self._selector_func is not None:
            OptiGenAlg_str += "selector = " + str(self._selector_func) + linesep
        else:
            OptiGenAlg_str += "selector = None" + linesep + linesep
        if self._crossover_str is not None:
            OptiGenAlg_str += "crossover = " + self._crossover_str + linesep
        elif self._crossover_func is not None:
            OptiGenAlg_str += "crossover = " + str(self._crossover_func) + linesep
        else:
            OptiGenAlg_str += "crossover = None" + linesep + linesep
        if self._mutator_str is not None:
            OptiGenAlg_str += "mutator = " + self._mutator_str + linesep
        elif self._mutator_func is not None:
            OptiGenAlg_str += "mutator = " + str(self._mutator_func) + linesep
        else:
            OptiGenAlg_str += "mutator = None" + linesep + linesep
        OptiGenAlg_str += "p_cross = " + str(self.p_cross) + linesep
        OptiGenAlg_str += "p_mutate = " + str(self.p_mutate) + linesep
        OptiGenAlg_str += "size_pop = " + str(self.size_pop) + linesep
        OptiGenAlg_str += "nb_gen = " + str(self.nb_gen) + linesep
        return OptiGenAlg_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiSolver
        if not super(OptiGenAlg, self).__eq__(other):
            return False
        if other._selector_str != self._selector_str:
            return False
        if other._crossover_str != self._crossover_str:
            return False
        if other._mutator_str != self._mutator_str:
            return False
        if other.p_cross != self.p_cross:
            return False
        if other.p_mutate != self.p_mutate:
            return False
        if other.size_pop != self.size_pop:
            return False
        if other.nb_gen != self.nb_gen:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OptiSolver
        diff_list.extend(super(OptiGenAlg, self).compare(other, name=name))
        if other._selector_str != self._selector_str:
            diff_list.append(name + ".selector")
        if other._crossover_str != self._crossover_str:
            diff_list.append(name + ".crossover")
        if other._mutator_str != self._mutator_str:
            diff_list.append(name + ".mutator")
        if other._p_cross != self._p_cross:
            diff_list.append(name + ".p_cross")
        if other._p_mutate != self._p_mutate:
            diff_list.append(name + ".p_mutate")
        if other._size_pop != self._size_pop:
            diff_list.append(name + ".size_pop")
        if other._nb_gen != self._nb_gen:
            diff_list.append(name + ".nb_gen")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OptiSolver
        S += super(OptiGenAlg, self).__sizeof__()
        S += getsizeof(self._selector_str)
        S += getsizeof(self._crossover_str)
        S += getsizeof(self._mutator_str)
        S += getsizeof(self.p_cross)
        S += getsizeof(self.p_mutate)
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

        # Get the properties inherited from OptiSolver
        OptiGenAlg_dict = super(OptiGenAlg, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs,
        )
        if self._selector_str is not None:
            OptiGenAlg_dict["selector"] = self._selector_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiGenAlg_dict["selector"] = self.selector
        else:
            OptiGenAlg_dict["selector"] = None
            if self.selector is not None:
                self.get_logger().warning(
                    "OptiGenAlg.as_dict(): "
                    + f"Function {self.selector.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self._crossover_str is not None:
            OptiGenAlg_dict["crossover"] = self._crossover_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiGenAlg_dict["crossover"] = self.crossover
        else:
            OptiGenAlg_dict["crossover"] = None
            if self.crossover is not None:
                self.get_logger().warning(
                    "OptiGenAlg.as_dict(): "
                    + f"Function {self.crossover.__name__} is not serializable "
                    + "and will be converted to None."
                )
        if self._mutator_str is not None:
            OptiGenAlg_dict["mutator"] = self._mutator_str
        elif "keep_function" in kwargs and kwargs["keep_function"]:
            OptiGenAlg_dict["mutator"] = self.mutator
        else:
            OptiGenAlg_dict["mutator"] = None
            if self.mutator is not None:
                self.get_logger().warning(
                    "OptiGenAlg.as_dict(): "
                    + f"Function {self.mutator.__name__} is not serializable "
                    + "and will be converted to None."
                )
        OptiGenAlg_dict["p_cross"] = self.p_cross
        OptiGenAlg_dict["p_mutate"] = self.p_mutate
        OptiGenAlg_dict["size_pop"] = self.size_pop
        OptiGenAlg_dict["nb_gen"] = self.nb_gen
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OptiGenAlg_dict["__class__"] = "OptiGenAlg"
        return OptiGenAlg_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.selector = None
        self.crossover = None
        self.mutator = None
        self.p_cross = None
        self.p_mutate = None
        self.size_pop = None
        self.nb_gen = None
        # Set to None the properties inherited from OptiSolver
        super(OptiGenAlg, self)._set_None()

    def _get_selector(self):
        """getter of selector"""
        return self._selector_func

    def _set_selector(self, value):
        """setter of selector"""
        if value is None:
            self._selector_str = None
            self._selector_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._selector_str = value
            self._selector_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._selector_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._selector_func = eval(basename(value[:-3]))
        elif callable(value):
            self._selector_str = None
            self._selector_func = value
        else:
            raise CheckTypeError(
                "For property selector Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    selector = property(
        fget=_get_selector,
        fset=_set_selector,
        doc="""Selector of the genetic algorithm

        :Type: function
        """,
    )

    def _get_crossover(self):
        """getter of crossover"""
        return self._crossover_func

    def _set_crossover(self, value):
        """setter of crossover"""
        if value is None:
            self._crossover_str = None
            self._crossover_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._crossover_str = value
            self._crossover_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._crossover_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._crossover_func = eval(basename(value[:-3]))
        elif callable(value):
            self._crossover_str = None
            self._crossover_func = value
        else:
            raise CheckTypeError(
                "For property crossover Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    crossover = property(
        fget=_get_crossover,
        fset=_set_crossover,
        doc="""Crossover of the genetic algorithm

        :Type: function
        """,
    )

    def _get_mutator(self):
        """getter of mutator"""
        return self._mutator_func

    def _set_mutator(self, value):
        """setter of mutator"""
        if value is None:
            self._mutator_str = None
            self._mutator_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._mutator_str = value
            self._mutator_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._mutator_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._mutator_func = eval(basename(value[:-3]))
        elif callable(value):
            self._mutator_str = None
            self._mutator_func = value
        else:
            raise CheckTypeError(
                "For property mutator Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    mutator = property(
        fget=_get_mutator,
        fset=_set_mutator,
        doc="""Mutator of the genetic algorithm

        :Type: function
        """,
    )

    def _get_p_cross(self):
        """getter of p_cross"""
        return self._p_cross

    def _set_p_cross(self, value):
        """setter of p_cross"""
        check_var("p_cross", value, "float", Vmin=0, Vmax=1)
        self._p_cross = value

    p_cross = property(
        fget=_get_p_cross,
        fset=_set_p_cross,
        doc="""Probability of crossover

        :Type: float
        :min: 0
        :max: 1
        """,
    )

    def _get_p_mutate(self):
        """getter of p_mutate"""
        return self._p_mutate

    def _set_p_mutate(self, value):
        """setter of p_mutate"""
        check_var("p_mutate", value, "float", Vmin=0, Vmax=1)
        self._p_mutate = value

    p_mutate = property(
        fget=_get_p_mutate,
        fset=_set_p_mutate,
        doc="""Probability of mutation 

        :Type: float
        :min: 0
        :max: 1
        """,
    )

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
        doc="""Size of the population

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
        doc="""Number of generations

        :Type: int
        :min: 1
        """,
    )
