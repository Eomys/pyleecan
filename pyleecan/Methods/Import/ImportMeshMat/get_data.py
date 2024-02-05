# -*- coding: utf-8 -*-

from os.path import splitext

import numpy as np

from ....Classes.ElementMat import ElementMat
from ....Classes.ImportMeshUnv import ImportMeshUnv
from ....Classes.MeshMat import MeshMat
from ....Classes.NodeMat import NodeMat
from ....Classes.RefQuad4 import RefQuad4
from ....Classes.RefTriangle3 import RefTriangle3


def get_data(self):
    """Import mesh and generate MeshMat object

    Parameters
    ----------
    self : ImportData
        An ImportData object

    Returns
    -------
    mesh: MeshMat
        The generated MeshMat object

    """

    # Get mesh data (nodes and elements)
    file_extension = splitext(self.file_path)[1]
    if file_extension == ".unv":
        nodes, elements = ImportMeshUnv(self.file_path).get_data()
    else:
        raise Exception(f"{file_extension} files are not supported")

    # Define MeshMat object
    if min(nodes[:, 0]) == 0 and max(nodes[:, 0]) == len(nodes[:, 0]) - 1:
        is_renum = False
    else:
        is_renum = True

    mesh = MeshMat(_is_renum=is_renum)

    node_indices = nodes[:, 0].astype(np.int32)

    # Node indices must start at 0 and be consecutive
    unique_node_indices = np.unique(node_indices)
    if unique_node_indices.size != node_indices.size:
        raise ValueError("Duplicated node index")

    if (
        unique_node_indices[0] != 0
        or unique_node_indices[-1] != unique_node_indices.size - 1
    ):
        for new_index, old_index in enumerate(unique_node_indices):
            node_indices[node_indices == old_index] = new_index

            # Change indices in element connectivity value
            for element in elements.values():
                element[:, 1:][element[:, 1:] == old_index] = new_index

    # Define NodeMat object
    mesh.node = NodeMat(
        coordinate=nodes[:, 1:],
        nb_node=nodes.shape[0],
        indice=node_indices,
    )

    # Ensure that element indices are between 0 and nb_element - 1
    element_indices = np.hstack(
        [elt[:, 0].astype(np.int32) for elt in elements.values()]
    )

    unique_element_indices = np.unique(element_indices)  # Values returned are sorted

    if unique_element_indices.size < element_indices.size:
        raise ValueError("Duplicated element index")

    min_indice = 0
    if (
        unique_element_indices[0] != 0
        or unique_element_indices[-1] != unique_element_indices.size - 1
    ):
        # Refactor indices
        for element in elements.values():
            nb_element = element.shape[0]
            element[:, 0] = np.arange(min_indice, min_indice + nb_element)
            min_indice += nb_element

    # Define ElementMat objects
    for elt_type, elt in elements.items():
        element = ElementMat(
            connectivity=elt[:, 1:],
            nb_element=elt.shape[0],
            nb_node_per_element=elt.shape[1] - 1,
            indice=elt[:, 0].astype(np.int32),
        )
        # Add element of reference using names from pyUFF
        if elt_type == "triangle":
            element.ref_element = RefTriangle3()
        elif elt_type == "quad":
            element.ref_element = RefQuad4()
        else:
            raise ValueError(f"Wrong element type {elt_type}.")

        mesh.element_dict[elt_type] = element

    return mesh
