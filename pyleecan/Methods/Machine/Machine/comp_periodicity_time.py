def comp_periodicity_time(self, slip=0):
    """Compute the (anti)-periodicities of the machine in time domain

    Parameters
    ----------
    self : Machine
        A Machine object
    slip: float
        Rotor asynchronous slip

    Returns
    -------
    pert_S : int
        Number of periodicities of the machine over time period (p/felec by default if Nrev is None) in static referential
    is_apert_S : bool
        True if an anti-periodicity is possible after the periodicities (in static referential)
    pert_R : int
        Number of periodicities of the machine over time period (p/felec by default if Nrev is None) in rotating referential
    is_apert_R : bool
        True if an anti-periodicity is possible after the periodicities (in rotating referential)
    """

    if slip == 0:
        # Rotor and fundamental field rotate synchronously

        # In static referential (stator), rotor (anti)-periodicity in spatial domain
        # becomes (anti)-periodicity in time domain
        pert_S, is_apert_S = self.rotor.comp_periodicity_spatial()

        # In rotating referential (rotor), fundamental field is static so there is no anti-periodicity
        # and periodicity is given by stator spatial periodicity
        pert_R, _ = self.stator.comp_periodicity_spatial()
        is_apert_R = False

    else:
        # In case of non-zero slip, rotor and fundamental field rotates asynchronously
        # so there is no (anti)-periodicity in time domain
        pert_S, is_apert_S, pert_R, is_apert_R = 1, False, 1, False

    return pert_S, is_apert_S, pert_R, is_apert_R
