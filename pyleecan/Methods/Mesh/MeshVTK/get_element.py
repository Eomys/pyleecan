# -*- coding: utf-8 -*-

import numpy as np
import pyvista as pv


def get_element(self, indices=None):
    """Return the elements (connectivities).

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    dict_connectivity: dict[str, ndarray]
        Dict of connectivity with element names as keys
    nb_element: int
        Number of element in the connectivity
    dict_index: dict
        When apply get_element on a MeshMat :
            Dict of the element element_indices for each ElementMat.
        Not use here, because it as any meanings for a MeshVTK

    """
    # Extract mesh
    mesh = self.get_mesh_pv(indices=indices)

    pv_to_str = {
        pv.CellType.TRIANGLE: "triangle",
        pv.CellType.QUAD: "quad",
        pv.CellType.QUADRATIC_EDGE: "line3",
        pv.CellType.BIQUADRATIC_QUAD: "quad9",
    }

    # Initialize the element dictionary with the keys
    elements = {pv_to_str[cell_type]: [] for cell_type in np.unique(mesh.celltypes)}

    # Get the connectivity of each element
    for cell_type, start_offset, end_offset in zip(
        mesh.celltypes, mesh.offset[:-1], mesh.offset[1:]
    ):
        nodes_indice = mesh.cell_connectivity[start_offset:end_offset]
        elements[pv_to_str[cell_type]].append(nodes_indice)

    # Convert a list of 1D-ndarray into a 2D-ndarray
    for key, value in elements.items():
        elements[key] = np.array(value)

    return elements, mesh.n_cells, {}
