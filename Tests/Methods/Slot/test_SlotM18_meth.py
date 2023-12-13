# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.LamSlotMag import LamSlotMag

from pyleecan.Classes.SlotM18 import SlotM18
from numpy import pi, exp, angle, array, arcsin
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

Mag18_test = list()
# Internal Lamination
lam = LamSlotMag(is_internal=True, Rext=0.5)
lam.slot = SlotM18(H0=0.1, Zs=4)
Mag18_test.append(
    {
        "test_obj": lam,
        "S_exp": 0,
        "SA_exp": 0.0863937,
        "H_exp": 0,
        "HA_exp": 0.1,
        "Rmec": 0.6,
    }
)

# External Lamination
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotM18(H0=2.5e-3, Zs=8)
Mag18_test.append(
    {
        "test_obj": lam,
        "S_exp": 0,
        "SA_exp": 0.000257708,
        "H_exp": 0,
        "HA_exp": 2.5e-3,
        "Rmec": 0.13,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_18_meth(object):
    """unittest for MagnetType18 methods"""

    @pytest.mark.parametrize("test_dict", Mag18_test)
    def test_schematics(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        assert abs(point_dict["ZM1"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.slot.H0
        )
        alpha = pi / test_obj.slot.Zs
        assert angle(point_dict["Z1"]) == pytest.approx(-alpha)
        assert angle(point_dict["Z2"]) == pytest.approx(alpha)
        assert angle(point_dict["ZM1"]) == pytest.approx(-alpha)
        assert angle(point_dict["ZM2"]) == pytest.approx(-alpha)
        assert angle(point_dict["ZM3"]) == pytest.approx(alpha)
        assert angle(point_dict["ZM4"]) == pytest.approx(alpha)

    @pytest.mark.parametrize("test_dict", Mag18_test)
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

    @pytest.mark.parametrize("test_dict", Mag18_test)
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

    @pytest.mark.parametrize("test_dict", Mag18_test)
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

    @pytest.mark.parametrize("test_dict", Mag18_test)
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

    @pytest.mark.parametrize("test_dict", Mag18_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(2 * pi / test_obj.slot.Zs, rel=DELTA)

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag18_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z2"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag18_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)


if __name__ == "__main__":
    a = Test_Magnet_Type_18_meth()
    for test_dict in Mag18_test:
        a.test_schematics(test_dict)
        a.test_comp_mec_radius(test_dict)
        a.test_comp_width_opening(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
        a.test_comp_height(test_dict)
        a.test_comp_height_active(test_dict)
    print("Done")
