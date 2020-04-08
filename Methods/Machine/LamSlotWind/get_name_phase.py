# -*- coding: utf-8 -*-
from pyleecan.Functions.Winding.gen_phase_list import gen_name


def get_name_phase(self):
    """Return the name of the winding phases

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    name_phase: list
        List with the phase names

    """

    if self.winding is None:
        return list()
    return gen_name(self.winding.qs)
