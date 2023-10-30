# -*- coding: utf-8 -*-
import copy

import numpy as np

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat


def renum(self):
    """Restart point indices from 0, and update connectivity. Indices of elements stay the same.

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
        connect_dict, nb_element, indices = self.get_element()

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
            self.element[key] = ElementMat(
                connectivity=connect_dict_new[key],
                nb_element=len(connect_dict_new[key]),
                nb_node_per_element=self.element[key].nb_node_per_element,
                indice=self.element[key].indice,
                interpolation=self.element[key].interpolation,
            )

        self._is_renum = False
