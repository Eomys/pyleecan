# -*- coding: utf-8 -*-


def update(indiv):
    """Update the individual output after the mutation

    Parameters
    ----------
        indiv : Individual

    """

    indiv.output = type(indiv.output)(simu=indiv.output.simu.as_dict())

    for k, setter in enumerate(indiv.setter_list):
        setter(indiv.output.simu, indiv[k])

    indiv.is_simu_valid = False
    indiv.cstr_viol = 0

    # Delete the fitness
    del indiv.fitness.values
