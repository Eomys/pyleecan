# -*- coding: utf-8 -*-


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

    propname = ""
    for bound_label in boundary_prop:
        if bound_label in line.label:
            propname = boundary_prop[bound_label]

    return propname
