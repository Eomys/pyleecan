# -*- coding: utf-8 -*-

import numpy as np
from numpy import real, linspace, exp, pi, argmax, sum as np_sum, max as np_max
import pyvista as pv

from ....Classes.MeshMat import MeshMat
from ....Functions.Structural.conversions import pol2cart


def plot_glyph_animated(
    self,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    is_time=False,
    is_point_arrow=False,
    ifreq=None,
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
    ifreq : int
        index of the frequency to use for plot (if exists)
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
            label,
            index,
            indices,
            clim,
            factor,
            field_name,
            is_time,
            is_point_arrow,
            ifreq,
            gif_name,
            gif_path,
            title,
            None,
        )
    else:

        # Get the mesh
        mesh = self.get_mesh(label=label, index=index)
        mesh_pv = mesh.get_mesh_pv(indices=indices)

        # Get the field
        solution = self.get_solution(label=label)
        points = mesh.get_point()
        points = np.column_stack((points, np.zeros(63612)))
        result = solution.field.get_rphiz_along("freqs=[0,5000]", "indice")
        field_pol = np.column_stack(
            (result["radial"][1, :], result["tangential"][1, :], result["axial"][1, :])
        )
        vect_field = pol2cart(field_pol, points)
        vect_field_data = real(vect_field)

        # vect_field = self.get_field(label=label, index=index, indices=indices)
        # if is_time:
        #     vect_field_data = real(vect_field[:, :, 0])
        # elif len(vect_field.shape) == 3:
        #     if ifreq is None:
        #         # Find frequency with highest response
        #         ifreq = argmax(np_sum(real(vect_field)))
        #     vect_field = vect_field[:, :, ifreq]
        #     vect_field_data = real(vect_field)

        # else:
        #     vect_field_data = real(vect_field)
        if field_name is None:
            if label is not None:
                field_name = label
            elif self.get_solution(index=index).label is not None:
                field_name = self.get_solution(index=index).label
            else:
                field_name = "Field"

        # Compute factor
        if factor is None:
            factor = 1 / (100 * np_max(vect_field))

        # if self.dimension == 2:
        #     vect_field = np.hstack((vect_field, np.zeros((vect_field.shape[0], 1))))

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
        p.add_mesh(arrows_plt, color="red")
        p.add_text(title, position="upper_edge")
        p.show(use_panel=False, auto_close=False)

        # GIF
        if is_time:
            p.open_gif(gif_path + "/" + gif_name)
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
