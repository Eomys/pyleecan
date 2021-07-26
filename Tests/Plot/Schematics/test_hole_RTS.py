# -*- coding: utf-8 -*-

from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleM51 import HoleM51
from Tests import save_plot_path as save_path


def test_plot_hole_RTS():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    rotor = LamHole(
        Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
    )
    rotor.hole = list()
    rotor.hole.append(
        HoleM51(
            Zh=6,
            W0=0.016,
            W1=pi / 6,
            W2=0.004,
            W3=0.01,
            W4=0.002,
            W5=0.01,
            W6=0.002,
            W7=0.01,
            H0=0.01096,
            H1=0.0015,
            H2=0.0055,
            magnet_0=Magnet(),
            magnet_1=Magnet(),
            magnet_2=Magnet(),
        )
    )
    rotor.hole.append(
        HoleM51(
            Zh=6,
            W0=0.016,
            W1=pi / 4,
            W2=0.004,
            W3=0.01,
            W4=0.002,
            W5=0.01,
            W6=0.002,
            W7=0.01,
            H0=0.02,
            H1=0.002,
            H2=0.0055,
            magnet_0=Magnet(),
            magnet_1=Magnet(),
            magnet_2=Magnet(),
        )
    )

    rotor.plot(
        is_show_fig=True
    )  # , save_path=join(save_path, "Shematics", "Hole_RTS.png"))
    plt.show()


if __name__ == "__main__":
    test_plot_hole_RTS()