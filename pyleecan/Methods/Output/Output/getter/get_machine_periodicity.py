# -*- coding: utf-8 -*-
from math import gcd


def get_machine_periodicity(self):
    """Return / Compute the (anti)-periodicities of the machine in time and space domain

    Parameters
    ----------
    self : Output
        An Output object

    Returns
    -------
    per_a : int
        Number of space periodicities of the machine
    is_antisym_a : bool
        True if an anti-periodicity is possible after the space periodicities
    per_t : int
        Number of time periodicities of the machine
    is_antisym_t : bool
        True if an anti-periodicity is possible after the time periodicities
    """
    if (
        self.geo.per_a is None
        or self.geo.is_antiper_a is None
        or self.geo.per_t is None
        or self.geo.is_antiper_t is None
    ):
        (
            self.geo.per_a,
            self.geo.is_antiper_a,
            self.geo.per_t,
            self.geo.is_antiper_t,
        ) = self.simu.machine.comp_periodicity()

    return (
        self.geo.per_a,
        self.geo.is_antiper_a,
        self.geo.per_t,
        self.geo.is_antiper_t,
    )
