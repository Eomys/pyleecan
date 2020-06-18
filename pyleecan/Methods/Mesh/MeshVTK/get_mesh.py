# -*- coding: utf-8 -*-

import pyvista as pv
from meshio import read


def get_mesh(self, indices=[]):
    """Return the pyvista mesh object (or submesh).

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
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
        if self.format != "vtk":
            # Write vtk files with meshio
            mesh = read(self.path + "/" + self.name + "." + self.format)
            mesh.write(self.path + "/" + self.name + ".vtk")

        # Read .vtk file with pyvista
        mesh = pv.read(self.path + "/" + self.name + ".vtk")

        # Extract submesh
        if indices != []:
            mesh = mesh.extract_points(indices)

        if self.is_pyvista_mesh:
            self.mesh = mesh

        return mesh
