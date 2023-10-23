# -*- coding: utf-8 -*-


def get_solution(self, label=None):
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

    # Search for the desired solution
    for solution in self.solution:
        if solution.label == label:
            return solution

    if label is not None:
        raise ValueError(
            f"Wrong solution label {label}, please use one of the following values: {[sol.label for sol in self.solution]}."
        )

    return self.solution[0]
