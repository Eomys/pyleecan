# -*- coding: utf-8 -*-
import pytest


from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.LamSlot import LamSlot
from numpy import ndarray, pi, arcsin, exp
from ddt import ddt, data
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotW21.check import S21_H1rCheckError

# For AlmostEqual
DELTA = 1e-4

slotW21_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.390225015189331e-4,
        "Aw": 0.132201,
        "SW_exp": 2.3e-4,
        "H_exp": 2.3011250632883697e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.3897749848106692e-4,
        "Aw": 0.10168861,
        "SW_exp": 2.3e-4,
        "H_exp": 2.30903427198e-2,
    }
)

# Rad H1
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=pi / 4, H1_is_rad=True, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.7897749848106692e-4,
        "Aw": 0.097386,
        "SW_exp": 2.3e-4,
        "H_exp": 2.8086e-2,
    }
)


@pytest.mark.METHODS
class Test_SlowW21_meth(object):
    """pytest for SlotW21 methods"""

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW21_test)
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
        test_obj = SlotW21(
            W0=0.2, H0=0.1, W1=0.4, H1=0.1, H1_is_rad=False, H2=0.1, W2=0.6
        )
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)
        # Rbo=1
        Z1 = exp(1j * float(arcsin(0.1)))

        Z2 = Z1 + 0.1
        Z3 = Z1 + 0.1j + 0.2
        Z4 = Z1 + 0.2j + 0.3
        Z5 = Z1 - 0.4j + 0.3
        Z6 = Z1 - 0.3j + 0.2
        Z7 = Z1 - 0.2j + 0.1
        Z8 = Z1 - 0.2j

        [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8]
        # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Segment(Z2, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z5))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Segment(Z6, Z7))
        curve_list.append(Segment(Z7, Z8))

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
        """Check if the build geometry of the winding works correctly"""
        test_obj = SlotW21(
            W0=0.2, H0=0.1, W1=0.4, H1=0.1, H1_is_rad=False, H2=0.1, W2=0.6
        )
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)
        # Rbo=1
        Z1 = exp(1j * float(arcsin(0.1)))

        Z2 = Z1 + 0.1
        Z3 = Z1 + 0.1j + 0.2
        Z4 = Z1 + 0.2j + 0.3
        Z5 = Z1 - 0.4j + 0.3
        Z6 = Z1 - 0.3j + 0.2
        Z7 = Z1 - 0.2j + 0.1
        Z8 = Z1 - 0.2j

        [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8]

        Ztan1 = (Z3 + Z6) / 2
        Ztan2 = Ztan1 + 0.1

        expected = list()

        # part(0, 0)
        curve_list = list()
        curve_list.append(Segment(Z3, Ztan1))
        curve_list.append(Segment(Ztan1, Ztan2))
        curve_list.append(Segment(Ztan2, Z4))
        curve_list.append(Segment(Z4, Z3))
        point_ref = (Z3 + Ztan1 + Ztan2 + Z4) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R0_T0_S0"
        )
        expected.append(surface)

        # part(0, 1)
        curve_list = list()
        curve_list.append(Segment(Ztan1, Z6))
        curve_list.append(Segment(Z6, Z5))
        curve_list.append(Segment(Z5, Ztan2))
        curve_list.append(Segment(Ztan2, Ztan1))
        point_ref = (Z5 + Ztan1 + Ztan2 + Z6) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R0_T1_S0"
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

    def test_check_error(self):
        """Check that the check method is correctly raising an error"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW21(Zs=69, H2=0.0015, H1_is_rad=True, H1=3.14)

        with pytest.raises(S21_H1rCheckError) as context:
            lam.slot.check()

    def test_get_surface_wind(self):
        """Check that the get_surface_wind works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW21(
            Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
        )
        result = lam.slot.get_surface_wind()
        assert result.label == "WindR_R0_T0_S0"
