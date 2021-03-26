# -*- coding: utf-8 -*-

from os import makedirs, remove
from os.path import isdir, split, dirname

import meshio
import pyvista as pv

from pyleecan.definitions import RESULT_DIR


def get_mesh_pv(self, path=RESULT_DIR + "/temp.vtk", indices=None):
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

    nodes = self.get_node()
    cells, _, _ = self.get_cell()

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
