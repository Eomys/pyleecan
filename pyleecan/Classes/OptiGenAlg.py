# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiGenAlg.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiGenAlg
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .OptiSolver import OptiSolver

from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
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
        if self._selector[1] is None:
            OptiGenAlg_str += "selector = " + str(self._selector[1])
        else:
            OptiGenAlg_str += (
                "selector = " + linesep + str(self._selector[1]) + linesep + linesep
            )
        if self._crossover[1] is None:
            OptiGenAlg_str += "crossover = " + str(self._crossover[1])
        else:
            OptiGenAlg_str += (
                "crossover = " + linesep + str(self._crossover[1]) + linesep + linesep
            )
        if self._mutator[1] is None:
            OptiGenAlg_str += "mutator = " + str(self._mutator[1])
        else:
            OptiGenAlg_str += (
                "mutator = " + linesep + str(self._mutator[1]) + linesep + linesep
            )
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
        if other.selector != self.selector:
            return False
        if other.crossover != self.crossover:
            return False
        if other.mutator != self.mutator:
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

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from OptiSolver
        OptiGenAlg_dict = super(OptiGenAlg, self).as_dict()
        if self.selector is None:
            OptiGenAlg_dict["selector"] = None
        else:
            OptiGenAlg_dict["selector"] = [
                dumps(self._selector[0]).decode("ISO-8859-2"),
                self._selector[1],
            ]
        if self.crossover is None:
            OptiGenAlg_dict["crossover"] = None
        else:
            OptiGenAlg_dict["crossover"] = [
                dumps(self._crossover[0]).decode("ISO-8859-2"),
                self._crossover[1],
            ]
        if self.mutator is None:
            OptiGenAlg_dict["mutator"] = None
        else:
            OptiGenAlg_dict["mutator"] = [
                dumps(self._mutator[0]).decode("ISO-8859-2"),
                self._mutator[1],
            ]
        OptiGenAlg_dict["p_cross"] = self.p_cross
        OptiGenAlg_dict["p_mutate"] = self.p_mutate
        OptiGenAlg_dict["size_pop"] = self.size_pop
        OptiGenAlg_dict["nb_gen"] = self.nb_gen
        # The class name is added to the dict fordeserialisation purpose
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
        return self._selector[0]

    def _set_selector(self, value):
        """setter of selector"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "selector"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = function()
        try:
            check_var("selector", value, "list")
        except CheckTypeError:
            check_var("selector", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._selector = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._selector = [None, None]
        elif callable(value):
            self._selector = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    selector = property(
        fget=_get_selector,
        fset=_set_selector,
        doc=u"""Selector of the genetic algorithm

        :Type: function
        """,
    )

    def _get_crossover(self):
        """getter of crossover"""
        return self._crossover[0]

    def _set_crossover(self, value):
        """setter of crossover"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "crossover"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = function()
        try:
            check_var("crossover", value, "list")
        except CheckTypeError:
            check_var("crossover", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._crossover = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._crossover = [None, None]
        elif callable(value):
            self._crossover = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    crossover = property(
        fget=_get_crossover,
        fset=_set_crossover,
        doc=u"""Crossover of the genetic algorithm

        :Type: function
        """,
    )

    def _get_mutator(self):
        """getter of mutator"""
        return self._mutator[0]

    def _set_mutator(self, value):
        """setter of mutator"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "mutator"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = function()
        try:
            check_var("mutator", value, "list")
        except CheckTypeError:
            check_var("mutator", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._mutator = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._mutator = [None, None]
        elif callable(value):
            self._mutator = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    mutator = property(
        fget=_get_mutator,
        fset=_set_mutator,
        doc=u"""Mutator of the genetic algorithm

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
        doc=u"""Probability of crossover

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
        doc=u"""Probability of mutation 

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
        doc=u"""Size of the population

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
        doc=u"""Number of generations

        :Type: int
        :min: 1
        """,
    )
