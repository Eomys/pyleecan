# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_tags, elem_type):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : Mesh
        an Mesh object
    node_tags : array
        an array of node tags

    Returns
    -------
        bool
            False if the element already exist
    """

    # Create the new element
    is_created = self.element[elem_type].add_element(node_tags)

    return is_created
