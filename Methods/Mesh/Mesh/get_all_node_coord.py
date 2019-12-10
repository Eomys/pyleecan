# -*- coding: utf-8 -*-

from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


def get_all_node_coord(self, group=None):
    """Return a matrix of nodes coordinates and the vector of nodes tags corresponding to group.
    If no group specified, it returns all the nodes of the mesh.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    group : numpy.array
        Vector of targeted group

    Returns
    -------
    coordinate: numpy.array
        Nodes coordinates
    tag : numpy.array
        Nodes tags

    """

    if type(self.node) is NodeMat:
        if group is None:
            return self.node.coordinate, self.node.tag
        else:
            for key in self.element:
                element_group = self.element[key].get_group(group)
                connect = element_group.get_all_node_tags()
                coord = self.node.get_coord(connect)
                tag = self.node.get_tag(connect)
    else:
        return None
