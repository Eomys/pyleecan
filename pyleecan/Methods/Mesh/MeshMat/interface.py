# -*- coding: utf-8 -*-
from itertools import combinations

import numpy as np

from ....Classes.ElementMat import ElementMat
from ....Classes.FPGNSeg import FPGNSeg
from ....Classes.RefSegmentP1 import RefSegmentP1


def interface(self, other_mesh: "MeshMat") -> "MeshMat":
    """Define a MeshMat object corresponding to the exact intersection between two meshes (nodes must be in both meshes).

    Parameters
    ----------
    self : MeshMat
        a Mesh object
    other_mesh : Mesh
        an other Mesh object

        Returns
    -------
    """

    # Dynamic import
    new_mesh = self.copy()
    new_mesh._is_renum = True

    new_mesh.element_dict = {
        "line": ElementMat(
            nb_node_per_element=2, gauss_point=FPGNSeg(), ref_element=RefSegmentP1()
        )
    }

    for key in self.element_dict:
        # Developer info: IDK if this code works with other than triangle elements. To be checked.
        if self.element_dict[key].nb_node_per_element == 3:  # Triangle case
            connect = self.element_dict[key].get_connectivity()
            connect2 = other_mesh.element_dict[key].get_connectivity()

            nb_elem_mesh1 = self.element_dict[key].nb_node_per_element
            nb_elem_mesh2 = other_mesh.element_dict[key].nb_node_per_element

            nodes_tags = np.unique(connect)
            other_nodes_tags = np.unique(connect2)

            # Find the nodes on the interface (they are in both in and out)
            interface_nodes_tags = np.intersect1d(nodes_tags, other_nodes_tags)

            # Extract elements which may belong to the interface
            is_interface_node_mesh1 = np.isin(connect, interface_nodes_tags)
            is_interface_node_mesh2 = np.isin(connect2, interface_nodes_tags)
            idx_elem_mesh1 = np.nonzero(is_interface_node_mesh1.sum(axis=1) >= 2)
            idx_elem_mesh2 = np.nonzero(is_interface_node_mesh2.sum(axis=1) >= 2)

            element_mesh1 = connect[idx_elem_mesh1]
            element_mesh2 = connect2[idx_elem_mesh2]

            # Compute the edges connectivity of the selected elements by extracting
            # (node[0],node[1]), (node[1],node[2]), ..., (node[-2],node[-1]), (node[-1], node[0])
            line_connect_mesh1 = np.vstack(
                [
                    *[element_mesh1[:, k : k + 2] for k in range(nb_elem_mesh1 - 1)],
                    element_mesh1[:, (-1, 0)],
                ]
            )
            line_connect_mesh2 = np.vstack(
                [
                    *[element_mesh2[:, k : k + 2] for k in range(nb_elem_mesh2 - 1)],
                    element_mesh2[:, (-1, 0)],
                ]
            )

            # Iterate on mesh1 lines to check if the edge is also in mesh2
            for line in line_connect_mesh1:
                if np.any(np.all(np.isin(line_connect_mesh2, line), axis=1)):
                    new_mesh.add_element(line, "line")

    return new_mesh
