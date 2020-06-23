# -*- coding: utf-8 -*-

import numpy as np
from ....definitions import PACKAGE_NAME


def get_group(self, group_number):
    """Define an Element object as submesh of parent mesh object

     Parameters
     ----------
     self : CellMat
         an CellMat object
     group_number : int
         a group number which define the elements which constitute the submesh

     Returns
     -------
     subelem: CellMat
         an CellMat which is a submesh of parent mesh self related to group_number

     """
    module = __import__(PACKAGE_NAME + ".Classes." + "CellMat", fromlist=["CellMat"])
    grp_elem = getattr(module, "CellMat")()

    connect_parent = self.connectivity
    groups = self.group
    tags = self.tag
    grp_elem.nb_node_per_element = self.nb_node_per_element

    grp_connect, grp_tags = self.get_all_connectivity(group_number)
    nb_elem_grp = len(grp_tags)
    if nb_elem_grp > 1:
        for ie in range(nb_elem_grp):
            grp_elem.add_element(grp_connect[ie], grp_tags[ie])
    elif nb_elem_grp == 1:
        grp_elem.add_element(grp_connect, grp_tags[0])

    return grp_elem
