# -*- coding: utf-8 -*-
from ...Classes.Output import Output


def update(indiv):
    """Update the individual output after the mutation
    
    Parameters
    ----------
        indiv : Individual

    """

    indiv.output = Output(simu=indiv.output.simu.as_dict())

    for k, dv_name in enumerate(indiv.design_var_name_list):
        exec("indiv." + indiv.design_var[dv_name].name + "=indiv[k]")

    indiv.is_simu_valid = False
    indiv.cstr_viol = 0

    # Delete the fitness
    del indiv.fitness.values
