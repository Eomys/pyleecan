from numpy import zeros
from femm import mo_getcircuitproperties


def comp_FEMM_Phi_wind(qs, Npcpp, is_stator, Lfemm, L1, sym, is_rescale_flux=True):
    """Compure the total fluxlinkage of the winding phases

    Parameters
    ----------
    qs              : number of phases
    Npcpp           : number of parallel circuits per phase (maximum 2p)
    is_stator       : True if windings are stator windings
    Lfemm           : lenght of FEMM model
    L1              : actual lenght for rescaling fluxlinkage 
    sym             : symmetry factor (ie. 1 = full machine, 2 = half machine ...)
    is_rescale_flux : True if rescaling should be applied

    Returns
    -------
    Phi_wind        : float (1x3 ndarray)
        fluxlinkage of the winding phases [Vs]

    """
    Phi_wind = zeros((1, qs))

    if is_stator:
        label = "Circs"
    else:
        label = "Circr"

    # For each phase/circuit
    for q in range(qs):
        PropCirc = mo_getcircuitproperties(label + str(q))
        # rescaling to account for end winding flux
        if is_rescale_flux:
            Kphi = L1 / Lfemm
        else:
            Kphi = 1
        # flux linkage of phase q in Wb=Vs=HA
        Phi_wind[0, q] = sym * PropCirc[2] * Kphi / Npcpp
    return Phi_wind
