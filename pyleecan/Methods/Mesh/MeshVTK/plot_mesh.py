# -*- coding: utf-8 -*-

import pyvistaqt as pv


def plot_mesh(self, indices=[]):
    """Plot the mesh using pyvista plotter.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    """

    mesh = self.get_mesh(indices)

    # Configure plot
    p = pv.BackgroundPlotter()
    p.set_background("white")
    p.add_mesh(
        mesh, color="grey", opacity=1, show_edges=True, edge_color="white", line_width=1
    )
    p.show()
