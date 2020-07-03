# -*- coding: utf-8 -*-

import pyvista as pv
import meshio
import os
import tempfile


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
    cells = self.get_cell()

    # for key in cells:
    cells = [("triangle", cells["triangle"])]  # TODO : Generalize to any cell type

    # get filename
    if not path:
        with tempfile.NamedTemporaryFile(suffix=".vtk") as file:
            path = file.name

    # Write .vtk file using meshio
    meshio.write_points_cells(
        filename=path, points=points, cells=cells, file_format="vtk"
    )

    # Read .vtk file with pyvista
    mesh = pv.read(path)

    # Extract submesh
    if indices is not None:
        mesh = mesh.extract_points(indices)

    os.remove(path)

    return mesh
