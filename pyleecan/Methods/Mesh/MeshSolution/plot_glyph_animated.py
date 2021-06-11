# -*- coding: utf-8 -*-

import numpy as np
from numpy import (
    real,
    linspace,
    exp,
    pi,
    argmax,
    sum as np_sum,
    max as np_max,
    abs as np_abs,
)
import pyvista as pv

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....Functions.Structural.conversions import pol2cart


def plot_glyph_animated(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    is_time=False,
    is_point_arrow=False,
    gif_name="animation.gif",
    gif_path="./",
    title="",
    group_names=None,
):
    """Plot the vector field as a glyph (or quiver) over the mesh.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    label : str
        a label
    index : int
        an index
    indices : list
        list of the points to extract (optional)
    clim : list
        a list of 2 elements for the limits of the colorbar
    factor : float
        factor to multiply vector field
    field_name : str
        title of the field to display on plot
    save_path : str
        path to save the plot into an image
    is_point_arrow : bool
        to plot a nodal field (point-wise solution required)
    group_names : [str]
        plot is restricted to the group(s) corresponding to this list of group names.


    Returns
    -------
    """
    if group_names is not None:
        meshsol_grp = self.get_group(group_names)
        meshsol_grp.plot_glyph(
            *args,
            label=label,
            index=index,
            indices=indices,
            clim=clim,
            factor=factor,
            field_name=field_name,
            is_time=is_time,
            is_point_arrow=is_point_arrow,
            gif_name=gif_name,
            gif_path=gif_path,
            title=title,
            group_names=None,
        )
    else:

        # Get the mesh and field
        mesh_pv, vect_field, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
        )
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)

        if is_time:
            vect_field_data = real(vect_field[:, :, 0])
        else:
            vect_field_data = real(vect_field)

        if field_name is None:
            if label is not None:
                field_name = label
            elif self.get_solution(index=index).label is not None:
                field_name = self.get_solution(index=index).label
            else:
                field_name = "Field"

        # Compute factor
        if factor is None:
            # factor = 1 / (100 * np_max(np_abs(vect_field)))
            factor = 1 / np_max(vect_field_data) * 10

        # Add third dimension if needed
        solution = self.get_solution(
            label=label,
            index=index,
        )
        if solution.dimension == 2:
            vect_field = np.hstack((vect_field, np.zeros((vect_field.shape[0], 1))))
            vect_field_data = np.hstack(
                (vect_field_data, np.zeros((vect_field_data.shape[0], 1)))
            )

        # Add field to mesh
        if is_point_arrow:
            mesh_pv.vectors = vect_field_data * factor
            arrows_plt = mesh_pv.arrows
        else:
            mesh_pv["field"] = vect_field_data
            mesh_cell = mesh_pv.point_data_to_cell_data()
            surf = mesh_cell.extract_geometry()
            centers2 = surf.cell_centers()
            centers2.vectors = surf["field"] * factor
            arrows_plt = centers2.arrows

        # Configure plot
        pv.set_plot_theme("document")
        p = pv.Plotter(notebook=False)
        p.add_mesh(
            mesh_pv, color="grey", opacity=1, show_edges=True, edge_color="white"
        )
        p.set_position((0.2, 0.2, 0.5))
        p.reset_camera()
        p.add_mesh(arrows_plt, color="red")
        p.add_text(title, position="upper_edge")
        p.add_axes()
        p.show(auto_close=False)
        # p.show(use_panel=False, auto_close=False)

        # GIF
        if is_time:
            p.open_gif(gif_path + "/" + gif_name)
            p.clear()
            for tind in range(vect_field.shape[3]):
                vect_field_data = real(vect_field[:, :, tind])
                if is_point_arrow:
                    mesh_pv.vectors = vect_field_data * factor
                    arrows_plt = mesh_pv.arrows
                else:
                    mesh_pv["field"] = vect_field_data
                    mesh_cell = mesh_pv.point_data_to_cell_data()
                    surf = mesh_cell.extract_geometry()
                    centers2 = surf.cell_centers()
                    centers2.vectors = surf["field"] * factor
                    arrows_plt = centers2.arrows
                p.add_mesh(
                    mesh_pv,
                    color="grey",
                    opacity=1,
                    show_edges=True,
                    edge_color="white",
                )
                p.add_mesh(arrows_plt, color="red")
                p.add_text(title, position="upper_edge")
                p.write_frame()
                p.clear()

        else:
            nframe = 25
            p.open_gif(gif_path + "/" + gif_name)
            p.clear()
            for t in linspace(0.0, 1.0, nframe + 1)[:nframe]:
                vect_field_data = real(vect_field * exp(1j * 2 * pi * t))
                if is_point_arrow:
                    mesh_pv.vectors = vect_field_data * factor
                    arrows_plt = mesh_pv.arrows
                else:
                    mesh_pv["field"] = vect_field_data
                    mesh_cell = mesh_pv.point_data_to_cell_data()
                    surf = mesh_cell.extract_geometry()
                    centers2 = surf.cell_centers()
                    centers2.vectors = surf["field"] * factor
                    arrows_plt = centers2.arrows
                p.add_mesh(
                    mesh_pv,
                    color="grey",
                    opacity=1,
                    show_edges=True,
                    edge_color="white",
                )
                p.add_mesh(arrows_plt, color="red")
                p.add_text(title, position="upper_edge")
                p.write_frame()
                p.clear()

        # Close movie and delete object
        p.close()
