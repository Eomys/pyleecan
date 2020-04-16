# -*- coding: utf-8 -*-
from unittest import TestCase

from ....Classes.SlotW28 import SlotW28
from numpy import ndarray, arcsin, exp
from ....Classes.LamSlot import LamSlot
from ....Classes.Segment import Segment
from ddt import ddt, data
from ....Methods.Slot.Slot.comp_height import comp_height
from ....Methods.Slot.Slot.comp_surface import comp_surface
from ....Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from ....Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW28_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=84e-3)
lam.slot = SlotW28(Zs=42, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3)
slotW28_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.1448e-4,
        "Ao": 0.0416696,
        "Aw": 0.107065,
        "SW_exp": 1.12862e-4,
        "H_exp": 2.0189e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=85e-3)
lam.slot = SlotW28(Zs=18, W0=7e-3, R1=10e-3, H0=5e-3, H3=30e-3, W3=5e-3)
slotW28_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.8896e-3,
        "Ao": 0.082376,
        "Aw": 0.753692,
        "SW_exp": 1.855e-3,
        "H_exp": 6.2602e-2,
    }
)


@ddt
class test_SlotW28_meth(TestCase):
    """unittest for SlotW28 methods"""

    @data(*slotW28_test)
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
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*slotW28_test)
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
        b = comp_surface_wind(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*slotW28_test)
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
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*slotW28_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect
        """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*slotW28_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
