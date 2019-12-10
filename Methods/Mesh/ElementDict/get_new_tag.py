# -*- coding: utf-8 -*-

import numpy as np


def get_new_tag(self):
    """Return an unused element tag

    Parameters
    ----------
    self : ElementDict
        an ElementDict object

    Returns
    -------
    new_tag: int
        a new available element tag

    """

    tag = self.tag
    new_tag = 0
    if tag is not None:
        for key in tag:  # There should only one solution
            for ie in range(len(tag[key])):
                new_tag = max(new_tag, tag[key][ie])
    new_tag += 1
    return new_tag
