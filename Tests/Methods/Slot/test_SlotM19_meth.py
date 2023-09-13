# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM19 import SlotM19
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

from numpy import exp, angle

Mag19_test = list()
# Internal Slot
lam = LamSlotMag(is_internal=True, Rext=0.1325)
lam.slot = SlotM19(W0=10e-3, Zs=4, Hmag=5e-3, W1=5e-3)
Mag19_test.append(
    {
        "test_obj": lam,
        "Rmec": 0.1325,
        "S_exp": 3.740172221187858e-5,
        "H_exp": 5.0e-3,
        "SA_exp": 3.740172221187858e-5,
        "HA_exp": 5.0000000000000044e-3,
        "Ao": 0.0377385,
    }
)

# Outward Slot
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotM19(W0=10e-3, Zs=4, Hmag=5e-3, W1=5e-3)
Mag19_test.append(
    {
        "test_obj": lam,
        "Rmec": 0.132476,
        "S_exp": 3.7598277788121487e-05,
        "H_exp": 0.005090879058170128,
        "SA_exp": 3.7598277788121487e-05,
        "HA_exp": 0.005090879058170128,
        "Ao": 0.0377385,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_19_meth(object):
    """unittest for MagnetType19 methods"""

    @pytest.mark.parametrize("test_dict", Mag19_test)
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

    @pytest.mark.parametrize("test_dict", Mag19_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the active surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot, Ndisc=2000)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag19_test)
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

    @pytest.mark.parametrize("test_dict", Mag19_test)
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

    @pytest.mark.parametrize("test_dict", Mag19_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_dict["Ao"], rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag19_test)
    def test_comp_point_coordinate(self, test_dict):
        """Check that the point coordinates are correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()
        Z1 = point_dict["Z1"]
        Z2 = point_dict["Z2"]
        Z3 = point_dict["Z3"]
        Z4 = point_dict["Z4"]
        W0 = test_obj.slot.W0
        W1 = test_obj.slot.W1
        Hmag = test_obj.slot.Hmag
        Rbo = test_obj.slot.get_Rbo()

        msg = "Return " + str(Rbo - (Z2 + Z3) / 2) + "expected " + str(Hmag)
        assert abs(Rbo - (Z2 + Z3) / 2) == pytest.approx(Hmag, rel=DELTA), msg
        assert abs(Z1 - Z4) == pytest.approx(W1, rel=DELTA)
        assert abs(Z2 - Z3) == pytest.approx(W0, rel=DELTA)


if __name__ == "__main__":
    a = Test_Magnet_Type_19_meth()
    for ii, test_dict in enumerate(Mag19_test):
        print("Running test for Slot[" + str(ii) + "]")

        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
        a.test_comp_height(test_dict)
        a.test_comp_height_active(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_point_coordinate(test_dict)

        print("Done")
