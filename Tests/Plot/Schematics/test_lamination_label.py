from os import remove
from os.path import isfile, join

import matplotlib.pyplot as plt
from numpy import exp, pi
from pyleecan.Classes.import_all import *

from pyleecan.Functions.Plot import P_FONT_SIZE, TEXT_BOX
from Tests import SCHEMATICS_PATH


def test_MachineUD():
    """Lamination label on MachineUD"""

    file_path = join(SCHEMATICS_PATH, "Lamination_label.png")
    # Delete previous plot
    if isfile(file_path):
        remove(file_path)

    machine = MachineUD()
    machine.name = "Machine with 4 laminations"

    # Main geometry parameter
    Rext = 170e-3  # Exterior radius of outter lamination
    W1 = 30e-3  # Width of first lamination
    A1 = 2.5e-3  # Width of the first airgap
    W2 = 20e-3
    A2 = 10e-3
    W3 = 20e-3
    A3 = 2.5e-3
    W4 = 60e-3

    # Outer stator
    lam1 = LamSlotWind(Rext=Rext, Rint=Rext - W1, is_internal=False, is_stator=True)
    lam1.slot = SlotW22(
        Zs=12, W0=2 * pi / 12 * 0.75, W2=2 * pi / 12 * 0.75, H0=0, H2=W1 * 0.65
    )
    lam1.winding = WindingCW2LT(qs=3, p=3)
    # Outer rotor
    lam2 = LamSlot(
        Rext=lam1.Rint - A1, Rint=lam1.Rint - A1 - W2, is_internal=True, is_stator=False
    )
    lam2.slot = SlotW10(Zs=22, W0=25e-3, W1=25e-3, W2=15e-3, H0=0, H1=0, H2=W2 * 0.75)
    # Inner rotor
    lam3 = LamSlot(
        Rext=lam2.Rint - A2,
        Rint=lam2.Rint - A2 - W3,
        is_internal=False,
        is_stator=False,
    )
    lam3.slot = SlotW10(
        Zs=22, W0=17.5e-3, W1=17.5e-3, W2=12.5e-3, H0=0, H1=0, H2=W3 * 0.75
    )
    # Inner stator
    lam4 = LamSlotWind(
        Rext=lam3.Rint - A3, Rint=lam3.Rint - A3 - W4, is_internal=True, is_stator=True
    )
    lam4.slot = SlotW10(Zs=12, W0=25e-3, W1=25e-3, W2=1e-3, H0=0, H1=0, H2=W4 * 0.75)
    lam4.winding = WindingCW2LT(qs=3, p=3)
    # Machine definition
    machine.lam_list = [lam1, lam2, lam3, lam4]
    label_list = machine.get_lam_list_label()
    lam_list = machine.get_lam_list()

    assert len(label_list) == 4
    assert label_list[0] == "Stator-0"
    assert label_list[1] == "Rotor-0"
    assert label_list[2] == "Rotor-1"
    assert label_list[3] == "Stator-1"

    machine.plot(is_show_fig=False)
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_xlim(-Rext * 1.01, Rext * 1.01)
    ax.set_ylim(0, Rext * 1.01)
    ax.set_title("")
    ax.get_legend().remove()
    ax.set_axis_off()

    for ii, lam in enumerate(lam_list):
        R = (lam.Rext + lam.Rint) / 2
        Z = R * exp(1j * pi / 2)
        ax.text(
            Z.real,
            Z.imag,
            label_list[ii],
            fontsize=P_FONT_SIZE,
            bbox=TEXT_BOX,
        )
    fig.savefig(file_path)


if __name__ == "__main__":
    test_MachineUD()