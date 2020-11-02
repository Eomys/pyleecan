# -*- coding: utf-8 -*-


def set_FEMM_circuit_prop(femm, circuits, Clabel, I=None):
    """Create or update the property of a circuit

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    circuits: list
        list the name of all circuits
    Clabel: str
        the label of the circuit surface
    q_id : int
        Index of the phase
    I : ndarray
        Lamination currents for given time step and for all phases [qs,1]

    Returns
    -------
    circuits : list
        list the name of the circuits in FEMM

    """
    
    # Find phase index of current surface label
    q_id = int(Clabel[5:])

    if Clabel not in circuits:
        # Create new circuit
        femm.mi_addcircprop(Clabel, 0, 1)
        circuits.append(Clabel)

    # Update circuit
    if I is not None:
        femm.mi_modifycircprop(Clabel, 1, I[q_id])
    else:
        femm.mi_modifycircprop(Clabel, 1, 0)

    return circuits
