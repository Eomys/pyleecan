# -*- coding: utf-8 -*-


def get_cell_area(self, indices=None):
    """Return the area of the cells on the outer surface.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    areas: ndarray
        Area of the cells
    """

    surf = self.get_surf(indices=indices)

    return surf.compute_cell_sizes(area=True)["Area"]
