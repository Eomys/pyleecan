# -*- coding: utf-8 -*-


def get_normal(self, element_coordinate):
    """Return the array of the normals coordinates.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)
    loc : str
        localization of the normals ("center" or "point")

    Returns
    -------
    normals: ndarray
        Normals coordinates
    """

    # u1 = element_coordinate[1, :] - element_coordinate[0, :]
    # u2 = element_coordinate[2, :] - element_coordinate[0, :]
    # n = np.cross(u1, u2)
    # n = n / np.linalg.norm(n)

    return None
