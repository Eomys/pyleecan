from typing import Optional

from pyleecan.Classes.Solution import Solution


def pop_solution(self, label: str) -> Solution:
    """Pop a solution from its solution_dict

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

    return self.solution_dict.pop(label)
