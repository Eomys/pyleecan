# -*- coding: utf-8 -*-

from numpy import exp, pi

from ...Functions.FEMM import GROUP_FM
from ...Functions.FEMM.create_FEMM_bar import create_FEMM_bar
from ...Functions.FEMM.create_FEMM_circuit_material import create_FEMM_circuit_material
from ...Functions.FEMM.create_FEMM_magnet import create_FEMM_magnet


def create_FEMM_materials(
    femm,
    machine,
    surf_list,
    Is,
    Ir,
    BHs,
    BHr,
    is_mmfs,
    is_mmfr,
    type_BH_stator,
    type_BH_rotor,
    is_eddies,
    j_t0,
):
    """Add materials in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
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
    type_BH_stator: int
        2 Infinite permeability, 1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    type_BH_rotor: int
        2 Infinite permeability, 1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
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
        if "Lamination_Stator" in label:  # Stator
            if type_BH_stator == 2:
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
        elif "Lamination_Rotor" in label:  # Rotor
            # Initialisation from the rotor of the machine
            if type_BH_rotor == 2:
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
        elif "Hole_" in label:  # Hole but not HoleMagnet
            # Check if the property already exist in FEMM
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label] = "Air"
        elif "Wind" in label or "Bar" in label:
            I = Is if "Stator" in label else Ir
            is_mmf = is_mmfs if "Stator" in label else is_mmfr
            lam = stator if "Stator" in label else rotor
            prop, materials, circuits = create_FEMM_circuit_material(
                femm, circuits, label, is_eddies, lam, I, is_mmf, j_t0, materials
            )
            prop_dict[label] = prop
        elif "Magnet" in label and "Rotor" in label:  # Rotor Magnet
            prop, materials = create_FEMM_magnet(
                femm, label, is_mmfr, is_eddies, materials, rotor
            )
            prop_dict[label] = prop
        elif "Magnet" in label and "Stator" in label:  # Stator Magnet
            prop, materials = create_FEMM_magnet(
                femm, label, is_mmfs, is_eddies, materials, stator
            )
            prop_dict[label] = prop
        elif "No_mesh" in label:  # Sliding band
            prop_dict[label] = "<No Mesh>"
        elif "Yoke" in label:
            prop_dict[label] = "<No Mesh>"

    # Set Rotor and Stator BH curves (if needed)
    if type_BH_stator == 0:
        for ii in range(BHs.shape[0]):
            femm.mi_addbhpoint("Stator Iron", BHs[ii][1], BHs[ii][0])
    if type_BH_rotor == 0:
        for ii in range(BHr.shape[0]):
            femm.mi_addbhpoint("Rotor Iron", BHr[ii][1], BHr[ii][0])

    return prop_dict, materials, circuits
