# -*- coding: utf-8 -*-

import numpy as np


def get_new_tag(self):
    """Return an unused element tag

    Parameters
    ----------
    self : ElementMat
        an ElementMat object

    Returns
    -------
    new_tag: int
        a new available element tag

    """

    tag = self.tag

    if tag.size == 0:
        new_tag = 0
    else:
        new_tag = max(tag) + 1

    return new_tag
