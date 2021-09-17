# -*- coding: utf-8 -*-

from os.path import join
import pytest

import matplotlib.pyplot as plt

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.labels import HOLEV_LAB


def test_HoleUD_vent_plot():
    plt.close("all")

    test_obj = Lamination(is_internal=True, Rint=0.1, Rext=0.2, is_stator=False, L1=0.7)
    vent = HoleUD(Zh=8)
    line_list = list()
    W = 0.01
    C = 0.15
    line_list.append(Segment(C - W - 1j * W, C + W - 1j * W))
    line_list.append(Segment(C + W - 1j * W, C + W + 1j * W))
    line_list.append(Segment(C + W + 1j * W, C - W + 1j * W))
    line_list.append(Segment(C - W + 1j * W, C - W - 1j * W))
    vent.surf_list = [SurfLine(line_list=line_list, label=HOLEV_LAB)]

    test_obj.axial_vent = [vent]
    test_obj.plot(is_show_fig=False)


if __name__ == "__main__":
    test_HoleUD_vent_plot()
