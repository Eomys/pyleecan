# -*- coding: utf-8 -*-

import pyvistaqt as pv


def plot_glyph(self, field, indices=[], factor=1):
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
    mesh["field"] = field
    mesh_cell = mesh.point_data_to_cell_data()
    surf = mesh_cell.extract_surface()
    centers2 = surf.cell_centers()
    centers2.vectors = surf["field"] * factor

    # Configure plot
    p = pv.Plotter()
    p.add_mesh(
        mesh, show_edges=True, edge_color="white", line_width=1,
    )
    p.add_mesh(centers2.arrows, color="black")
    p.show()
