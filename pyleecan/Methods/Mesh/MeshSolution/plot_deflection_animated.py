# -*- coding: utf-8 -*-

import pyvista as pv
from numpy import (
    real,
    linspace,
    exp,
    pi,
    argmax,
    sum as np_sum,
    min as np_min,
    max as np_max,
)

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....definitions import config_dict

COLOR_MAP = config_dict["color_dict"]["COLOR_MAP"]


def plot_deflection_animated(
    self,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    is_time=False,
    ifreq=None,
    gif_name="animation.gif",
    gif_path="./",
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

    Returns
    -------
    """

    # Get the mesh
    mesh = self.get_mesh(label=label, index=index)
    if isinstance(mesh, MeshMat):
        mesh_pv = mesh.get_mesh_pv(indices=indices)
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)

    # Get the field
    field = self.get_field(label=label, index=index, indices=indices, is_radial=True)
    vect_field = self.get_field(label=label, index=index, indices=indices)
    if is_time:
        field_data = real(field[:, 0])
        vect_field_data = real(vect_field[:, :, 0])
    elif len(field.shape) == 2:
        if ifreq is None:
            # Find frequency with highest response
            ifreq = argmax(np_sum(real(field), axis=0))
        field = field[:, ifreq]
        vect_field = vect_field[:, :, ifreq]
        field_data = real(field)
        vect_field_data = real(vect_field)

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

    # Compute deformation factor
    if factor is None:
        factor = 1 / (100 * clim[1])

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
    p = pv.Plotter(notebook=False)
    sargs = dict(
        interactive=True,
        title_font_size=20,
        label_font_size=16,
        font_family="arial",
        color="black",
    )
    p.add_mesh(
        surf_warp,
        scalars=field_name,
        opacity=1,
        show_edges=False,
        cmap=COLOR_MAP,
        clim=clim,
        scalar_bar_args=sargs,
    )
    p.show(use_panel=False, auto_close=False)

    # GIF
    if is_time:
        p.open_gif(gif_path + "/" + gif_name)
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
            p.write_frame()
            p.clear()

    else:
        nframe = 25
        p.open_gif(gif_path + "/" + gif_name)
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
            p.write_frame()
            p.clear()

    # Close movie and delete object
    p.close()
