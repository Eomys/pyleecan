# -*- coding: utf-8 -*-

import numpy as np


def get_node(self, elem):
    """Return the nodes coordinates in the element elem

    Parameters
    ----------
    self : ElementMat
        an ElementMat object

    Returns
    -------
    nodes: ndarray
        Selected nodes coordinates

    """

    indices = elem
    nodes = self.node[indices, :]

    return nodes, indices
