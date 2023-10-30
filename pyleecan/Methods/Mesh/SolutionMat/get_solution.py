# -*- coding: utf-8 -*-
from numpy import take, where, array


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

    if set(indice) - set(s_indice):
        logger.warning(
            "At least one input indice is not part of the solution. "
            + "Respective indice will be skipped."
        )

    # skip indice that are not part of the solution
    new_indice = [ii for ii in indice if ii in s_indice]

    # get array index of new_indice
    array_indice = [where(array(s_indice) == ii)[0][0] for ii in new_indice]

    # setup requested solution
    axis_size[Iindice] = len(new_indice)
    new_field_sol = take(field_sol, array_indice, axis=Iindice)

    solution = type(self)(
        label=self.label,
        type_element=self.type_element,
        field=new_field_sol,
        indice=indice,
        axis_name=axis_name,
        axis_size=axis_size,
        dimension=self.dimension,
    )

    return solution
