# -*- coding: utf-8 -*-
from numpy import take


def get_solution(self, indices=None):
    """Return a copy of the Solution with the option to only include specified indices.

    Parameters
    ----------
    self : SolutionMat
        a SolutionMat object
    indices : list
        list of indices, if list is empty or None all indices are included

    Returns
    -------
    solution: SolutionMat
        solution

    """
    logger = self.get_logger()

    field_sol = self.get_field()
    axis_name, axis_size = self.get_axes_list()

    if not indices:
        indices = self.indices
    else:
        max_indice = max(self.indices)
        if max_indice < max(indices):
            logger.warning(
                "Given indices exceed Solution indices. Indices will be truncated."
            )
        indices = [i for i in indices if i <= max_indice]

    Iindice = axis_name.index("indice")
    axis_size[Iindice] = len(indices)
    new_field_sol = take(field_sol, indices, axis=Iindice)

    solution = type(self)(
        label=self.label,
        type_cell=self.type_cell,
        field=new_field_sol,
        indice=indices,
        axis_name=axis_name,
        axis_size=axis_size,
    )

    return solution
