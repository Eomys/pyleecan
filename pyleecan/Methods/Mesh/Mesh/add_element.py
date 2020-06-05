# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_tags, elem_type, group=-1):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : Mesh
        an Mesh object
    node_tags : array
        an array of node tags

    Returns
    -------
    new_tag : int
        Tag of the created element. None if the element already exist
    """

    # Create the new element
    new_tag = self.get_new_tag()
    test_exist = self.element[elem_type].add_element(node_tags, new_tag, group)

    if test_exist:
        return new_tag
    else:
        return None
