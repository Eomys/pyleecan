# -*- coding: utf-8 -*-

from ...Classes.Lamination import Lamination
from ...Classes.Circle import Circle
from ...Functions.FEMM import (
    hidebc,
    is_eddies,
    is_middleag,
    pbtype,
    precision,
    type_yokeS,
)
from ...Functions.FEMM.assign_FEMM_surface import assign_FEMM_surface
from ...Functions.FEMM.comp_FEMM_dict import comp_FEMM_dict
from ...Functions.FEMM.create_FEMM_boundary_conditions import (
    create_FEMM_boundary_conditions,
)
from ...Functions.FEMM.create_FEMM_materials import create_FEMM_materials
from ...Functions.FEMM.get_sliding_band import get_sliding_band
from ...Functions.FEMM.get_airgap_surface import get_airgap_surface


def draw_FEMM(
    femm,
    output,
    is_mmfr,
    is_mmfs,
    sym,
    is_antiper,
    type_calc_leakage,
    is_remove_vent=False,
    is_remove_slotS=False,
    is_remove_slotR=False,
    type_BH_stator=0,
    type_BH_rotor=0,
    kgeo_fineness=1,
    kmesh_fineness=1,
    user_FEMM_dict={},
    path_save="FEMM_model.fem",
    is_sliding_band=True,
    transform_list=[],
    rotor_dxf=None,
    stator_dxf=None,
):
    """Draws and assigns the property of the machine in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
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
    type_BH_stator: int
        2 Infinite permeability, 1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
    type_BH_rotor: bool
        2 Infinite permeability, 1 to use linear B(H) curve according to mur_lin, 0 to use the B(H) curve
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
    rotor_dxf : DXFImport
        To use a dxf version of the rotor instead of build_geometry
    stator_dxf : DXFImport
        To use a dxf version of the stator instead of build_geometry

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

    # Computing parameter (element size, arcspan...) needed to define the simulation
    FEMM_dict = comp_FEMM_dict(
        machine, kgeo_fineness, kmesh_fineness, type_calc_leakage
    )
    FEMM_dict.update(user_FEMM_dict)  # Overwrite some values if needed

    # The package must be initialized with the openfemm command.
    try:
        femm.openfemm(1)  # 1 == open in background, 0 == open normally
    except Exception as e:
        raise FEMMError(
            "ERROR: Unable to open FEMM, please check that FEMM is correctly installed\n"
            + str(e)
        )

    # We need to create a new Magnetostatics document to work on.
    femm.newdocument(0)

    # Minimize the main window for faster geometry creation.
    femm.main_minimize()

    # defining the problem
    femm.mi_probdef(0, "meters", FEMM_dict["pbtype"], FEMM_dict["precision"])

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
    lam_list = machine.get_lam_list()
    lam_int = lam_list[0]
    lam_ext = lam_list[1]

    # Adding no_mesh for shaft if needed
    if lam_int.Rint > 0 and sym == 1:
        surf_list.append(Circle(point_ref=0, radius=lam_int.Rint, label="No_mesh"))

    # adding the Airgap surface
    if is_sliding_band:
        surf_list.extend(get_sliding_band(sym=sym, lam_int=lam_int, lam_ext=lam_ext))
    else:
        surf_list.extend(get_airgap_surface(lam_int=lam_int, lam_ext=lam_ext))

    # adding Both laminations surfaces (or import from DXF)
    if rotor_dxf is not None:
        femm.mi_readdxf(rotor_dxf.file_path)
        surf_list.extend(rotor_dxf.get_surfaces())
    else:
        surf_list.extend(machine.rotor.build_geometry(sym=sym))
    if stator_dxf is not None:
        femm.mi_readdxf(stator_dxf.file_path)
        surf_list.extend(stator_dxf.get_surfaces())
    else:
        surf_list.extend(machine.stator.build_geometry(sym=sym))

    # Applying user defined modifications
    for transfrom in transform_list:
        for surf in surf_list:
            if transfrom["label"] in surf.label and transfrom["type"] == "rotate":
                surf.rotate(transfrom["value"])
            elif transfrom["label"] in surf.label and transfrom["type"] == "translate":
                surf.translate(transfrom["value"])

    # Creation of all the materials and circuit in FEMM
    prop_dict, materials, circuits = create_FEMM_materials(
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
        j_t0=0,
    )
    create_FEMM_boundary_conditions(femm=femm, sym=sym, is_antiper=is_antiper)

    # Draw and assign all the surfaces of the machine
    for surf in surf_list:
        label = surf.label
        # Get the correct element size and group according to the label
        surf.draw_FEMM(
            femm=femm,
            nodeprop="None",
            maxseg=FEMM_dict["arcspan"],  # max span of arc element in degrees
            propname="None",
            FEMM_dict=FEMM_dict,
            hide=False,
        )
        assign_FEMM_surface(
            femm, surf, prop_dict[label], FEMM_dict, machine.rotor, machine.stator
        )

    # Apply BC for DXF import
    if rotor_dxf is not None:
        for BC in rotor_dxf.BC_list:
            if BC[1] is True:  # Select Arc
                femm.mi_selectarcsegment(BC[0].real, BC[0].imag)
                femm.mi_setarcsegmentprop(FEMM_dict["arcspan"], BC[2], False, None)
            else:  # Select Line
                femm.mi_selectsegment(BC[0].real, BC[0].imag)
                femm.mi_setsegmentprop(BC[2], None, None, False, None)
            femm.mi_clearselected()

    # femm.mi_zoomnatural()  # Zoom out
    femm.mi_probdef(
        FEMM_dict["freqpb"],
        "meters",
        FEMM_dict["pbtype"],
        FEMM_dict["precision"],
        FEMM_dict["Lfemm"],
        FEMM_dict["minangle"],
        FEMM_dict["acsolver"],
    )
    femm.mi_smartmesh(FEMM_dict["smart_mesh"])
    femm.mi_saveas(path_save)  # Save
    FEMM_dict["path_save"] = path_save
    # femm.mi_close()

    FEMM_dict["materials"] = materials
    FEMM_dict["circuits"] = circuits

    return FEMM_dict


class FEMMError(Exception):
    """Raised when FEMM is not possible to run"""
