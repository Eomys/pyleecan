# -*- coding: utf-8 -*-

import numpy as np


def get_new_tag(self):
    """Return an unused element tag

    Parameters
    ----------
    self : Mesh
        an Mesh object

    Returns
    -------
    new_tag: int
        a new available element tag

    """

    new_tag = 0

    for key in self.element:  # There should only one solution
        if self.element[key].tag.size > 0:
            tmp_tag = max(self.element[key].tag)
            new_tag = max(new_tag, tmp_tag)
            new_tag += 1

    return new_tag
