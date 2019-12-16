# -*- coding: utf-8 -*-

import numpy as np


def get_vertice(self, elem_type=None, group=None):
    """Return a connectivity matrix where the node tags are replaced by their coordinates.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    elem_type : str
        a key corresponding to an element type
    group : numpy.array
        One or several group numbers to be returned

    Returns
    -------
    vertice: numpy.array
        Selected vertices

    """

    connect_select, tags_select = self.get_all_connectivity(elem_type, group)
    nb_elem = len(tags_select)
    nb_node_per_elem = self.element[elem_type].nb_node_per_element
    vertices = np.zeros((nb_elem, nb_node_per_elem, 2))

    for ie in range(nb_elem):
        vertices[ie, :, :] = self.node.get_coord(connect_select[ie, :])

    return vertices
