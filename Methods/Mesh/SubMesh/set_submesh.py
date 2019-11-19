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
    """Define a MeshMat object corresponding to the submesh

    Parameters
    ----------
    self : SubMesh
        a SubMesh object
    parent_mesh : MeshMat
        a MeshMat object which contains the submesh

    Returns
    -------
    """

    # Dynamic import of MeshFEMM
    module = __import__("pyleecan.Classes." + "MeshMat", fromlist=["MeshMat"])
    mesh_group = getattr(module, "MeshMat")()
    # mesh_group = module.MeshMat()

    group_number = self.group_number
    interface = False
    elem_id = np.where(parent_mesh.group == group_number[0])[0]
    elem_id_no = np.where(parent_mesh.group != group_number[0])[0]

    for igr in range(1, len(group_number), 1):
        group = group_number[igr]
        if group == -1:
            interface = True
        else:
            elem_id = np.append(
                elem_id, np.where(parent_mesh.group == group)[0]
            )  # Find all element in the targeted group
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
