# -*- coding: utf-8 -*-

import numpy as np


def get_vertice(self, indices=None):
    """Return a connectivity matrix where the points indices are replaced by their coordinates.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    cell_type : str
        a key corresponding to an element type
    group : numpy.array
        One or several group numbers to be returned

    Returns
    -------
    vertice: numpy.array
        Selected vertices

    """

    cells, nb_cell, indices = self.get_cell(indices=indices)
    vertices = dict()
    for key in cells:
        vertices[key] = self.get_point(cells[key])

    return vertices
    # if nb_elem == 1:
    #     vertices = np.zeros((nb_node_per_elem, 2))
    #     vertices = self.node.get_coord(connect_select)
    # else:
    #     vertices = np.zeros((nb_elem, nb_node_per_elem, 2))
    #     for ie in range(nb_elem):
    #         vertices[ie, :, :] = self.node.get_coord(connect_select[ie, :])
    #
    # return vertices, nb_elem
