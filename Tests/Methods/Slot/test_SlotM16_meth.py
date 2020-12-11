# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM16 import SlotM16
from numpy import pi, exp, sqrt, arcsin, angle
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_height_active import comp_height_active
from pyleecan.Methods.Slot.SlotWind.comp_surface_active import comp_surface_active
from pyleecan.Methods import ParentMissingError


Mag16_test = list()
# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=80e-3, Rext=200e-3, is_internal=True, is_stator=False,)
lam.slot = SlotM16(Zs=4, W0=0.02, H0=0.02, H1=0.08, W1=0.04)

Mag16_test.append(
    {
        "test_obj": lam,
        "Rmec": 200e-3,
        "S_exp": 3.6033e-3,
        "SA_exp": 3.2e-3,
        "HA_exp": 0.081109,
        "Ao": 0.10004,
        "H_exp": 0.10025,
    }
)

# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=220e-3, Rext=400e-3, is_internal=False, is_stator=True,)
lam.slot = SlotM16(Zs=8, W0=0.02, H0=0.02, H1=0.08, W1=0.04)
Mag16_test.append(
    {
        "test_obj": lam,
        "Rmec": 220e-3,
        "S_exp": 3.5969e-3,
        "SA_exp": 0.0032,
        "HA_exp": 0.080624,
        "Ao": 0.09094,
        "H_exp": 0.10039,
    }
)

# For AlmostEqual
DELTA = 1e-4


@pytest.mark.METHODS
class Test_Magnet_Type_16_meth(object):
    """unittest for MagnetType16 methods"""

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the active surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_active(test_obj.slot, Ndisc=5000)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag16_test)
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

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_height_active(self, test_dict):
        """Check that the computation of the active height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height_active()

        a = result
        b = test_dict["HA_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_dict["Ao"], rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z8"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag16_test)
    def test_comp_point_coordinate(self, test_dict):
        """Check that the point coordinates are correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()
        Z1 = point_dict["Z1"]
        Z2 = point_dict["Z2"]
        Z3 = point_dict["Z3"]
        Z4 = point_dict["Z4"]
        Z5 = point_dict["Z5"]
        Z6 = point_dict["Z6"]
        Z7 = point_dict["Z7"]
        Z8 = point_dict["Z8"]
        W0 = test_obj.slot.W0
        H0 = test_obj.slot.H0
        W1 = test_obj.slot.W1
        H1 = test_obj.slot.H1
        Rbo = test_obj.get_Rbo()

        assert abs(Z1) == pytest.approx(Rbo, rel=DELTA)
        assert abs(Z8) == pytest.approx(Rbo, rel=DELTA)
        assert abs(Z1 - Z8) == pytest.approx(W0, rel=DELTA)
        assert abs(Z2 - Z7) == pytest.approx(W0, rel=DELTA)
        assert abs(Z1 - Z2) == pytest.approx(H0, rel=DELTA)
        assert abs(Z7 - Z8) == pytest.approx(H0, rel=DELTA)

        assert abs(Z4 - Z5) == pytest.approx(W1, rel=DELTA)
        assert abs(Z3 - Z6) == pytest.approx(W1, rel=DELTA)
        assert abs(Z3 - Z4) == pytest.approx(H1, rel=DELTA)
        assert abs(Z5 - Z6) == pytest.approx(H1, rel=DELTA)
