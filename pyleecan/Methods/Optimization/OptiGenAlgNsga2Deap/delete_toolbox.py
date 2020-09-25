# -*- coding: utf-8 -*-
from ....Classes.Output import Output
from deap import base, creator, tools


def delete_toolbox(self):
    """OptiGenAlgNsga2Deap method to delete DEAP toolbox
    Parameters
    ----------
    self : OptiGenAlgNsga2Deap
    """

    # Delete toolbox
    self.toolbox = None

    # Delete creator classes
    del creator.FitnessMin
    del creator.Individual