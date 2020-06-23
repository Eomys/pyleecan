# -*- coding: utf-8 -*-

import numpy as np


def get_all_node_tags(self):
    """Return a vector of all nodes tags related to the connectivity

    Parameters
    ----------
    self : CellMat
        an CellMat object

    Returns
    -------
    node_tags: numpy.array
        Selected nodes coordinates

    """

    return np.unique(self.connectivity)
