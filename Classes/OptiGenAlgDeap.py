# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiGenAlgDeap.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.OptiGenAlg import OptiGenAlg

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Optimization.OptiGenAlgDeap.gen_pop import gen_pop
except ImportError as error:
    gen_pop = error


from inspect import getsource
from cloudpickle import dumps, loads
from pyleecan.Classes.check import CheckTypeError
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.OutputMultiOpti import OutputMultiOpti
from pyleecan.Classes.OptiProblem import OptiProblem


class OptiGenAlgDeap(OptiGenAlg):
    """Multi-objectives optimization problem solver using DEAP"""

    VERSION = 1

    # cf Methods.Optimization.OptiGenAlgDeap.gen_pop
    if isinstance(gen_pop, ImportError):
        gen_pop = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiGenAlgDeap method gen_pop: " + str(gen_pop))
            )
        )
    else:
        gen_pop = gen_pop
    # save method is available in all object
    save = save

    def __init__(
        self,
        multi_output=-1,
        pop=[],
        selector=None,
        crossover=None,
        mutator=None,
        p_cross=0.9,
        p_mutate=0.1,
        size_pop=50,
        nb_gen=200,
        problem=-1,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if multi_output == -1:
            multi_output = OutputMultiOpti()
        if problem == -1:
            problem = OptiProblem()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "multi_output",
                    "pop",
                    "selector",
                    "crossover",
                    "mutator",
                    "p_cross",
                    "p_mutate",
                    "size_pop",
                    "nb_gen",
                    "problem",
                ],
            )
            # Overwrite default value with init_dict content
            if "multi_output" in list(init_dict.keys()):
                multi_output = init_dict["multi_output"]
            if "pop" in list(init_dict.keys()):
                pop = init_dict["pop"]
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
        # Initialisation by argument
        # Call OptiGenAlg init
        super(OptiGenAlgDeap, self).__init__(
            multi_output=multi_output,
            pop=pop,
            selector=selector,
            crossover=crossover,
            mutator=mutator,
            p_cross=p_cross,
            p_mutate=p_mutate,
            size_pop=size_pop,
            nb_gen=nb_gen,
            problem=problem,
        )
        # The class is frozen (in OptiGenAlg init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiGenAlgDeap_str = ""
        # Get the properties inherited from OptiGenAlg
        OptiGenAlgDeap_str += super(OptiGenAlgDeap, self).__str__() + linesep
        return OptiGenAlgDeap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiGenAlg
        if not super(OptiGenAlgDeap, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OptiGenAlg
        OptiGenAlgDeap_dict = super(OptiGenAlgDeap, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OptiGenAlgDeap_dict["__class__"] = "OptiGenAlgDeap"
        return OptiGenAlgDeap_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from OptiGenAlg
        super(OptiGenAlgDeap, self)._set_None()
