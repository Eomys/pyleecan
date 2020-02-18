# -*- coding: utf-8 -*-

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi, array, linspace

from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.LamSlotMulti import LamSlotMulti
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.VentilationTrap import VentilationTrap

from pyleecan.Tests import save_plot_path as save_path


class test_SlotMulti(TestCase):
    """unittest for UserDefined slot
    """

    def test_2_slot_notch(self):
        """Test that you can plot a LamSlotMulti
        """

        plt.close("all")
        test_obj = LamSlotMulti(
            Rint=0.2,
            Rext=0.7,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )

        Slot1 = SlotW10(
            Zs=10, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=12, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        slot_list = list()
        for ii in range(5):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        test_obj.slot_list = slot_list
        test_obj.slot_list[0].H2 = 300e-3
        test_obj.slot_list[7].H2 = 300e-3

        slot3 = SlotW10(Zs=12, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=15 * pi / 180)
        test_obj.notch = [notch]

        test_obj.alpha = (
            array([0, 29, 60, 120, 150, 180, 210, 240, 300, 330]) * pi / 180
        )

        # Plot, check and save
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_SlotMulti.png"))
        self.assertEqual(len(fig.axes[0].patches), 2)

    def test_sym(self):
        """Test that you can plot a LamSlotMulti with sym
        """

        plt.close("all")
        test_obj = LamSlotMulti(
            Rint=0.2,
            Rext=0.7,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )

        Zs = 8
        Slot1 = SlotW10(
            Zs=Zs, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=Zs, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        slot_list = list()
        for ii in range(Zs // 2):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        test_obj.slot_list = slot_list

        slot3 = SlotW10(Zs=Zs // 2, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=2 * pi / Zs)
        test_obj.notch = [notch]

        test_obj.alpha = linspace(0, 2 * pi, 8, endpoint=False) + pi / Zs

        # Plot, check and save
        test_obj.plot(sym=2)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_SlotMulti_sym.png"))
        self.assertEqual(len(fig.axes[0].patches), 1)
