# -*- coding: utf-8 -*-

from numpy import abs, pi, sqrt, sin


def comp_maxseg(self, elementsize, maxseg_amp):
    """
    Computes the number of segments per arc degrees in
    function of the elementsize of the region

    Parameters
    ----------
    self : Arc
        An Arc object
    elementsize : float
        max element size parameter
    maxseg_amp : float
        amplifying factor

    Returns
    -------
    maxseg : float
        number of segments per arc degrees
    """

    angle = self.get_angle(is_deg=True)
    begin = self.get_begin()
    end = self.get_end()

    if abs(angle) == 180:
        l_arc = pi * abs(begin - end) / 2
    elif abs(angle) == 90:
        l_arc = pi / 2 * abs(begin - end) / sqrt(2)
    else:
        l_arc = abs((begin - end) / (2 * sin(angle / 2 * pi / 180))) * abs(
            angle * pi / 180
        )

    n_seg = l_arc / elementsize

    maxseg = abs(min(10, abs(angle / n_seg * maxseg_amp)))

    return maxseg
