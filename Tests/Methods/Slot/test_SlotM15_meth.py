# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM15 import SlotM15
from numpy import pi, exp, sqrt, arcsin, angle
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError

mm = 1e-3

Mag15_test = list()
# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=110 * mm, is_internal=True)
lam.slot = SlotM15(
    Zs=4, W0=80 * pi / 180, H0=10 * mm, H1=20 * mm, W1=100 * mm, Rtopm=100 * mm
)
Mag15_test.append(
    {
        "test_obj": lam,
        "Rmec": 120 * mm,
        "S_exp": 1.46607e-3,
        "SA_exp": 2e-3,
        "HA_exp": 0.02,
        "Ao": 1.39626,
        "H_exp": 0.01,
    }
)

# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=110 * mm, is_internal=True)
lam.slot = SlotM15(
    Zs=4, W0=80 * pi / 180, H0=20 * mm, H1=20 * mm, W1=100 * mm, Rtopm=100 * mm
)
Mag15_test.append(
    {
        "test_obj": lam,
        "Rmec": 110 * mm,
        "S_exp": 2.7925e-3,
        "SA_exp": 2.0533e-3,
        "HA_exp": 0.02,
        "Ao": 1.39626,
        "H_exp": 20 * mm,
    }
)

# Internal slot surface magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=100 * mm, is_internal=True)
lam.slot = SlotM15(
    Zs=4, W0=80 * pi / 180, H0=0 * mm, H1=20 * mm, W1=100 * mm, Rtopm=100 * mm
)
Mag15_test.append(
    {
        "test_obj": lam,
        "Rmec": 120e-3,
        "S_exp": 0,
        "SA_exp": 2e-3,
        "HA_exp": 0.02,
        "Ao": 1.39626,
        "H_exp": 0,
    }
)

# Internal slot surface magnet with different top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=100 * mm, is_internal=True)
lam.slot = SlotM15(
    Zs=4, W0=80 * pi / 180, H0=0 * mm, H1=20 * mm, W1=100 * mm, Rtopm=65 * mm
)
Mag15_test.append(
    {
        "test_obj": lam,
        "Rmec": 120e-3,
        "S_exp": 0,
        "SA_exp": 1.7185e-3,
        "HA_exp": 0.02,
        "Ao": 1.39626,
        "H_exp": 0,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_Magnet_Type_15_meth(object):
    """unittest for MagnetType15 methods"""

    @pytest.mark.parametrize("test_dict", Mag15_test)
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

    @pytest.mark.parametrize("test_dict", Mag15_test)
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

    @pytest.mark.parametrize("test_dict", Mag15_test)
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

    @pytest.mark.parametrize("test_dict", Mag15_test)
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

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == pytest.approx(test_dict["Ao"], rel=DELTA)
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        point_dict = test_obj.slot._comp_point_coordinate()
        assert a == pytest.approx(abs(point_dict["Z1"] - point_dict["Z4"]), rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_mec_radius(self, test_dict):
        """Check that the computation of the mechanical radius is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.comp_radius_mec()
        assert a == pytest.approx(test_dict["Rmec"], rel=DELTA)

    @pytest.mark.parametrize("test_dict", Mag15_test)
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

        # Polar Slot
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

        # Polar bottom for magnet
        assert abs(Z2) == pytest.approx(abs(ZM1), rel=DELTA)
        assert abs(Z2) == pytest.approx(abs(ZM4), rel=DELTA)
        # Parallel side
        assert ZM1.imag == pytest.approx(ZM2.imag, rel=DELTA)
        assert ZM3.imag == pytest.approx(ZM4.imag, rel=DELTA)
        assert ZM1.imag == pytest.approx(-W1 / 2, rel=DELTA)
        assert ZM3.imag == pytest.approx(W1 / 2, rel=DELTA)
        # H1 def
        if test_obj.is_internal:
            assert ZM0 == pytest.approx(abs(Z2) + H1, rel=DELTA)
        else:
            assert ZM0 == pytest.approx(abs(Z2) - H1, rel=DELTA)
