# -*- coding: utf-8 -*-


def get_element_area(self, indices=None):
    """Return the area of the elements on the outer surface.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    areas: ndarray
        Area of the elements
    """

    surf = self.get_surf(indices=indices)

    return surf.compute_element_sizes(area=True)["Area"]
