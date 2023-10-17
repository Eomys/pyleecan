from ...Functions.FEMM.create_FEMM_circuit_material import create_FEMM_circuit_material
from ...Functions.FEMM.create_FEMM_magnet import create_FEMM_magnet
from ...Functions.labels import (
    LAM_LAB,
    STATOR_LAB,
    ROTOR_LAB,
    AIRGAP_LAB,
    VENT_LAB,
    NOTCH_LAB,
    HOLEV_LAB,
    HOLEM_LAB,
    MAG_LAB,
    SOP_LAB,
    KEY_LAB,
    WEDGE_LAB,
    WIND_LAB,
    BAR_LAB,
    SLID_LAB,
    NO_MESH_LAB,
    get_obj_from_label,
    decode_label,
)
from ...Functions.FEMM import LAM_MAT_NAME
from ...Classes.ImportMatrix import ImportMatrix


def create_FEMM_materials(
    femm,
    machine,
    surf_list,
    FEMM_dict,
    Is,
    Ir,
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
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    Is : ndarray
        Stator current matrix [A]
    Ir : ndarray
        Rotor current matrix [A]
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
    prop_dict, FEMM_dict : (dict, dict)
        Dictionary of properties and dictionary containing the main parameters of FEMM
    """

    prop_dict = dict()  # Initialisation of the dictionary to return

    rotor = machine.rotor
    stator = machine.stator

    materials = FEMM_dict["materials"]
    circuits = FEMM_dict["circuits"]
    # Starting creation of properties for each surface of the machine
    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if LAM_LAB in label_dict["surf_type"] and STATOR_LAB in label_dict["lam_type"]:
            lam_obj = get_obj_from_label(machine, label_dict=label_dict)
            mat_name = label_dict["lam_label"] + " " + LAM_MAT_NAME
            if type_BH_stator == 2:
                mu_is = 100000  # Infinite permeability
            else:
                mu_is = lam_obj.mat_type.mag.mur_lin  # Relative
            # Check if the property already exist in FEMM
            if mat_name not in materials:
                # magnetic permeability
                femm.mi_addmaterial(
                    mat_name, mu_is, mu_is, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
                )
                if type_BH_stator == 0:
                    BHs = lam_obj.mat_type.mag.get_BH()
                    add_BH_curve(femm, BHs, mat_name)
                materials.append(mat_name)
            prop_dict[label_dict["full"]] = mat_name
        elif LAM_LAB in label_dict["surf_type"] and ROTOR_LAB in label_dict["lam_type"]:
            lam_obj = get_obj_from_label(machine, label_dict=label_dict)
            mat_name = label_dict["lam_label"] + " " + LAM_MAT_NAME
            # Initialisation from the rotor of the machine
            if type_BH_rotor == 2:
                mu_ir = 100000  # Infinite permeability
            else:
                mu_ir = rotor.mat_type.mag.mur_lin  # Relative
            # Check if the property already exist in FEMM
            if mat_name not in materials:
                # magnetic permeability
                femm.mi_addmaterial(
                    mat_name, mu_ir, mu_ir, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
                )
                if type_BH_rotor == 0:
                    BHr = lam_obj.mat_type.mag.get_BH()
                    add_BH_curve(femm, BHr, mat_name)
                materials.append(mat_name)
            prop_dict[label_dict["full"]] = mat_name
        elif (
            AIRGAP_LAB in label_dict["surf_type"] or SLID_LAB in label_dict["surf_type"]
        ):
            # Airgap surface
            if "Airgap" not in materials:
                femm.mi_addmaterial("Airgap", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Airgap")
            prop_dict[label_dict["full"]] = "Airgap"
        elif SOP_LAB in label_dict["surf_type"]:  # Slot opening
            # Assigning air to the slot opening
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label_dict["full"]] = "Air"
        elif WEDGE_LAB in label_dict["surf_type"]:  # Wedge
            # Get the material used for the wedge
            if STATOR_LAB in label_dict["lam_type"]:
                wedge_mat = stator.slot.wedge_mat
                lam_mat = stator.mat_type
            elif ROTOR_LAB in label_dict["lam_type"]:
                wedge_mat = rotor.slot.wedge_mat
                lam_mat = rotor.mat_type
            mat_name = wedge_mat.name
            # Check if the wedge has the same material as the lamination
            if mat_name == lam_mat.name:
                mat_name = label_dict["lam_label"] + " " + LAM_MAT_NAME
            elif mat_name not in materials:
                # Create material if it doesn't already exist
                femm.mi_addmaterial(
                    mat_name,
                    wedge_mat.mag.mur_lin,
                    wedge_mat.mag.mur_lin,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                )
                if wedge_mat.mag.BH_curve is not None and not isinstance(
                    wedge_mat.mag.BH_curve, ImportMatrix  # abstract class
                ):
                    BH = wedge_mat.mag.BH_curve.get_data()
                    add_BH_curve(femm, BH, wedge_mat.name)
                materials.append(mat_name)
            prop_dict[label_dict["full"]] = mat_name
        elif NOTCH_LAB in label_dict["surf_type"]:  # Notches
            # Same material as Airgap but different mesh
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label_dict["full"]] = "Air"
        elif KEY_LAB in label_dict["surf_type"]:  # Key in notches
            # Get the material used for the wedge
            key_mat = get_obj_from_label(machine, label_dict=label_dict)
            mat_name = key_mat.name
            # Check if the key has the same material as the lamination
            if STATOR_LAB in label_dict["lam_type"]:
                lam_mat = stator.mat_type
            elif ROTOR_LAB in label_dict["lam_type"]:
                lam_mat = rotor.mat_type
            if mat_name == lam_mat.name:
                mat_name = label_dict["lam_label"] + " " + LAM_MAT_NAME
            elif mat_name not in materials:
                # Create material if it doesn't already exist
                femm.mi_addmaterial(
                    mat_name,
                    key_mat.mag.mur_lin,
                    key_mat.mag.mur_lin,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                )
                if (
                    key_mat.mag.BH_curve is not None
                    and not type(key_mat.mag.BH_curve) is ImportMatrix  # abstract class
                ):
                    BH = key_mat.mag.BH_curve.get_data()
                    add_BH_curve(femm, BH, key_mat.name)
                materials.append(mat_name)
            prop_dict[label_dict["full"]] = mat_name
        elif VENT_LAB in label_dict["surf_type"]:  # Ventilation
            vent = get_obj_from_label(machine, label_dict=label_dict)
            material = vent.mat_void
            # Check if the property already exist in FEMM
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label_dict["full"]] = "Air"
        elif HOLEV_LAB in label_dict["surf_type"]:  # Hole Void
            hole = get_obj_from_label(machine, label_dict=label_dict)
            material = hole.mat_void
            # Check if the property already exist in FEMM
            if "Air" not in materials:
                femm.mi_addmaterial("Air", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                materials.append("Air")
            prop_dict[label_dict["full"]] = "Air"
        elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
            is_stator = STATOR_LAB in label_dict["lam_type"]
            I = Is if is_stator else Ir
            is_mmf = is_mmfs if is_stator else is_mmfr
            lam_obj = get_obj_from_label(machine, label_dict=label_dict)
            prop, materials, circuits = create_FEMM_circuit_material(
                femm,
                circuits,
                label_dict,
                is_eddies,
                lam_obj,
                I,
                is_mmf,
                j_t0,
                materials,
            )
            prop_dict[label_dict["full"]] = prop
        elif MAG_LAB in label_dict["surf_type"] or HOLEM_LAB in label_dict["surf_type"]:
            T_mag = FEMM_dict["simu"]["T_mag"]
            is_stator = STATOR_LAB in label_dict["lam_type"]
            is_mmf = is_mmfs if is_stator else is_mmfr
            mag_obj = get_obj_from_label(machine, label_dict=label_dict)
            prop, materials = create_FEMM_magnet(
                femm, is_mmf, is_eddies, materials, mag_obj, T_mag
            )
            prop_dict[label_dict["full"]] = prop
        elif NO_MESH_LAB in label_dict["surf_type"]:
            prop_dict[label_dict["full"]] = "<No Mesh>"
        else:
            raise Exception("Unknown label " + label_dict["full"])

    FEMM_dict["materials"] = materials
    FEMM_dict["circuits"] = circuits
    return prop_dict, FEMM_dict


def add_BH_curve(femm, BH, mat_name):
    """Add the BH curve of a lamination on femm

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    BH : ndarray
        BH curve of the material
    mat_name : string
        material name
    """
    if BH is not None and BH.shape[0] > 1:
        for B, H in BH:
            femm.mi_addbhpoint(mat_name, H, B)
