# -*- coding: utf-8 -*-

import pyvista as pv
import meshio


def get_mesh(self, indices=None):
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

    # Already available => Return
    if self.mesh is not None:
        return self.mesh

    # Read mesh file
    else:
        name_file_vtk = "plot_mesh.vtk"
        points = self.get_point()
        cells = self.get_cell()
        cells = [("triangle", cells["triangle"])]

        # Write .vtk file using meshio
        meshio.write_points_cells(
            filename="mesh.vtk", points=points, cells=cells,
        )

        meshio.write(name_file_vtk)

        # Read .vtk file with pyvista
        mesh = pv.read(name_file_vtk)

        # Extract submesh
        if indices is not None:
            mesh = mesh.extract_points(indices)

        if self.is_pyvista_mesh:
            self.mesh = mesh

        return mesh
