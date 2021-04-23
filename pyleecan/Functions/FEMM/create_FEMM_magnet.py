# -*- coding: utf-8 -*-
from re import findall


def create_FEMM_magnet(femm, label, is_mmf, is_eddies, materials, lam):
    """Set the material of the magnet in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    label : str
        label of the magnet
    is_mmfr : bool
        1 to compute the lamination magnetomotive force / magnetic field
    is_eddies : bool
        1 to calculate eddy currents
    materials : list
        list of materials already created in FEMM
    lam : LamSlotMag
        Lamination to set the magnet material

    Returns
    -------
    (str, list)
        property, materials

    """
    # some if's and else's to find the correct material parameter from magnet label
    idx_str = findall(r"_T\d+_", label)[0][2:-1]
    if "HoleMagnet" in label:
        magnet_dict = lam.hole[0].get_magnet_dict()
        magnet = magnet_dict["magnet_" + idx_str]
    else:
        magnet = lam.magnet
        # pole_mag = "_" + label[12] + "_" + label[-4]

    rho = magnet.mat_type.elec.rho  # Resistivity at 20°C
    Hcm = magnet.mat_type.mag.Hc  # Magnet coercitivity field
    mur = magnet.mat_type.mag.mur_lin

    if label not in materials:
        femm.mi_addmaterial(
            label,
            mur,
            mur,
            is_mmf * Hcm,
            0,
            is_mmf * is_eddies * 1e-6 / rho,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
        )
        materials.append(label)

    return label, materials
