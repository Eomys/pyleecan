from ...Functions.FEMM import is_eddies
from ...Functions.FEMM.create_FEMM_materials import create_FEMM_materials
from ...Functions.FEMM.assign_FEMM_surface import assign_FEMM_surface


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
    is_assign=True,
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
    is_assign : bool
        1 to assign the surfaces
    is_draw : bool
        1 to draw the surfaces

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

        if is_draw:
            # Get the correct element size and group according to the label
            surf.draw_FEMM(
                femm=femm,
                nodeprop="None",
                maxseg=FEMM_dict["mesh"][
                    "arcspan"
                ],  # max span of arc element in degrees
                FEMM_dict=FEMM_dict,
                hide=False,
                BC_dict=BC_dict,
            )

        if is_assign:
            assign_FEMM_surface(femm, surf, prop_dict[label], FEMM_dict, machine)

    return FEMM_dict
