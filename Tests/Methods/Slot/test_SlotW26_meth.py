# -*- coding: utf-8 -*-
from unittest import TestCase

from ....Classes.SlotW26 import SlotW26
from numpy import ndarray
from ....Classes.LamSlot import LamSlot
from ddt import ddt, data
from ....Methods.Slot.Slot.comp_height import comp_height
from ....Methods.Slot.Slot.comp_surface import comp_surface
from ....Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from ....Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW26_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1)
lam.slot = SlotW26(Zs=12, H0=10e-3, W0=10e-3, H1=0.025, R1=0.01, R2=0.0075)
slotW26_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.7471e-4,
        "Ao": 0.10004,
        "Aw": 0.2362668,
        "SW_exp": 6.7387e-4,
        "H_exp": 5.1285e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW26(Zs=12, H0=10e-3, W0=10e-3, H1=0.025, R1=0.01, R2=0.0075)
slotW26_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.73044e-4,
        "Ao": 0.10004,
        "Aw": 0.1254996,
        "SW_exp": 6.7387e-4,
        "H_exp": 5.103517e-2,
    }
)


@ddt
class test_SlotW26_meth(TestCase):
    """unittest for SlotW26 methods"""

    @data(*slotW26_test)
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

    @data(*slotW26_test)
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

    @data(*slotW26_test)
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

    @data(*slotW26_test)
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

    @data(*slotW26_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
