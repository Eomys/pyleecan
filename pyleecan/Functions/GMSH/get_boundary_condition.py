# -*- coding: utf-8 -*-
# from numpy import exp, pi

# from ...Classes.Arc1 import Arc1
# from ...Classes.Circle import Circle
# from ...Classes.Segment import Segment
# from ...Classes.SurfLine import SurfLine


def get_boundary_condition(line, machine):
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

    slot_height = machine.stator.slot.comp_height()
    winding_slot_height = machine.stator.slot.comp_height_active()

    return None
