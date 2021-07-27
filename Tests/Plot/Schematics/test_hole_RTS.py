# -*- coding: utf-8 -*-

from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi, exp

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Functions.labels import decode_label
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
            magnet_1=None,
            magnet_2=Magnet(),
        )
    )
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

    rotor.plot(
        is_show_fig=True
    )  # , save_path=join(save_path, "Shematics", "Hole_RTS.png"))

    # Adding label
    surf_list = rotor.hole[0].build_geometry()
    surf_list.extend(rotor.hole[1].build_geometry())
    for surf in surf_list:
        Zref = surf.point_ref * exp(1j * pi / 2)
        plt.plot(Zref.real, Zref.imag, "xr")
        label_dict = decode_label(surf.label)
        plt.text(
            Zref.real,
            Zref.imag,
            label_dict["surf_type"][4:] + "_" + label_dict["index"],
            weight="bold",
        )
    ax = plt.gca()
    ax.set_xlim(-30e-3, 30e-3)
    ax.set_ylim(50e-3, 90e-3)
    # Set figure to full screen for readibility
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    # Set rotor color to while
    ax.patches[0].set_facecolor((1, 1, 1, 1))

    fig = plt.gcf()
    fig.savefig(join(save_path, "Schematics", "Hole_RTS.png"))
    plt.show()


if __name__ == "__main__":
    test_plot_hole_RTS()