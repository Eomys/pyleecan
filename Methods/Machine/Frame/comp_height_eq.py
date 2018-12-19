# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.comp_equivalent_height
Frame computation of equivalent height methods
@date Created on Mon Jan 26 17:57:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height_eq(self):
    """Computation of the Frame equivalent Height for the mechanical model

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Hfra: float
        Equivalent Height of the Frame [m]

    """

    return self.Rext - self.Rint
