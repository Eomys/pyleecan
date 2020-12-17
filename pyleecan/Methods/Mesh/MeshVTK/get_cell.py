# -*- coding: utf-8 -*-

from meshio import read
from os import remove

# TODO investigate on indices, also compare with MeshMat get_cell
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
        mesh = self.get_mesh_pv(indices=indices)
        # Write submesh in .vtk file
        mesh.save(self.path + "/temp.vtk")
        # Read mesh file with meshio (pyvista does not provide the correct cell format)
        mesh = read(self.path + "/temp.vtk")
        # Remove the temporary .vtk file
        remove(self.path + "/temp.vtk")

    else:
        # Read mesh file with meshio (pyvista does not provide the correct cell format)
        mesh = read(self.path + "/" + self.name + "." + self.format)
    
    cells = {}
    nb_cell = 0
    indice_dict = {}
    for cell in mesh.cells:
        cells[cell.type] = cell.data
        nb_cell += cell.data.shape[0]

    return cells, nb_cell, indice_dict
