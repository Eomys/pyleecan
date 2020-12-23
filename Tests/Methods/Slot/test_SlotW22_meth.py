# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.SlotW22 import SlotW22
from numpy import pi, ndarray, cos, sin, arcsin, exp
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.Slot.comp_surface_active import comp_surface_active

# For AlmostEqual
DELTA = 1e-4

slotW22_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=1)
lam.slot = SlotW22(Zs=36, W0=pi / 72, W2=pi / 36, H0=6e-3, H2=40e-3)
slotW22_test.append(
    {"test_obj": lam, "S_exp": 3.660915e-03, "SW_exp": 3.3999e-03, "H_exp": 0.046}
)

# External Slot
lam = LamSlot(is_internal=False, Rint=1)
lam.slot = SlotW22(Zs=36, W0=pi / 72, W2=pi / 36, H0=6e-3, H2=40e-3)
slotW22_test.append(
    {"test_obj": lam, "S_exp": 3.844e-03, "SW_exp": 3.5814e-03, "H_exp": 0.046}
)


@pytest.mark.METHODS
class Test_SlotW22_meth(object):
    """pytest for SlotW22 methods"""

    @pytest.mark.parametrize("test_dict", slotW22_test)
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

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW22_test)
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

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == test_obj.slot.W0
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_obj.slot.W2
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """check that curve_list is correct"""
        test_obj = SlotW22(W0=pi / 10, H0=0.1, W2=pi / 5, H2=0.1)
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)

        Z1 = cos(pi / 20) + 1j * sin(pi / 20)
        Z2 = 1.1 * (cos(pi / 20) + 1j * sin(pi / 20))
        Z3 = 1.1 * (cos(pi / 10) + 1j * sin(pi / 10))
        Z4 = 1.2 * (cos(pi / 10) + 1j * sin(pi / 10))
        Z5 = 1.2 * (cos(pi / 10) - 1j * sin(pi / 10))
        Z6 = 1.1 * (cos(pi / 10) - 1j * sin(pi / 10))
        Z7 = 1.1 * (cos(pi / 20) - 1j * sin(pi / 20))
        Z8 = cos(pi / 20) - 1j * sin(pi / 20)
        [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8]

        # Creation of curve
        curve_list = list()
        Zc = 0  # center
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Arc2(Z2, Zc, -pi / 20))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Arc2(Z4, Zc, pi / 5))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Arc2(Z6, Zc, -pi / 20))
        curve_list.append(Segment(Z7, Z8))

        result = test_obj.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            if isinstance(result[i], Segment):
                a = result[i].begin
                b = curve_list[i].begin
                assert abs((a - b) / a - 0) < DELTA
                a = result[i].end
                b = curve_list[i].end
                assert abs((a - b) / a - 0) < DELTA
            else:  # Arc2
                a = result[i].begin
                b = curve_list[i].begin
                assert abs((a - b) / a - 0) < DELTA
                a = result[i].center
                b = curve_list[i].center
                assert round(abs(a - b), 7) == 0
                a = result[i].angle
                b = curve_list[i].angle
                assert abs((a - b) / a - 0) < DELTA

    def test_build_geometry_active(self):
        """Check if the build geometry of the winding works correctly"""
        test_obj = SlotW22(W0=pi / 10, H0=0.1, W2=pi / 5, H2=0.1)
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)

        result = test_obj.build_geometry_active(Nrad=2, Ntan=4, is_simplified=True)
        a = result
        assert "Wind_Stator_R0_T0_S0" == a[0].label
        assert len(a) == 8

    def test_get_surface_active(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW22(Zs=36, W0=pi / 72, W2=pi / 36, H0=6e-3, H2=40e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 6
