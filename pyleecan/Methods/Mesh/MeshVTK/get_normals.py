# -*- coding: utf-8 -*-


def get_normals(self, indices=[]):
    """Return the array of the normals coordinates.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    normals: ndarray
        Normals coordinates
    """

    surf = self.get_surf(indices)

    return surf.cell_normals
