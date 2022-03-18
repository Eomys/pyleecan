# -*- coding: utf-8 -*-
from numpy import pi, angle

from ...Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop


def update_FEMM_simulation(
    femm,
    FEMM_dict,
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
    FEMM_dict : dict
        Dictionary containing main FEMM definition / properties
    is_internal_rotor: bool
        True if it is an Internal Rotor topology
    is_sliding_band: bool
        True if it is an Internal Rotor topology
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

    else:
        # Select and rotate rotor groups
        femm.mi_seteditmode("group")
        for key, val in FEMM_dict["groups"].items():
            if "GROUP_R" in key:
                femm.mi_selectgroup(val)
        femm.mi_moverotate(0, 0, 180 * angle_rotor[ii] / pi)

    # Update currents
    if Is is not None or Ir is not None:
        circuits = FEMM_dict["circuits"]
        for label in circuits:
            if "Circs" in label and Is is not None:  # Stator
                set_FEMM_circuit_prop(
                    femm,
                    circuits,
                    label,
                    Is[:, ii],
                )
            if "Circr" in label and Ir is not None:  # Rotor
                set_FEMM_circuit_prop(
                    femm,
                    circuits,
                    label,
                    Ir[:, ii],
                )
