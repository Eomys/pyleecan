# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW13 import SlotW13
from numpy import ndarray, arcsin, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotW13.check import S13_H1rCheckError

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
lam = LamSlot(is_internal=False, Rint=0.1325, is_stator=False)
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


@pytest.mark.METHODS
class Test_SlotW13_meth(object):
    """pytest for SlotW13 methods"""

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
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
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
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW13_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

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

    def test_get_surface_wind(self):
        """Check that the get_surface_wind works when stator = false"""
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
        result = lam.slot.get_surface_wind()
        assert result.label == "WindR_R0_T0_S0"
        assert len(result.get_lines()) == 4
