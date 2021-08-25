from numpy import gcd


def comp_periodicity_time(self):
    """Compute the (anti)-periodicities of the machine in time domain

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    pert : int
        Number of periodicities of the machine
    is_apert : bool
        True if an anti-periodicity is possible after the periodicities
    """
    # TODO

    # p = self.get_pole_pair_number()

    # # Get stator (anti)-periodicity in spatial domain
    # pera_s, is_antipera_s = self.stator.comp_periodicity_spatial()

    # # Get rotor (anti)-periodicities in spatial domain
    # pera_r, is_antipera_r = self.rotor.comp_periodicity_spatial()

    # # Get machine spatial periodicity
    # pera = int(gcd(gcd(pera_s, pera_r), p))

    # # Get machine time and spatial anti-periodicities
    # is_apera = bool(is_antipera_s and is_antipera_r)

    return pert, is_apert
