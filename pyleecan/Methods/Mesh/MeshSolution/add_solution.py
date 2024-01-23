from typing import Optional

from pyleecan.Classes.Solution import Solution


def add_solution(self, solution: Solution, label: Optional[str] = "") -> None:
    """Add a solution to its solution_dict

    Parameters
    ----------
    solution : Solution
        solution to add
    label : Optional[str], optional
        label of the solution, by default ""

    Raises
    ------
    ValueError
        The solution label must be unique
    """
    if not label:
        label = solution.label

    if label in self.keys():
        raise ValueError(f'A solution with label "{label}" is already in MeshSolution.')

    self.solution_dict[label] = solution
