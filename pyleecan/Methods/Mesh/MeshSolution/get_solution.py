# -*- coding: utf-8 -*-

import numpy as np


def get_solution(
    self, field_name="", field_symbol="", j_t0=None, indice=None, direction=None
):
    """Return the solution corresponding to a time step.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    field_name : strs

    j_t0 : int
        a time step

    Returns
    -------
    solution: Solution
        a Solution object

    """

    field = None

    for sol in self.solution:
        field = sol.get_field(
            field_name=field_name,
            field_symbol=field_symbol,
            j_t0=j_t0,
            indice=indice,
            direction=direction,
        )

        if field is not None:
            return field

    return field
