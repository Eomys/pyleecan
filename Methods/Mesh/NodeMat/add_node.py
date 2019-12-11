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
            self.coordinate = np.concatenate((self.coordinate, coord))
            new_tag = max(self.tag) + 1
            self.nb_node = self.nb_node + 1
        else:
            self.coordinate = np.concatenate((self.coordinate, coord))
            new_tag = 0
            self.tag = new_tag

    return new_tag
