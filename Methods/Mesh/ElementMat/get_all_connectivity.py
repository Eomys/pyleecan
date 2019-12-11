# -*- coding: utf-8 -*-

import numpy as np


def get_all_connectivity(self, group=None):
    """Return the connectivity and tags for a selected group of elements

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    group : numpy.array
        one or several group number

    Returns
    -------
    connect_select: ndarray
        Selected connectivity
    tag_select: ndarray
        Selected element tags

    """

    connect = self.connectivity
    elem_groups = self.group
    elem_tags = self.tag
    connect_select = np.array([], dtype=int)
    tag_select = np.array([], dtype=int)

    if group is not None:
        for grp in group:
            Ipos_select = np.where(elem_groups == grp)[0]
            tag_select = np.concatenate([tag_select, elem_tags[Ipos_select]])
            for Ipos in Ipos_select:
                connect_select = np.concatenate((connect_select, connect[Ipos, :]))

    else:
        connect_select = connect
        tag_select = elem_tags

    return connect_select, tag_select
