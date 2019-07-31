# -*- coding: utf-8 -*-
"""@package build_geometry_half_tooth
@date Created on 11:31 31.07.2019
@author sebastian_g
@todo distinguish between different bore geometries (line, arc, ...)
"""
from numpy import imag, pi, exp

from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc import Arc
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry_half_tooth(self, alpha=0, delta=0):
    """Build the geometry of a Half Tooth

    Parameters
    ----------
    self : LamSlot
        a LamSlot object
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the half tooth including slot base

    """

    # getting Number of Slot
    Zs = self.slot.Zs

    Rbo = self.get_Rbo()
    Zbo = Rbo * exp(-1j * pi / Zs)

    slot_list = self.slot.build_geometry()
    tooth_list = list()

    # delete some lines
    for line in slot_list:
        Zbegin = line.get_begin()
        Zend = line.get_end()
        # append line
        if imag(Zbegin) < 0 or imag(Zend) < 0:
            tooth_list.append(line)

    # add bore line
    tooth_list.insert(0, Arc1(Zbo, tooth_list[0].get_begin(), Rbo))

    # cut last line by half (yoke)
    if isinstance(tooth_list[-1], Segment):
        tooth_list[-1].end = tooth_list[-1].get_middle()

    elif isinstance(tooth_list[-1], Arc):
        R = tooth_list[-1].comp_radius()
        Zbegin = tooth_list[-1].get_begin()
        Zend = tooth_list[-1].get_middle()
        tooth_list[-1] = Arc1(Zbegin, Zend, R)

    # rotate
    for line in tooth_list:
        line.rotate(alpha + pi / Zs)

    # translate
    for line in tooth_list:
        line.translate(delta)

    return tooth_list
