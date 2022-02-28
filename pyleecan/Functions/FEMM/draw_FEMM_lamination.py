from ...Functions.FEMM.draw_FEMM_surfaces import draw_FEMM_surfaces


def draw_FEMM_lamination(lam, sym, femm, transform_list=list(), lam_dxf=None):
    """Draw a Lamination in FEMM

    lam_dxf : DXFImport
        To use a dxf version of the rotor instead of build_geometry
    """

    surf_list = list()

    # adding Both laminations surfaces (or import from DXF)
    if lam_dxf is not None:
        femm.mi_readdxf(lam_dxf.file_path)
        surf_list.extend(lam_dxf.get_surfaces())
    else:
        surf_list.extend(lam.build_geometry(sym=sym, is_circular_radius=True))

    # Applying user defined modifications
    for transform in transform_list:
        for surf in surf_list:
            if transform["label"] in surf.label and transform["type"] == "rotate":
                surf.rotate(transform["value"])
            elif transform["label"] in surf.label and transform["type"] == "translate":
                surf.translate(transform["value"])

    # Draw all the surfaces
    FEMM_dict = draw_FEMM_surfaces(surf_list, FEMM_dict)

    return FEMM_dict
