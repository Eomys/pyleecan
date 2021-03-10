# -*- coding: utf-8 -*-


def get_node_indice(self, coordinates=None):
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

    if coordinates is None:
        return self.node.get_indice()
    else:
        pass  # TODO Search for indice of a node from coordiantes
