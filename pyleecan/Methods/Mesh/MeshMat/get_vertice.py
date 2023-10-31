# -*- coding: utf-8 -*-

from numpy import array


def get_vertice(self, indices=None):
    """Return a connectivity matrix where the nodes indices are replaced by their coordinates.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    element_type : str
        a key corresponding to an element type
    group : ndarray
        One or several group numbers to be returned

    Returns
    -------
    node_coordinates: ndarray
        Nodes coordinates of each selected element

    """

    elements, *_ = self.get_element(indices=indices)
    node_coordinates = {}
    for key, element in elements.items():
        if element.ndim > 1:
            node_coordinates[key] = array([self.get_node(nodes) for nodes in element])
        else:
            node_coordinates[key] = self.get_node(element)

    return node_coordinates
