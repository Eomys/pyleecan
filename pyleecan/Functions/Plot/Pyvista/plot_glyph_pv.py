# -*- coding: utf-8 -*-


from numpy import (
    real,
    min as np_min,
    max as np_max,
    abs as np_abs,
)


from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_glyph_pv(
    p,
    mesh_pv,
    vect_field,
    is_point_arrow,
    factor=1,
    phase=1,
):
    """Plot the operational deflection shape using pyvista plotter. Made to be called from plot_pyvista.

    Parameters
    ----------

    clim : list
        a list of 2 elements for the limits of the colorbar
    factor : float
        factor to multiply vector field
    field_name : str
        title of the field to display on plot
    is_show_fig : bool
        To call show at the end of the method
    p=None,
    meshsol_list=[],
    plot_list=[],

    Returns
    -------
    """

    # Add field to mesh
    if is_point_arrow:
        mesh_pv.vectors = real(vect_field * factor * phase)
        arrows_plt = mesh_pv.arrows
    else:
        mesh_pv["field"] = real(vect_field * factor * phase)
        mesh_cell = mesh_pv.point_data_to_cell_data()
        surf = mesh_cell.extract_geometry()
        centers2 = surf.cell_centers()
        centers2.vectors = surf["field"] * factor
        arrows_plt = centers2.arrows

    p.add_mesh(arrows_plt, color="red")
