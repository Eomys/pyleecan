# -*- coding: utf-8 -*-

from numpy import pi, sign, sqrt

from ...Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop
from ...Functions.Winding.find_wind_phase_color import get_phase_id
from ...Functions.FEMM.set_FEMM_wind_material import set_FEMM_wind_material


def create_FEMM_circuit_material(
    femm, circuits, label, is_eddies, lam, I, is_mmf, j_t0, materials
):
    """Set in FEMM circuits property

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
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
    wind_mat = lam.winding.get_connection_mat(lam.get_Zs())
    Swire = lam.winding.conductor.comp_surface()

    # Decode the label
    st = label.split("_")
    Nrad_id = int(st[2][1:])  # zone radial coordinate
    Ntan_id = int(st[3][1:])  # zone tangential coordinate
    Zs_id = int(st[4][1:])  # Zone slot number coordinate
    # Get the phase value in the correct slot zone
    q_id = get_phase_id(wind_mat, Nrad_id, Ntan_id, Zs_id)
    s = sign(wind_mat[Nrad_id, Ntan_id, Zs_id, q_id])

    # circuit definition
    if "Rotor" in label:
        Clabel = "Circr" + str(q_id)
    else:
        Clabel = "Circs" + str(q_id)

    circuits = set_FEMM_circuit_prop(femm, circuits, Clabel, I=None)

    # definition of armature field current sources
    if "Rotor" in label:
        Jlabel = "Jr"
    else:
        Jlabel = "Js"
    if s == 1:
        cname = Jlabel + str(q_id) + "+"
    else:
        cname = Jlabel + str(q_id) + "-"

    # circuit definition
    circuits = set_FEMM_circuit_prop(femm, circuits, Clabel, I=None)

    # adding new current source material if necessary
    materials = set_FEMM_wind_material(
        femm,
        materials,
        cname=cname,
        Cduct=is_eddies * 1e-6 / rho,
        dwire=sqrt(4 * Swire / pi) * 1e-3,
    )

    return cname, materials, circuits
