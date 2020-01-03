# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiGenAlgNsga2Deap.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.OptiGenAlgDeap import OptiGenAlgDeap

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Optimization.OptiGenAlgNsga2Deap.solve import solve
except ImportError as error:
    solve = error


from inspect import getsource
from cloudpickle import dumps, loads
from pyleecan.Classes.check import CheckTypeError
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.OutputMultiOpti import OutputMultiOpti
from pyleecan.Classes.OptiProblem import OptiProblem


class OptiGenAlgNsga2Deap(OptiGenAlgDeap):
    """Multi-objectives optimization problem solver using DEAP"""

    VERSION = 1

    # cf Methods.Optimization.OptiGenAlgNsga2Deap.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use OptiGenAlgNsga2Deap method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # save method is available in all object
    save = save

    def __init__(self, multi_output=-1, pop=[], selector=None, crossover=None, mutator=None, p_cross=0.9, p_mute=0.1, size_pop=50, problem=-1, init_dict=None):
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
            check_init_dict(init_dict, ["multi_output", "pop", "selector", "crossover", "mutator", "p_cross", "p_mute", "size_pop", "problem"])
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
            if "p_mute" in list(init_dict.keys()):
                p_mute = init_dict["p_mute"]
            if "size_pop" in list(init_dict.keys()):
                size_pop = init_dict["size_pop"]
            if "problem" in list(init_dict.keys()):
                problem = init_dict["problem"]
        # Initialisation by argument
        # Call OptiGenAlgDeap init
        super(OptiGenAlgNsga2Deap, self).__init__(multi_output=multi_output, pop=pop, selector=selector, crossover=crossover, mutator=mutator, p_cross=p_cross, p_mute=p_mute, size_pop=size_pop, problem=problem)
        # The class is frozen (in OptiGenAlgDeap init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiGenAlgNsga2Deap_str = ""
        # Get the properties inherited from OptiGenAlgDeap
        OptiGenAlgNsga2Deap_str += super(OptiGenAlgNsga2Deap, self).__str__() + linesep
        return OptiGenAlgNsga2Deap_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OptiGenAlgDeap
        if not super(OptiGenAlgNsga2Deap, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OptiGenAlgDeap
        OptiGenAlgNsga2Deap_dict = super(OptiGenAlgNsga2Deap, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OptiGenAlgNsga2Deap_dict["__class__"] = "OptiGenAlgNsga2Deap"
        return OptiGenAlgNsga2Deap_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from OptiGenAlgDeap
        super(OptiGenAlgNsga2Deap, self)._set_None()
