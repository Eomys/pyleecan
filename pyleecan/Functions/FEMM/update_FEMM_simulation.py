# -*- coding: utf-8 -*-
from numpy import pi

from ...Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop


def update_FEMM_simulation(
    femm,
    circuits,
    is_internal_rotor,
    is_sliding_band,
    angle_rotor,
    Is,
    Ir,
    ii,
):
    """Update the simulation by changing the rotor position and
    updating the currents


    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    circuits :
        Output object
    is_internal_rotor: bool
        True if it is an internal rotor topology
    is_sliding_band: bool
        True if it is an internal rotor topology
    angle_rotor: ndarray
        Vector of rotor angular position over time [Nt,]
    Is : ndarray
        Stator currents function of phase and time [qs,Nt]
    Ir : ndarray
        Rotor currents function of phase and time [qr,Nt]
    ii : int
        Time step index

    """

    if is_sliding_band:  # No rotation without sliding band.
        # Rotor rotation using sliding band
        if is_internal_rotor:
            femm.mi_modifyboundprop("bc_ag2", 10, 180 * angle_rotor[ii] / pi)
        else:
            femm.mi_modifyboundprop("bc_ag2", 11, 180 * angle_rotor[ii] / pi)

    # Update currents
    for label in circuits:
        if "Circs" in label and Is is not None and not all(Is == 0):  # Stator
            set_FEMM_circuit_prop(
                femm,
                circuits,
                label,
                Is[:, ii],
            )
        if "Circr" in label and Ir is not None and not all(Ir == 0):  # Rotor
            set_FEMM_circuit_prop(
                femm,
                circuits,
                label,
                Ir[:, ii],
            )
