# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW11 import SlotW11
from numpy import ndarray, arcsin, exp, angle
from scipy.optimize import fsolve
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-6
slotW11_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW11(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3)
slotW11_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.06857e-4,
        "Aw": 0.1086124,
        "SW_exp": 3.7427e-4,
        "H_exp": 3.263591e-2,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW11(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3)
slotW11_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.04682446e-4,
        "Aw": 0.0832448,
        "SW_exp": 3.7427e-04,
        "H_exp": 3.236711e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW11_meth(object):
    """pytest for SlotW11 methods"""

    @pytest.mark.parametrize("test_dict", slotW11_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW11_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW11_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW11_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW11_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry_wind(self):
        """Check if the winding surface is correct"""
        test_obj = SlotW11(
            H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3
        )

        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1, is_stator=True)
        Z1 = exp(1j * (float(arcsin(12e-3 / 2.0))))
        Z2 = Z1 + 1e-3
        Z3 = Z2 + 1.5e-3 + (14e-3 - 12e-3) * 1j / 2.0
        Z4 = Z3 + (30e-3 - 5e-3) + (12e-3 - 14e-3) / 2.0 * 1j
        Z5 = Z4 + 5e-3 - 5e-3 * 1j
        Z6 = Z5.conjugate()
        Z7 = Z4.conjugate()
        Z8 = Z3.conjugate()
        Ztan1 = (Z3 + Z8) / 2.0
        Ztan2 = (Z5 + Z6) / 2.0
        Zmid = (Ztan1 + Ztan2) / 2.0
        x = fsolve(
            lambda x: angle((Z7 - (Zmid + 1j * x)) / (Z7 - Z8)), -(12e-3 + 14e-3) / 4.0
        )
        st = "S"
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()
        expected = list()
        # Part 1 (0,0)
        curve_list = list()
        curve_list.append(Segment(Z8, Ztan1))
        curve_list.append(Segment(Ztan1, Zmid))
        curve_list.append(Segment(Zmid, Zrad1))
        curve_list.append(Segment(Zrad1, Z8))
        point_ref = (Z8 + Ztan1 + Zmid + Zrad1) / 4
        surface = SurfLine(
            line_list=curve_list, label="Wind" + st + "_R0_T0_S0", point_ref=point_ref
        )
        expected.append(surface)
        # Part2 (1,0)
        curve_list = list()
        curve_list.append(Segment(Zrad1, Zmid))
        curve_list.append(Segment(Zmid, Ztan2))
        curve_list.append(Segment(Ztan2, Z6))
        curve_list.append(Arc1(Z6, Z7, -1 * 5e-3))
        curve_list.append(Segment(Z7, Zrad1))
        point_ref = (Zrad1 + Zmid + Ztan2 + Z6 + Z7) / 5
        surface = SurfLine(
            line_list=curve_list, label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
        )
        expected.append(surface)
        # Part3 (0,1)
        curve_list = list()
        curve_list.append(Segment(Ztan1, Z3))
        curve_list.append(Segment(Z3, Zrad2))
        curve_list.append(Segment(Zrad2, Zmid))
        curve_list.append(Segment(Zmid, Ztan1))
        point_ref = (Ztan1 + Z3 + Zrad2 + Zmid) / 4
        surface = SurfLine(
            line_list=curve_list, label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
        )
        expected.append(surface)
        # Part4 (1,1)
        curve_list = list()
        curve_list.append(Segment(Zmid, Zrad2))
        curve_list.append(Segment(Zrad2, Z4))
        curve_list.append(Arc1(Z4, Z5, -1 * 5e-3))
        curve_list.append(Segment(Z5, Ztan2))
        curve_list.append(Segment(Ztan2, Zmid))
        point_ref = (Zmid + Zrad2 + Z4 + Z5 + Ztan2) / 5
        surface = SurfLine(
            line_list=curve_list, label="Wind" + st + "_R1_T1_S0", point_ref=point_ref
        )
        expected.append(surface)
        result = test_obj.build_geometry_wind(Nrad=2, Ntan=2)
        assert len(result) == len(expected)
        for i in range(0, len(result)):
            for jj in range(len(result[i].line_list)):
                a = result[i].line_list[jj].begin
                b = expected[i].line_list[jj].begin
                assert abs((a - b) / a - 0) < DELTA
                a = result[i].line_list[jj].end
                b = expected[i].line_list[jj].end
                assert abs((a - b) / a - 0) < DELTA

            assert result[i].label == expected[i].label
