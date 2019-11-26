# -*- coding: utf-8 -*-

from pyleecan.Classes.ElementMat import ElementMat
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
    subelem = ElementMat()

    elements_parent = self.connectivity
    groups = self.group
    elem_tags = np.where(groups == group_number)[0]

    subelem.connectivity = elements_parent[elem_tags, :]
    subelem.group = groups[elem_tags]  # Should be only one type
    subelem.nb_elem = len(elem_tags)
    subelem.nb_node_per_element = self.nb_node_per_element  # Must be the same

    return subelem
