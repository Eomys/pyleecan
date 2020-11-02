# -*- coding: utf-8 -*-
from numpy import pi

from ...Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop


def update_FEMM_simulation(
    femm, circuits, is_internal_rotor, is_sliding_band, angle_rotor, Is, Ir, 
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
        Stator currents for given time step and for all phases [qs,1]
    Ir : ndarray
        Rotor currents for given time step and for all phases [qr,1]       
        
    """ 

    if is_sliding_band:  # No rotation without sliding band.
        # Rotor rotation using sliding band
        if is_internal_rotor:
            femm.mi_modifyboundprop("bc_ag2", 10, 180 * angle_rotor / pi)
        else:
            femm.mi_modifyboundprop("bc_ag2", 11, 180 * angle_rotor / pi)
            
    # Update currents
    for label in circuits:
        if "Circs" in label:  # Stator
            set_FEMM_circuit_prop(
                femm,
                circuits,
                label,
                Is,
            )
        if "Circr" in label:  # Rotor
            set_FEMM_circuit_prop(
                femm,
                circuits,
                label,
                Ir,
            )
