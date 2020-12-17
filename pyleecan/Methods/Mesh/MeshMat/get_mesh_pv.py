# -*- coding: utf-8 -*-

import pyvista as pv
import meshio
from os import makedirs, remove
from os.path import isdir, split
from pyleecan.definitions import RESULT_DIR


def get_mesh_pv(self, path=RESULT_DIR + "/temp.vtk", indices=None):
    """Return the pyvista mesh object (or submesh).

    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    mesh : pyvista.core.pointset.UnstructuredGrid
        a pyvista UnstructuredGrid object
    """

    points = self.get_point()
    cells, _, _ = self.get_cell()

    cells_meshio = list()
    for key in cells:
        cells_meshio.append((key, cells[key]))
        # Write .vtk file using meshio

    # Make sure that the file exists
    if not isdir(split(path)[0]):
            makedirs(split(path)[0])
     
    meshio.write_points_cells(filename=path, points=points, cells=cells_meshio)

    # Read .vtk file with pyvista
    mesh = pv.read(path)

    # Extract submesh
    if indices is not None:
        mesh = mesh.extract_points(indices)

    remove(path)

    return mesh
