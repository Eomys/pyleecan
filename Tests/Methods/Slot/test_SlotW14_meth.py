# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data

from pyleecan.Classes.SlotW14 import SlotW14
from numpy import ndarray, arcsin
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

SlotW14_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10e-3)
SlotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.9443933e-4,
        "Aw": 0.08445503,
        "SW_exp": 2.28378e-4,
        "H_exp": 0.03486507,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10e-3)
SlotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.0790294e-4,
        "Aw": 0.108324,
        "SW_exp": 4.332517e-4,
        "H_exp": 0.03572334,
    }
)


@ddt
class test_SlotW14_meth(TestCase):
    """unittest for SlotW14 methods"""

    @data(*SlotW14_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*SlotW14_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*SlotW14_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*SlotW14_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        self.assertEqual(a, 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325)))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW14_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
