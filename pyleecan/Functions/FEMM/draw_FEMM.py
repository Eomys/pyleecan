from ...Classes.Lamination import Lamination
from ...Classes.Circle import Circle

from ...Functions.FEMM.draw_FEMM_lamination import draw_FEMM_lamination
from ...Functions.FEMM.draw_FEMM_surfaces import draw_FEMM_surfaces
from ...Functions.FEMM.comp_FEMM_dict import comp_FEMM_dict
from ...Functions.FEMM.get_sliding_band import get_sliding_band
from ...Functions.FEMM.get_airgap_surface import get_airgap_surface
from ...Functions.labels import NO_MESH_LAB


def draw_FEMM(
    femm,
    output,
    is_mmfr,
    is_mmfs,
    sym,
    is_antiper,
    type_calc_leakage,
    is_remove_ventS=False,
    is_remove_ventR=False,
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
    is_fast_draw=False,
):
    """Draws and assigns the property of the machine in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    output : Output
        Output object
    is_mmfr : bool
        1 to compute the rotor magnetomotive force / rotor magnetic field
    is_mmfs : bool
        1 to compute the stator magnetomotive force/stator magnetic field
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
    is_antiper: bool
        To apply antiperiodicity boundary conditions
    type_calc_leakage : int
        0 no leakage calculation, 1 calculation using single slot
    is_remove_ventS : bool
        True to remove the ventilation ducts on stator in FEMM (Default value = False)
    is_remove_ventR : bool
        True to remove the ventilation ducts on rotor in FEMM (Default value = False)
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
    user_FEMM_dict : dict
        To enforce parameters in the FEMM_dict
    path_save : str
        Path to save resulting fem file
    is_sliding_band : bool
        True to use sliding band else use airgap surface
    transform_list : list
        List of transfromation to apply on the surfaces
    rotor_dxf : DXFImport
        To use a dxf version of the rotor instead of build_geometry
    stator_dxf : DXFImport
        To use a dxf version of the stator instead of build_geometry
    is_fast_draw : bool
        True to use lamination symetry to accelerate the drawing of the machine

    Returns
    -------
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM (including circuits and materials)
    """

    # Initialization from output for readibility
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
    # femm.main_minimize()

    # defining the problem
    femm.mi_probdef(
        0, "meters", FEMM_dict["simu"]["pbtype"], FEMM_dict["simu"]["precision"]
    )

    # Modifiy the machine to match the conditions
    machine_edit = machine.copy()
    if is_remove_slotR:  # Remove all slots on the rotor
        lam_dict = machine_edit.rotor.as_dict()
        machine_edit.rotor = Lamination(init_dict=lam_dict)
    if is_remove_slotS:  # Remove all slots on the stator
        lam_dict = machine_edit.stator.as_dict()
        machine_edit.stator = Lamination(init_dict=lam_dict)
    # Remove ventilations
    if is_remove_ventR:
        for lam in machine_edit.get_lam_list(is_int_to_ext=True):
            if not lam.is_stator:
                lam.axial_vent = list()
    if is_remove_ventS:
        for lam in machine_edit.get_lam_list(is_int_to_ext=True):
            if lam.is_stator:
                lam.axial_vent = list()

    # Lamination list organized from interior to exterior
    lam_list = machine_edit.get_lam_list(is_int_to_ext=True)

    # Init Boundary condition dict (will be filled while drawing Surface/Lines)
    BC_dict = {"sym": sym, "is_antiper": is_antiper}

    # Draw all the laminations
    for lam in lam_list:
        if lam.is_stator:
            lam_dxf = stator_dxf
        else:
            lam_dxf = rotor_dxf
        FEMM_dict = draw_FEMM_lamination(
            machine,
            lam,
            sym,
            femm,
            FEMM_dict,
            transform_list,
            lam_dxf,
            BC_dict,
            Is,
            Ir,
            is_mmfs,
            is_mmfr,
            type_BH_stator,
            type_BH_rotor,
            is_fast_draw,
        )

    # List of the Non lamination related surfaces
    other_surf_list = list()

    # Adding no_mesh for shaft if needed
    if lam_list[0].Rint > 0 and sym == 1:
        label_int = lam_list[0].get_label()
        other_surf_list.append(
            Circle(
                point_ref=0,
                radius=lam_list[0].Rint,
                label=label_int + "_" + NO_MESH_LAB,
            )
        )

    # Adding the Airgap surface
    for ii in range(len(lam_list) - 1):
        if is_sliding_band:
            other_surf_list.extend(
                get_sliding_band(
                    sym=sym, lam_int=lam_list[ii], lam_ext=lam_list[ii + 1]
                )
            )
        else:
            other_surf_list.extend(
                get_airgap_surface(lam_int=lam_list[ii], lam_ext=lam_list[ii + 1])
            )

    # Draw the surfaces not related to lamination
    draw_FEMM_surfaces(
        femm,
        machine,
        other_surf_list,
        FEMM_dict,
        BC_dict,
        Is,
        Ir,
        is_mmfs,
        is_mmfr,
        type_BH_stator,
        type_BH_rotor,
    )

    # Define simulation parameters
    # femm.mi_zoomnatural()  # Zoom out
    femm.mi_probdef(
        FEMM_dict["simu"]["freqpb"],
        "meters",
        FEMM_dict["simu"]["pbtype"],
        FEMM_dict["simu"]["precision"],
        FEMM_dict["simu"]["Lfemm"],
        FEMM_dict["simu"]["minangle"],
        FEMM_dict["simu"]["acsolver"],
    )
    femm.mi_smartmesh(FEMM_dict["mesh"]["smart_mesh"])
    if path_save is not None:
        output.get_logger().debug("Saving FEMM file at: " + path_save)
        femm.mi_saveas(path_save)  # Save
        FEMM_dict["path_save"] = path_save
        # femm.mi_close()

    return FEMM_dict


class FEMMError(Exception):
    """Raised when FEMM is not possible to run"""

    pass
