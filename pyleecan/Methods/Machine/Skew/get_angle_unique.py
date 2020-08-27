# -*- coding: utf-8 -*-

from numpy import unique, array


def get_angle_unique(self):
    """Returns unique skew angles
    
    Parameters
    ----------
    self : Skew
        a Skew object
    
    Returns
    -------
    angles : list
        list of unique skew angles

    """

    if self.angle_list is None:
        self.comp_angle()

    angles = unique(array(self.angle_list).round(decimals=4))

    return angles.tolist()
