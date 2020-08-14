# -*- coding: utf-8 -*-


def get_points(self, indices=None):
    """Return the array of the points coordinates.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    points: ndarray
        Points coordinates
    """

    mesh = self.get_mesh(indices=indices)

    return mesh.points
