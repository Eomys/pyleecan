# -*- coding: utf-8 -*-

import numpy as np


def get_solution(self, j_t0=0):
    """Return the solution corresponding to a time step.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    j_t0 : int
        a time step

    Returns
    -------
    solution: Solution
        a Solution object

    """

    return self.solution[j_t0]
