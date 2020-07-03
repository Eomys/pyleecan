# -*- coding: utf-8 -*-


def get_normals(self, indices=None, loc="center"):
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

    surf = self.get_surf(indices=indices)

    if loc == "center":
        return surf.cell_normals
    elif loc == "point":
        surf.compute_normals(cell_normals=False, point_normals=True, inplace=True)
        return surf["Normals"]
