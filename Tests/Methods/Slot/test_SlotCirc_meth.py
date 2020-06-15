# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotCirc import SlotCirc
from numpy import exp, arcsin, ndarray, pi
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotWind.comp_height_wind import comp_height_wind

# For AlmostEqual
DELTA = 1e-6

SlotCirc_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rint=0, Rext=0.1325)
lam.slot = SlotCirc(Zs=6, H0=25e-3, W0=30e-3)
SlotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.3260467e-4,
        "SW_exp": 7.3260467e-4,
        "Aw": 0.2369964,
        "H_exp": 0.0258517945,
        "HW_exp": 0.0258517945,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325, Rext=0.2)
lam.slot = SlotCirc(Zs=6, H0=25e-3, W0=30e-3)
SlotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 6.985109e-4,
        "SW_exp": 6.985109e-4,
        "Aw": 0.20007731,
        "H_exp": 0.024148205,
        "HW_exp": 0.024148205,
    }
)


@ddt
class test_SlotCirc_meth(TestCase):
    """unittest for SlotCirc methods"""

    @data(*SlotCirc_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot, Ndisc=1750)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotCirc_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot, Ndisc=1750)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotCirc_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot, Ndisc=1750)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotCirc_test)
    def test_comp_height_wind(self, test_dict):
        """Check that the computation of the winding's height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height_wind()

        a = result
        b = test_dict["HW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height_wind(test_obj.slot, Ndisc=1750)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotCirc_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect
        """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        self.assertEqual(a, 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325)))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotCirc_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
