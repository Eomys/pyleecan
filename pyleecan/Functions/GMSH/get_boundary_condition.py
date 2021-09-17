# -*- coding: utf-8 -*-
from ...Functions.labels import BOUNDARY_PROP_LAB


def get_boundary_condition(line, boundary_prop):
    """Returns the boundary name on a line that is used in FEA coupling

    Parameters
    ----------
    line :
        a line with a label

    Returns
    -------
    label : string
        boundary name
    """

    if (
        line.prop_dict
        and BOUNDARY_PROP_LAB in line.prop_dict
        and line.prop_dict[BOUNDARY_PROP_LAB] in boundary_prop
    ):
        return boundary_prop[line.prop_dict[BOUNDARY_PROP_LAB]]
    return ""
