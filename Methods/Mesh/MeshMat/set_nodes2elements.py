# -*- coding: utf-8 -*-

import numpy as np


def set_nodes2elements(self):
    """Compute the total number of elements in the stored mesh

    Parameters
    ----------
    self : Mesh
        an Mesh object

    Returns
    -------
    Nb_elem_tot: int
        Total number of elements mesh

    """

    elements = self.elements
    nodes_to_elements = dict()

    Ntype_elem = self.get_Ntype_elem()
    # Compute the number of elements
    for jj in range(self.Nb_nodes_tot):
        nodes_to_elements[jj] = list()
        for je in range(Ntype_elem):
            Ie2n = np.where(jj == elements[je].connectivity)
            Ie2n_list = Ie2n[0].tolist()
            nodes_to_elements[jj].extend(Ie2n_list)

    return nodes_to_elements

