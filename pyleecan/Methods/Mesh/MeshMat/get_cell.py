# -*- coding: utf-8 -*-


def get_cell(self, indice=None):
    """Return the connectivity for one selected element

    Parameters
    ----------
    self : Mesh
        an Mesh object
    indice : list
        list of indice. If None, return all.

    Returns
    -------
    cells: dict
        Dict of connectivities

    """

    cells = dict()
    for key in self.element:
        cells[key] = self.element[key].get_connectivity(indice)

    return cells
