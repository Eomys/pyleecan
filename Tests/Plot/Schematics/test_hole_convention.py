# -*- coding: utf-8 -*-

from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import pi, exp

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Functions.load import load
from pyleecan.Functions.labels import HOLEM_LAB, decode_label
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path as save_path


def test_plot_radius():
    """Plot the min/max radius of the Hole"""
    plt.close("all")
    BMW = load(join(DATA_DIR, "Machine", "BMW_i3.json"))

    # Modification for better visualization
    BMW.rotor.hole[0].Zh = 6
    for surf in BMW.rotor.hole[0].surf_list:
        surf.translate(-5e-3)

    fig, ax = BMW.rotor.plot(is_show_fig=False, edgecolor="k")
    # Top and Bottom arc
    (Rint, Rext) = BMW.rotor.hole[0].comp_radius()
    line = Arc1(
        begin=Rext * exp(1j * pi / 4),
        end=Rext * exp(1j * 3 * pi / 4),
        radius=Rext,
        is_trigo_direction=True,
    )
    line.plot(
        fig=fig,
        ax=ax,
        color="0.5",
        linestyle="dotted",
        linewidth=1,
    )
    line = Arc1(
        begin=Rint * exp(1j * pi / 4),
        end=Rint * exp(1j * 3 * pi / 4),
        radius=Rint,
        is_trigo_direction=True,
    )
    line.plot(
        fig=fig,
        ax=ax,
        color="0.5",
        linestyle="dotted",
        linewidth=1,
    )
    # Adding Label
    Zref = Rext * exp(1j * pi / 2)
    ax.plot(Zref.real, Zref.imag, "xr")
    ax.text(
        Zref.real,
        Zref.imag + 1e-3,
        "Rext",
        weight="bold",
    )
    Zref = Rint * exp(1j * pi / 2)
    ax.plot(Zref.real, Zref.imag, "xr")
    ax.text(
        Zref.real,
        Zref.imag + 1e-3,
        "Rint",
        weight="bold",
    )
    # Graph clean-up
    ax.set_xlim(-30e-3, 30e-3)
    ax.set_ylim(50e-3, 90e-3)
    ax.set_axis_off()
    ax.get_legend().remove()
    ax.set_title("")
    # Set rotor color to while
    ax.patches[0].set_facecolor((1, 1, 1, 1))

    fig.savefig(join(save_path, "Schematics", "Hole_radius.png"))
    # plt.show()
    plt.close(fig=fig)


def test_plot_magnet_id():
    """Plot magnet_0, 1 and 2"""
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

    fig, ax = rotor.plot(is_show_fig=False, edgecolor="k")

    # Adding label
    surf_list = rotor.hole[0].build_geometry()
    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if HOLEM_LAB in label_dict["surf_type"]:
            Zref = surf.point_ref * exp(1j * pi / 2)
            ax.text(
                Zref.real - 5e-3,
                Zref.imag,
                "magnet_" + str(label_dict["T_id"]),
                weight="bold",
            )
    ax.set_xlim(-30e-3, 30e-3)
    ax.set_ylim(50e-3, 90e-3)

    # Set rotor color to while
    ax.patches[0].set_facecolor((1, 1, 1, 1))
    ax.set_axis_off()
    ax.get_legend().remove()
    ax.set_title("")

    fig.savefig(join(save_path, "Schematics", "Hole_magnet_id.png"))
    plt.close(fig=fig)


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

    fig, ax = rotor.plot(is_show_fig=False, edgecolor="k")

    # Adding label
    surf_list = rotor.hole[0].build_geometry()
    surf_list.extend(rotor.hole[1].build_geometry())
    for surf in surf_list:
        Zref = surf.point_ref * exp(1j * pi / 2)
        ax.plot(Zref.real, Zref.imag, "xr")
        label_dict = decode_label(surf.label)
        ax.text(
            Zref.real,
            Zref.imag,
            label_dict["surf_type"][4:] + "_" + label_dict["index"],
            weight="bold",
        )
    ax.set_xlim(-30e-3, 30e-3)
    ax.set_ylim(50e-3, 90e-3)
    # Set figure to full screen for readibility
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    # Set rotor color to while
    ax.patches[0].set_facecolor((1, 1, 1, 1))
    ax.set_axis_off()
    ax.get_legend().remove()
    ax.set_title("")
    fig.savefig(join(save_path, "Schematics", "Hole_RTS.png"))
    plt.close(fig=fig)


if __name__ == "__main__":
    test_plot_radius()
    test_plot_magnet_id()
    test_plot_hole_RTS()
    print("Done")
