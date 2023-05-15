# -*- coding: utf-8 -*-


def add_cell(self, node_indices, cell_type):
    """Add a new cell defined by node indices and cell type.

    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    node_indices : ndarray or list of int
        a ndarray of nodes indices (length must match cell.nb_node_per_cell)
    cell_type : str
        Define the type of cell to add (key of self.cell dict)

    Returns
    -------
    new_index : int
        indice of the newly created cell. None if the cell already exists.
    """

    # The cell index must be unique for all cell type
    new_index = self.get_cell_nb()  # index start at 0 (last index = nb-1)

    is_created = self.cell[cell_type].add_cell(node_indices, new_index)

    if is_created:
        return new_index
    else:
        return None
