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


def build_geometry_half_tooth(self, is_top=False, alpha=0, delta=0):
    """Build the geometry of a Half Tooth

    Parameters
    ----------
    self : LamSlot
        a LamSlot object
    is_top : bool
        To select the part of the tooth (X>0 or X <0)
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
    Zs = self.Zs
    Rbo = self.get_Rbo()

    slot_list = self.build_geometry()
    tooth_list = list()

    # delete some lines
    if is_top:
        for line in slot_list:
            Zbegin = line.get_begin()
            Zend = line.get_end()
            # append line
            if imag(Zbegin) < 0 or imag(Zend) < 0:
                tooth_list.append(line)
        T_angle = pi / Zs  # To rotate the tooth
        # add bore line
        Zbo = Rbo * exp(-1j * pi / Zs)
        split_id = -1
        tooth_list.insert(0, Arc1(Zbo, tooth_list[0].get_begin(), Rbo))
    else:
        for line in slot_list:
            Zbegin = line.get_begin()
            Zend = line.get_end()
            # append line
            if imag(Zbegin) > 0 or imag(Zend) > 0:
                tooth_list.append(line)
        T_angle = -pi / Zs  # To rotate the tooth
        # add bore line
        Zbo = Rbo * exp(1j * pi / Zs)
        split_id = 0
        tooth_list.append(Arc1(tooth_list[-1].get_end(), Zbo, Rbo))

    # cut by half (yoke)
    if isinstance(tooth_list[split_id], Segment):
        tooth_list[split_id].end = tooth_list[split_id].get_middle()
    elif isinstance(tooth_list[split_id], Arc):
        R = tooth_list[split_id].comp_radius()
        Zbegin = tooth_list[split_id].get_begin()
        Zend = tooth_list[split_id].get_middle()
        tooth_list[split_id] = Arc1(Zbegin, Zend, R)

    # rotate
    for line in tooth_list:
        line.rotate(alpha + T_angle)

    # translate
    for line in tooth_list:
        line.translate(delta)

    return tooth_list
