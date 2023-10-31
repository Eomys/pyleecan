# -*- coding: utf-8 -*-


def get_node(self, indices=None):
    """Return the array of the nodes coordinates.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the nodes to extract (optional)

    Returns
    -------
    nodes: ndarray
        Points coordinates
    """

    mesh = self.get_mesh_pv(indices=indices)

    return mesh.points
