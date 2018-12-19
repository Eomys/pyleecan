# -*- coding: utf-8 -*-
"""
@date Created on Thu Dec 18 13:56:20 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from unittest import TestCase

from ddt import ddt, data

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.Segment import Segment
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface

from numpy import exp

Mag10_test = list()
# Internal Slot
lam = LamSlotMag(is_internal=True, Rext=0.1325)
lam.slot = SlotMFlat(H0=5e-3, W0=10e-3, Zs=12)
lam.slot.magnet = [MagnetType10(Hmag=5e-3, Wmag=10e-3)]
Mag10_test.append({"test_obj": lam, "S_exp": 5e-5, "Ao": 0.078449, "H_exp": 5e-3})

# Outward Slot
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotMFlat(H0=5e-3, W0=10e-3, Zs=12)
lam.slot.magnet = [MagnetType10(Hmag=5e-3, Wmag=10e-3)]
Mag10_test.append({"test_obj": lam, "S_exp": 5e-5, "Ao": 0.072745, "H_exp": 5e-3})

# For AlmostEqual
DELTA = 1e-4


@ddt
class test_Magnet_Type_10_meth(TestCase):
    """unittest for MagnetType10 methods
    """

    @data(*Mag10_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Compare numerical and analytical results
        b = comp_surface(test_obj.slot.magnet[0])
        msg = "Analytical: " + str(a) + " Numerical " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*Mag10_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*Mag10_test)
    def test_comp_angle_op(self, test_dict):
        """Check that the computation of the opening angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_angle_opening()

        a = result
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    def test_build_geometry_in(self):
        """check that curve_list is correct (inwards magnet)
        """
        lam = LamSlotMag(
            Rint=40e-3,
            Rext=1,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        lam.slot = SlotMFlat(
            Zs=8, W0=0.6, H0=0.2, magnet=[MagnetType10(Wmag=0.6, Hmag=0.2)]
        )
        test_obj = lam.slot.magnet[0]
        alpha = lam.slot.comp_angle_opening_magnet()
        Z1 = 1 * exp(-1j * alpha / 2) - 0.2
        Z2 = 1 * exp(1j * alpha / 2) - 0.2
        Z3 = Z1 + 0.2
        Z4 = Z2 + 0.2

        # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z2))
        curve_list.append(Segment(Z2, Z1))

        surface = test_obj.build_geometry()
        result = surface[0].get_lines()
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

            a = result[i].end
            b = curve_list[i].end
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_build_geometry_out(self):
        """check that curve_list is correct (outwards magnet)
        """

        lam = LamSlotMag(
            Rint=1,
            Rext=0.09,
            is_internal=False,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        lam.slot = SlotMFlat(
            Zs=8, W0=0.6, H0=0.2, magnet=[MagnetType10(Wmag=0.6, Hmag=0.2)]
        )
        test_obj = lam.slot.magnet[0]
        alpha = lam.slot.comp_angle_opening_magnet()
        Z1 = 1 * exp(-1j * alpha / 2) + 0.2
        Z2 = 1 * exp(1j * alpha / 2) + 0.2
        Z3 = Z1 - 0.2
        Z4 = Z2 - 0.2

        # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z2))
        curve_list.append(Segment(Z2, Z1))

        surface = test_obj.build_geometry()
        result = surface[0].get_lines()
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

            a = result[i].end
            b = curve_list[i].end
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)
