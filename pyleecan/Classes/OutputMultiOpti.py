# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Output/OutputMultiOpti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .OutputMulti import OutputMulti

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutputMultiOpti.add_evaluation import add_evaluation
except ImportError as error:
    add_evaluation = error

try:
    from ..Methods.Output.OutputMultiOpti.plot_pareto import plot_pareto
except ImportError as error:
    plot_pareto = error

try:
    from ..Methods.Output.OutputMultiOpti.plot_generation import plot_generation
except ImportError as error:
    plot_generation = error

try:
    from ..Methods.Output.OutputMultiOpti.get_pareto import get_pareto
except ImportError as error:
    get_pareto = error

try:
    from ..Methods.Output.OutputMultiOpti.plot_pareto_design_space import (
        plot_pareto_design_space,
    )
except ImportError as error:
    plot_pareto_design_space = error

try:
    from ..Methods.Output.OutputMultiOpti.plot_generation_design_space import (
        plot_generation_design_space,
    )
except ImportError as error:
    plot_generation_design_space = error


from ._check import InitUnKnowClassError
from .Output import Output


class OutputMultiOpti(OutputMulti):
    """Optimization results"""

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutputMultiOpti.add_evaluation
    if isinstance(add_evaluation, ImportError):
        add_evaluation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method add_evaluation: "
                    + str(add_evaluation)
                )
            )
        )
    else:
        add_evaluation = add_evaluation
    # cf Methods.Output.OutputMultiOpti.plot_pareto
    if isinstance(plot_pareto, ImportError):
        plot_pareto = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method plot_pareto: " + str(plot_pareto)
                )
            )
        )
    else:
        plot_pareto = plot_pareto
    # cf Methods.Output.OutputMultiOpti.plot_generation
    if isinstance(plot_generation, ImportError):
        plot_generation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method plot_generation: "
                    + str(plot_generation)
                )
            )
        )
    else:
        plot_generation = plot_generation
    # cf Methods.Output.OutputMultiOpti.get_pareto
    if isinstance(get_pareto, ImportError):
        get_pareto = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method get_pareto: " + str(get_pareto)
                )
            )
        )
    else:
        get_pareto = get_pareto
    # cf Methods.Output.OutputMultiOpti.plot_pareto_design_space
    if isinstance(plot_pareto_design_space, ImportError):
        plot_pareto_design_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method plot_pareto_design_space: "
                    + str(plot_pareto_design_space)
                )
            )
        )
    else:
        plot_pareto_design_space = plot_pareto_design_space
    # cf Methods.Output.OutputMultiOpti.plot_generation_design_space
    if isinstance(plot_generation_design_space, ImportError):
        plot_generation_design_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMultiOpti method plot_generation_design_space: "
                    + str(plot_generation_design_space)
                )
            )
        )
    else:
        plot_generation_design_space = plot_generation_design_space
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        fitness=[],
        constraint=[],
        ngen=[],
        fitness_names=[],
        output_ref=-1,
        outputs=list(),
        is_valid=[],
        design_var=[],
        design_var_names=[],
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if output_ref == -1:
            output_ref = Output()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            fitness = obj.fitness
            constraint = obj.constraint
            ngen = obj.ngen
            fitness_names = obj.fitness_names
            output_ref = obj.output_ref
            outputs = obj.outputs
            is_valid = obj.is_valid
            design_var = obj.design_var
            design_var_names = obj.design_var_names
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "fitness" in list(init_dict.keys()):
                fitness = init_dict["fitness"]
            if "constraint" in list(init_dict.keys()):
                constraint = init_dict["constraint"]
            if "ngen" in list(init_dict.keys()):
                ngen = init_dict["ngen"]
            if "fitness_names" in list(init_dict.keys()):
                fitness_names = init_dict["fitness_names"]
            if "output_ref" in list(init_dict.keys()):
                output_ref = init_dict["output_ref"]
            if "outputs" in list(init_dict.keys()):
                outputs = init_dict["outputs"]
            if "is_valid" in list(init_dict.keys()):
                is_valid = init_dict["is_valid"]
            if "design_var" in list(init_dict.keys()):
                design_var = init_dict["design_var"]
            if "design_var_names" in list(init_dict.keys()):
                design_var_names = init_dict["design_var_names"]
        # Initialisation by argument
        if fitness == -1:
            fitness = []
        self.fitness = fitness
        if constraint == -1:
            constraint = []
        self.constraint = constraint
        if ngen == -1:
            ngen = []
        self.ngen = ngen
        if fitness_names == -1:
            fitness_names = []
        self.fitness_names = fitness_names
        # Call OutputMulti init
        super(OutputMultiOpti, self).__init__(
            output_ref=output_ref,
            outputs=outputs,
            is_valid=is_valid,
            design_var=design_var,
            design_var_names=design_var_names,
        )
        # The class is frozen (in OutputMulti init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutputMultiOpti_str = ""
        # Get the properties inherited from OutputMulti
        OutputMultiOpti_str += super(OutputMultiOpti, self).__str__()
        OutputMultiOpti_str += (
            "fitness = "
            + linesep
            + str(self.fitness).replace(linesep, linesep + "\t")
            + linesep
        )
        OutputMultiOpti_str += (
            "constraint = "
            + linesep
            + str(self.constraint).replace(linesep, linesep + "\t")
            + linesep
        )
        OutputMultiOpti_str += (
            "ngen = "
            + linesep
            + str(self.ngen).replace(linesep, linesep + "\t")
            + linesep
        )
        OutputMultiOpti_str += (
            "fitness_names = "
            + linesep
            + str(self.fitness_names).replace(linesep, linesep + "\t")
            + linesep
        )
        return OutputMultiOpti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutputMulti
        if not super(OutputMultiOpti, self).__eq__(other):
            return False
        if other.fitness != self.fitness:
            return False
        if other.constraint != self.constraint:
            return False
        if other.ngen != self.ngen:
            return False
        if other.fitness_names != self.fitness_names:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OutputMulti
        OutputMultiOpti_dict = super(OutputMultiOpti, self).as_dict()
        OutputMultiOpti_dict["fitness"] = self.fitness
        OutputMultiOpti_dict["constraint"] = self.constraint
        OutputMultiOpti_dict["ngen"] = self.ngen
        OutputMultiOpti_dict["fitness_names"] = self.fitness_names
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OutputMultiOpti_dict["__class__"] = "OutputMultiOpti"
        return OutputMultiOpti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.fitness = None
        self.constraint = None
        self.ngen = None
        self.fitness_names = None
        # Set to None the properties inherited from OutputMulti
        super(OutputMultiOpti, self)._set_None()

    def _get_fitness(self):
        """getter of fitness"""
        return self._fitness

    def _set_fitness(self, value):
        """setter of fitness"""
        check_var("fitness", value, "list")
        self._fitness = value

    # List of the corresponding output objective values
    # Type : list
    fitness = property(
        fget=_get_fitness,
        fset=_set_fitness,
        doc=u"""List of the corresponding output objective values""",
    )

    def _get_constraint(self):
        """getter of constraint"""
        return self._constraint

    def _set_constraint(self, value):
        """setter of constraint"""
        check_var("constraint", value, "list")
        self._constraint = value

    # List of the corresponding output constraint values
    # Type : list
    constraint = property(
        fget=_get_constraint,
        fset=_set_constraint,
        doc=u"""List of the corresponding output constraint values""",
    )

    def _get_ngen(self):
        """getter of ngen"""
        return self._ngen

    def _set_ngen(self, value):
        """setter of ngen"""
        check_var("ngen", value, "list")
        self._ngen = value

    # Number of generation of the indiv
    # Type : list
    ngen = property(
        fget=_get_ngen, fset=_set_ngen, doc=u"""Number of generation of the indiv"""
    )

    def _get_fitness_names(self):
        """getter of fitness_names"""
        return self._fitness_names

    def _set_fitness_names(self, value):
        """setter of fitness_names"""
        check_var("fitness_names", value, "list")
        self._fitness_names = value

    # Names of the objectives functions
    # Type : list
    fitness_names = property(
        fget=_get_fitness_names,
        fset=_set_fitness_names,
        doc=u"""Names of the objectives functions""",
    )
