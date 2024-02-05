from typing import Iterator


def __iter__(self) -> Iterator[str]:
    """Mimic dict behaviour"""
    return iter(self.solution_dict)
