# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, field_name="mu", node_tags=None):
    """Define a new NodeMat object based on a set of elements.

     Parameters
     ----------
     self : SolutionFEMM
         an SolutionFEMM object
     node_tags : array
         an array of node tags

     Returns
     -------
     field: array
         an array of field values

     """
    nb_field = len(self.mu)

    if node_tags is None:
        node_tags = np.linspace(0, nb_field - 1, nb_field, dtype=int)

    if field_name is "B":
        field = self.B[node_tags, :]
    elif field_name is "H":
        field = self.H[node_tags, :]
    elif field_name is "mu":
        field = self.mu[node_tags]
    else:
        field = np.zeros((nb_field, 1))

    return field
