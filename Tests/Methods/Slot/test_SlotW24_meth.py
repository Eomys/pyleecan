# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW24 import SlotW24
from numpy import ndarray
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotW24.check import S24_HWCheckError

# For AlmostEqual
DELTA = 1e-4

slotW24_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW24(Zs=6, H2=30e-3, W3=12e-3)
slotW24_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.33105250485e-3,
        "Ao": 0.9566,
        "Aw": 0.94497,
        "SW_exp": 3.33105e-3,
        "H_exp": 0.03,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW24(Zs=6, H2=30e-3, W3=12e-3)
slotW24_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.27405010925e-3,
        "Ao": 0.9566,
        "Aw": 0.965887,
        "SW_exp": 4.27405e-3,
        "H_exp": 0.03,
    }
)


@pytest.mark.METHODS
class Test_SlotW24_meth(object):
    """pytest for SlotW24 methods"""

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW24_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check_error(self):
        """Check that the check method is correctly raising an error"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW24(Zs=69, H2=0.0015, W3=12e-3)

        with pytest.raises(S24_HWCheckError) as context:
            lam.slot.check()
