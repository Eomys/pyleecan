# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.LamSlotMag import LamSlotMag

from pyleecan.Classes.SlotM11 import SlotM11
from numpy import pi, exp, angle, array, arcsin
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

Mag11_test = list()
# Internal Slot surface
lam = LamSlotMag(is_internal=True, Rext=0.5)
lam.slot = SlotM11(H1=1, W1=pi / 4, H0=0, W0=pi / 4, Zs=4)
Mag11_test.append(
    {
        "test_obj": lam,
        "S_exp": 0,
        "SA_exp": 0.78539616,
        "H_exp": 0,
        "HA_exp": 1,
        "Rmec": 1.5,
    }
)

# Internal Slot inset
lam = LamSlotMag(is_internal=True, Rext=0.5)
lam.slot = SlotM11(H1=20e-3, W1=pi / 4, H0=40e-3, W0=pi / 4, Zs=4)
Mag11_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.015079,
        "SA_exp": 7.3827e-3,
        "H_exp": 40e-3,
        "HA_exp": 20e-3,
        "Rmec": 0.5,
    }
)

# Outward Slot inset
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotM11(H1=8e-3, W1=pi / 12, H0=5e-3, W0=pi / 10, Zs=8)
Mag11_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.1205e-4,
        "SA_exp": 2.7961e-4,
        "H_exp": 5e-3,
        "HA_exp": 8e-3,
        "Rmec": 0.1295,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_11_meth(object):
    """unittest for MagnetType11 methods"""

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the active surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_height_active(self, test_dict):
        """Check that the computation of the active height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height_active()

        a = result
        b = test_dict["HA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_obj.slot.W0, rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z4"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)
