from numpy import gcd


def comp_periodicity_spatial(self):
    """Compute the (anti)-periodicities of the machine in space domain

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    pera : int
        Number of spatial periodicities of the machine over 2*pi
    is_apera : bool
        True if an anti-periodicity is possible after the periodicities
    """

    p = self.get_pole_pair_number()

    # Get stator (anti)-periodicity in spatial domain
    pera_s, is_antipera_s = self.stator.comp_periodicity_spatial()

    # Get rotor (anti)-periodicities in spatial domain
    pera_r, is_antipera_r = self.rotor.comp_periodicity_spatial()

    # Get machine spatial periodicity
    pera = int(gcd(gcd(pera_s, pera_r), p))

    # Get machine time and spatial anti-periodicities
    is_apera = bool(is_antipera_s and is_antipera_r)

    return pera, is_apera
