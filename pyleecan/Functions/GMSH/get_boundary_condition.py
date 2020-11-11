# -*- coding: utf-8 -*-
# from numpy import exp, pi

# from ...Classes.Arc1 import Arc1
# from ...Classes.Circle import Circle
# from ...Classes.Segment import Segment
# from ...Classes.SurfLine import SurfLine

from ...Functions.GMSH import boundary_prop

def get_boundary_condition(line):
    """Returns

    Parameters
    ----------
    sym: int
        Symmetry factor (1= full machine, 2= half of the machine...)
    Rgap_mec_int: float
        Internal lamination mechanic radius
    Rgap_mec_ext: float
        External lamination mechanic radius

    Returns
    -------
    surf_list: list
        List of surface in the airgap including the sliding band surface
    """

    propname = ""
    for bound_label in boundary_prop:
        if bound_label in line.label:
            propname = boundary_prop[bound_label]
        elif line.label.find("Rotor_Yoke_Side") != -1:
            print(line.label)
            propname = boundary_prop["Rotor_Yoke_Side"]
        elif line.label.find("Stator_Yoke_Side") != -1:
            print(line.label)
            propname = boundary_prop["Stator_Yoke_Side"]

    return propname
