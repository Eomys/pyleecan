# -*- coding: utf-8 -*-
"""@package set_FEMM_magnet
@date Created on août 09 17:40 2018
@author franco_i
@TODO: it would be better to have the magnets as input instead of the lamination
@TODO: decision about the magnet renaming, removed at the moment
"""
import femm
from re import findall


def create_FEMM_magnet(label, is_mmf, is_eddies, materials, lam):
    """Set the material of the magnet in FEMM

    Parameters
    ----------
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
    if "HoleMagnet" in label:
        if "T0" in label:
            magnet = lam.hole[0].magnet_0
        elif "T1" in label:
            magnet = lam.hole[0].magnet_1
        elif "T2" in label:
            magnet = lam.hole[0].magnet_2
    else:
        idx_str = findall(r"_T\d+_", label)[0][2:-1]
        magnet = lam.slot.magnet[int(idx_str)]
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
