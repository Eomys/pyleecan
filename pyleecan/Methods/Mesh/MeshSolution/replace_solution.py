from typing import Optional

from pyleecan.Classes.Solution import Solution


def replace_solution(self, solution: Solution, label: Optional[str] = ""):
    """Replace the solution in the solution_didct

    Parameters
    ----------
    solution : Solution
        solution to insert
    label : Optional[str], optional
        label of the solution corresponding , by default ""
    """
    if not label:
        label = solution.label

    self[label] = solution
