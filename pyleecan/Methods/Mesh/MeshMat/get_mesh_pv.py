# -*- coding: utf-8 -*-

import pyvista as pv
import meshio
import os


def get_mesh_pv(self, path="temp.vtk", indices=None):
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
    cells, nb_cell, indice_dict = self.get_cell()

    # for key in cells:
    cells = [("triangle", cells["triangle"])]  # TODO : Generalize to any cell type

    # Write .vtk file using meshio
    meshio.write_points_cells(
        filename=path, points=points, cells=cells,
    )

    # Read .vtk file with pyvista
    mesh = pv.read(path)

    # Extract submesh
    if indices is not None:
        mesh = mesh.extract_points(indices)

    os.remove(path)

    return mesh
