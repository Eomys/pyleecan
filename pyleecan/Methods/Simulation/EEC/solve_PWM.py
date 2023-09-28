# -*- coding: utf-8 -*-
from ..EEC import AbstractClassError


def solve_PWM(self, output):
    """Get stator current harmonics due to PWM harmonics

    Parameters
    ----------
    self : EEC
        an EEC object
    output: Output
        An Output object
    is_dqh_freq: bool
        True to consider frequencies in dqh frame

    Returns
    ------
    Is_PWM : DataFreq
        Stator current harmonics as DataFreq
    """
    raise AbstractClassError(
        "EEC is an abstract class, please create one of its daughters."
    )
