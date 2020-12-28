# -*- coding: utf-8 -*-
from numpy import take


def get_solution(self, indice=None):
    """Return a copy of the solution with the option to only include specified indices.

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
    s_indice = self.indice

    Iindice = axis_name.index("indice")

    # create indices of solution if None
    if s_indice is None:
        s_indice = [i for i in range(field_sol.shape[Iindice])]

    # check input indices
    if not indice:
        indice = s_indice
    else:
        max_indice = max(s_indice)
        if max_indice < max(indice):
            logger.warning(
                "Given indices exceed Solution indices. Indices will be truncated."
            )
        indice = [i for i in indice if i <= max_indice]

    # setup requested solution
    axis_size[Iindice] = len(indice)
    new_field_sol = take(field_sol, indice, axis=Iindice)

    solution = type(self)(
        label=self.label,
        type_cell=self.type_cell,
        field=new_field_sol,
        indice=indice,
        axis_name=axis_name,
        axis_size=axis_size,
        dimension=self.dimension,
    )

    return solution
