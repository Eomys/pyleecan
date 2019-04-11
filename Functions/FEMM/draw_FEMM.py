# -*- coding: utf-8 -*-
"""@package draw_FEMM
@date Created on juil. 30 17:34 2018
@author franco_i
"""

import femm
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Functions.FEMM import (
    hidebc,
    is_eddies,
    is_middleag,
    pbtype,
    precision,
    type_yokeS,
)
from pyleecan.Functions.FEMM.assign_FEMM_surface import assign_FEMM_surface
from pyleecan.Functions.FEMM.comp_FEMM_dict import comp_FEMM_dict
from pyleecan.Functions.FEMM.get_mesh_param import get_mesh_param
from pyleecan.Functions.FEMM.create_FEMM_boundary_conditions import (
    create_FEMM_boundary_conditions,
)
from pyleecan.Functions.FEMM.create_FEMM_materials import create_FEMM_materials
from pyleecan.Functions.FEMM.get_sliding_band import get_sliding_band


def draw_FEMM(
    output,
    is_mmfr,
    is_mmfs,
    sym,
    is_antiper,
    type_calc_leakage,
    is_remove_vent=False,
    is_remove_slotS=False,
    is_remove_slotR=False,
    is_stator_linear_BH=False,
    is_rotor_linear_BH=False,
    kgeo_fineness=1,
    kmesh_fineness=1,
    user_FEMM_dict={},
    path_save="FEMM_model.fem",
):
    """Draws and assigns the property of the machine in FEMM
    
    Parameters
    ----------
    output : Output
        Output object
    is_mmfr : bool
        1 to compute the rotor magnetomotive force / rotor
        magnetic field
    is_mmfs : bool
        1 to compute the stator magnetomotive force/stator
        magnetic field
    type_calc_leakage : int
        0 no leakage calculation
        1 calculation using single slot
    is_remove_vent : bool
        True to remove the ventilation ducts in FEMM (Default value = False)
    is_remove_slotS : bool
        True to solve without slot effect on the Stator (Default value = False)
    is_remove_slotR : bool
        True to solve without slot effect on the Rotor (Default value = False)
    is_stator_linear_BH: bool
        1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    is_rotor_linear_BH: bool
        1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    kgeo_fineness : float
        global coefficient to adjust geometry fineness
        in FEMM (1: default ; > 1: finner ; < 1: less fine)
    kmesh_fineness : float
        global coefficient to adjust mesh fineness
        in FEMM (1: default ; > 1: finner ; < 1: less fine)
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
    is_antiper: bool
        To apply antiperiodicity boundary conditions

    Returns
    -------

    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM (including circuits and materials)
    """

    # Initialization from output for readibility
    BHs = output.geo.stator.BH_curve  # Stator B(H) curve
    BHr = output.geo.rotor.BH_curve  # Rotor B(H) curve
    Is = output.elec.Is  # Stator currents waveforms
    Ir = output.elec.Ir  # Rotor currents waveforms
    machine = output.simu.machine

    # Modifiy the machine to match the conditions
    machine = type(machine)(init_dict=machine.as_dict())
    if is_remove_slotR:  # Remove all slots on the rotor
        lam_dict = machine.rotor.as_dict()
        machine.rotor = Lamination(init_dict=lam_dict)
    if is_remove_slotS:  # Remove all slots on the stator
        lam_dict = machine.stator.as_dict()
        machine.stator = Lamination(init_dict=lam_dict)
    if is_remove_vent:  # Remove all ventilations
        machine.rotor.axial_vent = list()
        machine.stator.axial_vent = list()

    # Building geometry of the (modified) stator and the rotor
    surf_list = list()
    lam_ext = machine.get_lamination(is_internal=False)
    lam_int = machine.get_lamination(is_internal=True)
    # adding Internal Lamination surface
    surf_list.extend(lam_int.build_geometry(sym=sym))
    # adding the Airgap surface
    surf_list.extend(
        get_sliding_band(
            sym=sym,
            lam_int=output.simu.machine.get_lamination(True),
            lam_ext=output.simu.machine.get_lamination(False),
        )
    )
    # adding External Lamination surface
    surf_list.extend(lam_ext.build_geometry(sym=sym))

    # Computing parameter (element size, arcspan...) needed to define the simulation
    FEMM_dict = comp_FEMM_dict(
        machine, kgeo_fineness, kmesh_fineness, type_calc_leakage
    )
    FEMM_dict.update(user_FEMM_dict)  # Overwrite some values if needed

    # The package must be initialized with the openfemm command.
    femm.openfemm()

    # We need to create a new Magnetostatics document to work on.
    femm.newdocument(0)

    # Minimize the main window for faster geometry creation.
    femm.main_minimize()

    # defining the problem
    femm.mi_probdef(0, "meters", FEMM_dict["pbtype"], FEMM_dict["precision"])

    # Creation of all the materials and circuit in FEMM
    prop_dict, materials, circuits = create_FEMM_materials(
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
        j_t0=0,
    )
    create_FEMM_boundary_conditions(sym=sym, is_antiper=is_antiper)

    # Draw and assign all the surfaces of the machine
    for surf in surf_list:
        label = surf.label
        # Get the correct element size and group according to the label
        mesh_dict = get_mesh_param(label, FEMM_dict)
        surf.draw_FEMM(
            nodeprop="None",
            maxseg=FEMM_dict["arcspan"],  # max span of arc element in degrees
            propname="None",
            elementsize=mesh_dict["element_size"],
            automesh=mesh_dict["automesh"],
            hide=False,
            group=mesh_dict["group"],
        )
        assign_FEMM_surface(
            surf, prop_dict[label], mesh_dict, machine.rotor, machine.stator
        )

    femm.mi_zoomnatural()  # Zoom out
    femm.mi_probdef(
        FEMM_dict["freqpb"],
        "meters",
        FEMM_dict["pbtype"],
        FEMM_dict["precision"],
        FEMM_dict["Lfemm"],
        FEMM_dict["minangle"],
        FEMM_dict["acsolver"],
    )
    femm.smartmesh(FEMM_dict["smart_mesh"])
    femm.mi_saveas(path_save)  # Save
    # femm.mi_close()

    FEMM_dict["materials"] = materials
    FEMM_dict["circuits"] = circuits

    return FEMM_dict
