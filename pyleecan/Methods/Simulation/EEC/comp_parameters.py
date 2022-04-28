# -*- coding: utf-8 -*-
from ..EEC import AbstractClassError


def comp_parameters(self):
    """Compute and set the parameter attributes of the EEC that are not set.

    Parameters
    ----------
    self : EEC
        an EEC object

    """

    raise AbstractClassError(
        "EEC is an abstract class, please create one of its daughters."
    )
