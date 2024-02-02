# -*- coding: utf-8 -*-

import pyvista as pv
from meshio import read
import numpy as np


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
            mesh = self.mesh
            mesh["mask"] = np.zeros(mesh.points.shape)
            mesh["mask"][indices] = 1
            mesh.set_active_scalars("mask")
            thresh = mesh.threshold(1)
            mesh = thresh
        else:
            mesh = self.mesh
        return mesh

    # Read mesh file
    else:
        if self.format != "vtk" and self.format != "vtu":
            # Write vtk files with meshio
            # in case replace whitespace in point data keys since vtk doesn't like it
            mesh = read(self.get_path(name=self.name, file_format=self.format))
            mesh.point_data = {
                k.replace(" ", "_"): v for k, v in mesh.point_data.items()
            }
            mesh.write(self.get_path())
            use_this_format = "vtk"
        else:
            use_this_format = self.format

        # Read .vtk file with pyvista
        mesh = pv.read(self.get_path(name=self.name, file_format=use_this_format))

        # Extract submesh
        if indices is not None:
            mesh = mesh.extract_points(indices)

        if self.is_pyvista_mesh:
            self.mesh = mesh

        return mesh
