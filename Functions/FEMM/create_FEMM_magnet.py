# -*- coding: utf-8 -*-
"""@package set_FEMM_magnet
@date Created on août 09 17:40 2018
@author franco_i
@TODO: it would be better to have the magnets as input instead of the lamination
@TODO: decision about the magnet renaming, remove for the moment
"""
import femm
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53


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
    if type(lam) == LamHole:
        if (type(lam.hole[0]) == HoleM50) or (type(lam.hole[0]) == HoleM53):
            if lam.hole[0].magnet_0:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_0
                elif "T1" in label:
                    magnet = lam.hole[0].magnet_1
            else:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_1
        if type(lam.hole[0]) == HoleM51:
            if lam.hole[0].magnet_0 and lam.hole[0].magnet_1:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_0
                elif "T1" in label:
                    magnet = lam.hole[0].magnet_1
                elif "T2" in label:
                    magnet = lam.hole[0].magnet_2
            elif lam.hole[0].magnet_0 and not lam.hole[0].magnet_1:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_0
                elif "T1" in label:
                    magnet = lam.hole[0].magnet_2
            elif not lam.hole[0].magnet_0 and lam.hole[0].magnet_1:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_1
                elif "T1" in label:
                    magnet = lam.hole[0].magnet_2
            else:
                if "T0" in label:
                    magnet = lam.hole[0].magnet_2
    else:
        magnet = lam.slot.magnet[int(label[-4])]
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
