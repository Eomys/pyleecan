# -*- coding: utf-8 -*-
import numpy as np


def add_cell(self, pt_indice, cell_type, group_name=None):
    """Add a new cell defined by a point indices

    Parameters
    ----------
    self : MeshMat
        an Mesh object
    pt_indice : ndarray
        a ndarray of points indices
    group_name : str
        name of the group

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

    test_exist = self.cell[cell_type].add_cell(pt_indice, new_ind)

    if test_exist:
        if group_name in self.group:
            self.group[group_name] = np.append(self.group[group_name], new_ind)
        else:
            self.group[group_name] = np.array([new_ind])

        return new_ind
    else:
        return None
