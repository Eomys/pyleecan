from logging import Logger, FileHandler, Formatter, INFO, NOTSET
from datetime import datetime


class OptimizationAttributeError(Exception):
    """Class to Raise an error"""

    def __init__(self, message):
        self.message = message


def check_optimization_input(self):
    """ Check optimization parameters before solving the problem

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
        for name, obj_func in self.problem.obj_func.items():
            if not callable(obj_func.func):
                mess = "The objective function '{}' is not callable.".format(name)
                raise OptimizationAttributeError(mess)

    # Check the problem contains at least one objective function
    if self.problem.design_var == None or (
        isinstance(self.problem.design_var, dict) and len(self.problem.design_var) == 0
    ):
        raise OptimizationAttributeError(
            "Optimization problem must contain at least one design variable"
        )
    else:
        for name, design_var in self.problem.design_var.items():
            if design_var.type_var not in ["set", "interval"]:
                mess = 'The design variable \'{}\' has a wrong type_var got {} expected "set" or "interval".'.format(
                    name, design_var.type_var
                )
                raise OptimizationAttributeError(mess)

    # Check constraints type
    if self.problem.constraint != None:
        for name, cstr in self.problem.constraint.items():
            if cstr.type_const not in ["<=", "<", "==", "=", ">=", ">"]:
                mess = "The constraint '{}' has a wrong type: expected one of {} received '{}'.".format(
                    name, ["<=", "<", "==", "=", ">=", ">"], cstr.type_const
                )
                raise OptimizationAttributeError(mess)
