# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.SlotW22 import SlotW22
from numpy import pi, ndarray, cos, sin, arcsin, exp, angle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot

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


class Test_SlotW22_meth(object):
    """pytest for SlotW22 methods"""

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert angle(point_dict["Z1"]) == pytest.approx(-test_obj.slot.W0 / 2)
        assert angle(point_dict["Z2"]) == pytest.approx(-test_obj.slot.W0 / 2)
        assert angle(point_dict["Z3"]) == pytest.approx(-test_obj.slot.W2 / 2)
        assert angle(point_dict["Z4"]) == pytest.approx(-test_obj.slot.W2 / 2)
        assert angle(point_dict["Z7"]) == pytest.approx(test_obj.slot.W0 / 2)
        assert angle(point_dict["Z8"]) == pytest.approx(test_obj.slot.W0 / 2)
        assert angle(point_dict["Z5"]) == pytest.approx(test_obj.slot.W2 / 2)
        assert angle(point_dict["Z6"]) == pytest.approx(test_obj.slot.W2 / 2)
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.H2
        )

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
        test_obj = test_dict["test_obj"]
        surf_list = test_obj.slot.build_geometry_active(Nrad=3, Ntan=2)

        # Check label
        assert surf_list[0].label == "Stator_Winding_R0-T0-S0"
        assert surf_list[1].label == "Stator_Winding_R1-T0-S0"
        assert surf_list[2].label == "Stator_Winding_R2-T0-S0"
        assert surf_list[3].label == "Stator_Winding_R0-T1-S0"
        assert surf_list[4].label == "Stator_Winding_R1-T1-S0"
        assert surf_list[5].label == "Stator_Winding_R2-T1-S0"
        # Check tangential position
        assert surf_list[0].point_ref.imag < 0
        assert surf_list[1].point_ref.imag < 0
        assert surf_list[2].point_ref.imag < 0
        assert surf_list[3].point_ref.imag > 0
        assert surf_list[4].point_ref.imag > 0
        assert surf_list[5].point_ref.imag > 0
        # Check radial position
        if test_obj.is_internal:
            # Tan=0
            assert surf_list[0].point_ref.real > surf_list[1].point_ref.real
            assert surf_list[1].point_ref.real > surf_list[2].point_ref.real
            # Tan=1
            assert surf_list[3].point_ref.real > surf_list[4].point_ref.real
            assert surf_list[4].point_ref.real > surf_list[5].point_ref.real
        else:
            # Tan=0
            assert surf_list[0].point_ref.real < surf_list[1].point_ref.real
            assert surf_list[1].point_ref.real < surf_list[2].point_ref.real
            # Tan=1
            assert surf_list[3].point_ref.real < surf_list[4].point_ref.real
            assert surf_list[4].point_ref.real < surf_list[5].point_ref.real

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
        b = Slot.comp_surface(test_obj.slot)
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
        b = Slot.comp_surface_active(test_obj.slot)
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
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW22_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == test_obj.slot.W0
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
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

    def test_get_surface_active(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW22(Zs=36, W0=pi / 72, W2=pi / 36, H0=6e-3, H2=40e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 6


if __name__ == "__main__":
    a = Test_SlotW22_meth()
    a.test_get_surface_active()

    for test_dict in slotW22_test:
        a.test_schematics(test_dict)
        a.test_build_geometry_active(test_dict)
        a.test_comp_angle_active_eq(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_height(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
