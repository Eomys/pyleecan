# -*- coding: utf-8 -*-


def get_cell_area(self, indices=[]):
    """Return the area of the cells on the outer surface.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    areas: ndarray
        Area of the cells
    """

    surf = self.get_surf(indices)

    return surf.compute_cell_sizes(area=True)["Area"]
