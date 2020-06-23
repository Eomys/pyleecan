# -*- coding: utf-8 -*-


def get_point(self, indice=None, is_indice=False):
    """Return a matrix of points coordinates.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    indice : list
        Indices of the targeted points. If None, return all.
    is_indice: bool
        Option to return the points indices (useful for unsorted

    Returns
    -------
    coordinates: ndarray
        points coordinates
    indices : ndarray
        points indices

    """
    if indice is None:
        if is_indice:
            return self.point.coordinate, self.point.indice
        else:
            return self.point.coordinate
    else:
        return self.point.coordinate[indice, :]
