# -*- coding: utf-8 -*-

import pyvista as pv
from numpy import (
    real,
    linspace,
    exp,
    pi,
    argmax,
    zeros,
    hstack,
    sum as np_sum,
    min as np_min,
    max as np_max,
)

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_deflection_animated(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    is_time=False,
    gif_name="animation.gif",
    gif_path="./",
    title="",
    group_names=None,
):
    """Create the gif of the animated operational deflection shape.

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
    gif_name : str
        name of the gif file (should end with .gif)
    gif_path : str
        path where gif will be saved
    group_names : [str]
        plot is restricted to the group(s) corresponding to this list of group names.

    Returns
    -------
    """
    if group_names is not None:
        meshsol_grp = self.get_mesh(group_names)
        meshsol_grp.plot_deflection_animated(
            *args,
            label=label,
            index=index,
            indices=indices,
            clim=clim,
            factor=factor,
            field_name=field_name,
            is_time=is_time,
            gif_name=gif_name,
            gif_path=gif_path,
            title=title,
            group_names=None,
        )
    else:

        # Get mesh and field
        mesh_pv, field, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
            is_radial=True,
        )
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)
        _, vect_field, _ = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
            is_radial=False,
        )

        if is_time:
            field_data = real(field[:, 0])
            vect_field_data = real(vect_field[:, :, 0])
        else:
            field_data = real(field)
            vect_field_data = real(vect_field)

        if field_name is None:
            if label is not None:
                field_name = label
            elif self.get_solution(index=index).label is not None:
                field_name = self.get_solution(index=index).label
            else:
                field_name = "Field"

        # Compute colorbar boundaries
        if clim is None:
            clim = [np_min(real(field)), np_max(real(field))]
            if (clim[1] - clim[0]) / clim[1] < 0.01:
                clim[0] = -abs(clim[1])
                clim[1] = abs(clim[1])

        # Compute deformation factor
        if factor is None:
            # factor = 1 / (100 * clim[1])
            factor = 1 / clim[1] * 10

        # Add third dimension if needed
        solution = self.get_solution(
            label=label,
            index=index,
        )
        if solution.dimension == 2:
            vect_field = hstack((vect_field, zeros((vect_field.shape[0], 1))))
            vect_field_data = hstack(
                (vect_field_data, zeros((vect_field_data.shape[0], 1)))
            )

        # Extract surface
        surf = mesh.get_surf(indices=indices)

        # Add field to surf
        surf.vectors = real(vect_field_data) * factor

        # Warp by vectors
        surf_warp = surf.warp_by_vector()

        # Add radial field
        surf_warp[field_name] = real(field_data)

        # Configure plot
        pv.set_plot_theme("document")
        p = pv.Plotter(notebook=False, title=title)
        sargs = dict(
            interactive=True,
            title_font_size=20,
            label_font_size=16,
            font_family="arial",
            color="black",
        )
        p.add_mesh(
            mesh_pv, color="grey", opacity=1, show_edges=True, edge_color="white"
        )
        p.set_position((0.2, 0.2, 0.5))
        p.reset_camera()
        p.clear()
        p.add_mesh(
            surf_warp,
            scalars=field_name,
            show_edges=False,
            cmap=COLOR_MAP,
            clim=clim,
            scalar_bar_args=sargs,
        )
        p.add_text(title, position="upper_edge")
        p.add_axes()

        p.show(auto_close=False)
        # p.show(use_panel=False, auto_close=False)

        # GIF
        if is_time:
            p.open_gif(gif_path + "/" + gif_name)
            p.clear()
            for tind in range(field.shape[2]):
                field_data = real(field[:, tind])
                vect_field_data = real(vect_field[:, :, tind])
                surf.vectors = vect_field_data * factor
                surf_warp = surf.warp_by_vector()
                surf_warp[field_name] = field_data
                p.add_mesh(
                    surf_warp,
                    scalars=field_name,
                    show_edges=False,
                    cmap=COLOR_MAP,
                    clim=clim,
                    scalar_bar_args=sargs,
                )
                p.add_text(title, position="upper_edge")
                p.write_frame()
                p.clear()

        else:
            nframe = 25
            p.open_gif(gif_path + "/" + gif_name)
            p.clear()
            for t in linspace(0.0, 1.0, nframe + 1)[:nframe]:
                vect_field_data = real(vect_field * exp(1j * 2 * pi * t))
                field_data = real(field * exp(1j * 2 * pi * t))
                surf.vectors = vect_field_data * factor
                surf_warp = surf.warp_by_vector()
                surf_warp[field_name] = field_data
                p.add_mesh(
                    surf_warp,
                    scalars=field_name,
                    show_edges=False,
                    cmap=COLOR_MAP,
                    clim=clim,
                    scalar_bar_args=sargs,
                )
                p.add_text(title, position="upper_edge")
                p.write_frame()
                p.clear()

        # Close movie and delete object
        p.close()
