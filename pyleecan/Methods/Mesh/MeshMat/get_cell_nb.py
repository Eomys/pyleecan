def get_cell_nb(self):
    """Return the total number of cell of all kind

    Parameters
    ----------
    self : MeshMat
        A MeshMat object

    Returns
    -------
    nb_cell : int
        total number of cell of all kind
    """

    nb_cell = 0
    for key in self.cell:
        if self.cell[key].nb_cell is not None:
            nb_cell += self.cell[key].nb_cell

    return nb_cell
