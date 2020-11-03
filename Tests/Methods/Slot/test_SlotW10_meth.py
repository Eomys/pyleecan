# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW10 import SlotW10
from numpy import exp, arcsin, ndarray, pi
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-6

slotW10_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW10(
    H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, H1_is_rad=False
)
slotW10_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.9258746e-4,
        "Aw": 0.1044713,
        "SW_exp": 3.6e-4,
        "H_exp": 3.263591e-2,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW10(
    H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, H1_is_rad=False
)
slotW10_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.904125e-4,
        "Aw": 8.0014282e-2,
        "SW_exp": 3.6e-4,
        "H_exp": 3.247322e-2,
    }
)

# H1 is rad
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW10(
    H0=1e-3, H1=pi / 4, H2=20e-3, W0=12e-3, W1=14e-3, W2=12e-3, H1_is_rad=True
)
slotW10_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.639125e-4,
        "Aw": 8.3056107e-2,
        "SW_exp": 2.4e-4,
        "H_exp": 2.1980644e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW10_meth(object):
    """pytest for SlotW10 methods"""

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        assert a == test_obj.slot.W0

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """check that curve_list is correct"""
        test_obj = SlotW10(
            W0=0.2, H0=0.1, W1=0.4, H1=0.1, H1_is_rad=False, H2=0.1, W2=0.6
        )
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)

        # Rbo=1
        Z10 = exp(1j * float(arcsin(0.1)))
        Z9 = Z10 + 0.1
        Z8 = Z10 + 0.1j + 0.2
        Z7 = Z10 + 0.2
        Z6 = Z10 + 0.2j + 0.3
        Z5 = Z10 - 0.4j + 0.3
        Z4 = Z10 - 0.2j + 0.2
        Z3 = Z10 - 0.3j + 0.2
        Z2 = Z10 - 0.2j + 0.1
        Z1 = Z10 - 0.2j

        # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Segment(Z2, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z5))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Segment(Z6, Z7))
        curve_list.append(Segment(Z7, Z8))
        curve_list.append(Segment(Z8, Z9))
        curve_list.append(Segment(Z9, Z10))

        result = test_obj.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA

    def test_build_geometry_wind(self):
        """Check if the surface of winding surface is correct"""
        test_obj = SlotW10(
            W0=0.2, H0=0.1, W1=0.4, H1=0.1, H1_is_rad=False, H2=0.1, W2=0.6
        )
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)
        Z1 = exp(1j * float(arcsin(0.1)))

        # Rbo=1
        Z2 = Z1 + 0.1
        Z3 = Z1 + 0.1j + 0.2
        Z4 = Z1 + 0.2
        Z5 = Z1 + 0.2j + 0.3
        Z6 = Z1 - 0.4j + 0.3
        Z7 = Z1 - 0.2j + 0.2
        Z8 = Z1 - 0.3j + 0.2
        Z9 = Z1 - 0.2j + 0.1
        Z10 = Z1 - 0.2j

        Ztan1 = (Z4 + Z7) / 2.0
        Ztan2 = (Z5 + Z6) / 2.0
        expected = list()
        # part(0,0)
        curve_list = list()
        curve_list.append(Segment(Z7, Ztan1))
        curve_list.append(Segment(Ztan1, Ztan2))
        curve_list.append(Segment(Ztan2, Z6))
        curve_list.append(Segment(Z6, Z7))
        point_ref = (Z7 + Ztan1 + Ztan2 + Z6) / 4

        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="Wind_Stator_R0_T0_S0"
        )
        expected.append(surface)

        # part(0,1)
        curve_list = list()
        curve_list.append(Segment(Ztan1, Z4))
        curve_list.append(Segment(Z4, Z5))
        curve_list.append(Segment(Z5, Ztan2))
        curve_list.append(Segment(Ztan2, Ztan1))
        point_ref = (Z4 + Ztan1 + Ztan2 + Z5) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="Wind_Stator_R0_T1_S0"
        )
        expected.append(surface)

        result = test_obj.build_geometry_wind(Nrad=1, Ntan=2)
        assert len(result) == len(expected)
        for i in range(0, len(result)):
            assert len(result[i].line_list) == len(expected[i].line_list)
            for jj in range(len(result[i].line_list)):
                a = result[i].line_list[jj].begin
                b = expected[i].line_list[jj].begin
                assert abs((a - b) / a - 0) < DELTA
                a = result[i].line_list[jj].end
                b = expected[i].line_list[jj].end
                assert abs((a - b) / a - 0) < DELTA

            assert result[i].label == expected[i].label

    def test_get_surface_wind(self):
        """Check that the get_surface_wind works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW10(
            H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, H1_is_rad=False
        )
        result = lam.slot.get_surface_wind()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 4
