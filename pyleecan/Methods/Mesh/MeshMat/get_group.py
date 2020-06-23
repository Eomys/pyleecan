# -*- coding: utf-8 -*-

import numpy as np
from pyleecan.definitions import PACKAGE_NAME


def get_group(self, group_name):
    """Return all cells of the group.

     Parameters
     ----------
     self : MeshMat
         an MeshMat object
     group_name : str
         the name of the group (e.g. "stator")

     Returns
     -------
     grp_cells: dict
         a dict sorted by cell type containing connectivity of the group

     """

    group_ind = self.group[group_name]
    grp_cells = dict()
    connect = list()

    for key in self.cell:
        for ind in group_ind:
            connect.append(self.cell[key].get_connectivity(ind))
        grp_cells[key] = np.array(connect)

    return grp_cells
