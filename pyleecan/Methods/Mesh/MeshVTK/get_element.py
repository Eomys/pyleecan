# -*- coding: utf-8 -*-

from meshio import read
from os import remove


def get_element(self, indices=None):
    """Return the elements (connectivities).

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    elements: list
        List of element groups (type + array)
    """

    if indices is not None:
        # Extract submesh
        mesh = self.get_mesh_pv(indices=indices)
        # Write submesh in .vtk file
        mesh.save(self.get_path(name="temp"))
        # Read mesh file with meshio (pyvista does not provide the correct element format)
        mesh = read(self.get_path(name="temp"))
        # Remove the temporary .vtk file
        remove(self.get_path(name="temp"))
    else:
        if self.is_pyvista_mesh:
            mesh = self.get_mesh_pv()
            mesh.save(self.get_path(name="mesh"))
        # Read mesh file with meshio (pyvista does not provide the correct element format)
        mesh = read(self.get_path(name=self.name, file_format=self.format))

    elements = {}
    nb_element = 0
    indice_dict = {}
    for element in mesh.cells:
        elements[element.type] = element.data
        nb_element += element.data.shape[0]

    return elements, nb_element, indice_dict
