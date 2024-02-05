from typing import Hashable
from pyleecan.Classes.Solution import Solution


def __setitem__(self, label: Hashable, solution: Solution) -> None:
    """Mimic dict behaviour self[__key] = __value"""
    if label in self.solution_dict:
        self.replace_solution(solution, label)
    else:
        self.add_solution(solution, label)
