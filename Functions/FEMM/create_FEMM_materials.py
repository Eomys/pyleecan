# -*- coding: utf-8 -*-
"""@package set_FEMM_materials
@date Created on août 06 17:04 2018
@author franco_i
"""

import femm
from numpy import exp, pi

from pyleecan.Functions.FEMM import GROUP_FM
from pyleecan.Functions.FEMM.create_FEMM_bar import create_FEMM_bar
from pyleecan.Functions.FEMM.create_FEMM_circuit_material import (
    create_FEMM_circuit_material,
)
from pyleecan.Functions.FEMM.create_FEMM_magnet import create_FEMM_magnet


def create_FEMM_materials(
    machine,
    surf_list,
    Is,
    Ir,
    BHs,
    BHr,
    is_mmfs,
    is_mmfr,
    is_stator_linear_BH,
    is_rotor_linear_BH,
    is_eddies,
    j_t0,
):
    """Add materials in FEMM

    Parameters
    ----------
    machine : Machine
        the machine to simulate
    surf_list : list
        List of surface of the machine
    Is : ndarray
        Stator current matrix [A]
    Ir : ndarray
        Rotor current matrix [A]
    BHs: ndarray
        B(H) curve of the stator
    BHr: ndarray
        B(H) curve of the rotor
    is_mmfs : bool
        1 to compute the stator magnetomotive force/stator magnetic field
    is_mmfr : bool
        1 to compute the rotor magnetomotive force / rotor magnetic field
    is_stator_linear_BH: bool
        1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    is_rotor_linear_BH: bool
        1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    is_eddies : bool
        1 to calculate eddy currents
    jt_0 : int
        Current time step for winding calculation
    
    Returns
    -------
    Tuple: dict, list
        Dictionary of properties and list containing the name of the circuits created
    """

    prop_dict = dict()  # Initialisation of the dictionnary to return

    rotor = machine.rotor
    stator = machine.stator

    materials = list()
    circuits = list()
    # Starting creation of properties for each surface of the machine
    for surf in surf_list:
        label = surf.label
        if "Lamination_Stator_bore" in label:  # Stator
            if is_stator_linear_BH == 2:
                mu_is = 100000  # Infinite permeability
            else:
                mu_is = stator.mat_type.mag.mur_lin  # Relative
            # Check if the property already exist in FEMM
            if "Stator Iron" not in materials:
                # magnetic permeability
                femm.mi_addmaterial(
                    "Stator Iron", mu_is, mu_is, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
                )
                materials.append("Stator Iron")
            prop_dict[label] = "Stator Iron"
        elif "Lamination_Rotor_bore" in label:  # Rotor
            # Initialisation from the rotor of the machine
            if is_rotor_linear_BH == 2:
                mu_ir = 100000  # Infinite permeability
            else:
                mu_ir = rotor.mat_type.mag.mur_lin  # Relative
            # Check if the property already exist in FEMM
            if "Rotor Iron" not in materials:
                # magnetic permeability
                femm.mi_addmaterial(
                    "Rotor Iron", mu_ir, mu_ir, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
                )
                materials.append("Rotor Iron")
            prop_dict[label] = "Rotor Iron"
        elif "Airgap" in label:  # Airgap surface
            if "Airgap" not in materials:
                femm.mi_addmaterial("Airgap", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Airgap")
            prop_dict[label] = "Airgap"
        elif "Ventilation" in label:  # Ventilation
            # Check if the property already exist in FEMM
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label] = "Air"
        elif "Bar" in label:  # Squirrel cage
            prop, materials = create_FEMM_bar(
                is_mmfr, rotor.mat_type.elec.rho, materials
            )
            prop_dict[label] = prop
        elif "WindR" in label:  # Rotor Winding
            prop, materials, circuits = create_FEMM_circuit_material(
                circuits, label, is_eddies, rotor, Ir, is_mmfr, j_t0, materials
            )
            prop_dict[label] = prop
        elif "WindS" in label:  # Stator Winding
            prop, materials, circuits = create_FEMM_circuit_material(
                circuits, label, is_eddies, stator, Is, is_mmfs, j_t0, materials
            )
            prop_dict[label] = prop
        elif "Magnet" in label and "Rotor" in label:  # Rotor Magnet
            prop, materials = create_FEMM_magnet(
                label, is_mmfr, is_eddies, materials, rotor
            )
            prop_dict[label] = prop
        elif "Magnet" in label and "Stator" in label:  # Stator Magnet
            prop, materials = create_FEMM_magnet(
                label, is_mmfs, is_eddies, materials, stator
            )
            prop_dict[label] = prop
        elif "No_mesh" in label:  # Sliding band
            prop_dict[label] = None
        elif "yoke" in label:
            prop_dict[label] = "<No Mesh>"

    # Set Rotor and Stator BH curves (if needed)
    if is_stator_linear_BH == 0:
        for ii in range(BHs.shape[0]):
            femm.mi_addbhpoint("Stator Iron", BHs[ii][0], BHs[ii][1])
    if is_rotor_linear_BH == 0:
        for ii in range(BHr.shape[0]):
            femm.mi_addbhpoint("Rotor Iron", BHr[ii][0], BHr[ii][1])

    return prop_dict, materials, circuits
