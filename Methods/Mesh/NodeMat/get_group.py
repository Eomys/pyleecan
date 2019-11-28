# -*- coding: utf-8 -*-


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
    module = __import__("pyleecan.Classes." + "NodeMat", fromlist=["NodeMat"])
    node = getattr(module, "NodeMat")()

    node_tags = element.get_node_tags()
    node.coordinate = self.coordinate[node_tags, :]
    node.nb_node = len(node.coordinate)

    return node
