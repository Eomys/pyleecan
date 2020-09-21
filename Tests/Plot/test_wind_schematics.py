from os.path import join

import matplotlib.pyplot as plt
import pytest
from numpy import exp, pi, zeros

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.definitions import config_dict
from Tests import save_plot_path as save_path


test_obj = LamSlotWind(Rint=0.4, Rext=1, is_stator=True, is_internal=False)
test_obj.slot = SlotW10(
    Zs=6, W0=125e-3 * 2, W1=200e-3 * 2, W2=125e-3 * 2, H0=30e-3, H1=60e-3, H2=0.4
)
sp = 2 * pi / test_obj.slot.Zs
wind_mat = zeros((3, 2, 6, 6))
wind_mat[0, 0, 0, 0] = 1
wind_mat[1, 0, 0, 1] = 1
wind_mat[2, 0, 0, 2] = 1
wind_mat[0, 1, 0, 3] = -1
wind_mat[1, 1, 0, 4] = -1
wind_mat[2, 1, 0, 5] = -1
test_obj.winding = WindingUD(user_wind_mat=wind_mat)


CURVE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]


def test_slot():
    """Schematics for slot number"""

    plt.close("all")
    test_obj.plot(is_lam_only=True)

    # Add Label
    fig = plt.gcf()

    R = test_obj.Rint + (test_obj.Rext - test_obj.Rint) / 4
    for ii in range(test_obj.slot.Zs):
        Z = R * exp(1j * (ii * sp + sp / 2))
        fig.axes[0].text(Z.real, Z.imag, str(ii))

    # Remove legend
    ax = plt.gca()
    ax.get_legend().remove()

    # Add X axis
    plt.arrow(0, 0, test_obj.Rext * 1.1, 0, color=CURVE_COLORS[0], width=0.025)
    ax.text(test_obj.Rext * 1.2, 0.1, "X axis")

    # Save
    fig.savefig(join(save_path, "test_Wind_Slot.png"))


def test_rad_tan():
    """Schematics for rad/tan layer"""

    plt.close("all")
    # Plot first slot on X axis
    test_obj.plot(alpha=-sp / 2)

    # # Add Label
    fig = plt.gcf()
    surf_list = test_obj.slot.build_geometry_wind(3, 2)
    for surf in surf_list:
        txt = surf.label[6:-3]
        fig.axes[0].text(surf.point_ref.real, surf.point_ref.imag, txt)
    fig.axes[0].text(0.6, 0.15, "Nlay_rad = 3")
    fig.axes[0].text(0.9, -0.05, "Nlay_tan = 2", rotation=90)

    # Zoom on first slot
    fig.axes[0].set_xlim(0.4, 1)
    fig.axes[0].set_ylim(-0.25, 0.25)

    # Remove legend
    fig.axes[0].get_legend().remove()

    # Save
    fig.savefig(join(save_path, "test_Wind_Layer.png"))
