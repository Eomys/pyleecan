# -*- coding: utf-8 -*-
from ..EEC import AbstractClassError


def comp_joule_losses(self, out_dict, machine):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : EEC
        an EEC object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    machine : Machine
        a Machine object

    Returns
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    raise AbstractClassError(
        "EEC is an abstract class, please create one of its daughters."
    )
