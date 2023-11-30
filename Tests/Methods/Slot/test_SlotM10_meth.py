# -*- coding: utf-8 -*-

import pytest
from numpy import exp, arcsin

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

Mag10_test = list()
# Internal Slot
lam = LamSlotMag(is_internal=True, Rext=0.1325)
lam.slot = SlotM10(H1=5e-3, W1=10e-3, H0=5e-3, W0=10e-3, Zs=12)
Mag10_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.0629e-5,
        "SA_exp": 5e-5,
        "Ao": 0.078449,
        "H_exp": 5.0943e-3,
        "HA_exp": 5.09437e-3,
        "Rmec": 0.1325,
    }
)

# Outward Slot
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotM10(H1=5e-3, W1=10e-3, H0=5e-3, W0=10e-3, Zs=12)
Mag10_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.93708e-5,
        "SA_exp": 5e-5,
        "Ao": 0.072745,
        "H_exp": 4.9965e-3,
        "HA_exp": 5.0909e-3,
        "Rmec": 0.1324056630650208,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_10_meth(object):
    """unittest for MagnetType10 methods"""

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the active surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_height_active(self, test_dict):
        """Check that the computation of the active height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height_active()

        a = result
        b = test_dict["HA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        assert a == test_obj.slot.W0

    @pytest.mark.parametrize("test_dict", Mag10_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)
