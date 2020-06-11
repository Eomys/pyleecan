# -*- coding: utf-8 -*-

import pyvista as pv
from numpy import rollaxis, take


def plot_deformation_animated(
    self, field, Nt_tot, indices=[], factor=1, gif_name="animation.gif", gif_path="./"
):
    """Plot a vector field as glyphs over a mesh.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    field : ndarray
        array of the field
    Nt_tot : int
        number of time steps (and frames)
    indices : list
        list of the points to extract (optional)
    factor : float
        factor to multiply the field vectors for visualization
    gif_name : str
        name of the gif file
    gif_path : str
        path where to save the gif

    Returns
    -------
    """

    # Get the mesh
    mesh = self.get_mesh(indices)

    # Time must be the last dimension
    if field.shape[-1] != Nt_tot:
        field = rollaxis(field, 0, field.ndim)

    # Extract subset of the field if necessary
    if indices != [] and take(field, 0, axis=-1).shape != indices.shape:
        field = field[indices]

    # Add field to mesh
    mesh.vectors = field

    # Warp by vectors
    mesh_warp = mesh.warp_by_vector()

    # Configure plot: set camera view then press "q" to launch gif
    pv.set_plot_theme("document")
    p = pv.Plotter(notebook=False)
    p.add_mesh(
        mesh_warp,
        color="grey",
        opacity=1,
        show_edges=True,
        edge_color="white",
        line_width=1,
    )
    p.show(use_panel=False, auto_close=False)

    # GIF
    p.open_gif(gif_path + "/" + gif_name)
    for i in range(Nt_tot):
        field = take(field, i, axis=-1)
        mesh.vectors = field
        mesh_warp = mesh.warp_by_vector()
        p.add_mesh(
            mesh_warp,
            color="grey",
            show_edges=True,
            edge_color="white",
            line_width=0.0001,
        )
        p.write_frame()
        p.clear()

    # Close movie and delete object
    p.close()
