# -*- coding: utf-8 -*-
from numpy import linalg as LA


def set_FEMM_circuit_prop(femm, circuits, Clabel, I, is_mmf, Npcpp, j_t0):
    """Create or update the property of a circuit

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
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
    if Clabel not in circuits:
        # Create new circuit
        femm.mi_addcircprop(Clabel, 0, 1)
        circuits.append(Clabel)

    # Update circuit
    if I is not None and I.size != 0 and LA.norm(I) != 0:
        femm.mi_modifycircprop(Clabel, 1, is_mmf * I[q_id, j_t0] / Npcpp)
    else:
        femm.mi_modifycircprop(Clabel, 1, 0)

    return circuits
