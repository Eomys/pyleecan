# -*- coding: utf-8 -*-
import femm
from numpy import linalg as LA


def set_FEMM_circuit_prop(circuits, Clabel, I, is_mmf, Npcpp, j_t0):
    """Create or update the property of a circuit

    Parameters
    ----------
    circuits: list
        list the name of all circuits
    label: str
        the label of the related surface
    q_id : int
        Index of the phase
    I : Data
        Lamination currents waveforms
    is_mmf: bool
        1 to compute the lamination magnetomotive
        force / lamination magnetic field
    Npcpp: int
        number of parallel circuits  per phase (maximum 2p)
    j_t0 : int
        time step for winding current calculation

    Returns
    -------
    circuits : list
        list the name of the circuits in FEMM

    """

    q_id = int(Clabel[5:])
    if I is not None:
        I = I.values
    if Clabel in circuits:
        if I is not None and I.size != 0 and LA.norm(I) != 0:
            # Update existing circuit
            femm.mi_modifycircprop(Clabel, 1, is_mmf * I[j_t0, q_id] / Npcpp)
    else:
        # Create new circuit
        femm.mi_addcircprop(Clabel, 0, 1)
        circuits.append(Clabel)

    return circuits
