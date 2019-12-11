# -*- coding: utf-8 -*-

import numpy as np


def get_group(self, group_number):
    """Define an Element object as submesh of parent mesh object

     Parameters
     ----------
     self : ElementMat
         an ElementMat object
     group_number : int
         a group number which define the elements which constitute the submesh

     Returns
     -------
     subelem: ElementMat
         an ElementMat which is a submesh of parent mesh self related to group_number

     """
    module = __import__("pyleecan.Classes." + "ElementMat", fromlist=["ElementMat"])
    subelem = getattr(module, "ElementMat")()

    connect_parent = self.connectivity
    groups = self.group
    tags = self.tag
    Ielem = np.where(groups == group_number)[0]
    subelem.connectivity = connect_parent[Ielem, :]
    subelem.group = groups[Ielem]  # Should be only one type
    subelem.tag = tags[Ielem]
    subelem.nb_elem = len(Ielem)
    subelem.nb_node_per_element = self.nb_node_per_element  # Must be the same

    return subelem
