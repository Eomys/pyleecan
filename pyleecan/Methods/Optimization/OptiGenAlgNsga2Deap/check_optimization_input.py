from logging import Logger, FileHandler, Formatter, INFO, NOTSET
from datetime import datetime
from ....Classes.OptiObjective import OptiObjective
from ....Classes.OptiDesignVarSet import OptiDesignVarSet
from ....Classes.OptiDesignVarInterval import OptiDesignVarInterval


class OptimizationAttributeError(Exception):
    """Class to Raise an error"""

    def __init__(self, message):
        self.message = message


def check_optimization_input(self):
    """Check optimization parameters before solving the problem

    Parameters
    ----------
    solver : Solver
        solver to perform the genetic algorithm with DEAP
    """

    logger = self.get_logger()

    # Check problem existence
    if self.problem == None:
        raise OptimizationAttributeError(
            "The problem has not been defined, please add a problem to OptiGenAlgNsga2Deap."
        )

    # Check population size
    if self.size_pop % 4 > 0:
        mess = "Change population size from {} to {} to fit with the tournament selection".format(
            self.size_pop, self.size_pop + (self.size_pop % 4)
        )
        self.size_pop += self.size_pop % 4

        logger.warning(mess)

    # Check the problem contains at least one design variable
    if self.problem.obj_func == None or (
        isinstance(self.problem.obj_func, dict) and len(self.problem.obj_func) == 0
    ):
        raise OptimizationAttributeError(
            "Optimization problem must contain at least one objective function"
        )

    else:
        for obj_func in self.problem.obj_func:
            if not isinstance(obj_func, OptiObjective):
                raise TypeError(
                    "Wrong obj_func type: OptiObjective expected, got {}".format(
                        type(obj_func).__name__
                    )
                )
            elif not callable(obj_func.keeper):
                mess = "The objective function '{}' is not callable, please define the attribute 'keeper'.".format(
                    obj_func.name
                )
                raise OptimizationAttributeError(mess)

        # Check if objectives and other datakeepers have different symbol
        if isinstance(self.problem.datakeeper_list, list):
            symbol_list = [of.symbol for of in self.problem.obj_func] + [
                dk.symbol for dk in self.problem.datakeeper_list
            ]
        else:
            symbol_list = [of.symbol for of in self.problem.obj_func]

        if len(symbol_list) != len(set(symbol_list)):
            mess = "Every objective function and datakeeper must have a unique symbol."
            raise OptimizationAttributeError(mess)

    # Check the problem contains at least one objective function
    if self.problem.design_var == None or (
        isinstance(self.problem.design_var, list) and len(self.problem.design_var) == 0
    ):
        raise OptimizationAttributeError(
            "Optimization problem must contain at least one design variable"
        )
    else:
        for design_var in self.problem.design_var:
            if not isinstance(design_var, OptiDesignVarInterval) and not isinstance(
                design_var, OptiDesignVarSet
            ):
                mess = "The design variable '{}' is expected to be an OptiDesignVarSet or an OptiDesignVarInterval.".format(
                    design_var.name
                )
                raise OptimizationAttributeError(mess)
            elif design_var.symbol in [None, ""]:
                mess = "The design variable '{}' has no symbol.".format(design_var.name)
                raise OptimizationAttributeError(mess)
            elif not callable(design_var.get_value):
                mess = "OptiDesignVar '{}' get_value is not callable.".format(
                    design_var.name
                )
                raise OptimizationAttributeError(mess)
            elif not callable(design_var.setter):
                mess = "OptiDesignVar '{}' setter is not callable.".format(
                    design_var.name
                )
                raise OptimizationAttributeError(mess)

    # Check constraints type
    if self.problem.constraint != None:
        for cstr in self.problem.constraint:
            # Check type of constraint
            if cstr.type_const not in ["<=", "<", "==", "=", ">=", ">"]:
                mess = "The constraint '{}' has a wrong type: expected one of {} received '{}'.".format(
                    cstr.name, ["<=", "<", "==", "=", ">=", ">"], cstr.type_const
                )
                raise OptimizationAttributeError(mess)
            # Check getter
            elif not callable(cstr.keeper):
                mess = "The constraint '{}' function keeper is not callable.".format(
                    cstr.name
                )
                raise OptimizationAttributeError(mess)
