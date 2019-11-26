# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag=None):
    """Return the nodes tags in the element elem_tag

    Parameters
    ----------
    self : ElementMat
        an ElementMat object

    Returns
    -------
    node_tags: ndarray
        Selected nodes coordinates

    """

    connect = self.connectivity
    node_tags = np.array([], dtype=int)

    if elem_tag is None:
        for ie in range(len(connect)):
            node_tags = np.concatenate((node_tags, connect[ie, :]))
        node_tags = np.unique(node_tags)

    if type(elem_tag) is int:
        node_tags = connect[elem_tag, :]

    if type(elem_tag) is np.ndarray:
        for ie in range(len(elem_tag)):
            node_tags = np.concatenate((node_tags, connect[elem_tag[ie], :]))

        node_tags = np.unique(node_tags)

    return node_tags
