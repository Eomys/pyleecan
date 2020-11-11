# -*- coding: utf-8 -*-
# from numpy import exp, pi

# from ...Classes.Arc1 import Arc1
# from ...Classes.Circle import Circle
# from ...Classes.Segment import Segment
# from ...Classes.SurfLine import SurfLine


def get_boundary_condition(line, machine):
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

    # slot_height = machine.stator.slot.comp_height()
    # winding_slot_height = machine.stator.slot.comp_height_wind()

    if "Yoke_Side" in line.label and "Rotor" in line.label:
        label = "Rotor_Side"
    else:
        label = None

    return label
