# -*- coding: utf-8 -*-


def get_node(self, indices=None):
    """Return a matrix of nodes coordinates.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    indices : list
        Indices of the targeted nodes. If None, return all.
    is_indice: bool
        Option to return the nodes indices (useful for unsorted

    Returns
    -------
    coordinates: ndarray
        nodes coordinates
    indices : ndarray
        nodes indices

    """
    if indices is None:
        return self.node.coordinate, self.node.indice
    else:
        return self.node.get_coord(indices)
