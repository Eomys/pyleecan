# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, new_coord):
    """Check the existence of a node defined by its coordinates

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coord : numpy.array
        coordinate of the node

    Returns
    -------
        bool
            True if the element already exist
    """
    # Check the existence of the element
    delta = self.delta
    nb_node = self.nb_node
    coords = self.coordinate

    if nb_node == 0:
        return False
    if nb_node == 1:
        dist = np.sqrt(np.sum(np.square(coords - new_coord)))
        if dist > delta:
            return False
        else:
            return True
    else:
        point = np.tile(new_coord, (nb_node, 1))
        dist_node = np.reshape(
            np.sqrt(
                np.square(coords[:, 0] - point[:, 0])
                + np.square(coords[:, 1] - point[:, 1])
            ),
            (nb_node, 1),
        )

        min_node_list = np.argsort(dist_node, axis=0)

        if dist_node[min_node_list[0]] > delta:
            return False
        else:
            return True
