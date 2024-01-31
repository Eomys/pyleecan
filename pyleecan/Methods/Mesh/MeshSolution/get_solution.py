# -*- coding: utf-8 -*-
from typing import Optional

from ....Classes.Solution import Solution


def get_solution(self, label: Optional[str] = None) -> Solution:
    """Return the solution corresponding to label or the first solution by default.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    label : str
        solution label

    Returns
    -------
    solution: Solution
        a Solution object

    """

    # Return first solution
    if label is None:
        return next(iter(self.values()))

    # Search for the desired solution
    try:
        return self[label]
    except KeyError:
        raise KeyError(
            f'Wrong solution label "{label}", please use one of the following values: {list(self.keys())}.'
        )
