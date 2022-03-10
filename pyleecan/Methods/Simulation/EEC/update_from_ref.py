# -*- coding: utf-8 -*-
from ..EEC import AbstractClassError


def update_from_ref(self, LUT_ref):
    """Compute and set the parameter attributes of the EEC from a reference LUT

    Parameters
    ----------
    self : EEC
        an EEC object
    LUT_ref : LUTdq
        a LUTdq object

    """

    raise AbstractClassError(
        "EEC is an abstract class, please create one of its daughters."
    )
