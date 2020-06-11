# -*- coding: utf-8 -*-

from meshio import read


def get_cells(self, indices=[]):
    """Return the cells (connectivities).

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    cells: list
        List of cell groups (type + array)
    """

    # Read mesh file with meshio (pyvista does not provide the correct cell format)
    mesh = read(self.path + "/" + self.name + "." + self.format)

    return mesh.cells
