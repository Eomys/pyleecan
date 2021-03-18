# -*- coding: utf-8 -*-

from numpy import array

def get_vertice(self, indices=None):
    """Return a connectivity matrix where the nodes indices are replaced by their coordinates.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    cell_type : str
        a key corresponding to an element type
    group : ndarray
        One or several group numbers to be returned

    Returns
    -------
    vertice: ndarray
        Selected vertices

    """

    cells, nb_cell, indices = self.get_cell(indices=indices)
    vertices = dict()
    for key in cells:
        if len(cells[key].shape) > 1:
            vertices[key] = list()
            for ii in range(cells[key].shape[0]):
                vertices[key].append(self.get_node(cells[key][ii, :]))
            vertices[key] = array(vertices[key])
        else:
            vertices[key] = self.get_node(cells[key])

    return vertices
