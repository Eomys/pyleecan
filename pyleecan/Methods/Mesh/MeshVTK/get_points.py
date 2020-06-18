# -*- coding: utf-8 -*-


def get_points(self, indices=[]):
    """Return the array of the points coordinates.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    points: ndarray
        Points coordinates
    """

    mesh = self.get_mesh(indices)

    return mesh.points
