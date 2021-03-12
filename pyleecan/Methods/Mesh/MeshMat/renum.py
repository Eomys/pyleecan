# -*- coding: utf-8 -*-
import numpy as np
import copy

from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat


def renum(self):
    """Restart point indices from 0, and update connectivity. Indices of cells stay the same.

    Parameters
    ----------
    self : MeshMat
        an Mesh object

    Returns
    -------

    """

    if self._is_renum:
        coord_init = self.get_node()
        node_indice = self.get_node_indice()
        connect_dict, nb_cell, indices = self.get_cell()

        nb_node_new = len(node_indice)
        node_indice_new = np.linspace(0, nb_node_new - 1, nb_node_new, dtype=int)
        connect_dict_new = copy.deepcopy(connect_dict)
        for inode in range(nb_node_new):
            for key in connect_dict:
                connect_dict_new[key][
                    connect_dict[key] == node_indice[inode]
                ] = node_indice_new[inode]

        self.node.indice = node_indice_new

        for key in connect_dict:
            self.cell[key] = CellMat(
                connectivity=connect_dict_new[key],
                nb_cell=len(connect_dict_new[key]),
                nb_node_per_cell=self.cell[key].nb_node_per_cell,
                indice=self.cell[key].indice,
                interpolation=self.cell[key].interpolation,
            )
        
        self._is_renum = False
