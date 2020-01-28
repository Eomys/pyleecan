# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutputMultiOpti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.OutputMulti import OutputMulti

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Output.OutputMultiOpti.add_evaluation import add_evaluation
except ImportError as error:
    add_evaluation = error

try:
    from pyleecan.Methods.Output.OutputMultiOpti.plot_pareto import plot_pareto
except ImportError as error:
    plot_pareto = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Output import Output


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
    # save method is available in all object
    save = save

    def __init__(
        self,
        fitness=[],
        constraint=[],
        ngen=[],
        output_ref=-1,
        outputs=list(),
        is_valid=[],
        design_var=[],
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if output_ref == -1:
            output_ref = Output()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "fitness",
                    "constraint",
                    "ngen",
                    "output_ref",
                    "outputs",
                    "is_valid",
                    "design_var",
                ],
            )
            # Overwrite default value with init_dict content
            if "fitness" in list(init_dict.keys()):
                fitness = init_dict["fitness"]
            if "constraint" in list(init_dict.keys()):
                constraint = init_dict["constraint"]
            if "ngen" in list(init_dict.keys()):
                ngen = init_dict["ngen"]
            if "output_ref" in list(init_dict.keys()):
                output_ref = init_dict["output_ref"]
            if "outputs" in list(init_dict.keys()):
                outputs = init_dict["outputs"]
            if "is_valid" in list(init_dict.keys()):
                is_valid = init_dict["is_valid"]
            if "design_var" in list(init_dict.keys()):
                design_var = init_dict["design_var"]
        # Initialisation by argument
        self.fitness = fitness
        self.constraint = constraint
        self.ngen = ngen
        # Call OutputMulti init
        super(OutputMultiOpti, self).__init__(
            output_ref=output_ref,
            outputs=outputs,
            is_valid=is_valid,
            design_var=design_var,
        )
        # The class is frozen (in OutputMulti init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutputMultiOpti_str = ""
        # Get the properties inherited from OutputMulti
        OutputMultiOpti_str += super(OutputMultiOpti, self).__str__() + linesep
        OutputMultiOpti_str += "fitness = " + linesep + str(self.fitness) + linesep
        OutputMultiOpti_str += (
            "constraint = " + linesep + str(self.constraint) + linesep
        )
        OutputMultiOpti_str += "ngen = " + linesep + str(self.ngen)
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OutputMulti
        OutputMultiOpti_dict = super(OutputMultiOpti, self).as_dict()
        OutputMultiOpti_dict["fitness"] = self.fitness
        OutputMultiOpti_dict["constraint"] = self.constraint
        OutputMultiOpti_dict["ngen"] = self.ngen
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OutputMultiOpti_dict["__class__"] = "OutputMultiOpti"
        return OutputMultiOpti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.fitness = None
        self.constraint = None
        self.ngen = None
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
