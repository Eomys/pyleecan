# -*- coding: utf-8 -*-

import numpy as np

from ....Classes.NodeMat import NodeMat


def clear_node(self):
    """Remove non-used nodes based on elements connectivity.

    Parameters
    ----------
    self : MeshMat
        an Mesh object

    Returns
    -------

    """

    coord_init = self.get_node_coordinate()
    node_indice_init = self.get_node_indice()
    connect_dict, *_ = self.get_element()

    # Extract index of use nodes in elements
    node_indice = np.unique(
        [np.unique(connectivity) for connectivity in connect_dict.values()]
    )

    common, _, index2 = np.intersect1d(
        node_indice, node_indice_init, return_indices=True
    )

    if not np.array_equal(node_indice, common):
        raise ValueError("")

    self.node = NodeMat(
        coordinate=coord_init[index2, :],
        nb_node=len(index2),
        indice=node_indice,
    )
