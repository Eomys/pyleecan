from ...Functions.FEMM.draw_FEMM_surfaces import draw_FEMM_surfaces


def draw_FEMM_lamination(
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
    is_mmfs=True,
    is_mmfr=True,
    type_BH_stator=0,
    type_BH_rotor=0,
):
    """Draw a Lamination in FEMM

    Parameters
    ----------
    machine : Machine
        Machine object to draw
    lam : Lamination
        Lamination object to draw
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
    femm : FEMMHandler
        client to send command to a FEMM instance
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    transform_list : list
        List of transfromation to apply on the surfaces
    lam_dxf : DXFImport
        To use a dxf version of the Lamination instead of build_geometry
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

    Returns
    -------
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    """

    # Adding lamination surfaces (or import from DXF)
    if lam_dxf is not None:
        femm.mi_readdxf(lam_dxf.file_path)
        surf_list = lam_dxf.get_surfaces()
    else:
        surf_list = lam.build_geometry(sym=sym, is_circular_radius=True)

    # Applying user defined modifications
    for transform in transform_list:
        for surf in surf_list:
            if transform["label"] in surf.label and transform["type"] == "rotate":
                surf.rotate(transform["value"])
            elif transform["label"] in surf.label and transform["type"] == "translate":
                surf.translate(transform["value"])

    # Draw all the lamination related surfaces
    FEMM_dict = draw_FEMM_surfaces(
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
    )

    # Apply BC for DXF import
    if lam_dxf is not None:
        for BC in lam_dxf.BC_list:
            if BC[1] is True:  # Select Arc
                femm.mi_selectarcsegment(BC[0].real, BC[0].imag)
                femm.mi_setarcsegmentprop(
                    FEMM_dict["mesh"]["arcspan"], BC[2], False, None
                )
            else:  # Select Line
                femm.mi_selectsegment(BC[0].real, BC[0].imag)
                femm.mi_setsegmentprop(BC[2], None, None, False, None)
            femm.mi_clearselected()

    return FEMM_dict
