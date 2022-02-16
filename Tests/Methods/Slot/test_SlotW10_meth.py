# -*- coding: utf-8 -*-
import pytest
from numpy import exp, arcsin, pi

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.Slot import Slot

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
        "SO_exp": 3.258746e-05,
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
        "SO_exp": 3.0412538e-05,
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
        "SO_exp": 2.391253e-05,
        "H_exp": 2.1980644e-2,
    }
)


class Test_SlotW10_meth(object):
    """pytest for SlotW10 methods"""

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z10"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z3"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W1
        )
        assert abs(point_dict["Z4"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.W2
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z2"].real - point_dict["Z3"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z4"].real - point_dict["Z5"].real) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z10"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z9"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z9"].real - point_dict["Z8"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z6"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.H2
        )

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
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
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

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_surface_opening(self, test_dict):
        """Check that the computation of the opening surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_opening()

        a = result
        b = test_dict["SO_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_opening(test_obj.slot, Ndisc=300)
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
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
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

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_width_opening(self, test_dict):
        """Check that the computation of the average opening width is correct"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_width_opening()
        assert a == test_obj.slot.W0

    @pytest.mark.parametrize("test_dict", slotW10_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_get_surface(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW10(
            H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, H1_is_rad=False
        )
        result = lam.slot.get_surface_active()
        assert result.label == "Rotor_Winding_R0-T0-S0"
        assert len(result.get_lines()) == 4

        result = lam.slot.get_surface_opening()
        assert len(result) == 1
        assert result[0].label == "Rotor_SlotOpening_R0-T0-S0"
        assert (
            len(result[0].get_lines()) == 8
        )  # TODO Add missing line (limit opening/winding)

        result = lam.slot.get_surface()
        assert len(result.get_lines()) == 10


if __name__ == "__main__":
    a = Test_SlotW10_meth()
    a.test_get_surface()
    for ii, test_dict in enumerate(slotW10_test):
        print("Running test for Slot[" + str(ii) + "]")
        a.test_schematics(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
        a.test_comp_surface_opening(test_dict)
        a.test_comp_height(test_dict)
        a.test_build_geometry_active(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_width_opening(test_dict)
        a.test_comp_angle_active_eq(test_dict)
        print("Done")

