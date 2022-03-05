# -*- coding: utf-8 -*-
from ..EEC import AbstractClassError


def solve(self):
    """Compute the parameters dict for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC
        an EEC object

    Returns
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    raise AbstractClassError(
        "EEC is an abstract class, please create one of its daughters."
    )
