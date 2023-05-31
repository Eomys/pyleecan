# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError
import matplotlib.pyplot as plt
from numpy import exp

Mag12_test = list()
# Internal Slot
lam = LamSlotMag(is_internal=True, Rext=0.1325)
lam.slot = SlotM12(H0=5e-3, W0=10e-3, Zs=12, Hmag=5e-3, Wmag=10e-3)
Mag12_test.append(
    {
        "test_obj": lam,
        "Rmec": 0.1325,
        "S_exp": 5.062918e-5,
        "H_exp": 5.094e-3,
        "SA_exp": 4.9685e-5,
        "HA_exp": 5e-3,
        "Ao": 0.075489,
    }
)

# Outward Slot
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotM12(H0=5e-3, W0=10e-3, Zs=12, Hmag=5e-3, Wmag=10e-3)
Mag12_test.append(
    {
        "test_obj": lam,
        "Rmec": 0.1324056,
        "S_exp": 4.937e-5,
        "H_exp": 4.9965e-3,
        "SA_exp": 5.03147e-5,
        "HA_exp": 5.0909e-3,
        "Ao": 0.075489,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_12_meth(object):
    """unittest for MagnetType12 methods"""

    @pytest.mark.parametrize("test_dict", Mag12_test)
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

    @pytest.mark.parametrize("test_dict", Mag12_test)
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

    @pytest.mark.parametrize("test_dict", Mag12_test)
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

    @pytest.mark.parametrize("test_dict", Mag12_test)
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

    @pytest.mark.parametrize("test_dict", Mag12_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_dict["Ao"], rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag12_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z4"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag12_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag12_test)
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
        Wmag = test_obj.slot.Wmag
        Hmag = test_obj.slot.Hmag

        assert abs(Z1 - Z4) == pytest.approx(W0, rel=DELTA)
        assert abs(Z2 - Z3) == pytest.approx(W0, rel=DELTA)
        assert abs(Z1 - Z2) == pytest.approx(H0, rel=DELTA)
        assert abs(Z3 - Z4) == pytest.approx(H0, rel=DELTA)

        if test_obj.is_internal:
            assert ZM0 == pytest.approx(Z1.real + Hmag - H0, rel=DELTA)
        else:
            assert ZM0 == pytest.approx(Z1.real - Hmag + H0, rel=DELTA)
        assert abs(ZM1 - ZM4) == pytest.approx(Wmag, rel=DELTA)
        assert abs(ZM2 - ZM3) == pytest.approx(Wmag, rel=DELTA)
        assert abs(ZM0 - (Z2 + Z3) / 2) == pytest.approx(Hmag, rel=DELTA)

        assert abs(ZM2) == pytest.approx(abs(ZM0), rel=DELTA)
        assert abs(ZM3) == pytest.approx(abs(ZM0), rel=DELTA)

if __name__ == "__main__":
    a = Test_Magnet_Type_12_meth()
    for test_dict in Mag12_test:
        a.test_comp_mec_radius(test_dict)
    print("Done")
