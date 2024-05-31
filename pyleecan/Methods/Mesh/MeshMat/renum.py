# -*- coding: utf-8 -*-
import copy

import numpy as np

from ....Classes.ElementMat import ElementMat


def renum(self):
    """Restart point indices from 0, and update connectivity. Indices of elements stay the same.

    Parameters
    ----------
    self : MeshMat
        an Mesh object
    """

    if self._is_renum:
        coord_init = self.get_node_coordinate()
        node_indice = self.get_node_indice()
        connect_dict, *_ = self.get_element()

        if max(node_indice) != len(node_indice) - 1:
            connect_dict, *_ = self.get_element()

            nb_node_new = len(node_indice)
            node_indice_new = np.linspace(0, nb_node_new - 1, nb_node_new, dtype=int)
            connect_dict_new = copy.deepcopy(connect_dict)
            for inode in range(nb_node_new):
                for key in connect_dict:
                    connect_dict_new[key][connect_dict[key] == node_indice[inode]] = (
                        node_indice_new[inode]
                    )

            self.node.indice = node_indice_new

            for key in connect_dict:
                self.element_dict[key] = ElementMat(
                    connectivity=connect_dict_new[key],
                    nb_element=len(connect_dict_new[key]),
                    nb_node_per_element=self.element_dict[key].nb_node_per_element,
                    indice=self.element_dict[key].indice,
                    ref_element=self.element_dict[key].ref_element,
                    gauss_point=self.element_dict[key].gauss_point,
                    scalar_product=self.element_dict[key].scalar_product,
                )

        if len(coord_init) != len(node_indice):
            self.clear_node()

        self._is_renum = False
