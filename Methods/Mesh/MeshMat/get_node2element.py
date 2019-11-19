# -*- coding: utf-8 -*-

import numpy as np


def get_nodes2elements(self, node_id):
    """Return all elements containing the node node_id

    Parameters
    ----------
    self : MeshMat
        an MeshMat object

    Returns
    -------
    elems: ndarray
        all elements containing node_id

    """
    elems = np.where(self.elements == node_id)

    return elems
