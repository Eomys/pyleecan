# -*- coding: utf-8 -*-

import pyvistaqt as pv


def plot_contour(self, field, field_name="Magnitude", indices=[], cmap="RdBu_r"):
    """Plot a scalar field as a color contour over a mesh.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    field : ndarray
        array of the field
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    """

    # Get the mesh
    mesh = self.get_mesh(indices)

    # Extract subset of the field if necessary
    if indices != [] and field.shape != indices.shape:
        field = field[indices]

    # Add field to mesh
    mesh[field_name] = field

    # Configure plot
    p = pv.BackgroundPlotter()
    p.set_background("white")
    sargs = dict(
        interactive=True,
        title_font_size=20,
        label_font_size=16,
        font_family="arial",
        color="black",
    )
    p.add_mesh(
        mesh,
        scalars=field_name,
        show_edges=True,
        edge_color="white",
        line_width=1,
        cmap=cmap,
        scalar_bar_args=sargs,
    )
    p.show()
