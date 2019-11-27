# -*- coding: utf-8 -*-

from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat


def set_submesh(self, group_number):
    """Define a mesh object as submesh of parent mesh object

     Parameters
     ----------
     self : Mesh
         an Mesh object
     group_number : int
         a group number which define the elements which constitute the submesh

     Returns
     -------

     """
    submesh = Mesh()
    submesh.element = self.element.get_group(
        group_number
    )  # Create a new Element object which is restrained to group_number
    submesh.node = self.node.get_group(
        element=submesh.element
    )  # Create a new Node object which corresponds to selection of element
