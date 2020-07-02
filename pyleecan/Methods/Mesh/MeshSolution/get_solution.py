# -*- coding: utf-8 -*-


def get_solution(self, label=None, index=None):
    """Return the solution corresponding to label or an index.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    label : str
        a label
    index : int
        an index

    Returns
    -------
    solution: Solution
        a Solution object

    """

    if index is None:
        index = 0
        if label is not None:
            for i, solution in enumerate(self.solution):
                if solution.label == label:
                    index = i
    return self.solution[index]
