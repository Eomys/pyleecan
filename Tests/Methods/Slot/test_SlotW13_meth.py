# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW13 import SlotW13
from numpy import ndarray, arcsin, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW13 import S13_H1rCheckError

# For AlmostEqual
DELTA = 1e-4

slotW13_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW13(
    H0=5e-3, H1=10e-3, H2=30e-3, W0=10e-3, W1=14e-3, W2=8e-3, W3=20e-3, H1_is_rad=False
)
slotW13_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.906291e-4,
        "Aw": 0.13671123,
        "SW_exp": 4.2e-4,
        "H_exp": 0.04509437,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW13(
    H0=5e-3, H1=10e-3, H2=30e-3, W0=10e-3, W1=14e-3, W2=8e-3, W3=20e-3, H1_is_rad=False
)
slotW13_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.8937e-4,
        "Aw": 0.0860546,
        "SW_exp": 4.2e-4,
        "H_exp": 0.04518724,
    }
)

# H1 is rad
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW13(
    H0=5e-3, H1=pi / 4, H2=30e-3, W0=10e-3, W1=14e-3, W2=8e-3, W3=20e-3, H1_is_rad=True
)
slotW13_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.9337e-4,
        "Aw": 0.09049743,
        "SW_exp": 4.2e-4,
        "H_exp": 3.72005e-2,
    }
)


class Test_SlotW13_meth(object):
    """pytest for SlotW13 methods"""

    @pytest.mark.parametrize("test_dict", slotW13_test)
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
            test_obj.slot.W2
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.W3
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"].real - point_dict["Z4"].real) == pytest.approx(
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
        assert abs(point_dict["Z9"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z9"].real - point_dict["Z8"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z6"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.H2
        )

    @pytest.mark.parametrize("test_dict", slotW13_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
        test_obj = test_dict["test_obj"]
        surf_list = test_obj.slot.build_geometry_active(Nrad=3, Ntan=2)

        # Check label
        assert surf_list[0].label == "Wind_Stator_R0_T0_S0"
        assert surf_list[1].label == "Wind_Stator_R1_T0_S0"
        assert surf_list[2].label == "Wind_Stator_R2_T0_S0"
        assert surf_list[3].label == "Wind_Stator_R0_T1_S0"
        assert surf_list[4].label == "Wind_Stator_R1_T1_S0"
        assert surf_list[5].label == "Wind_Stator_R2_T1_S0"
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

    @pytest.mark.parametrize("test_dict", slotW13_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check(self):
        """Check that the check function is raising error"""

        test_obj = SlotW13(
            H0=0.005,
            H1=3,
            H2=0.02,
            W0=0.01,
            W1=0.06,
            W2=0.05,
            W3=0.00015,
            H1_is_rad=True,
        )

        with pytest.raises(S13_H1rCheckError) as context:
            test_obj.check()

    def test_get_surface_active(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW13(
            H0=5e-3,
            H1=10e-3,
            H2=30e-3,
            W0=10e-3,
            W1=14e-3,
            W2=8e-3,
            W3=20e-3,
            H1_is_rad=False,
        )
        result = lam.slot.get_surface_active()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 4
