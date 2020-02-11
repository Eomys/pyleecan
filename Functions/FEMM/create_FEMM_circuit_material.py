# -*- coding: utf-8 -*-
"""@package set_FEMM_circuit
@date Created on août 09 17:25 2018
@author franco_i
"""

import femm
from numpy import linalg as LA, pi, sign, sqrt

from pyleecan.Functions.FEMM.comp_FEMM_Jcus import comp_FEMM_Jcus
from pyleecan.Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop
from pyleecan.Functions.Winding.find_wind_phase_color import get_phase_id
from pyleecan.Functions.FEMM.set_FEMM_wind_material import set_FEMM_wind_material


def create_FEMM_circuit_material(
    circuits, label, is_eddies, lam, I, is_mmf, j_t0, materials
):
    """Set in FEMM circuits property
    
    Parameters
    ----------
    circuits: list
        list the name of all circuits
    label : str
        label of the surface
    sym : bool
        integer for symmetry
    is_eddies :
        1 to calculate eddy currents
    lam : LamSlotWind
        Lamination to set the winding
    I : ndarray
        Lamination currents waveforms
    is_mmf :
        1 to compute the lamination magnetomotive
        force / lamination magnetic field
    j_t0 :
        time step for winding current calculation@type integer
    materials :
        list of materials already created in FEMM
    
    Returns
    -------
    property, materials, circuits: tuple
        the property of the surface having label as surf.label (str),
        materials (list) and the circuits (list)
    """

    # Load parameter for readibility
    rho = lam.winding.conductor.cond_mat.elec.rho  # Resistivity at 20°C
    wind_mat = lam.winding.comp_connection_mat(lam.slot.Zs)
    Npcpp = lam.winding.Npcpp  # number of parallel circuits  per phase (maximum 2p)
    Swire = lam.winding.conductor.comp_surface()

    # Decode the label
    st = label.split("_")
    Nrad_id = int(st[1][1:])  # zone radial coordinate
    Ntan_id = int(st[2][1:])  # zone tangential coordinate
    Zs_id = int(st[3][1:])  # Zone slot number coordinate
    # Get the phase value in the correct slot zone
    q_id = get_phase_id(wind_mat, Nrad_id, Ntan_id, Zs_id)
    s = sign(wind_mat[Nrad_id, Ntan_id, Zs_id, q_id])

    # circuit definition
    if "Rotor" in label:
        Clabel = "Circr" + str(q_id)
    else:
        Clabel = "Circs" + str(q_id)
    circuits = set_FEMM_circuit_prop(circuits, Clabel, I, is_mmf, Npcpp, j_t0)

    # definition of armature field current sources
    if "Rotor" in label:
        Jlabel = "Jr"
    else:
        Jlabel = "Js"
    if s == 1:
        cname = Jlabel + str(q_id) + "+"
    else:
        cname = Jlabel + str(q_id) + "-"

    # adding new current source material if necessary
    Jcus = comp_FEMM_Jcus(lam, cname, I, j_t0, is_mmf)
    materials = set_FEMM_wind_material(
        materials, cname, Jcus, is_eddies * 1e-6 / rho, sqrt(4 * Swire / pi)
    )

    return cname, materials, circuits
