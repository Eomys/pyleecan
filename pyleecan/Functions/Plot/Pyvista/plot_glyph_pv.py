# -*- coding: utf-8 -*-

import numpy as np
from pyvista import UnstructuredGrid

from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_glyph_pv(
    pv_plotter,
    mesh_pv: UnstructuredGrid,
    vect_field: np.ndarray,
    is_point_arrow,
    factor=1,
    phase=1,
):
    """Plot a vector field as arrow (or glyph) using pyvista plotter.

    Parameters
    ----------
    pv_plotter : pyvista.Plotter
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

    field = np.real(vect_field * factor * phase)
    is_nodal_sol = field.shape[0] == mesh_pv.n_points

    # Add field to mesh
    if is_nodal_sol:
        mesh_pv.point_data["field_to_plot"] = field
        mesh_pv.set_active_vectors("field_to_plot", "point")
        if is_point_arrow:
            arrows_plt = mesh_pv.arrows
        else:
            # Convert point_data to cell data
            mesh_cell = mesh_pv.point_data_to_cell_data()
            surf = mesh_cell.extract_geometry()
            centers2 = surf.cell_centers()
            centers2.vectors = surf["field_to_plot"]
            arrows_plt = centers2.arrows

    else:
        mesh_pv.cell_data["field_to_plot"] = field
        mesh_pv.active_vectors_name = "field_to_plot"
        if is_point_arrow:
            mesh_node = mesh_pv.cell_data_to_point_data()
            mesh_node.set_active_vectors("field_to_plot", "cell")
            arrows_plt = mesh_node.arrows

        else:
            cell_centers = mesh_pv.cell_centers()
            cell_centers.set_active_vectors("field_to_plot", "cell")
            arrows_plt = cell_centers.arrows

    pv_plotter.add_mesh(arrows_plt, color="red")
