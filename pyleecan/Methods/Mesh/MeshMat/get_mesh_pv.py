# -*- coding: utf-8 -*-

from os import makedirs, remove
from os.path import dirname, isdir
from typing import List, Optional

import meshio
import pyvista as pv
from pyvista.core.pointset import UnstructuredGrid

from ....definitions import RESULT_DIR


def get_mesh_pv(
    self, path: str = f"{RESULT_DIR}/temp.vtk", indices: Optional[List[int]] = None
) -> UnstructuredGrid:
    """Return the pyvista mesh object (or submesh).

    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    indices : list
        list of the nodes to extract (optional)

    Returns
    -------
    mesh : pyvista.core.pointset.UnstructuredGrid
        a pyvista UnstructuredGrid object
    """

    # Numbering and indices compatible with pyvista
    mesh_renum = self.copy()
    mesh_renum.renum()

    nodes = mesh_renum.get_node_coordinate()
    cells, _, _ = mesh_renum.get_element()

    cells_meshio = list()
    for key in cells:
        cells_meshio.append((key, cells[key]))
        # Write .vtk file using meshio

    # Make sure that the file exists
    if not isdir(dirname(path)):
        makedirs(dirname(path))

    meshio.write_points_cells(filename=path, points=nodes, cells=cells_meshio)

    # Read .vtk file with pyvista
    mesh = pv.read(path)

    # Extract submesh
    if indices is not None:
        mesh = mesh.extract_points(indices)

    remove(path)

    return mesh
