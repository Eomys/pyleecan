# -*- coding: utf-8 -*-
from numpy import imag, pi, exp
from numpy import abs as np_abs
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
    top_list = list()
    bot_list = list()

    for line in slot_list:
        Zbegin = line.get_begin()
        Zend = line.get_end()
        # append line
        if imag(Zbegin) <= 0 and imag(Zend) <= 0:
            top_list.append(line)
        elif imag(Zbegin) >= 0 and imag(Zend) >= 0:
            bot_list.append(line)
        else:  # The line cross the X axis => split
            # Copy the line (split_half modify the object)
            line2 = type(line)(init_dict=line.as_dict())
            # Split the lines
            line.split_half(is_begin=True)
            line2.split_half(is_begin=False)
            if imag(Zbegin) < 0:
                top_list.append(line)
                bot_list.append(line2)
            else:
                top_list.append(line2)
                bot_list.append(line)

    # add bore lines
    Zbo = Rbo * exp(-1j * pi / Zs)
    if np_abs(Zbo - top_list[0].get_begin()) > 1e-6:
        top_list.insert(
            0, Arc1(Zbo, top_list[0].get_begin(), Rbo, label="Tooth_bore_arc_top")
        )
    Zbo = Rbo * exp(1j * pi / Zs)
    if np_abs(Zbo - bot_list[-1].get_end()) > 1e-6:
        bot_list.append(
            Arc1(bot_list[-1].get_end(), Zbo, Rbo, label="Tooth_bore_arc_bot")
        )

    # Select the lines to return
    if is_top:
        tooth_list = top_list
        T_angle = pi / Zs
    else:
        tooth_list = bot_list
        T_angle = -pi / Zs

    # rotate
    for line in tooth_list:
        line.rotate(alpha + T_angle)

    # translate
    for line in tooth_list:
        line.translate(delta)

    return tooth_list
