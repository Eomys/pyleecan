# -*- coding: utf-8 -*-

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.OptiGenAlg import OptiGenAlg

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Optimization.OptiGenAlgNsga2Deap.solve import solve
except ImportError as error:
    solve = error

try:
    from pyleecan.Methods.Optimization.OptiGenAlgNsga2Deap.mutate import mutate
except ImportError as error:
    mutate = error

try:
    from pyleecan.Methods.Optimization.OptiGenAlgNsga2Deap.create_toolbox import (
        create_toolbox,
    )
except ImportError as error:
    create_toolbox = error

from inspect import getsource
from cloudpickle import dumps, loads
from pyleecan.Classes.check import CheckTypeError
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.OutputMultiOpti import OutputMultiOpti
from pyleecan.Classes.OptiProblem import OptiProblem


class OptiGenAlgNsga2Deap(OptiGenAlg):
    """Multi-objectives optimization problem solver using DEAP"""

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
    # save method is available in all object
    save = save

    def __init__(
        self,
        multi_output=-1,
        selector=None,
        crossover=None,
        mutator=None,
        p_cross=0.9,
        p_mutate=0.1,
        size_pop=50,
        nb_gen=200,
        problem=-1,
    ):
        """Constructor of the class."""

        if multi_output == -1:
            multi_output = OutputMultiOpti()
        if problem == -1:
            problem = OptiProblem()

        # Initialisation by argument
        self.toolbox = None

        # Call OptiGenAlg init
        super(OptiGenAlgNsga2Deap, self).__init__(
            multi_output=multi_output,
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

        OptiGenAlgNsga2Deap_str = ""
        # Get the properties inherited from OptiGenAlg
        OptiGenAlgNsga2Deap_str += super(OptiGenAlgNsga2Deap, self).__str__() + linesep
        OptiGenAlgNsga2Deap_str += "toolbox = " + linesep + str(None)
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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OptiGenAlg
        OptiGenAlgNsga2Deap_dict = super(OptiGenAlgNsga2Deap, self).as_dict()
        OptiGenAlgNsga2Deap_dict["toolbox"] = None
        # The class name is added to the dict fordeserialisation purpose
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
        self._toolbox = value

    # Toolbox to use DEAP tools
    # Type : list
    toolbox = property(
        fget=_get_toolbox, fset=_set_toolbox, doc=u"""Toolbox to use DEAP tools"""
    )
