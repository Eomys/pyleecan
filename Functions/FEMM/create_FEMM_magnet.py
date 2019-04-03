# -*- coding: utf-8 -*-
"""@package set_FEMM_magnet
@date Created on août 09 17:40 2018
@author franco_i
@TODO: it would be better to have the magnets as input instead of the lamination
"""
import femm
from pyleecan.Classes.LamHole import LamHole


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
    if type(lam) == LamHole:
        if "T0" in label:
            rho = lam.hole[0].magnet_0.mat_type.elec.rho  # Resistivity at 20°C
            Hcm = lam.hole[0].magnet_0.mat_type.mag.Hc  # Magnet coercitivity field
            mur = lam.hole[0].magnet_0.mat_type.mag.mur_lin
            pole_mag = label[6:9] + "_0"
        elif "T1" in label:
            rho = lam.hole[0].magnet_1.mat_type.elec.rho  # Resistivity at 20°C
            Hcm = lam.hole[0].magnet_1.mat_type.mag.Hc  # Magnet coercitivity field
            mur = lam.hole[0].magnet_1.mat_type.mag.mur_lin
            pole_mag = label[6:9] + "_1"
    else:
        rho = lam.slot.magnet[int(label[-4])].mat_type.elec.rho  # Resistivity at 20°C
        Hcm = lam.slot.magnet[int(label[-4])].mat_type.mag.Hc  # Magnet coercitivity field
        mur = lam.slot.magnet[int(label[-4])].mat_type.mag.mur_lin
        pole_mag = "_" + label[12] + "_" + label[-4]
        
    prop = "Magnet" + pole_mag
    if prop not in materials:
        femm.mi_addmaterial(
            prop,
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
        materials.append(prop)

    return prop, materials
