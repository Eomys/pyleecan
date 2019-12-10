# -*- coding: utf-8 -*-


def get_coord(self, node_tags=None):
    """Return the coordinates of node(s).

     Parameters
     ----------
     self : NodeMat
         an NodeMat object
     node_tags : array
         an array of node tags

     Returns
     -------
     coord: array
         an array of node coordinates

     """

    if node_tags is None:
        coord = self.coordinate
    else:
        coord = self.coordinate[node_tags, :]

    return coord
