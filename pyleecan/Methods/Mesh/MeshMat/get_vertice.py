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
    vertice: ndarray
        Selected vertices

    """

    elements, nb_element, indices = self.get_element(indices=indices)
    vertices = dict()
    for key in elements:
        if len(elements[key].shape) > 1:
            vertices[key] = list()
            for ii in range(elements[key].shape[0]):
                vertices[key].append(self.get_node(elements[key][ii, :]))
            vertices[key] = array(vertices[key])
        else:
            vertices[key] = self.get_node(elements[key])

    return vertices
