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

    # Get surfaces
    surf = self.get_surf()

    if loc == "center":
        normals = surf.cell_normals

    elif loc == "point":
        if self.node_normals is None:
            self.surf.compute_normals(
                cell_normals=False, point_normals=True, inplace=True
            )

            self.node_normals = self.surf["Normals"]

        normals = self.node_normals

    if indices is None:
        return normals

    else:
        return normals[indices, :]
