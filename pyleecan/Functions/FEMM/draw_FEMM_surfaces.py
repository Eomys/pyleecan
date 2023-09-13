from ...Functions.FEMM import is_eddies
from ...Functions.FEMM.create_FEMM_materials import create_FEMM_materials
from ...Functions.FEMM.assign_FEMM_surface import assign_FEMM_surface
from ...Functions.labels import (
    decode_label,
    get_obj_from_label,
    WIND_LAB,
    HOLEM_LAB,
    MAG_LAB,
    BAR_LAB,
)


def draw_FEMM_surfaces(
    femm,
    machine,
    surf_list,
    FEMM_dict,
    BC_dict,
    Is,
    Ir,
    is_mmfs,
    is_mmfr,
    type_BH_stator,
    type_BH_rotor,
    type_assign=0,
    type_set_BC=0,
    is_draw=True,
):
    """Draw a list of surfaces in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    machine : Machine
        Machine object to draw
    surf_list : list
        List of surfaces to draw
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    BC_dict : dict
        Boundary condition dict ([line label] = BC name)
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
    type_assign : int
        2 to assign all but WIND and MAG, 1 to assign WIND and MAG and 0 to assign all
    type_set_BC : bool
        1 to set BC of the yoke only, 0 to set all
    is_draw : bool
        1 to draw the list of surfaces given
    Returns
    -------
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    """
    # Creation of all the materials and circuit in FEMM
    prop_dict, FEMM_dict = create_FEMM_materials(
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
        j_t0=0,
    )

    # Draw and assign all the surfaces of the machine
    for surf in surf_list:
        label = surf.label

        # Get the correct element size and group according to the label
        surf.draw_FEMM(
            femm=femm,
            nodeprop="None",
            maxseg=FEMM_dict["mesh"]["arcspan"],  # max span of arc element in degrees
            FEMM_dict=FEMM_dict,
            hide=False,
            BC_dict=BC_dict,
            is_draw=is_draw,
            type_set_BC=type_set_BC,
        )

        # Detecting if the property assigned is related to the magnet or the winding
        label_dict = decode_label(label)

        is_mag_wind_lab = (
            WIND_LAB in label_dict["surf_type"]
            or BAR_LAB in label_dict["surf_type"]
            or HOLEM_LAB in label_dict["surf_type"]
            or MAG_LAB in label_dict["surf_type"]
        )

        if (
            type_assign == 0
            or (type_assign == 1 and is_mag_wind_lab)
            or (type_assign == 2 and not is_mag_wind_lab)
        ):
            assign_FEMM_surface(femm, surf, prop_dict[label], FEMM_dict, machine)

    return FEMM_dict
