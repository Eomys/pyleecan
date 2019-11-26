# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag=None):
    """Return the nodes tags in the element elem_tag

    Parameters
    ----------
    self : ElementDict
        an ElementDict object

    Returns
    -------
    node_tags: ndarray
        Selected nodes coordinates

    """

    connect = self.connectivity
    tag = self.tag
    node_tags = np.array([], dtype=int)

    if elem_tag is None:
        for key in connect:  # There should only one solution
            for ie in range(len(connect[key])):
                node_tags = np.concatenate((node_tags, connect[key][ie]))
        node_tags = np.unique(node_tags)

    if type(elem_tag) is int:
        for key in connect:
            Ielem = int(
                np.where(tag[key] == elem_tag)[0]
            )  # There should only one solution
            node_tags = np.concatenate((node_tags, connect[key][Ielem]))

    if type(elem_tag) is np.ndarray:
        for ie in range(len(elem_tag)):
            for key in connect:
                Ielem = int(
                    np.where(tag[key] == elem_tag[ie])[0]
                )  # There should only one solution
                node_tags = np.concatenate((node_tags, connect[key][Ielem]))
        node_tags = np.unique(node_tags)

    return node_tags
