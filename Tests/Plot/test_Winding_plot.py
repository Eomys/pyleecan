# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui, QtCore

from os.path import join

import matplotlib.pyplot as plt
from numpy import pi, linspace

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from Tests import save_plot_path as save_path
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


class Test_Winding_plot(object):
    """unittest for Winding connection matrix plot"""

    def test_type_wind_CW2LT(self):
        """Test Winding matrix plot for type_winding CW2LT"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW22(Zs=6, H0=20e-3, H2=0.2, W0=pi / 10, W2=pi / 6)
        test_obj.winding = WindingUD(p=2, qs=3)
        test_obj.winding.init_as_CW2LT()

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_wind.png"))

        test_obj.slot = SlotW22(Zs=12, H0=20e-3, H2=0.2, W0=pi / 12, W2=pi / 8)
        test_obj.winding.init_as_CW2LT()
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_ms=0,25.png"))

        test_obj.winding.p = 4
        test_obj.winding.init_as_CW2LT()
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LT_lam_p=4.png"))

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False, is_stator=False)
        test_obj.slot = SlotW22(Zs=6, H0=20e-3, H2=0.2, W0=pi / 10, W2=pi / 6)
        test_obj.winding = WindingUD(p=2, qs=3)
        test_obj.winding.init_as_CW2LT()
        test_obj.plot_winding(all_slot=True, is_show_fig=False)

    def test_type_wind_CW1L(self):
        """Test Winding matrix plot for type_winding CW1L"""

        plt.close("all")
        # Artificial winding for test purpose
        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=36, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingUD(p=3, qs=3)
        test_obj.winding.init_as_CW1L()

        test_obj.plot(
            is_show_fig=False, save_path=join(save_path, "test_Wind_CW1L_lam.png")
        )

        test_obj.plot_winding(
            is_show_fig=False, save_path=join(save_path, "test_Wind_CW1L_wind.png")
        )

        test_obj.slot.Zs = 20
        test_obj.winding.qs = 5

        test_obj.winding.init_as_CW1L()
        test_obj.plot(
            is_show_fig=False, save_path=join(save_path, "test_Wind_CW1L_lam2.png")
        )

        test_obj.plot_winding(
            is_show_fig=False, save_path=join(save_path, "test_Wind_CW1L_wind2.png")
        )

    def test_type_wind_DW2L(self):
        """Test Winding matrix plot for type_winding DW2L"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=36, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingUD(p=3, qs=3, coil_pitch=5)
        test_obj.winding.init_as_DWL(nlay=2)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_wind.png"))

        test_obj.slot.Zs = 24
        test_obj.winding = WindingUD(p=1, qs=3, coil_pitch=10)
        test_obj.winding.init_as_DWL(nlay=2)
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW2L_wind2.png"))

    def test_type_wind_DW1L(self):
        """Test Winding matrix plot for type_winding DW1L"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=24, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingUD(p=1, qs=3)
        test_obj.winding.init_as_DWL(nlay=1)

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.winding = WindingUD(p=2, qs=3)
        test_obj.winding.init_as_DWL(nlay=1)
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_DW1L_wind2.png"))

    def test_type_wind_CW2LR(self):
        """Test Winding matrix plot for type_winding CW2LR"""

        plt.close("all")

        test_obj = LamSlotWind(Rint=0.5, Rext=0.9, is_internal=False)
        test_obj.slot = SlotW21(
            Zs=12, H0=20e-3, H1=0, H1_is_rad=False, H2=0.2, W0=30e-3, W1=0.06, W2=0.06
        )
        test_obj.winding = WindingUD(p=5, qs=3)
        test_obj.winding.init_as_CW2LR()

        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind.png"))

        test_obj.slot.Zs = 36
        test_obj.winding.init_as_CW2LR()
        test_obj.plot(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_lam2.png"))

        test_obj.plot_winding(is_show_fig=False)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Wind_CW2LR_wind2.png"))

    def test_plot_mmf_unit(self):
        """Test plot unit mmf"""
        Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
        Toyota_Prius.stator.plot_mmf_unit(
            save_path=join(save_path, "test_unit_mmf.png")
        )

    def test_plot_radial(self):
        machine_list = [
            "Toyota_Prius",
            "Audi_eTron",
            "Benchmark",
            "BMW_i3",
            "Jaguar_I_Pace",
            "Railway_Traction",
            "Renault_Zoe",
            "Protean_InWheel",
        ]
        for machine_name in machine_list:
            machine = load(join(DATA_DIR, "Machine", machine_name + ".json"))
            machine.stator.plot(
                is_winding_connection=True,
                save_path=join(save_path, "test_plot_radial_" + machine_name + ".png"),
            )

    def test_plot_linear(self):
        machine_list = [
            "Toyota_Prius",
            "Renault_Zoe",
            "Audi_eTron",
            "Benchmark",
            "Railway_Traction",
            "Protean_InWheel",
        ]
        for machine_name in machine_list:
            machine = load(join(DATA_DIR, "Machine", machine_name + ".json"))
            machine.stator.winding.plot_linear(
                is_max_sym=True,
                save_path=join(
                    save_path, "test_plot_linear_" + machine_name + "_max_sym_.png"
                ),
            )
            machine.stator.winding.plot_linear(
                is_max_sym=False,
                save_path=join(save_path, "test_plot_linear_" + machine_name + ".png"),
            )


if __name__ == "__main__":
    a = Test_Winding_plot()
    # a.test_plot_mmf_unit()
    a.test_plot_radial()
    # a.test_plot_linear()
    print("Done")
