# -*- coding: utf-8 -*-


def add_cell(self, pt_indice, cell_type, group=-1):
    """Add a new cell defined by a point indices

    Parameters
    ----------
    self : MeshMat
        an Mesh object
    pt_indice : ndarray
        a ndarray of points indices

    Returns
    -------
    new_ind : int
        Tag of the created element. None if the element already exist
    """

    # Create the new element
    new_ind = 0
    for key in self.cell:  # There should only one solution
        if self.cell[key].indice.size > 0:
            tmp_ind = max(self.cell[key].indice)
            new_ind = max(new_ind, tmp_ind)
            new_ind += 1

    test_exist = self.cell[cell_type].add_cell(pt_indice, new_ind, group)

    if test_exist:
        return new_ind
    else:
        return None
