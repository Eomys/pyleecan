# -*- coding: utf-8 -*-
import numpy as np
import copy

from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat


def clear_node(self):
    """Remove non-used nodes based on cells connectivity.

    Parameters
    ----------
    self : MeshMat
        an Mesh object

    Returns
    -------

    """

    coord_init = self.get_node()
    node_indice_init = self.node.indice
    connect_dict, nb_cell, indices = self.get_cell()

    node_indice = list()
    for key in connect_dict:
        node_indice.extend(np.unique(connect_dict[key]))

    node_indice = np.unique(node_indice)
    common, index1, index2 = np.intersect1d(
        node_indice, node_indice_init, return_indices=True
    )

    if not np.array_equal(node_indice, common):
        raise ValueError

    self.node = NodeMat(
        coordinate=coord_init[index2, :],
        nb_node=len(index2),
        indice=node_indice,
    )
