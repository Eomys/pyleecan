def get_machine_periodicity(self, is_rotor_ref=False):
    """Return / Compute the (anti)-periodicities of the machine in time and space domain

    Parameters
    ----------
    self : Output
        An Output object

    Returns
    -------
    per_a : int
        Number of space periodicities of the machine over 2*pi
    is_antisym_a : bool
        True if an anti-periodicity is possible after the space periodicities
    per_t : int
        Number of time periodicities of the machine over time period (p/felec by default if Nrev is None) in static or rotating referential
    is_antisym_t : bool
        True if an anti-periodicity is possible after the time periodicities (in static or rotating referential)
    """

    if (
        self.geo.per_a is None
        or self.geo.is_antiper_a is None
        or self.geo.per_t_S is None
        or self.geo.is_antiper_t_S is None
        or self.geo.per_t_R is None
        or self.geo.is_antiper_t_R is None
    ):
        # Spatial periodicities
        (
            self.geo.per_a,
            self.geo.is_antiper_a,
        ) = self.simu.machine.comp_periodicity_spatial()

        # Time periodicities in both static and rotating referentials
        (
            self.geo.per_t_S,
            self.geo.is_antiper_t_S,
            self.geo.per_t_R,
            self.geo.is_antiper_t_R,
        ) = self.simu.machine.comp_periodicity_time(slip=self.elec.OP.get_slip())

    if is_rotor_ref:
        return (
            self.geo.per_a,
            self.geo.is_antiper_a,
            self.geo.per_t_R,
            self.geo.is_antiper_t_R,
        )

    else:
        return (
            self.geo.per_a,
            self.geo.is_antiper_a,
            self.geo.per_t_S,
            self.geo.is_antiper_t_S,
        )
