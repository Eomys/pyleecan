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
    """Plot a vector field as arrow (or glyph) using pyvista plotter.

    Parameters
    ----------
    p : pyvista.Plotter
        a pyvista plotting object
    mesh_pv : UnstructuredGrid
        a pyvista mesh object
    vect_field : ndaray
        field to plot
    is_point_arrow : bool
        True to plot arrows on the nodes
    factor : float
        amplitude factor for vector field
    phase : complex
        coefficient to change the phase of the plot

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
