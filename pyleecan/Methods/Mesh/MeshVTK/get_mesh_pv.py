# -*- coding: utf-8 -*-

import pyvista as pv
from meshio import read


def get_mesh_pv(self, indices=None):
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
        # Extract submesh
        if indices is not None:
            mesh = self.mesh.extract_points(indices)
        return mesh

    # Read mesh file
    else:
        if self.format != "vtk":
            # Write vtk files with meshio
            # in case replace whitespace in point data keys since vtk doesn't like it
            mesh = read(self.path + "/" + self.name + "." + self.format)
            mesh.point_data = {
                k.replace(" ", "_"): v for k, v in mesh.point_data.items()
            }
            mesh.write(self.path + "/" + self.name + ".vtk")
            
        # Read .vtk file with pyvista
        mesh = pv.read(self.path + "/" + self.name + ".vtk")

        # Extract submesh
        if indices is not None:
            mesh = mesh.extract_points(indices)

        if self.is_pyvista_mesh:
            self.mesh = mesh

        return mesh
