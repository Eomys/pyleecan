# -*- coding: utf-8 -*-


def add_cell(self, node_indices, cell_type):
    """Add a new cell defined by node indices and cell type.

    Parameters
    ----------
    self : MeshMat
        an Mesh object
    node_indices : ndarray
        a ndarray of points indices
    cell_type : str
        Define the type of cell.

    Returns
    -------
    new_ind : int
        indice of the newly created cell. None if the cell already exists.
    """

    # Create the new element
    new_ind = 0
    for key in self.cell:  # There should only one solution
        if self.cell[key].indice is not None and self.cell[key].indice.size > 0:
            tmp_ind = max(self.cell[key].indice)
            new_ind = max(new_ind, tmp_ind)
            new_ind += 1

    test_exist = self.cell[cell_type].add_cell(node_indices, new_ind)

    if test_exist:
        return new_ind
    else:
        return None
