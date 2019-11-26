# -*- coding: utf-8 -*-

from pyleecan.Classes.NodeMat import NodeMat


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

    node = NodeMat()
    node_tags = element.get_node_tags()
    node.coordinate = self.get_coord(node_tags)
    node.nb_node = len(node.coordinate)

    return node
