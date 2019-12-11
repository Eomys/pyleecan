# -*- coding: utf-8 -*-

import numpy as np


def add_node(self, coord):
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
    if self.is_exist(coord):
        return None
    else:
        if self.coordinate.size > 0:
            self.coordinate = np.vstack((self.coordinate, coord))
            new_tag = max(self.tag) + 1
            self.tag = np.concatenate((self.tag, np.array([new_tag], dtype=int)))
            self.nb_node = self.nb_node + 1
        else:
            self.coordinate = np.concatenate((self.coordinate, coord))
            new_tag = 0
            self.tag = np.array([], dtype=int)
            self.tag = np.concatenate((self.tag, np.array([new_tag], dtype=int)))
            self.nb_node = self.nb_node + 1

    return new_tag
