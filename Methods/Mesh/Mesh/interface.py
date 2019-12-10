# -*- coding: utf-8 -*-
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.NodeMat import NodeMat
from collections import Counter
import numpy as np


def interface(self, other_mesh):
    """Define an Mesh object corresponding to the exact intersection between two Mesh (nodes must be in both meshes,
    the nodes tags must be identically defined).

    Parameters
    ----------
    self : Mesh
        a Mesh object
    other_mesh : Mesh
        an other Mesh object

        Returns
    -------
    """

    # Dynamic import of ElementDict
    module = __import__("pyleecan.Classes." + "Mesh", fromlist=["Mesh"])
    new_mesh = getattr(module, "Mesh")()
    new_mesh.element = ElementDict()
    new_mesh.node = NodeMat()

    # Meshes attributes
    nodes_tags = self.element.get_all_node_tags()
    other_nodes_tags = other_mesh.element.get_all_node_tags()

    # Find the nodes on the interface (they are in both in and out)
    interface_nodes_tags = np.intersect1d(nodes_tags, other_nodes_tags)
    nb_interf_nodes = len(interface_nodes_tags)

    tmp_element_tags = np.array([], dtype=int)
    tmp_element_tags_other = np.array([], dtype=int)
    node2elem_dict = dict()
    node2elem_other_dict = dict()
    # Find the elements in contact with the interface (they contain the interface nodes)
    for ind in range(nb_interf_nodes):
        tmp_tag = self.element.get_node2element(interface_nodes_tags[ind])
        node2elem_dict[interface_nodes_tags[ind]] = tmp_tag
        tmp_element_tags = np.concatenate((tmp_element_tags, tmp_tag))

        tmp_tag = other_mesh.element.get_node2element(interface_nodes_tags[ind])
        node2elem_other_dict[interface_nodes_tags[ind]] = tmp_tag
        tmp_element_tags_other = np.concatenate((tmp_element_tags_other, tmp_tag))

    # Find element tags in contact and number of nodes in contact for each element
    tmp_element_tags_unique = np.unique(
        tmp_element_tags
    )  # List of element tag which are in contact with the interface
    nb_elem_contact = len(tmp_element_tags_unique)
    nb_element_tags_unique = np.zeros((nb_elem_contact, 1), dtype=int)
    elem2node_dict = dict()
    for ind in range(nb_elem_contact):
        # Number of node on the interface for each element from tmp_element_tags_unique
        Ipos = np.where(tmp_element_tags_unique[ind] == tmp_element_tags)[0]
        nb_element_tags_unique[ind] = len(Ipos)
        # Which nodes exactly are concerned; store them in elem2node_dict
        nodes_tmp = self.element.get_node_tags(tmp_element_tags_unique[ind])
        nodes_tmp_interf = np.array([], dtype=int)
        for ipos in range(len(nodes_tmp)):
            if nodes_tmp[ipos] in interface_nodes_tags:
                nodes_tmp_interf = np.concatenate(
                    (nodes_tmp_interf, np.array([nodes_tmp[ipos]], dtype=int))
                )
        elem2node_dict[tmp_element_tags_unique[ind]] = nodes_tmp_interf

    # Build element
    seg_elem_pos = np.where(nb_element_tags_unique == 2)[
        0
    ]  # Position in the vector tmp_element_tags_unique
    seg_elem_tag = tmp_element_tags_unique[
        seg_elem_pos
    ]  # Vector of element tags with only 2 nodes on the interface
    nb_elem_segm = len(seg_elem_tag)
    for i_seg in range(nb_elem_segm):
        tag_two_nodes = elem2node_dict[seg_elem_tag[i_seg]]
        new_mesh.element.add_element(tag_two_nodes)

    # The same operation is applied in the other mesh because in the corners, 1 element will contain 3 nodes,
    # and it will not be detected by seg_elem_pos. Applying the same process to the other mesh solve the issue
    # if add_element ignore the already defined elements.
    tmp_element_tags_other_unique = np.unique(tmp_element_tags_other)
    nb_node_other_contact = len(tmp_element_tags_other_unique)
    nb_element_tags_other_unique = np.zeros((nb_node_other_contact, 1), dtype=int)
    elem2node_other_dict = dict()
    for ind in range(nb_node_other_contact):
        Ipos = np.where(tmp_element_tags_other_unique[ind] == tmp_element_tags_other)[0]
        nb_element_tags_other_unique[ind] = len(Ipos)
        nodes_tmp = other_mesh.element.get_node_tags(tmp_element_tags_other_unique[ind])
        nodes_tmp_interf = np.array([], dtype=int)
        for ipos in range(len(nodes_tmp)):
            if nodes_tmp[ipos] in interface_nodes_tags:
                nodes_tmp_interf = np.concatenate(
                    (nodes_tmp_interf, np.array([nodes_tmp[ipos]], dtype=int))
                )
        elem2node_other_dict[tmp_element_tags_other_unique[ind]] = nodes_tmp_interf

    # Build segment elements in other mesh
    seg_elem_pos = np.where(nb_element_tags_other_unique == 2)[0]
    seg_elem_tag = tmp_element_tags_other_unique[seg_elem_pos]
    nb_elem_segm = len(seg_elem_tag)
    for i_seg in range(nb_elem_segm):
        tag_two_nodes = elem2node_other_dict[seg_elem_tag[i_seg]]
        new_mesh.element.add_element(
            tag_two_nodes
        )  # It is not really added if it already exist

    return new_mesh
    # TODO : Extend the code to higher dimension (3 nodes triangles for tetrahedra interfaces ...)

    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots()
    # x = mesh_group.node[:,0]
    # y = mesh_group.node[:,1]
    # ax.scatter(x, y)
    # for ieleme in range(mesh_group.nb_elem):
    #     x = mesh_group.node[interface_elem[ieleme,:],0]
    #     y = mesh_group.node[interface_elem[ieleme,:],1]
    #     ax.plot(x, y)
    #
    # fig, ax = plt.subplots()
    # x = nodes_in[:, 0]
    # y = nodes_in[:, 1]
    # ax.scatter(x, y)
    # x = nodes_out[:, 0]
    # y = nodes_out[:, 1]
    # ax.scatter(x, y)
    # x = nodes_parent[interface_nodes_id, 0]
    # y = nodes_parent[interface_nodes_id, 1]
    # ax.scatter(x, y, marker='x')
