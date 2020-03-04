from logging import Logger, FileHandler, Formatter, INFO, NOTSET
from datetime import datetime


class MissingProblem(Exception):
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

    # Check problem existence
    if self.problem == None:
        raise MissingProblem(
            "The problem has not been defined, please add a problem to OptiGenAlgNsga2Deap."
        )

    # Check population size
    if self.size_pop % 4 > 0:
        mess = "Change population size from {} to {} to fit with the tournament selection".format(
            self.size_pop, self.size_pop + (self.size_pop % 4)
        )
        self.size_pop += self.size_pop % 4
