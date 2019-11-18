# -*- coding: utf-8 -*-
import numpy as np

from pyleecan.Functions.FEMM import (
    GROUP_RC,
    GROUP_RH,
    GROUP_RV,
    GROUP_RW,
    GROUP_SC,
    GROUP_SH,
    GROUP_SV,
    GROUP_SW,
    GROUP_AG,
)


def set_submesh(self, parent_mesh):
    """Define a mesh object as submesh of parent mesh object

    Parameters
    ----------
    :param self : an SubMesh object
    :param parent_mesh: a Mesh object which contain the submesh

    Returns
    -------

    """

    #Dynamic import of MeshFEMM
    module = __import__("pyleecan.Classes." + "MeshMat", fromlist=["MeshMat"])
    mesh_group = getattr(module, "MeshMat")()
    #mesh_group = module.MeshMat()

    group_number = self.group_number
    interface = False
    elem_id = np.where(parent_mesh.group == group_number[0])[0]
    elem_id_no = np.where(parent_mesh.group != group_number[0])[0]

    for igr in range(1, len(group_number), 1):
        group = group_number[igr]
        if group == -1:
            interface = True
        else:
            elem_id = np.append(elem_id, np.where(parent_mesh.group == group)[0]) # Find all element in the targeted group
            elem_id_no = np.append(elem_id_no, np.where(parent_mesh.group != group)[0])

    if interface:
        self.parent_elem = None
    else:
        self.parent_elem = elem_id

    element = parent_mesh.element[elem_id, :]
    element_no = parent_mesh.element[elem_id_no, :]
    node_id = np.unique(element)
    self.parent_node = node_id
    mesh_group.nb_node = len(self.parent_node)

    if interface:
        # Define the interfacegroup
        nodes_no = np.unique(element)
        parent_node = np.intersect1d(node_id, nodes_no)
        mesh_group.node = np.copy(parent_mesh.node)[parent_node, 0:2]
        tmp_element = element*0

        # New numerotation of nodes (from 1 to nb_node)
        for ind in range(mesh_group.nb_node):
            element[np.where(element == node_id[ind])] = ind
            element_no[np.where(element == node_id[ind])] = ind
            #mesh_group.node[np.where(parent_node == node_id[ind])] = ind

        #  Find the elements in contact with the interface
        for ind in range(len(parent_node)):
            tmp_element[np.where(element == parent_node[ind])] = 1

        tmp_element_sum = np.sum(tmp_element, axis=1)

        # Build elements which constitute the interface

        # Segments (tmp_element_sum = 2)
        seg_elem = np.where(tmp_element_sum == 2)[0]
        nb_elem_segm = len(seg_elem)

        interface_elem = np.zeros((nb_elem_segm, 2), dtype=int)

        for i_seg in range(nb_elem_segm):
            tmp_seg = tmp_element[seg_elem[i_seg]] * element[seg_elem[i_seg]]
            interface_elem[i_seg, :] = np.delete(tmp_seg, np.where(tmp_seg == 0))

        # Triangle (elements in corner) (tmp_element_sum = 3)
        triangle_elem = np.where(tmp_element_sum == 3)[0]
        nb_elem_triangle = len(triangle_elem)
        interface_elem_tgl = np.zeros((2 * nb_elem_triangle, 2), dtype=int)

        for i_tgl in range(nb_elem_triangle):
            interface_elem_tgl[i_tgl, :] = self.element[triangle_elem[i_tgl]][0:2]
            interface_elem_tgl[i_tgl + nb_elem_triangle, :] = self.element[triangle_elem[i_tgl]][1:3]

        interface_elem = np.concatenate([interface_elem, interface_elem_tgl])
        subsubmesh.element = interface_elem

        # New numerotation of nodes (from 1 to nb_node)
        for ind in range(len(interface_node)):
            interface_elem[np.where(interface_elem == interface_node[ind])] = ind

        subsubmesh.element = interface_elem

        subsubmesh.nb_elem = len(interface_elem)
        subsubmesh.nb_node = len(interface_node)

        submesh.subsubmesh.append(subsubmesh)

        self.submesh.append(submesh)

    else:
        mesh_group.node = parent_mesh.node[node_id]
        mesh_group.element = element
        mesh_group.nb_elem = len(element)
        mesh_group.nb_node_per_element = parent_mesh.nb_node_per_element
        mesh_group.projection = parent_mesh.projection
        mesh_group.projection.ref_element = parent_mesh.projection.ref_element
        mesh_group.projection.scalar_product = parent_mesh.projection.scalar_product

        # New numerotation of nodes (from 1 to nb_node)
        for ind in range(mesh_group.nb_node):
            mesh_group.element[np.where(element == node_id[ind])] = ind

        self.mesh = mesh_group










