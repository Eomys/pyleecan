# -*- coding: utf-8 -*-
from pyleecan.Classes.Output import Output


def update(indiv):
    """Update the individual output after the mutation"""

    indiv.output = Output(simu=indiv.output.simu.as_dict())

    for k in range(len(indiv.keys)):
        exec("indiv." + indiv.design_var[indiv.keys[k]].name + "=indiv[k]")

    indiv.is_simu_valid = False
    indiv.cstr_viol = 0

    # Delete the fitness
    del indiv.fitness.values
