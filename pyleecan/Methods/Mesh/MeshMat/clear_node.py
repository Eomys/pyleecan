# -*- coding: utf-8 -*-
import numpy as np
import copy

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat


def clear_node(self):
    """Remove non-used nodes based on elements connectivity.

    Parameters
    ----------
    self : MeshMat
        an Mesh object

    Returns
    -------

    """

    coord_init = self.get_node()
    node_indice_init = self.get_node_indice()
    connect_dict, *_ = self.get_element()

    node_indice = []
    for key in connect_dict:
        node_indice.extend(np.unique(connect_dict[key]))

    node_indice = np.unique(node_indice)
    common, _, index2 = np.intersect1d(
        node_indice, node_indice_init, return_indices=True
    )

    if not np.array_equal(node_indice, common):
        raise ValueError

    self.node = NodeMat(
        coordinate=coord_init[index2, :],
        nb_node=len(index2),
        indice=node_indice,
    )
