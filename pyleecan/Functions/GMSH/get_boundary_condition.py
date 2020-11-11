# -*- coding: utf-8 -*-
# from numpy import exp, pi

# from ...Classes.Arc1 import Arc1
# from ...Classes.Circle import Circle
# from ...Classes.Segment import Segment
# from ...Classes.SurfLine import SurfLine

from ...Functions.GMSH import boundary_prop


def get_boundary_condition(line):
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
        elif "Rotor_Yoke_Side" in line.label:
            print(line.label)
            propname = boundary_prop["Rotor_Yoke_Side"]
        elif "Stator_Yoke_Side" in line.label:
            print(line.label)
            propname = boundary_prop["Stator_Yoke_Side"]

    return propname
