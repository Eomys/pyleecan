# -*- coding: utf-8 -*-

from numpy import unique, array


def get_ind_unique(self):
    """Returns indices corresponding to unique skew angles
    
    Parameters
    ----------
    self : Skew
        a Skew object
    
    Returns
    -------
    indices : list
        list of indices corresponding to unique skew angles

    """

    if self.angle_list is None:
        self.comp_angle()

    (angles, indices) = unique(
        array(self.angle_list).round(decimals=4), return_inverse=True
    )

    return indices.tolist()
