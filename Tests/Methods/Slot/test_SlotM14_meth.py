# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM14 import SlotM14
from numpy import pi, exp, sqrt, angle
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

Mag14_test = list()
# Internal Slot inset
lam = LamSlotMag(Rint=40e-3, Rext=90e-3, is_internal=True)
lam.slot = SlotM14(Zs=4, W0=0.628, H0=0.02, H1=0.02, W1=0.628, Rtopm=0.04)
Mag14_test.append(
    {
        "test_obj": lam,
        "Rmec": 90e-3,
        "S_exp": 0.0010048,
        "SA_exp": 9.022e-4,
        "Ao": 0.628,
        "H_exp": 0.02,
        "HA_exp": 0.02,
    }
)

# Internal slot surface
lam = LamSlotMag(Rint=40e-3, Rext=90e-3, is_internal=True)
lam.slot = SlotM14(Zs=8, W0=0.628, H0=0, H1=0.02, W1=0.628, Rtopm=0.05)
Mag14_test.append(
    {
        "test_obj": lam,
        "Rmec": 0.11,
        "S_exp": 0,
        "SA_exp": 1.1089e-3,
        "Ao": 0.628,
        "H_exp": 0,
        "HA_exp": 0.02,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_14_meth(object):
    """unittest for MagnetType14 methods"""

    @pytest.mark.parametrize("test_dict", Mag14_test)
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

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the active surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot, Ndisc=1000)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag14_test)
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

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_height_active(self, test_dict):
        """Check that the computation of the active height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height_active()

        a = result
        b = test_dict["HA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        # assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_dict["Ao"], rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z4"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_point_coordinate(self, test_dict):
        """Check that the point coordinates are correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()
        Z1 = point_dict["Z1"]
        Z2 = point_dict["Z2"]
        Z3 = point_dict["Z3"]
        Z4 = point_dict["Z4"]
        ZM0 = point_dict["ZM0"]
        ZM1 = point_dict["ZM1"]
        ZM2 = point_dict["ZM2"]
        ZM3 = point_dict["ZM3"]
        ZM4 = point_dict["ZM4"]
        W0 = test_obj.slot.W0
        H0 = test_obj.slot.H0
        W1 = test_obj.slot.W1
        H1 = test_obj.slot.H1
        Rbo = test_obj.get_Rbo()

        assert abs(Z1) == pytest.approx(Rbo, rel=DELTA)
        assert angle(Z1) == pytest.approx(-W0 / 2, rel=DELTA)
        assert abs(Z4) == pytest.approx(Rbo, rel=DELTA)
        assert angle(Z4) == pytest.approx(W0 / 2, rel=DELTA)
        if test_obj.is_internal:
            assert abs(Z2) == pytest.approx(Rbo - H0, rel=DELTA)
            assert abs(Z3) == pytest.approx(Rbo - H0, rel=DELTA)
        else:
            assert abs(Z3) == pytest.approx(Rbo + H0, rel=DELTA)
            assert abs(Z2) == pytest.approx(Rbo + H0, rel=DELTA)
        assert angle(Z2) == pytest.approx(-W0 / 2, rel=DELTA)
        assert angle(Z3) == pytest.approx(W0 / 2, rel=DELTA)

        assert angle(ZM1) == pytest.approx(angle(ZM2), rel=DELTA)
        assert angle(ZM1) == pytest.approx(-W1 / 2, rel=DELTA)
        assert angle(ZM3) == pytest.approx(angle(ZM4), rel=DELTA)
        assert angle(ZM3) == pytest.approx(W1 / 2, rel=DELTA)

        if test_obj.is_internal:
            assert ZM0 == pytest.approx(Rbo + H1 - H0, rel=DELTA)
        else:
            assert ZM0 == pytest.approx(Rbo - H1 + H0, rel=DELTA)
