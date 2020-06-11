# -*- coding: utf-8 -*-

import pyvistaqt as pv


def plot_deformation(self, field, indices=[], factor=1):
    """Plot a vector field as glyphs over a mesh.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    field : ndarray
        array of the field
    indices : list
        list of the points to extract (optional)
    factor : float
        factor to multiply the field vectors for visualization

    Returns
    -------
    """

    # Get the mesh
    mesh = self.get_mesh(indices)

    # Extract subset of the field if necessary
    if indices != [] and field.shape != indices.shape:
        field = field[indices]

    # Add field to mesh
    mesh.vectors = field

    # Warp by vectors
    mesh_warp = mesh.warp_by_vector()

    # Configure plot
    p = pv.Plotter()
    p.add_mesh(
        mesh_warp,
        color="grey",
        opacity=1,
        show_edges=True,
        edge_color="white",
        line_width=1,
    )
    p.show()
