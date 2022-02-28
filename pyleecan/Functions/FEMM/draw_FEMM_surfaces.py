def draw_FEMM_surfaces():
    """Draw a list of surfaces in pyleecan"""
    # Creation of all the materials and circuit in FEMM
    prop_dict, materials, circuits = create_FEMM_materials(
        femm,
        machine,
        surf_list,
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
            maxseg=FEMM_dict["arcspan"],  # max span of arc element in degrees
            FEMM_dict=FEMM_dict,
            hide=False,
            BC_dict=BC_dict,
        )
        assign_FEMM_surface(femm, surf, prop_dict[label], FEMM_dict, machine)

    FEMM_dict["materials"] = materials
    FEMM_dict["circuits"] = circuits

    return FEMM_dict
