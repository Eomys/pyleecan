# -*- coding: utf-8 -*-

from numpy import linalg as LA, pi, sign, sqrt


def create_FEMM_circuit(femm, label, is_eddies, lam, I, is_mmf, j_t0, materials):
    """Set in FEMM circuits property

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    label :
        label of the surface
    sym :
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
    (str, list)
        the property of the surface having label as surf.label and
        materials
    """

    is_defcirc = 1  # 1 to define circuits (necessary for eddy current loss
    kJ = 1
    # estimation in AC mode, not necessary for magnetostatics)
    Zs = lam.slot.Zs
    rho = lam.mat_type.elec.rho  # Resistivity at 20°C
    wind_mat = lam.winding.comp_connection_mat(Zs)
    # number of parallel circuits  per phase (maximum 2p)
    Npcpp = lam.winding.Npcpp
    Ntcoil = lam.winding.Ntcoil  # number of turns per coil
    Swire = lam.winding.conductor.comp_surface()
    Sact = lam.winding.conductor.comp_active_surface()
    if "Rotor" in label:  # winding on the rotor
        Jlabel = "Jr"
        Clabel = "Circr"
    else:
        Jlabel = "Js"
        Clabel = "Circs"

    st = label.split("_")
    Nr = int(st[1][1:])  # zone radial coordinate
    Nt = int(st[2][1:])  # zone tangential coordinate
    pos = int(st[3][1:])  # Zone slot number coordinate
    A = wind_mat[Nr, Nt, pos, :]

    for zz in range(len(A)):  # search  for the phase of the winding
        if A[zz] != 0:
            q = zz
    # circuit definition
    if is_defcirc:
        if I.size == 0 or LA.norm(I) == 0:
            femm.mi_addcircprop(Clabel + str(q), 0, 1)  # series connected
        else:
            femm.mi_addcircprop(
                Clabel + str(q), is_mmf * I[j_t0][q] / Npcpp, 1
            )  # series connected

    # definition of armature field current sources and  circuits
    s = sign(wind_mat[Nr, Nt, pos, q])  # same as the sign of Cwind1
    if s == 1:
        cname = Jlabel + str(q) + "+"
    else:
        cname = Jlabel + str(q) + "-"

    if LA.norm(I) == 0:
        Jcus = 0
    else:
        # equivalent stator current density [A/mm2]
        Jcus = kJ * 1e-6 * Ntcoil * (I[j_t0, q] / Npcpp) * is_mmf / Sact

    if cname not in materials:
        # adding new current source material if necessary
        femm.mi_addmaterial(
            cname,
            1,
            1,
            0,
            s * Jcus,
            is_eddies * 1e-6 / rho,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            sqrt(4 * Swire / pi),
        )
        materials.append(cname)

    return cname, materials
