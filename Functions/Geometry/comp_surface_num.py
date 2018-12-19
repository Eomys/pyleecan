# -*- coding: utf-8 -*-
"""@package Functions.comp_num_surface
Computation of the surface of a Polygon function
@date Created on Mon Feb 02 13:54:40 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import array


def comp_surface_num(point_list):
    """Compute the surface of the Poygon defined by the points

    Parameters
    ----------
    point_list : list
        List of complex coordinate of the points

    Returns
    -------
    S: float
        Surface of the closed surface [m**2]

    """

    # We have to be sure that the surface is closed
    # (ie point_list[0]=point_list[end]) If it's already the case Xi+1 - Xi =0
    point_list.append(point_list[0])

    point_array = array(point_list)

    # We translate the points so every point have imag >=0
    min_imag = min(point_array.imag)
    if min_imag < 0:
        point_array += abs(min_imag) * 1j

    S_acc = 0
    for ii in range(point_array.size - 1):
        Var_X = point_array[ii + 1].real - point_array[ii].real
        Var_Y = point_array[ii + 1].imag + point_array[ii].imag

        S_acc += Var_Y * Var_X

    return abs(S_acc / 2.0)
