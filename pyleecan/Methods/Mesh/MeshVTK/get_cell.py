# -*- coding: utf-8 -*-

from meshio import read
from os import remove


def get_cell(self, indices=None):
    """Return the cells (connectivities).

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    cells: list
        List of cell groups (type + array)
    """

    if indices is not None:
        # Extract submesh
        mesh = self.get_mesh(indices=indices)
        # Write submesh in .vtk file
        mesh.save("temp.vtk")
        # Read mesh file with meshio (pyvista does not provide the correct cell format)
        mesh = read("temp.vtk")

    else:
        # Read mesh file with meshio (pyvista does not provide the correct cell format)
        mesh = read(self.path + "/" + self.name + "." + self.format)

    cells = mesh.cells

    if indices is not None:
        remove("temp.vtk")

    return cells
