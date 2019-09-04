"""@package Methods.Machine.NotchEvenDist.build_geometry
NotchEvenDist build_geometry method
@date Created on 03-09-2019 15:47
@author sebastian_g
@todo: intermediate solution, <nittest it ony if needed
"""

from pyleecan.Classes.Arc1 import Arc1
import numpy as np


def build_geometry(self, alpha_begin, alpha_end, label=""):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object

    Returns
    -------
    curve_list: list
        A list of every individual notches lines

    """
    Rbo = self.get_Rbo()

    alphaM = np.array([])
    alpha0 = np.array([])
    alpha1 = np.array([])
    _line_list = list()

    # collect all notches data
    for idx, shape in enumerate(self.notch_shape):
        Zs = shape.Zs

        ang_open = self.notch_shape[idx].comp_angle_opening()

        aM = np.linspace(0, Zs, Zs, endpoint=False) * 2 * np.pi / Zs + self.alpha[idx]
        a0 = aM - ang_open / 2
        a1 = aM + ang_open / 2

        sid = np.ones_like(alphaM) * idx

        alphaM = np.append(alphaM, aM)
        alpha0 = np.append(alpha0, a0)
        alpha1 = np.append(alpha1, a1)

        for ang in aM:
            lines = shape.build_geometry()
            for line in lines:
                line.rotate(ang)
                line.label = label
            _line_list.append(lines)

    # sort notches by angle
    sort_id = np.argsort(alphaM)
    alphaM = alphaM[sort_id]
    alpha0 = alpha0[sort_id]
    alpha1 = alpha1[sort_id]
    _line_list = [_line_list[id] for id in sort_id]

    # delete notches outside desired angular range
    keep_id = (alpha0 > alpha_begin) & (alpha1 < alpha_end)
    keep_id = np.where(keep_id)[0]
    alphaM = alphaM[keep_id]
    alpha0 = alpha0[keep_id]
    alpha1 = alpha1[keep_id]
    _line_list = [_line_list[id] for id in keep_id]

    # build connected line list
    line_list = list()

    # if there are notches left
    if _line_list:

        # arc to first notch
        Z1 = Rbo * np.exp(1j * alpha_begin)
        Z2 = _line_list[0][0].get_begin()
        arc = Arc1(begin=Z1, end=Z2, radius=Rbo, label=label)
        line_list.append(arc)
        line_list.extend(_line_list[0])

        # inter notch arcs
        for idx in range(len(_line_list) - 1):
            Z1 = _line_list[idx][-1].get_end()
            Z2 = _line_list[idx + 1][0].get_begin()
            arc = Arc1(begin=Z1, end=Z2, radius=Rbo, label=label)
            line_list.append(arc)
            line_list.extend(_line_list[idx + 1])

        Z1 = _line_list[-1][-1].get_end()
        Z2 = Rbo * np.exp(1j * alpha_end)
        arc = Arc1(begin=Z1, end=Z2, radius=Rbo, label=label)
        line_list.append(arc)
    # if there are no notches on bore line
    else:
        # print("No Notches on Bore Line  ")
        Z1 = Rbo * np.exp(1j * alpha_begin)
        Z2 = Rbo * np.exp(1j * alpha_end)
        arc = Arc1(begin=Z1, end=Z2, radius=Rbo, label=label)
        line_list.append(arc)

    return line_list
