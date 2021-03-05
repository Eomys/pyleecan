# -*- coding: utf-8 -*-
from ....definitions import PACKAGE_NAME

import numpy as np


def get_group(self, element):
    """Define a new NodeMat object based on a set of elements.

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    element : Element
        an Element object

    Returns
    -------
    node: Node
        a Node object corresponding to Element

    """
    module = __import__(PACKAGE_NAME + ".Classes." + "NodeMat", fromlist=["NodeMat"])
    node = getattr(module, "NodeMat")()

    node_tags = element.get_all_node_tags()

    node.nb_node = len(node_tags)
    node.coordinate = np.zeros((node.nb_node, 2))  # TO BE Extended to 3D
    node.tag = np.zeros((node.nb_node))
    for ind in range(node.nb_node):
        Ipos = np.where(node_tags[ind] == self.tag)[0]
        node.coordinate[ind, :] = self.coordinate[Ipos, :]
        node.tag[ind] = self.tag[Ipos]

    return node
