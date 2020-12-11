# -*- coding: utf-8 -*-
import pytest
from numpy import abs as np_abs
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotDC import SlotDC
from numpy import exp, arcsin, ndarray, pi
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

SlotDC_test = list()

# Inner lamination
lam = LamSlot(is_stator=False, is_internal=True, Rext=0.4, Rint=0.2)
lam.slot = SlotDC(
    Zs=6,
    W1=10e-3,
    W2=15e-3,
    H1=30e-3,
    H2=60e-3,
    H3=60e-3,
    D1=40e-3,
    D2=50e-3,
    R3=10e-3,
)

SlotDC_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.8356e-3,
        "SW_exp": 4.7291e-3,
        "H_exp": 0.16003,
    }
)
# Outer lamination
lam = LamSlot(is_stator=False, is_internal=False, Rext=0.4, Rint=0.2)
lam.slot = SlotDC(
    Zs=6,
    W1=10e-3,
    W2=15e-3,
    H1=30e-3,
    H2=60e-3,
    H3=60e-3,
    D1=40e-3,
    D2=50e-3,
    R3=10e-3,
)
SlotDC_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.835e-3,
        "SW_exp": 4.7291e-3,
        "H_exp": 0.15993,
    }
)


@pytest.mark.METHODS
class Test_SlotDC_meth(object):
    """pytest for SlotDC methods"""

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface of the slotDC is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot, Ndisc=2000)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot, Ndisc=2000)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W1 / (2 * test_dict["test_obj"].get_Rbo()))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        assert a == test_obj.slot.W1

    @pytest.mark.parametrize("test_dict", SlotDC_test)
    def test_comp_point_coordinate(self, test_dict):
        """Check that the computation of the point is correct"""
        test_obj = test_dict["test_obj"]
        [
            Z1,
            Z2,
            Z3,
            Z4,
            Z5,
            Z6,
            Z7,
            Z8,
            Z9,
            Z10,
            Z11,
            Z12,
            Zc1,
            Zc2,
            Zc3,
        ] = test_obj.slot._comp_point_coordinate()

        # Check W1
        assert np_abs(Z1 - Z12), pytest.approx(test_obj.slot.W1, rel=DELTA)
        assert np_abs(Z2 - Z11), pytest.approx(test_obj.slot.W1, rel=DELTA)
        # Check W2
        assert np_abs(Z10 - Z3), pytest.approx(test_obj.slot.W2, rel=DELTA)
        assert np_abs(Z9 - Z4), pytest.approx(test_obj.slot.W2, rel=DELTA)
        # Check circle D1
        assert np_abs(Z3 - Zc1), pytest.approx(test_obj.slot.D1 / 2, rel=DELTA)
        assert np_abs(Z2 - Zc1), pytest.approx(test_obj.slot.D1 / 2, rel=DELTA)
        assert np_abs(Z10 - Zc1), pytest.approx(test_obj.slot.D1 / 2, rel=DELTA)
        assert np_abs(Z11 - Zc1), pytest.approx(test_obj.slot.D1 / 2, rel=DELTA)
        # Check circle D2
        assert np_abs(Z9 - Zc2), pytest.approx(test_obj.slot.D2 / 2, rel=DELTA)
        assert np_abs(Z8 - Zc2), pytest.approx(test_obj.slot.D2 / 2, rel=DELTA)
        assert np_abs(Z4 - Zc2), pytest.approx(test_obj.slot.D2 / 2, rel=DELTA)
        assert np_abs(Z5 - Zc2), pytest.approx(test_obj.slot.D2 / 2, rel=DELTA)
        # Check circle R3
        assert np_abs(Z7 - Zc3), pytest.approx(test_obj.slot.R3, rel=DELTA)
        assert np_abs(Z6 - Zc3), pytest.approx(test_obj.slot.R3, rel=DELTA)
