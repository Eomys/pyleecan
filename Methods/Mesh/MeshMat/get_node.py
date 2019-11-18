# -*- coding: utf-8 -*-

import numpy as np


def get_node(self, elem):
    """Return the nodes coordinates in the element elem

    Parameters
    ----------
    self : MeshMat
        an MeshMat object

    Returns
    -------
    nodes: ndarray
        Selected nodes coordinates

    """

    indices = elem
    nodes = self.node[indices, :]

    return nodes, indices
